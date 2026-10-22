# 目录维护与自动检查

[数据入口](../data/README.md) · [当前统计](collection-status.md)

JSON为主记录，CSV与标记统计块为导出。新增或改动时先更新主数据及`data/coverage.json`，再运行：

```bash
python -m pip install -r requirements-checks.txt
python scripts/generate_catalog.py
python scripts/generate_catalog.py --check
python scripts/check_catalog.py
python scripts/verify.py
```

`generate_catalog.py`生成角色索引、首页/视频/缺口统计、完整统计页和CSV；`--check`只比较，不修改文件。尚未进行画面分类的视频仍导出到CSV，留空主品类并说明观察用途。

`check_catalog.py`对角色、图片、来源、视频、下载包和逐包许可记录应用[JSON Schema](../schemas/catalog.schema.json)，并检查重复来源网址、图片路径与逐包许可覆盖。`verify.py`继续检查实际文件大小/SHA256、ID关系、内部Markdown链接和主数据统计。

[GitHub Actions工作流](../.github/workflows/catalog.yml)在main推送与PR时运行这三项检查，也可手动运行。流程使用只读仓库权限，不下载或执行第三方素材工程。通过表示库内记录满足这些约束，不等于视频完整观看、模型实机验收或作者权利独立核实。

更改统计需同时改主记录；历史日期的采样记录保留原日期。新增下载包要补`package-rights.json`，注明适用素材、许可原文、声明层级、应保留的说明与未确定项。
