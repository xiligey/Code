# 配置数据库连接导致错误：主机“ xxxxxxx”不允许连接到该MySQL服务器

## 问题

navicat连接mysql时报错

```none
 Host '10.0.0.20' is not allowed to connect to this MySQL server
```

## 原因

发生此错误是由于您的MySQL数据库当前正在使用默认配置。当来自“本地主机”时，此配置仅允许来自“ root”用户的连接，而不允许其他IP地址范围。

## 解决方法

在必须使用“ root”用户的情况下，以下是针对上述情况的解决方法，但是**不建议这样**做，因为这会产生安全漏洞。有关此问题的建议解决方案，请参阅下面的**解决方案**。

- 打开你的MySQL终端；

    - 在Linux中：

        ```none
        mysql -u root -p
        ```

    - 在Windows中，打开MySQL命令行。

- 运行以下查询：

    ```none
    USE mysql;
    SELECT user,host FROM user;
    ```

    ![（信息）](https://confluence.atlassian.com/s/en_GB/7901/af536c7c6dffcc1d697b914b797aa7f2f306b4f8/_/images/icons/emoticons/information.svg) 注意：您将看到“ root”用户仅与“ localhost”主机相关

- 一旦确认root用户仅具有在localhost中的连接权限，请运行以下查询：

    ```none
    GRANT ALL PRIVILEGES ON *.* TO root@my_ip IDENTIFIED BY ‘root_password‘ WITH GRANT OPTION;
    ```

    ![（信息）](https://confluence.atlassian.com/s/en_GB/7901/af536c7c6dffcc1d697b914b797aa7f2f306b4f8/_/images/icons/emoticons/information.svg) 其中“ my_ip”是您的JIRA服务器IP，“ root_password”是root用户密码。

-  如果愿意，请再次运行第一个查询，以验证root用户是否具有JIRA服务器IP的连接权限；