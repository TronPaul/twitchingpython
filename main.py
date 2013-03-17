'''
Created on Mar 11, 2013

@author: Martin-PC8
'''

import json
import time
import requests

waittime = 1
baseurl = 'https://api.twitch.tv/kraken/'

class TwitchingWrapper():
    def __init__(self,token):
        self.token = token
        if self.token != None:
            self.headers = {'Authorization':'OAuth ' + token}
            dict1  = requests.get(baseurl + 'user', headers = self.headers)
            dict1.raise_for_status()
            self.dict1 = json.loads(dict1.text)
            self.name = self.dict1 ['name']
        else:
            pass

    def getblocklist(self,limit):
        params = {'limit':limit}
        time.sleep(waittime)
        dict1 = requests.get(baseurl + 'users/' + self.name + '/blocks', headers = self.headers,params = params)
        dict1.raise_for_status()
        return json.loads(dict1.text)
        
    def putblocklist(self,target):
        time.sleep(waittime)
        requests.put(baseurl + 'users/' + self.name + '/blocks/' + target,headers = self.headers).raise_for_status()
        
    def deleteblocklist(self,target):
        time.sleep(waittime)
        requests.delete(baseurl + 'users/' + self.name + '/blocks/' + target,headers = self.headers).raise_for_status()
               
    def getchannelinfo(self):
        time.sleep(waittime)
        dict1 = requests.get(baseurl + 'channel',headers = self.headers)
        dict1.raise_for_status()
        return json.loads(dict1.text)
    
    def getchanneleditors(self,channel):
        time.sleep(waittime)
        dict1 = requests.get(baseurl + 'channels/' + channel +'/editors', headers = self.headers)
        dict1.raise_for_status()
        return json.loads(dict1.text)
    
    def getchannelfollowers(self,channel):
        time.sleep(waittime)
        dict1 = requests.get(baseurl + 'channels/' + channel +'/follows', headers = self.headers)
        dict1.raise_for_status()
        return json.loads(dict1.text)
    
    def getchannelvideos(self,channel):
        time.sleep(waittime)
        dict1 = requests.get(baseurl + 'channels/' + channel +'/videos', headers = self.headers)
        dict1.raise_for_status()
        return json.loads(dict1.text)
    
    def updatechannel(self,channel,status,game):
        params = {'status':status,'game':game}
        time.sleep(waittime)
        requests.put(baseurl + 'channels/' + channel, headers = self.headers, params = params).raise_for_status()
    
    def startcommercial(self,length,channel):
        parms = {'channel_commercial':length}
        time.sleep(waittime)
        requests.post(baseurl + 'channels/' + channel + '/commercial', headers = self.headers, parms = parms).raise_for_status()
    
    def resetstreamkey(self,channel):
        time.sleep(waittime)
        requests.delete(baseurl + 'channels/' + channel + '/stream_key', headers = self.headers).raise_for_status()
    
class twitchchannelinfo():
    def __init__ (self,channel):
        self.channel = channel
        time.sleep(waittime)
        dict1 = requests.get(baseurl + 'channels/' + channel)
        dict1.raise_for_status()
        self.dict1 = json.loads(dict1.text)
    def getname(self):
        return self.dict1 ['name']
    def getgame(self):
        return self.dict1 ['game']
    def getcreated(self):
        return self.dict1 ['created_at']
    def getteams(self):
        return self.dict1 ['teams']
    def gettitle(self):
        return self.dict1 ['title']
    def getupdateat(self):
        return self.dict1 ['updated_at']
    def getbanner(self):
        return self.dict1 ['banner']
    def getvideobanner(self):
        return self.dict1 ['video_banner']
    def getbackground(self):
        return self.dict1 ['background']
    def getlinks(self):
        return self.dict1 ['_links']
    def getlogo(self):
        return self.dict1 ['logo']
    def getid(self):
        return self.dict1 ['_id']
    def getmature(self):
        return self.dict1 ['mature']
    def getchanurl(self):
        return self.dict1 ['url']
    def getdisplayname(self):
        return self.dict1 ['display_name']
