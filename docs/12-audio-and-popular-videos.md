# 声音、歌曲与较热视频

更新于2026-10-21。本轮新增独立声音索引，收集音色候选、歌曲、翻唱、MV、朗读与上游原曲；保存来源关系和用途，不复制歌词。

## 声音来源与版本

| 入口 | 发布者 | 类型 | 值得参考什么 |
| --- | --- | --- | --- |
| [音色初始候选](https://www.bilibili.com/video/BV1PPYM6EEUR/) | 星落落_oi | 音色 | 作为音色方向的早期参考，不等于固定的TTS模型文件。 |
| [十种音色对比](https://www.bilibili.com/video/BV16NYS6ZE8H/) | 星落落_oi | 音色对比 | 比较候选声音的入口；各段主观听感留给试听。 |
| [音色迭代](https://www.bilibili.com/video/BV1vSYe6kESU/) | 星落落_oi | 音色 | 同作者后续版本，便于追踪选声过程。 |
| [《人是猫》翻唱](https://www.bilibili.com/video/BV1fYpn6SEk9/) | 星落落_oi | 翻唱 | 音色、角色动画、词曲作者分开记录。 |
| [《人是猫》上游原曲](https://www.bilibili.com/video/BV1Bfjq6LEDi/) | 张卡斯 | 原曲（非AI娘） | 张卡斯创作、洛天依演唱；原页提供伴奏入口。 |
| [Let Me Go一分钟版本](https://www.bilibili.com/video/BV1R5YL69EC5/) | 星落落_oi | 歌曲早期版本 | 作者简介说明未能稳定复现该音色，适合追踪版本来源。 |
| [Let Me Go改编版](https://www.bilibili.com/video/BV1XbY66nEWr/) | 罐装毕加索 | 歌曲改编 | 简介回链一分钟版本，分别署词、曲和背景形象。 |
| [Let Me Go对唱版](https://www.bilibili.com/video/BV13SYr6dEiQ/) | 星落落_oi | 歌曲版本 | 同名歌的另一演绎，不与其他MV视为同一原文件。 |
| [Let Me Go动画MV](https://www.bilibili.com/video/BV1pueU6cEfg/) | 星落落_oi | MV | 把声音与角色舞台演出放在同一版本观察。 |
| [Let Me Go温柔版本](https://www.bilibili.com/video/BV1gaeA6mEyJ/) | 星落落_oi | 音色变体 | 温柔是作者标题的描述；本轮不作实听音质结论。 |
| [《屏幕两端》](https://www.bilibili.com/video/BV1GZaN6DEBR/) | 八千女鬼- | 改编歌曲 | 原页标注星落落_oi音色及《燕无歇》改编关系。 |
| [DeepSeek语音展示](https://www.bilibili.com/video/BV1nJY26QEdV/) | earth五行 | 朗读演示 | 区别于演唱音色，原页未给可下载统一音库。 |
| [像素鲸鱼娘资讯播报](https://www.bilibili.com/video/BV1arpN6FEHv/) | AI鼓励师_悠一 | 合成播报线索 | 作者简介称Fish Audio苏晓晓配音、程序合成BGM；未试听，属于栏目用声。 |

本轮读取公开标题、简介与署名，没有对所有候选完整试听，故不把标题中的“最温柔”“SSR”写成实听结论。声音条目的机器记录在[audio.json](../data/audio.json)，便览版为[audio.csv](../data/audio.csv)。

### 《人是猫》的来源链

星落落_oi的翻唱简介直接列出张卡斯原曲、蒙德砍壬动画、SSR大肥鱼音色和ZipZipPipe形象。因此至少有词曲、声音演绎、动画和形象四种贡献。原曲是洛天依作品，保留在声音上游里，未作为一位新“AI娘”扩充角色数。

重点仓库新增的`DeepSeek娘_人声.mp3`来自该翻唱成片的分离人声。它是声音参考文件，并不等于训练好的音色模型；图像的CC许可也不覆盖它。本库登记[上游文件说明](https://github.com/shuaizenge/ai-girls/tree/dcd69f5f4f2dff1a9c0031e82deb49e0fe949c76/characters/deepseek)和[原视频](https://www.bilibili.com/video/BV1fYpn6SEk9/)，不重复上传该声音。

### Let Me Go为何要按版本保存

“一分钟纯享”“重新编曲”“用户对唱”“动画MV”和“柔和版本”可能共用歌名，但不是同一个制作阶段。罐装毕加索的改编简介回链一分钟版本，并分别署词、曲和背景。保留这些关系，比把每条都叫“原版大肥鱼声音”更方便继续取材。

另有[Let Me Go专题](https://render.xiaoke.ai/challenges/let-me-go)可发现不同制作人的演绎。专题的作品评分与B站播放统计是两种信息，不能合成“全网公认最佳”。

### 声音条目还可以补什么

短句、对话、长读、哼唱和完整歌曲的用途不同。今后发现作者提供的干音、伴奏、音色模型或预设，可以在同一条目下新增对应文件类型；目前仅标题有“音色”二字的作品，不据此填入模型名称或可下载权重。选声优先回作者原作品试听，同一角色可以保留多个作者的声音版本。

## 本轮较热视频候选

以下按2026-10-21公开API返回的单条播放数排序，只在本轮取得统计的候选内比较。没有把合集播放量当作单条播放量；《人是猫》原曲属于声音上游，未混入下表。部分旧视频只有首轮元数据，未为凑排名全部重抓。

| 视频 | 作者 | 播放快照 | 时长 | 参考方向 |
| --- | --- | ---: | ---: | --- |
| [琵琶曲 | 大肥鱼 vs 豆包](https://www.bilibili.com/video/BV1MNYy6WEgY/) | 小猪P_ | 2,919,195 | 1:12 | 双角色对照、音乐节奏与造型识别 |
| [deepseek 翻唱《人是猫》真完整版，大肥鱼觉得人和猫一样可爱,所以人是猫](https://www.bilibili.com/video/BV1fYpn6SEk9/) | 星落落_oi | 2,412,023 | 2:15 | 声音来源、翻唱与角色MV |
| [大肥鱼 炸盆子](https://www.bilibili.com/video/BV15X3n6mEWy/) | 蒙德砍壬 | 1,761,016 | 0:16 | 极短动作、道具与反应 |
| [大肥鱼Let me go 首支mv！出道进度（1/10）](https://www.bilibili.com/video/BV1pueU6cEfg/) | 星落落_oi | 892,325 | 3:39 | 声音到动画MV的转化 |
| [音鲸干活唱歌1分钟纯享版](https://www.bilibili.com/video/BV1R5YL69EC5/) | 星落落_oi | 859,440 | 1:01 | 早期音色与歌曲版本 |
| [【白饭决战】大肥鱼VS梁圣](https://www.bilibili.com/video/BV1gVJe6cEVU/) | 小猪P_ | 666,392 | 1:49 | 对战二创、动作与戏剧冲突 |
| [Let me go大肥鱼和用户深情对唱](https://www.bilibili.com/video/BV13SYr6dEiQ/) | 星落落_oi | 631,983 | 3:39 | 用户与角色的对唱演绎 |
| [各AI娘形象盘点](https://www.bilibili.com/video/BV14phK66Ejw/) | 想看故事的lazy | 560,394 | 0:45 | 多角色盘点及署名回溯 |
| [一发入魂！ssr大肥鱼音色！](https://www.bilibili.com/video/BV1PPYM6EEUR/) | 星落落_oi | 421,622 | 0:11 | 音色初始参考 |
| [[AI] 大肥鱼摸鱼歌《Let Me Go》](https://www.bilibili.com/video/BV1XbY66nEWr/) | 罐装毕加索 | 414,013 | 2:06 | 角色演出、声音或主题参考 |
| [大肥鱼工作摸鱼歌，10种音色你喜欢哪个？](https://www.bilibili.com/video/BV16NYS6ZE8H/) | 星落落_oi | 373,584 | 1:41 | 多音色比较 |
| [终于把音鲸的音色熔炼完成了！](https://www.bilibili.com/video/BV1vSYe6kESU/) | 星落落_oi | 295,438 | 0:21 | 角色演出、声音或主题参考 |
| [【10月新番】败犬AI太多了！ 正式PV【4K】](https://www.bilibili.com/video/BV1Nfag6xEHQ/) | ScientificNNChan | 149,978 | 3:02 | 角色演出、声音或主题参考 |
| [deepseek语音 大肥鱼每次读出来的语气都不一样呢😍](https://www.bilibili.com/video/BV1nJY26QEdV/) | earth五行 | 121,692 | 0:47 | 角色演出、声音或主题参考 |

这些数值是读取时的快照，后续可能增长。热门程度用于决定先研究哪些作品，不当作角色设计的统一标准。三条超过百万的候选横跨音乐对照、翻唱MV和短动作，说明素材仓可以同时从声音、道具、动作和人物组合扩充，而不只搜静态立绘。

## 声音署名的简短模板

```text
角色版本：作者与参考图入口
音色/演唱：制作者、具体作品或模型预设
词曲/编曲：各自作者与原曲入口
动画/MV：制作者与作品入口
用途：试听参考 / 已开放文件 / 作者许可范围
```

只填已经找到的字段。这样不需要繁重表单，也能在以后增加配音、音效或素材包时继续接上来源。


## 新增独立视频栏目

已补入[18类视频与23篇画面案例](../videos/README.md)，包括音乐MV、关系短剧、合租群像、单梗、换装、MMD/Live2D、像素主持、游戏与实体化方法。每篇附原片时间点。另有[12条模型、桌面、声音和流程入口](../videos/materials.md)，已有声音记录沿用，不重复建立同名音色。当前音频仍未试听；模型包和工坊入口的未取项见该页。


## 创作百科扩充

已接入[完整专题与新作品大类](../encyclopedia/README.md)。声音来源现为19条，另有[六段实际音轨分析](../encyclopedia/formats/audio.md)；工程与模型新增具体分发入口，见[素材关联包](../encyclopedia/production/README.md)。
