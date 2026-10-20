# 数据入口

所有记录均为2026-10-20整理的快照。`characters`的单位混合产品、模型家族、工具和平台，用`entity_kind`明确区分。`status=wanted`没有已确认形象；`visual_lead`只有作品线索；`profile_and_references`有文字档案和外链；`local_assets`有本地图片。

| 文件 | 用途 |
| --- | --- |
| characters.json / characters.csv | 角色、识别点、版本规则、来源关系 |
| assets.json / assets.csv | 本地图片的作者、文件、大小、SHA256、许可与供应方 |
| references.json | 外部44项图库参考；不等同于本地文件 |
| videos.json / videos.csv | 视频元数据、题材和观察范围 |
| memes.json / memes.csv | 少量作品导航；站点许可字段未升级为本库许可 |
| sources.json | 稳定来源ID、网址、日期和证据层级 |
| upstream-snapshots.json | 固定上游树与站点元数据统计 |
| coverage.json | 本库条目、图片与待补数，不是市场覆盖率 |
| corrections.json | 原图目视核对后纠正的上游角色误分类，保留原记录与依据 |

JSON是主记录，CSV为便于阅读的导出。数据中所有引用的source ID必须能在sources.json找到。`creative_options_original`为本库新写的创作建议，不能当作原作者原始设定。`license_as_recorded`与`license_type_as_recorded`仅表示来源怎么写。
