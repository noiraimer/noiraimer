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
    "placeholder": "请畅所欲言，昵称可填QQ号（自动获取头像）或自定义，全部信息留空可匿名留言。",
    "comment_count": "true",
    "visitor":  "true",
    "enableQQ": "true",
    "serverURLs": "https://tab.leancloud.cn",
    "emojiMaps": {
                "阿部高和": "https://js2.a.yximgs.com/bs2/emotion/1585589497461third_party_b35232076.gif",
                "偷笑": "https://ali2.a.yximgs.com/bs2/emotion/1585589499179third_party_b35232117.gif",
                "闪": "https://js2.a.yximgs.com/bs2/emotion/1585589497940third_party_b35232087.gif",
                "哭笑不得": "https://tx2.a.yximgs.com/bs2/emotion/1585589498975third_party_b35232110.gif",
                  "tv_doge": "https://i0.hdslb.com/bfs/emote/6ea59c827c414b4a2955fe79e0f6fd3dcd515e24.png",
                  "tv_亲亲": "https://i0.hdslb.com/bfs/emote/a8111ad55953ef5e3be3327ef94eb4a39d535d06.png",
                  "tv_偷笑": "https://i0.hdslb.com/bfs/emote/bb690d4107620f1c15cff29509db529a73aee261.png",
                  "tv_再见": "https://i0.hdslb.com/bfs/emote/180129b8ea851044ce71caf55cc8ce44bd4a4fc8.png",
                  "tv_冷漠": "https://i0.hdslb.com/bfs/emote/b9cbc755c2b3ee43be07ca13de84e5b699a3f101.png",
                  "tv_发怒": "https://i0.hdslb.com/bfs/emote/34ba3cd204d5b05fec70ce08fa9fa0dd612409ff.png",
                  "tv_发财": "https://i0.hdslb.com/bfs/emote/34db290afd2963723c6eb3c4560667db7253a21a.png",
                  "tv_可爱": "https://i0.hdslb.com/bfs/emote/9e55fd9b500ac4b96613539f1ce2f9499e314ed9.png",
                  "tv_吐血": "https://i0.hdslb.com/bfs/emote/09dd16a7aa59b77baa1155d47484409624470c77.png",
                  "tv_呆": "https://i0.hdslb.com/bfs/emote/fe1179ebaa191569b0d31cecafe7a2cd1c951c9d.png",
                  "tv_呕吐": "https://i0.hdslb.com/bfs/emote/9f996894a39e282ccf5e66856af49483f81870f3.png",
                  "tv_困": "https://i0.hdslb.com/bfs/emote/241ee304e44c0af029adceb294399391e4737ef2.png",
                  "tv_坏笑": "https://i0.hdslb.com/bfs/emote/1f0b87f731a671079842116e0991c91c2c88645a.png",
                  "tv_大佬": "https://i0.hdslb.com/bfs/emote/093c1e2c490161aca397afc45573c877cdead616.png",
                  "tv_大哭": "https://i0.hdslb.com/bfs/emote/23269aeb35f99daee28dda129676f6e9ea87934f.png",
                  "tv_委屈": "https://i0.hdslb.com/bfs/emote/d04dba7b5465779e9755d2ab6f0a897b9b33bb77.png",
                  "tv_害羞": "https://i0.hdslb.com/bfs/emote/a37683fb5642fa3ddfc7f4e5525fd13e42a2bdb1.png",
                  "tv_尴尬": "https://i0.hdslb.com/bfs/emote/7cfa62dafc59798a3d3fb262d421eeeff166cfa4.png",
                  "tv_微笑": "https://i0.hdslb.com/bfs/emote/70dc5c7b56f93eb61bddba11e28fb1d18fddcd4c.png",
                  "tv_思考": "https://i0.hdslb.com/bfs/emote/90cf159733e558137ed20aa04d09964436f618a1.png",
                  "tv_惊吓": "https://i0.hdslb.com/bfs/emote/0d15c7e2ee58e935adc6a7193ee042388adc22af.png",
                  "tv_打脸": "https://i0.hdslb.com/bfs/emote/56ab10b624063e966bfcb76ea5dc4794d87dfd47.png",
                  "tv_抓狂": "https://i0.hdslb.com/bfs/emote/fe31c08edad661d63762b04e17b8d5ae3c71a757.png",
                  "tv_抠鼻": "https://i0.hdslb.com/bfs/emote/c666f55e88d471e51bbd9fab9bb308110824a6eb.png",
                  "tv_斜眼笑": "https://i0.hdslb.com/bfs/emote/911f987aa8bc1bee12d52aafe62bc41ef4474e6c.png",
                  "tv_无奈": "https://i0.hdslb.com/bfs/emote/ea8ed89ee9878f2fece2dda0ea8a5dbfe21b5751.png",
                  "tv_晕": "https://i0.hdslb.com/bfs/emote/5443c22b4d07fb1907ccc610c8e6db254f2461b7.png",
                  "tv_流汗": "https://i0.hdslb.com/bfs/emote/cead1c351ab8d79e9f369605beb90148db0fbed3.png",
                  "tv_流泪": "https://i0.hdslb.com/bfs/emote/7e71cde7858f0cd50d74b0264aa26db612a8a167.png",
                  "tv_流鼻血": "https://i0.hdslb.com/bfs/emote/c32d39db2737f89b904ca32700d140a9241b0767.png",
                  "tv_点赞": "https://i0.hdslb.com/bfs/emote/f85c354995bd99e28fc76c869bfe42ba6438eff4.png",
                  "tv_生气": "https://i0.hdslb.com/bfs/emote/26702dcafdab5e8225b43ffd23c94ac1ff932654.png",
                  "tv_生病": "https://i0.hdslb.com/bfs/emote/8b0ec90e6b86771092a498c54f09fc94621c1900.png",
                  "tv_疑问": "https://i0.hdslb.com/bfs/emote/0793d949b18d7be716078349c202c15ff166f314.png",
                  "tv_白眼": "https://i0.hdslb.com/bfs/emote/c1d59f439e379ee50eef488bcb5e5378e5044ea4.png",
                  "tv_皱眉": "https://i0.hdslb.com/bfs/emote/72ccad6679fea0d14cce648b4d818e09b8ffea2d.png",
                  "tv_目瞪口呆": "https://i0.hdslb.com/bfs/emote/0b8cb81a68de5d5365212c99375e7ace3e7891b7.png",
                  "tv_睡着": "https://i0.hdslb.com/bfs/emote/8b196675b53af58264f383c50ad0945048290b33.png",
                  "tv_笑哭": "https://i0.hdslb.com/bfs/emote/1abc628f6d4f4caf9d0e7800878f4697abbc8273.png",
                  "tv_腼腆": "https://i0.hdslb.com/bfs/emote/89712c0d4af73e67f89e35cbc518420380a7f6f4.png",
                  "tv_色": "https://i0.hdslb.com/bfs/emote/61822c7e9aae5da76475e7892534545336b23a6f.png",
                  "tv_调侃": "https://i0.hdslb.com/bfs/emote/4bc022533ef31544ca0d72c12c808cf4a1cce3e3.png",
                  "tv_调皮": "https://i0.hdslb.com/bfs/emote/b9c41de8e82dd7a8515ae5e3cb63e898bf245186.png",
                  "tv_鄙视": "https://i0.hdslb.com/bfs/emote/6e72339f346a692a495b123174b49e4e8e781303.png",
                  "tv_闭嘴": "https://i0.hdslb.com/bfs/emote/c9e990da7f6e93975e25fd8b70e2e290aa4086ef.png",
                  "tv_难过": "https://i0.hdslb.com/bfs/emote/87f46748d3f142ebc6586ff58860d0e2fc8263ba.png",
                  "tv_馋": "https://i0.hdslb.com/bfs/emote/fc7e829b845c43c623c8b490ee3602b7f0e76a31.png",
                  "tv_鬼脸": "https://i0.hdslb.com/bfs/emote/0ffbbddf8a94d124ca2f54b360bbc04feb6bbfea.png",
                  "tv_黑人问号": "https://i0.hdslb.com/bfs/emote/45821a01f51bc867da9edbaa2e070410819a95b2.png",
                  "tv_鼓掌": "https://i0.hdslb.com/bfs/emote/1d21793f96ef4e6f48b23e53e3b9e42da833a0f6.png"}
}

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
