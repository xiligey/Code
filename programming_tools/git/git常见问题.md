# 1、解决git的pull和push每次都需要输入密码的问题

如果我们git clone的下载代码的时候是连接的https://而不是git@git (ssh)的形式，当我们操作git pull/push到远程的时候，总是提示我们输入账号和密码才能操作成功，频繁的输入账号和密码会很麻烦。

解决办法：

git bash进入你的项目目录，输入：

git config --global credential.helper store

然后你会在你本地生成一个文本，上边记录你的账号和密码。当然这些你可以不用关心。

然后你使用上述的命令配置好之后，再操作一次git pull，然后它会提示你输入账号密码，这一次之后就不需要再次输入密码了。



# 2、git添加子模块时报错【已经存在于索引中】

添加一个新的子模块时报错【已经存在于索引中】：

```bash
git submodule add <https://github.com/xiligey/ruby_basic.git>

'ruby_basic' 已经存在于索引中
```

解决方案：

- `git ls-files --stage ~/Study`

查看已添加了的子模块，发现确实存在 `ruby_basic`

- `git rm --cached ruby_basic`删掉已添加的子模块，然后重新添加即可