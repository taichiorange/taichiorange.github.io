( 参考了这个英文网站：https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-18-04）
第一步，缺省安装，对密码等没有做任何设置。数据库处于不安全状态。在后续步骤中会设置安全密码。

> $     sudo apt install mysql-server

第二步，设置密码，剔除一些不安全的缺省设置

> sudo mysql_secure_installation

修改 root 用户的安全验证机制，改为密码方式
> $ sudo mysql
> mysql>  SELECT user,authentication_string,plugin,host FROM mysql.user;
> mysql> ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '***password***';
> mysql> FLUSH PRIVILEGES;

检查 mysql 服务是否已经启动

> 
> systemctl status mysql.service
