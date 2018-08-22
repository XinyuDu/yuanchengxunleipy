# -*- coding: utf-8 -*-

import requests
import json
from six.moves.urllib.parse import quote

#python2 改变标准输出的默认编码
import sys
reload(sys)
sys.setdefaultencoding('utf8')

#python3 改变标准输出的默认编码
#import io
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') 
class YCXunlei(object):
    def __init__(self, cookie_str=r'this is a cookie'):
        '''
        YCXunlei constructor.
        cookie_str: the cookie string after login yuancheng.xunlei.com
        '''
        self.cookie_str = cookie_str

        url = 'http://homecloud.yuancheng.xunlei.com/listPeer?'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36','cookie': self.cookie_str}
        req = requests.get(url, headers=headers)
        result = req.json()

        if result['rtn']==0:
            self.login = True
            self.devices = result['peerList']
        else:
            self.login = False
            self.devices = None

    def isLogin(self):
        '''
        check if the cookie string is valid
        '''
        return self.login

    def getDevices(self):
        '''
        get remote devices
        return: a list of the devices include name,pid,online....
        '''
        return self.devices

    def getPid(self, name):
        '''
        get pid number of a device by device name
        return None if no matched name found
        '''
        for device in self.devices:
            if device['name'] == name:
                return device['pid']

    def getTasks(self,pid):
        '''
        get the xunlei tasks on device
        pid: the pid of the device
        '''
        url = 'http://homecloud.yuancheng.xunlei.com/list?pid='+pid+'&type=0&pos=0&number=10&needUrl=1&v=2'
        headers = {'cookie': self.cookie_str,'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
        req = requests.get(url, headers=headers)
        result = req.json()

        if result['rtn']==0:
            return result
        else:
            return None

    def addTask(self, pid, links):
        '''
        add download task to yuancheng xunlei
        pid: the remote device pid number
        links: an array contain download urls
        '''
        url = 'http://homecloud.yuancheng.xunlei.com/createTask?pid='+pid+'&v=2&ct=0'

        tasks = []
        for link in links:
            tasks.append({"url":link,"gcid":"","cid":""})
        data = {"path":"C:/影视/","tasks":tasks}
        # print(links)
        # data = {"path":"C:/影视/","tasks":[{"url":links,"gcid":"","cid":""}]}
        data = json.dumps(data)
        data = quote(data)
        data = 'json=' + data
        data = data.encode('utf-8')

        headers = {'cookie': self.cookie_str,"Content-Type": "application/x-www-form-urlencoded"}

        req = requests.post(url, headers=headers, data = data)

        result = req.json()

        return result

    def getFileInfo(self,pid,link):
        '''
        get file name and file size of a download url
        pid:the remote device pid number
        link: download url
        '''
        url = 'http://homecloud.yuancheng.xunlei.com/urlResolve?pid='+pid+'&v=2&ct=0'

        data = {"url":link,}
        data = json.dumps(data)
        data = quote(data)
        data = 'json=' + data
        data = data.encode('utf-8')

        headers = {'cookie': self.cookie_str,"Content-Type": "application/x-www-form-urlencoded"}

        req = requests.post(url, headers=headers, data = data)
        result = req.json()

        if result['rtn']==0:
            return result#['taskInfo']['name']
        else:
            return None

    def delTask(self,pid,id):
        '''
        del task
        pid:the remote device pid number
        id: task id
        '''
        url = 'http://homecloud.yuancheng.xunlei.com/del?pid='+pid+'&tasks='+id+'_0&recycleTask=1&deleteFile=false&v=2&ct=0'

        headers={'cookie': self.cookie_str, 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
        req = request.get(url, headers=headers)
        result = req.json()
        return result

    def getStatus(self,pid):
        tasks = self.getTasks(pid)['tasks']
        returncontent = ''
        for task in tasks:
            size = task['size']/1048576.0
            unit = 'MB'
            if size > 1024.0:
                size = size/1024.0
                unit = 'GB'
            time = task['remainTime']
            m, s = divmod(time, 60)
            h, m = divmod(m, 60)
            returncontent = returncontent + task['name']+' %.2f '%size + unit +'\n'+u'下载速度：%.2f KB/s\n'%(task['speed']/1024)+u'下载进度: %.2f%%\n'%(task['progress']/100.0)+u'剩余时间：%02d:%02d:%02d \n\n' % (h, m, s)
        return returncontent
