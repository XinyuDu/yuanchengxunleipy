# yuanchengxunleipy

用python实现的一个模拟登录远程迅雷（yuancheng.xunlei.com）并对远程下载设备进行管理的类。

主要功能如下：

1. 获取绑定设备信息
2. 向指定设备添加下载任务
3. 查看指定设备下载任务状态
4. 删除下载任务

## 使用方法

类名: YCXunlei

定义类文件：ycxunlei.py

使用方法见：example.py

需要注意的是不能根据用户名和密码进行模拟登录，需要用户自己在浏览器中获得自己登录yuancheng.xunlei.com时的cookie信息：userid和sessionid。根据userid和sessionid构建cookie进行模拟登录。

获得cookie信息的方法如下，以Chrome浏览器为例：

1.打开Chrome浏览器，输入网址yuancheng.xunlei.com并回车。

2.按F12，打开开发者窗口。勾选Preserve log，点击Doc。

3.输入用户名，密码，也许还要输入识别码并点击登录按钮。

4.在name栏选中login，在Headers中找到userid和sessionid信息。



## 用例

```
from ycxunlei import YCXunlei
import json

#get the cookie information from the browser when you login yuancheng.xunlei.com 
#all you need are userid and sessionid
#Chrome user can press F12 to get these information
cookie_str = r'userid=xxxxxxx; sessionid=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx;'

#init the class with cookie information
xl = YCXunlei(cookie_str)

#get the device pid by device name
#the device name shoud be supplied
pid = xl.getPid(r'小米路由器')
print('-----------------------------')
print(pid)

#支持多任务下载，支持多种下载链接
res = xl.addTask(pid,['thunder://1'，'thunder://2','ed2k:3','magnet:4','ftp://5'])
```

