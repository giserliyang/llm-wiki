"""本地视频 → Whisper 转写 → raw-video 笔记（一条命令）。

必须传入完整视频路径（无默认库）。
YAML 与 templates/raw-video.md、B 站 Clipper 对齐（无 series）。
字幕只写入笔记正文，不保留 .srt。

用法:
  python scripts/video_to_note.py "C:\\path\\to\\xx.mp4"
  python scripts/video_to_note.py "C:\\path\\to\\xx.mp4" --outdir "raw\\videos\\某目录"
  python scripts/video_to_note.py --list "C:\\Videos\\folder"
"""
from __future__ import annotations

import argparse
import re
import sys
from datetime import date
from pathlib import Path

VAULT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = VAULT / "raw" / "videos"
MODEL = "small"
DEVICE = "cpu"
COMPUTE = "int8"


def safe_name(name: str) -> str:
    return re.sub(r'[<>:"/\\|?*]', "_", name).strip()


def fmt_clock(seconds: float) -> str:
    s = int(seconds)
    h, m, sec = s // 3600, (s % 3600) // 60, s % 60
    return f"{h:02d}:{m:02d}:{sec:02d}" if h else f"{m:02d}:{sec:02d}"


def file_uri(path: Path) -> str:
    return path.resolve().as_uri()


def local_video_html(src: str) -> str:
    return (
        f'<video controls preload="metadata" '
        f'style="width:100%;max-height:480px;" src="{src}"></video>'
    )


def transcribe(video: Path) -> list[tuple[float, str]]:
    from faster_whisper import WhisperModel

    print(f"加载模型 {MODEL} ({DEVICE}/{COMPUTE})…")
    model = WhisperModel(MODEL, device=DEVICE, compute_type=COMPUTE)
    print(f"转写: {video.name}")
    segments, _info = model.transcribe(
        str(video),
        language="zh",
        vad_filter=True,
        beam_size=5,
    )
    lines: list[tuple[float, str]] = []
    for seg in segments:
        t = seg.text.strip()
        if t:
            lines.append((seg.start, t))
            print(f"[{fmt_clock(seg.start)}] {t}")
    return lines


def write_note(
    note_path: Path,
    *,
    title: str,
    video_path: Path,
    lines: list[tuple[float, str]],
) -> None:
    transcript = "\n".join(f"[{fmt_clock(t)}] {c}" for t, c in lines) or "（无字幕）"
    today = date.today().isoformat()
    src = file_uri(video_path)
    embed = local_video_html(src)
    note_path.parent.mkdir(parents=True, exist_ok=True)
    # 字段与 templates/raw-video.md / B 站 Clipper 对齐；无 series
    note_path.write_text(
        f"""---
title: "{title}"
type: raw
source_type: video
tags: []
status: 未读
created: {today}
source_url: "{src}"
bvid: ""
cid: ""
author: ""
duration: ""
---

{embed}

## 字幕 / 文稿

> 来源：本地 faster-whisper 转写（{MODEL}/{DEVICE}/{COMPUTE}）。时间轴仅作定位。

{transcript}

---

# 学习附录

## 视频信息

| 字段 | 值 |
| --- | --- |
| URL | {src} |
| 平台 | 本地文件 |
| 频道/UP主 | |
| 时长 | |
| 为什么看 | |
| 什么时候用 | |

## 观看进度

> 未勾选会出现在 [[dashboards/素材收件箱]]。

- [ ] 通读字幕
- [ ] 对照源码动手
- [ ] 写入 notes/（若有要点）

## 拆解索引

```dataview
LIST
FROM "notes"
WHERE source = this.file.link
SORT understanding_level DESC
```

## 速记（可选）

> 只写「用自己的话」的一两句。
""",
        encoding="utf-8",
    )


def process_one(video: Path, outdir: Path) -> Path:
    title = video.stem
    outdir.mkdir(parents=True, exist_ok=True)
    note_path = outdir / f"{safe_name(title)}.md"

    if note_path.exists():
        print(f"已存在，跳过: {note_path}")
        return note_path

    lines = transcribe(video)
    write_note(note_path, title=title, video_path=video, lines=lines)
    print(f"OK: {note_path}")
    return note_path


def main() -> None:
    p = argparse.ArgumentParser(
        description="本地视频完整路径 → Whisper → raw-video 笔记（无 srt 残留）"
    )
    p.add_argument(
        "video",
        nargs="?",
        type=Path,
        help="视频完整路径，例如 C:\\path\\to\\xx.mp4",
    )
    p.add_argument(
        "--outdir",
        type=Path,
        default=DEFAULT_OUT,
        help=f"笔记输出目录（默认 {DEFAULT_OUT}）",
    )
    p.add_argument(
        "--list",
        metavar="DIR",
        type=Path,
        help="列出目录下 mp4 后退出",
    )
    args = p.parse_args()

    if args.list is not None:
        if not args.list.is_dir():
            print(f"不是目录: {args.list}")
            sys.exit(1)
        for f in sorted(args.list.glob("*.mp4")):
            print(f)
        return

    if not args.video:
        p.print_help()
        print("\n示例:")
        print(
            "  python scripts/video_to_note.py "
            r'"C:\Users\HP\Codes\_Externals\Videos\芋道源码\OAuth2.0 授权 01：xxx.mp4"'
        )
        sys.exit(1)

    video = args.video
    if not video.is_file():
        print(f"文件不存在: {video}")
        sys.exit(1)

    process_one(video, args.outdir)


if __name__ == "__main__":
    main()
