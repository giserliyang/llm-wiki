# 全局链接索引

每张表 **动态列出当前 wiki 内全部页**；新摄入后自动出现，无需手改。

## 概念

```dataview
LIST
FROM "wiki/concepts"
SORT file.name ASC
```

## 对比 / 实体 / 实践 / 决策

```dataview
LIST
FROM "wiki/comparisons" OR "wiki/entities" OR "wiki/practice" OR "wiki/decisions"
SORT file.name ASC
```

## 按 source（教程 vs 数据分析）

```dataview
TABLE rows.file.link AS "页"
FROM "wiki"
WHERE source
GROUP BY source
```

## 互链体检（互相链接的 wiki 页）

> 同主题跨页应有 `[[页名]]`；全为「无入链」说明两套教程尚未织网。

```dataview
TABLE length(file.inlinks) AS "被链数", file.outlinks.length AS "出链数"
FROM "wiki/concepts" OR "wiki/comparisons" OR "wiki/entities" OR "wiki/practice"
WHERE !contains(file.path, "README") AND file.name != "overview" AND file.name != "links" AND file.name != "glossary"
SORT length(file.inlinks) DESC
```
