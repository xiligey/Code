格式： mysql -h主机地址 -u用户名－p用户密码

1、例1：连接到本机上的MYSQL

一般可以直接键入命令

```bash
mysql -uroot -p1
```

回车后提示你输密码，如果刚安装好MYSQL，超级用户root是没有密码的，故直接回车即可进入到MYSQL中了，MYSQL的提示符是：mysql>

2、连接到远程主机上的MySQL

假设远程主机的IP为：10.0.0.1，用户名为root,密码为123。则键入以下命令：

```bash
mysql -h10.0.0.1 -uroot -p1231
```

（注：u与root可以不用加空格，其它也一样）

3、退出MySQL命令

```bash
exit （回车）
```

