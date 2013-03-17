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
    def __init__(self,token = None):
        if token == None:
            self.headers = None
            self.name = None
        else:
            if not isinstance(token, str) or not token:
                raise Exception
            self.headers = {'Authorization':'OAuth ' + token}
            time.sleep(waittime)
            dict1  = requests.get(baseurl + 'user', headers = self.headers)
            dict1.raise_for_status()
            dict1 = json.loads(dict1.text)
            self.name = dict1 ['name']

    def getblocklist(self,limit):
        if not isinstance(limit, int) or not limit:
            raise Exception
        params = {'limit':limit}
        time.sleep(waittime)
        dict1 = requests.get(baseurl + 'users/' + self.name + '/blocks', headers = self.headers,params = params)
        dict1.raise_for_status()
        return json.loads(dict1.text)
        
    def putblocklist(self,target):
        if not isinstance(target, str) or not target:
            raise Exception
        time.sleep(waittime)
        requests.put(baseurl + 'users/' + self.name + '/blocks/' + target, headers = self.headers).raise_for_status()
        
    def deleteblocklist(self,target):
        if not isinstance(target, str) or not target:
            raise Exception
        time.sleep(waittime)
        requests.delete(baseurl + 'users/' + self.name + '/blocks/' + target, headers = self.headers).raise_for_status()
               
    def getchannelinfo(self,channel = None):
        if channel == None:
            time.sleep(waittime)
            dict1 = requests.get(baseurl + 'channel', headers = self.headers)
            dict1.raise_for_status()
            return json.loads(dict1.text)
        else:
            if not isinstance(channel, str) or not channel:
                raise Exception
            time.sleep(waittime)
            dict1 = requests.get(baseurl + 'channels/' + channel, headers = self.headers)
            dict1.raise_for_status()
            return json.loads(dict1.text)    
    
    def getchanneleditors(self,channel):
        if not isinstance(channel, str) or not channel:
            raise Exception
        time.sleep(waittime)
        dict1 = requests.get(baseurl + 'channels/' + channel +'/editors', headers = self.headers)
        dict1.raise_for_status()
        return json.loads(dict1.text)
    
    def getchannelfollowers(self,channel):
        if not isinstance(channel, str) or not channel:
            raise Exception
        time.sleep(waittime)
        dict1 = requests.get(baseurl + 'channels/' + channel +'/follows', headers = self.headers)
        dict1.raise_for_status()
        return json.loads(dict1.text)
    
    def getchannelvideos(self,channel):
        if not isinstance(channel, str) or not channel:
            raise Exception
        time.sleep(waittime)
        dict1 = requests.get(baseurl + 'channels/' + channel +'/videos', headers = self.headers)
        dict1.raise_for_status()
        return json.loads(dict1.text)
    
    def updatechannel(self,channel,status,game):
        if not isinstance(channel, str) or not channel:
            raise Exception
        if not isinstance(status, str) or not status:
            raise Exception
        if not isinstance(game, str) or not game:
            raise Exception
        params = {'status':status,'game':game}
        time.sleep(waittime)
        requests.put(baseurl + 'channels/' + channel, headers = self.headers, params = params).raise_for_status()
    
    def startcommercial(self,length,channel):
        if not isinstance(length, int) or not length:
            raise Exception
        if not isinstance(channel, str) or not channel:
            raise Exception
        parms = {'channel_commercial':length}
        time.sleep(waittime)
        requests.post(baseurl + 'channels/' + channel + '/commercial', headers = self.headers, parms = parms).raise_for_status()
    
    def resetstreamkey(self,channel):
        if not isinstance(channel, str) or not channel:
            raise Exception
        time.sleep(waittime)
        requests.delete(baseurl + 'channels/' + channel + '/stream_key', headers = self.headers).raise_for_status()
