# demo18-lyricsDownloader-Netease
[![Github](https://img.shields.io/badge/Github-https%3A%2F%2Fgithub.com%2FZichen3317%2Fdemo18--lyrics--downloader--netease-green)](https://github.com/Zichen3317/demo18-lyrics-downloader-netease)
[![Version](https://img.shields.io/badge/Version-0.2.0-blue)]()
#### 介绍
lyricsDownloader 是一个下载歌词的小脚本    

#### 🛠功能
1. 支持通过网易云音乐分享链接直接下载单曲/歌单歌曲（非专辑，专辑歌曲下载未实装）的歌词  
所用API通过Vercel托管，感谢Bingaryify大佬的教程！  
[这是所参考的大佬的github项目](https://github.com/Binaryify/NeteaseCloudMusicApi)  
[大佬的API文档](https://binaryify.github.io/NeteaseCloudMusicApi/#/)
2.  **新增** 支持通过QQ音乐分享链接直接下载单曲的歌词
所用获取歌词API系 **QQ音乐官方API**,其他歌曲信息如歌曲名和歌手名通过自制爬虫获取

#### 🔧报错说明
1. 【歌曲名称错误！下载歌词文件后请自行更改歌词文件名！】  
因为有一些歌曲的歌曲名or歌手名（多个歌手的时候）里有 **/** 导致程序写入歌词文件时报错，故折中的方法是将 **/**改为 **,**再进行写入  
 出现此报错后请在歌词文件生成后自行将**,**改为 **/**以免歌词文件无法被播放器识别（播放器识别歌词文件是按照歌词文件名的，如果不符则识别不到）
  推荐使用[ **Utools** ](https://u.tools/)中的 **批量重命名**功能，快捷又简便👍 

#### 温馨提示
1. 目前仅支持 **网易云音乐** |  **QQ音乐** 
2. 目前仅支持上架的音乐，不支持 **已下架/纯音乐（无歌词）/云盘音乐** 