# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/noiraimer.github.io/"
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
    "repo": "noiraimer/noiraimer.github.io@gh-pages"
}

# 站点设置
site_name = "解语知音"
site_logo = "${static_prefix}logo.png"
site_build_date = "2020/1/31 16:51"
author = "无尽藏海"
email = "liushu1187419589@live.com"
author_homepage = "https://noiraimer.github.io/"
description = "温故而知新"
key_words = ['blog']
language = 'zh-CN'
external_links = [
    {
        "name": "友情链接",
        "url": "${site_prefix}friends/",
        "brief": "山水会知音",
        "target": "_self"
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
        "url": "https://noiraimer.github.io/feed/index.xml",
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

head_addon = r'''
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/noiraimer/blog@gh-pages/css/custom-0005.css">
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
<link rel="dns-prefetch" href="//noiramr.cn" />
<link rel="shortcut icon" href="${static_prefix}favicon.ico?v=yyLyaqbyRG">
<script src="https://cdn.jsdelivr.net/gh/noiraimer/blog@gh-pages/js/time-0005.js"></script>
<script src="https://cdn.jsdelivr.net/npm/hls.js/dist/hls.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/dplayer/dist/DPlayer.min.js"></script>
'''

footer_addon = r'''

'''

body_addon = r'''
<script src="//instant.page/5.0.1" type="module" integrity="sha384-0DvoZ9kNcB36fWcQApIMIGQoTzoBDYTQ85e8nmsfFOGz4RHAdUhADqJt4k3K2uLS"></script>
<script src="${static_prefix}js/email-decode.min.js"></script>
'''
main_addon = r'''

'''
