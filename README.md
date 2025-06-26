# speedtest.net-CN-ID

[![Update](https://github.com/spiritLHLS/speedtest.net-CN-ID/actions/workflows/main.yml/badge.svg)](https://github.com/spiritLHLS/speedtest.net-CN-ID/actions/workflows/main.yml)



## 说明

数据每天更新一次，感谢官方测速站点提供的服务

这里只展示部分地区的节点信息(全部CN地区和部分全球地区)，含 speedtest.net 的测速地址，且只保证节点列表的可用性而不是完整性，官网说有1.6万个节点我只爬了1.4万个左右

定期自动更新爬取到的测速节点ID，闭源爬虫，自动推送

闭源收录服务器数量(实时)：13965

数据更新时间: 2025/06/26

### 对应 [speedtest.net](https://www.speedtest.net/) 的自动更新测速服务器ID的测速脚本

```
bash <(wget -qO- bash.spiritlhl.net/ecs-net)
```

或

```
bash <(wget -qO- --no-check-certificate https://github.com/spiritLHLS/ecsspeed/raw/main/script/ecsspeed-net.sh)
```

或国内用

```
bash <(wget -qO- --no-check-certificate https://ghproxy.com/https://raw.githubusercontent.com/spiritLHLS/ecsspeed/main/script/ecsspeed-net.sh)
```

<details>

支持测速的架构：i386, x86_64, amd64, arm64, s390x, riscv64, ppc64le, ppc64

涵盖中国三大运营商、香港、台湾的测速节点，默认的三网测速每个运营商选择本机ping值最低的两个节点测速，详情三网测速才是全测，节点列表大概每7天自动更新一次。

支持国内服务器测试(有判断是否为国内机器)，但由于国内服务器带宽过小，会很慢，详见初次运行的显示

当官方CLI安装失败(如罕见的架构或者官方网站访问失败时)自动使用 [speedtest-go](https://github.com/showwin/speedtest-go) 作为替代品测速

</details>

## 交流

https://t.me/spiritlhl_bot

# 免责声明

* 本仓库仅供学习使用。
* 不可用于商业以及非法目的，使用本仓库代码产生的一切后果, 作者不承担任何责任。
* 本仓库链接仅网络收集，侵权告知必删，使用相关链接产生的一切后果，作者不承担任何责任。

## Special statement:

Any unlocking and decryption analysis scripts involved in the Script project released by this warehouse are only used for testing, learning and research, and are forbidden to be used for commercial purposes. Their legality, accuracy, completeness and effectiveness cannot be guaranteed. Please make your own judgment based on the situation. .

All resource files in this project are forbidden to be reproduced or published in any form by any official account or self-media.

This warehouse is not responsible for any script problems, including but not limited to any loss or damage caused by any script errors.

Any user who indirectly uses the script, including but not limited to establishing a VPS or disseminating it when certain actions violate national/regional laws or related regulations, this warehouse is not responsible for any privacy leakage or other consequences caused by this.

Do not use any content of the Script project for commercial or illegal purposes, otherwise you will be responsible for the consequences.

If any unit or individual believes that the script of the project may be suspected of infringing on their rights, they should promptly notify and provide proof of identity and ownership. We will delete the relevant script after receiving the certification document.

Anyone who views this item in any way or directly or indirectly uses any script of the Script item should read this statement carefully. This warehouse reserves the right to change or supplement this disclaimer at any time. Once you have used and copied any relevant scripts or rules of the Script project, you are deemed to have accepted this disclaimer.

