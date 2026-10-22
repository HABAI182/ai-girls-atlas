# 数据入口

资料主要采集于2026-10-20至21日；目录维护于2026-10-22，具体来源日期保留在各条记录。`characters`的单位混合产品、模型家族、工具和平台，用`entity_kind`明确区分。`status=wanted`没有已确认形象；`visual_lead`或`external_work_lead`只有作品线索；`profile_and_references`有文字档案和外链；`local_assets`有本地图片。

| 文件 | 用途 |
| --- | --- |
| characters.json / characters.csv | 角色、识别点、版本规则、来源关系 |
| assets.json / assets.csv | 本地图片的作者、文件、大小、SHA256、许可与供应方 |
| references.json | 外部作品与图库参考；不等同于本地文件 |
| videos.json / videos.csv | 视频元数据、题材和观察范围 |
| memes.json / memes.csv | 少量作品导航；站点许可字段未升级为本库许可 |
| sources.json | 稳定来源ID、网址、日期和证据层级 |
| upstream-snapshots.json | 固定上游树与站点元数据统计 |
| coverage.json | 本库条目、图片与待补数，不是市场覆盖率 |
| corrections.json | 原图目视核对后纠正的上游角色误分类，保留原记录与依据 |

JSON是主记录，CSV为便于阅读的导出。数据中所有引用的source ID必须能在sources.json找到。`creative_options_original`为本库新写的创作建议，不能当作原作者原始设定。`license_as_recorded`与`license_type_as_recorded`仅表示来源怎么写。


本轮新增数据：

| 文件 | 用途 |
| --- | --- |
| variants.json / variants.csv | 按作者系列比较造型、关联图片与提示词 |
| projects.json | 参考GitHub项目与固定提交、固定提交与用途 |
| audio.json / audio.csv | 19条声音、歌曲与原曲来源；不含音频文件 |
| expressions.json / expressions.csv | 11张本地表情的情绪与对话用途 |
| source-updates.json | 重点来源的差异和去重处理，含TreapGoGo复用记录 |

Copilot校园项目未区分具体产品，使用独立条目copilot-school。variants是本轮扩写索引，不替代assets中的所有历史图片版本。

## 创作百科数据

| 文件 | 内容 |
| --- | --- |
| meme-encyclopedia.json | 10个梗的作品语境、变体与原始出处 |
| performances.json | 8位角色档案、31条观察及32格原创情境提案 |
| actions-props.json / relationships.json | 23条动作道具与17条作品关系 |
| production-kits.json | 同系列关联包及原文件/分发入口 |
| creators.json / design-history.json | 贡献者与公开版本节点 |
| cross-media.json | 16张实际图像观察与6个跨语种来源 |
| wardrobe-scenes.json | 各8种服装、场景及已有版本关联 |
| audio-observations.json | 6段机器解码/识别观察，无人耳听感或完整转录 |
| video-observations.json | 14篇补充抽帧观察与实际时间点 |
| collection-gaps.json | 8个补查方向及元宝已找到的作者分支 |
| reference-guides.json | 用户新给TreapGoGo视频到仓库/网站/画廊/投稿的关系 |
| encyclopedia-coverage.json | 本轮专题计数与原创素材数量 |

## 可用文件与直接音轨分析

| 文件 | 用途 |
| --- | --- |
| ready-packages.json | 14组实际ZIP目录、摘要及Release入口 |
| material-checks.json | 7项实际素材运行记录，含静态3D、Live2D与图集 |
| audio-performances.json | 6段原始音轨直接输入模型后的声音/演法摘要 |
| gap-followup.json | 3个新角色确认、StepFun/MiMo补充及新增检索记录 |

## 维护与导出

`coverage.json`是统一统计入口，完整数量见[当前统计](../docs/collection-status.md)。修改主JSON后运行`python scripts/generate_catalog.py`，同步角色索引、首页/视频/缺口统计和全部CSV。`package-rights.json`保存逐包许可范围、声明层级和未确定项。核心字段约束见[JSON Schema](../schemas/catalog.schema.json)，提交检查见[维护说明](../docs/maintenance.md)。
