#!/usr/local/python2.7/bin/python
#coding:utf-8
#Auther：火星小刘
#Email：xtlyk@163.com
#转载请保留出处

import re,cgi,cgitb,time,os



print "Content-type: text/html\n"
form = cgi.FieldStorage()
#从GET请其中获取IP和Key
IP = form.getvalue("IP")
Key = form.getvalue("Key")


#获取当前小时
Time = time.strftime("%H")

#更新apache配置文件
def UpdataFile():
   File = open("/etc/httpd/conf.d/apache-webui-cgi.conf","r+")
   FileRead = File.read()
   OldIP = re.findall('Allow from.*\d+', FileRead)
   NewIP = "Allow from " + IP
   FileNew = FileRead.replace(str(OldIP[0]), NewIP)
   File.seek(0,0)
   File.write(FileNew)
   File.close()
   print OldIP
   print NewIP

#reload apache
def RestartHttpd():
   StopHttpd = os.system('sudo /etc/init.d/httpd reload')
   
   print RestartHttpd

print Time
print Key

#判断key与是否有效
if int(Time) == int(Key):
   print Time
   UpdataFile()
   RestartHttpd()


