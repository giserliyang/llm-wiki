import re, json, sys

# Force UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\HP\Documents\llm_wiki\llm-wiki\raw\tutorials\Python教程\20260921_Python教程_尚硅谷.md', encoding='utf-8') as f:
    lines = f.readlines()

chapters = []
for i, line in enumerate(lines):
    m = re.match(r'^# 第\s*(\d+)\s章\s*(.+)$', line)
    if m:
        chapters.append({'num': int(m.group(1)), 'title': m.group(2).strip(), 'start_line': i+1})

for j, ch in enumerate(chapters):
    end = chapters[j+1]['start_line'] if j+1 < len(chapters) else len(lines)+1
    ch['end_line'] = end
    ch['lines'] = end - ch['start_line']

    sections = []
    for i in range(ch['start_line']-1, ch['end_line']-1):
        line = lines[i]
        m = re.match(r'^(#{1,3})\s+(.+)$', line)
        if m:
            sections.append({
                'level': len(m.group(1)),
                'title': m.group(2).strip(),
                'line': i+1
            })
    ch['sections'] = sections

print(json.dumps(chapters, ensure_ascii=False, indent=2))
