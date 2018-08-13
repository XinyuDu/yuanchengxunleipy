# -*- coding: utf-8 -*-
from ycxunlei import YCXunlei
import json

#get the cookie information from the browser when you login yuancheng.xunlei.com 
#all you need are userid and sessionid
#Chrome user can press F12 to get these information
cookie_str = r'userid=xxxxxx; sessionid=xxxxxxxxxxxxxxxxxxxxxxxxxx;'

#init the class
xl = YCXunlei(cookie_str)

#login
re = xl.isLogin()
print('-----------------------------')
print('islogin=%s'%re)

#get the devices information
dvs = xl.getDevices()
if dvs != None:
    print('-----------------------------')
    print(json.dumps(dvs).decode("unicode-escape"))

#get the device pid by device name
pid = xl.getPid(r'小米路由器')
print('-----------------------------')
print(pid)

#get the current download tasks of a device
#the device pid should be supplied as a parameter
tks = xl.getTasks(pid)
if tks != None:
    print('-----------------------------')
    print(json.dumps(tks).decode("unicode-escape"))


#delete a current download task
#the device pid and task id should be supplied
delre = xl.delTask(pid,tks[0]['id'])
print('-----------------------------')
print(delre)

#add a download task to the device
#device pid and a array of download links should be supplied
res = xl.addTask(pid,['thunder://QUFmdHA6Ly95Z2R5ODp5Z2R5OEB5ZzkwLmR5ZHl0dC5uZXQ6ODM2My8lRTklOTglQjMlRTUlODUlODklRTclOTQlQjUlRTUlQkQlQjF3d3cueWdkeTguY29tLiVFNyVBMCVCNCVFOSU5NyVBOCVFOCU4MCU4QyVFNSU4NSVBNS5CRC43MjBwLiVFNCVCOCVBRCVFOCU4QiVCMSVFNSU4RiU4QyVFNSVBRCU5NyVFNSVCOSU5NS5ta3ZaWg=='])
print('-----------------------------')
print(res)


#get the filename of a download link
#device pid and download link should be supplied
filename = xl.getFileInfo(pid,"thunder://QUFtYWduZXQ6P3h0PXVybjpidGloOjM0Q0IwQjY2QUVBRjk5MDVBQTAxQzJBNDcyNzVFMDBBREFBNjMyQzEmZG490dPs+7mlwtQuMjAxOC5FUDAxLTEwLjE5MjBYMTA4MFAuV0VCLURMLlgyNjQuQXVkaW8uQUFDLm1wNFpa")
print('-----------------------------')
print(filename)

