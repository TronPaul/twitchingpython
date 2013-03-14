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
            self.dict1 = json.loads(requests.get(baseurl + 'user', headers = self.headers).text)
            self.name = self.dict1 ['name']
        else:
            pass

    def getblocklist(self,limit = None):
        if limit == None:
            params = {}
        else:
            params = {'limit':self.limit}
        
        dict1 = json.loads(requests.get(baseurl + 'users/' + self.name + '/blocks', headers = self.headers,params = params).text)
        return dict1
        
    def putblocklist(self,target):
        requests.put(baseurl + 'users/' + self.name + '/blocks/' + target,headers = self.headers)
        
    def deleteblocklist(self,target):
        requests.delete(baseurl + 'users/' + self.name + '/blocks/' + target,headers = self.headers)
               
    def getchannelinfo(self):
        dict1 = json.loads(requests.get(baseurl + 'channel',headers = self.headers).text)
        return dict1
        
class twitchchannelinfo():
    def __init__ (self,channel):
        self.channel = channel
        time.sleep(waittime)
        self.dict1 = json.loads(requests.get(baseurl + 'channels/' + channel).text)
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

t = TwitchingWrapper('2z8qndwhjih2gch7x9g1yqj4hjcitnt')