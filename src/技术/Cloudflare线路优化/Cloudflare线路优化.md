---
layout: post
title: Cloudflare线路优化
slug: gitpage-cloudflare
date: 2020-02-10
status: publish
author: 无尽藏海
categories: 
  - 技术
tags:
  - Gitpage
  - Cloudflare
excerpt: 使用CNAME接入Cloudflare实现线路优化
---

[notice]去年用Hexo简单配置了一个博客，但是访问速度很不理想(特指移动宽带)。绑定免费域名套上CDN后有所改善，然而好景不长，域名到期后开始收费(特指Freenom)，遂放弃。后来找到Maverick搭建Gitpage，决定好好利用一下，在博客优化上做点功夫。所有技术及工具均来自网络，我只是一名搬运工哈哈。[/notice]

网上很多优化教程都是针对CF基础功能的配置，治标不治本。后来找到使用CNAME替代NS接入CF的方法，比较适用于国内，也是我推荐的。一开始我真没搞懂“CNAME接入”是什么意思😆我寻思这Cloudflare（简称CF）本身就有CNAME了啊。后来明白其实是为了**用DNS(国内)替代DNS(CF)，这样就能自定义要指向的DNS(CF)节点，从而我们可以挑选国内访问较稳定的节点**。

即由：用户->DNS(CF)->随机CDN(CF)->Github

改成：用户->DNS(国内)->自定CDN(CF)->Github

## 原理探究

### 问题

![2、3、5、8相对不畅通](assets/Cloudflare-1.webp)

那么为什么要放弃使用DNS(CF)呢？因为在大陆会产生如下两个问题：

**1.DNS解析缓慢（对应2、3）**

DNS将域名转换为IP地址，充当互联网的地址簿。当用户输入网站域名时，该查询通常会转到递归DNS以查找相应的计算机地址。如果递归DNS未查询到，则会向权威DNS查询，权威DNS将该域名映射的IP地址给本地。最后本地服务器将获取到的IP返回给用户，并进行网站访问。所以域名的NS在国外的话，解析速度会变慢。

**2.连接CDN不畅通（对应5、8）**

免费用户无法指定CDN节点，大陆用户用DNS(CF)解析域名，经常会返回美国IP，造成国内访问不畅，响应慢，间歇性丢包。

### 对策

#### CNAME接入CF

![](assets/Cloudflare-2.webp)

CNAME接入后我们可以在本地DNS设定优选CDN的IP，DNS(国内)就不必去DNS(CF)寻找，用户可以很快得到优选CDN的IP，并与其畅通地交换数据。

PS：虽然说的是“CNAME接入CDN(CF)”，但在设置DNS(国内)解析记录时却是使用的A记录，目的是为了更自由地选择CDN节点。

#### CDN缓存静态文件(可选)

这一步可有可无，推荐静态博客使用。主机用户可用CP面板免费提供的Railgun动态加速。

![](assets/Cloudflare-3.webp)

---

## 动手改造

![方法流程](assets/step.webp)

CF没有对免费用户开放CNAME接入，但是可以使用Cloudflare Partner（简称CP）曲线救国，我用的是[笨牛网](https://cdn.bnxb.com)。步骤如下：

### Cloudflare Partner配置

1.若未在官网申请过域名接入，可直接在CP**添加域名**。回源地址，静态博客(Gitpage)可以直接填写域名，如果使用自用主机，回源地址先不必填，提交后到“解析管理”把默认生成的CNAME记录改成A记录（IP方式回源）。

![](assets/2020-02-11-10-56-35.png)

2.若已在CF中添加过域名，可在**域名列表**中找到并到**解析设置**中选择**接入本站CNAME**即可

![](assets/2020-02-11-10-48-23.png)

### DNS(国内)解析设置

若曾把域名的DNS服务器改为CF，需要在域名面板还原，或另选DNS服务商，最好是国内的。没改过就不必动啦。我的域名是在万网买的，所以直接用了阿里云的DNS。

在DNS**解析设置**添加一个记录，主机记录就随意啦，但是**要和CP面板保持一致**。**记录值**是重点，也就是我们要指定的CDN的IP。可以到网上搜索稳定的CDN节点。推荐两个列表：[Cloudflare指定IP集合](https://wzfou.com/question/11632/)和[Cloudflare 推荐节点IP](https://www.iamhippo.com/2019-06/866.html)，百度云合作节点或者1.0.0.1也不错。可以只指定默认线路，也可针对移动、联通、电信分设不同记录值。

![](assets/2020-02-11-11-16-23.png)

至此DNS的配置就结束了，等其生效即可。

### CDN缓存优化

#### 缓存静态内容

适用于静态博客(Gitpage)，Wordpress用户请搜索排除后端程序的规则。页面规则(Page Rules)添加一条规则，用来缓存所有内容。

![](assets/2020-02-11-16-51-15.png)

#### 压缩HTML、CSS、JS

“Speed”->“Optimization”->“Auto Minify”选中HTML、CSS、JS。

---

## 后记

在万网买了域名之后，原想备案后白嫖国内CDN，结果备案还要买三个月主机🤦‍♂️本来是只想加速Gitpage的说。罢了罢了，只能接着用Cloudflare，网上发现了CNAME教程，就索性整理一下。CNAME接入需要定位到稳定的CDN节点才有好的效果，所以不是很完美，现在我的博客有时也会加载不出来，但是比原先好了不少。这是一个不靠谱的优化推荐😆用词及绘图有不正确的地方欢迎指出。
