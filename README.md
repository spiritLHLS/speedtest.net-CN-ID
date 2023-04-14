# speedtest.net-CN-ID

[![Update](https://github.com/spiritLHLS/speedtest.net-CN-ID/actions/workflows/main.yml/badge.svg)](https://github.com/spiritLHLS/speedtest.net-CN-ID/actions/workflows/main.yml)

## 说明

闭源爬虫代码版本(非仓库数据更新日期)：2023.03.30

定期自动更新爬取到的测速节点ID，闭源爬虫，自动推送

所有数据以国家代号或运营商划分 

CSV格式：
```
id country_code country city ip host port supplier
```

闭源收录服务器数量(实时)：13946

数据更新时间: 2023/04/13

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

支持测速的架构：i386, x86_64, amd64, arm64, s390x, riscv64, ppc64le, ppc64

涵盖中国三大运营商、香港、台湾的测速节点，默认的三网测速每个运营商选择本机ping值最低的两个节点测速，详情三网测速才是全测，节点列表大概每7天自动更新一次。

支持国内服务器测试(有判断是否为国内机器)，但由于国内服务器带宽过小，会很慢，详见初次运行的显示

当官方CLI安装失败(如罕见的架构或者官方网站访问失败时)自动使用 [speedtest-go](https://github.com/showwin/speedtest-go) 作为替代品测速

## 交流

admin@spiritlhl.net

## 赞助

https://afdian.net/a/spiritlhl/plan
