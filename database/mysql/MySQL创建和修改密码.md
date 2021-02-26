## 创建密码的三种方式

`mysqladmin -u root password "newpass"`

`mysql -u root`

`SET PASSWORD FOR 'root'@'localhost'=PASSWORD('newpassword');`

`mysql -u root`

`use mysql`

`UPDATE user SET password = PASSWORD('newpassword') WHERE user='root'`

`FLUSH PRIVILEGES`