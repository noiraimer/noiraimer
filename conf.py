# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
#template = {
#    "name": "Maverick-Theme-Galileo",
#    "type": "local",
#    "path": "../Maverick-Theme-Galileo"
#}
template = {
    "name": "Galileo",
    "type": "git",
    "url": "https://github.com/noiraimer/Galileo-custom.git",
    "branch": "latest"
}
enable_jsdelivr = {
    "enabled": True,
    "repo": "noiraimer/blog@gh-pages"
}

# 站点设置
site_name = "解语知音"
site_logo = "${static_prefix}logo.png"
site_build_date = "2020/1/31 16:51"
author = "无尽藏海"
email = "liushu1187419589@live.com"
author_homepage = "https://noiramr.cn"
description = "温故而知新"
key_words = ['blog']
language = 'zh-CN'
external_links = [
    {
        "name": "友情链接",
        "url": "${site_prefix}friends/",
        "brief": "山水会知音",
        "target": "_self"
    },
    {
        "name": "朝花夕拾",
        "url": "https://noiramr.cn/archives/day",
        "brief": "我思故我在",
        "target": "_self"
    },
    {
        "name": "解语知识",
        "url": "https://wiki.noiramr.cn",
        "brief": "学而时习之",
        "target": "_blank"
    }

]
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "RSS",
        "url": "https://noiramr.cn/feed/index.xml",
        "icon": ""
    },
    {
        "name": "GitHub",
        "url": "https://github.com/noiraimer",
        "icon": ""
    },
        {
        "name": "邮件",
        "url": "mailto:liushu1187419589@live.com",
        "icon": ""
    },
    {
        "name": "语雀",
        "url": "https://www.yuque.com/blancaimer",
        "icon": ""
    },
]

valine = {
    "enable": True,
    "el": '#vcomments',
    "appId": "KgL1pm7KXVOK7PlT4SFO8vYJ-9Nh9j0Va",
    "appKey": "dkFFObbxzdOEUUccBaq0Oxsp",
    "placeholder": "说点什么，昵称可填QQ号，上述信息均可留空。",
    "comment_count": "true",
    "visitor":  "true",
    "emojiCDN": 'https://i0.hdslb.com/bfs/emote/', 
    "enableQQ": "true"
}

head_addon = r'''
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/noiraimer/blog@gh-pages/css/custom-0001.css">
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
<link rel="dns-prefetch" href="//noiramr.cn" />
<link rel="shortcut icon" href="${static_prefix}favicon.ico?v=yyLyaqbyRG">
<script src="https://cdn.jsdelivr.net/npm/hls.js/dist/hls.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/dplayer/dist/DPlayer.min.js"></script>
'''

footer_addon = r'''

'''

body_addon = r'''
<script src="${static_prefix}js/instant.js" type="module" defer integrity="sha384-OeDn4XE77tdHo8pGtE1apMPmAipjoxUQ++eeJa6EtJCfHlvijigWiJpD7VDPWXV1"></script>
<script src="${static_prefix}js/email-decode.min.js"></script>
'''
main_addon = r'''

'''
