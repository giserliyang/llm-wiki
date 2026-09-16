<%*
// 生成「阅读进度」：抓全部级别标题
// 显示为章节名，实际链到 [[笔记名#标题|标题]]
// 素材收件箱 TASK 里也能跳回教程

const file = app.workspace.getActiveFile();
if (!file) {
  new Notice("请先打开一篇教程笔记");
  return "";
}

const content = await app.vault.read(file);
const lines = content.split(/\r?\n/);
const noteName = file.basename;

let inCode = false;
const items = [];

for (const line of lines) {
  if (line.trim().startsWith("```")) {
    inCode = !inCode;
    continue;
  }
  if (inCode) continue;

  const m = line.match(/^(#{1,6})\s+(.+?)\s*$/);
  if (!m) continue;

  const level = m[1].length;
  const title = m[2];

  if (/^学习附录$/.test(title)) break;

  items.push({ level, title });
}

if (items.length === 0) {
  new Notice("未找到标题");
  return "";
}

const minLevel = Math.min(...items.map((i) => i.level));
const out = items.map((it) => {
  const depth = Math.max(0, it.level - minLevel);
  const indent = "\t".repeat(depth);
  // [[目标#标题|显示文字]] — 显示干净，跨文件可跳
  return `${indent}- [ ] [[${noteName}#${it.title}|${it.title}]]`;
});

tR += out.join("\n");
%>
