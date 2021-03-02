## 切换远程仓库

切换远程仓库地址（3种方法皆可）

```bash
git remote set-url origin git@code.bizseer.com:algorithm/fastseer-core.git
git remote rm origin
git remote add origin git@code.bizseer.com:algorithm/fastseer-core.git
到项目根目录下，进入.git文件夹，找到config文件，修改其中的git remote origin地址即可
```

## 查看提交历史

`git log`
## 标签管理
### 创建一个标签
`git tag v1.0`

该命令会在当前commit创建一个标签

注意： 创建的标签默认只存储在本地，不会自动推送到远程。
### 创建标签时指定commit id
`git tag v1.1 f52c633`
### 查看所有标签
`git tag`
注意，标签不是按时间顺序列出，而是按字母排序
### 查看标签信息
`git show v1.1`
注意：标签总是和commit id挂钩，所以，如果这个commit既出现在了master分支，也出现在了dev分支，那么在这两个分支上都可以看到这个标签。
### 删除标签
删除本地标签 
`git tag -d v1.0`
删除远程标签

```bash
# 先删除本地标签
git tag -d v1.0
# 再删除远程标签
git push origin :refs/tags/v1.0
```

要看看是否真的从远程库删除了标签，可以登录github查看。
### 推送远程标签
推送单个标签
`git push origin v1.0`
推送全部标签
`git push origin --tags`

