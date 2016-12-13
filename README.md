# SpecifyDynamicIPAccess
指定动态ip访问apache网站
### 应用场景
如果您在办公室内远程访问svn、phpmyadmin、OA等内部应用，而办公室是动态ip，无法在apache限制ip访问，那么本工具可以而帮助您动态更新您的ip到apache配置文件中。
### 实现原理
1. 百度搜索IP，获取本地公网IP  
2. 通过浏览器访问的方式将IP和Key发送给服务端程序  
3. 服务器程序获取到IP和Key，验证Key是否正确，正确则更新apache配置，然后reload apache  
4. Key的值为当前时间（24进制）的小时  

### 使用方法
#### 服务器端
1. 服务端安装**python2.7**、**apache**
2. 配置工具
```shell
cd /var/www/cgi-bin
git clone https://github.com/X-Mars/SpecifyDynamicIPAccess.git
chmod +x UpgradeWhiteList.py
```
3. 服务器visudo,给apache用户reload httpd的权限  
```shell
visudo
```
添加一下一行   
```conf
www ALL=(root) NOPASSWD: /etc/init.d/httpd
```

4. 客户端浏览器访问    
http://xxx.xxx.com/cgi-bin/UpgradeWhiteList.py?IP=144.144.144.144&Key=21

### 不足
1. 由于程序是挂载apache下面的，因此不能使用**service httpd restart**，只能用reload
2. 也是由于程序是挂载apache下面的，所以访问链接后，页面会显示无法打开，因为reload的时候，apache关闭了连接进程

