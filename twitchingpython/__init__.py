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
            self.headers = {'Accept':'application/vnd.twitchtv.v2+json'}
            self.name = None
        elif checktoken(token):
            self.headers = {'Authorization':'OAuth ' + token,'Accept':'application/vnd.twitchtv.v2+json'}
            time.sleep(waittime)
            dict1 = requests.get(baseurl + 'user', headers = self.headers)
            dict1.raise_for_status()
            self.name = json.loads(dict1.text) ['name']
        else:
            raise Exception

    def getblocklist(self,limit):
        limit = checkint(limit)                
        params = {'limit':limit}
        time.sleep(waittime)
        dict1 = requests.get(baseurl + 'users/' + self.name + '/blocks', headers = self.headers,params = params)
        dict1.raise_for_status()
        return json.loads(dict1.text)
        
    def putblocklist(self,target):
        target = checkstring(target)
        time.sleep(waittime)
        requests.put(baseurl + 'users/' + self.name + '/blocks/' + target, headers = self.headers).raise_for_status()
        
    def deleteblocklist(self,target):
        target = checkstring(target)
        time.sleep(waittime)
        requests.delete(baseurl + 'users/' + self.name + '/blocks/' + target, headers = self.headers).raise_for_status()
               
    def getchannelinfo(self,channel = None):
        if channel == None:
            time.sleep(waittime)
            dict1 = requests.get(baseurl + 'channel', headers = self.headers)
            dict1.raise_for_status()
            return json.loads(dict1.text)
        else:
            channel = checkstring(channel)
            time.sleep(waittime)
            dict1 = requests.get(baseurl + 'channels/' + channel, headers = self.headers)
            dict1.raise_for_status()
            return json.loads(dict1.text)    
    
    def getchanneleditors(self,channel):
        channel = checkstring(channel)
        time.sleep(waittime)
        dict1 = requests.get(baseurl + 'channels/' + channel +'/editors', headers = self.headers)
        dict1.raise_for_status()
        return json.loads(dict1.text)
    
    def getchannelfollowers(self,channel):
        channel = checkstring(channel)
        time.sleep(waittime)
        dict1 = requests.get(baseurl + 'channels/' + channel +'/follows', headers = self.headers)
        dict1.raise_for_status()
        return json.loads(dict1.text)
    
    def getchannelvideos(self,channel):
        channel = checkstring(channel)
        time.sleep(waittime)
        dict1 = requests.get(baseurl + 'channels/' + channel +'/videos', headers = self.headers)
        dict1.raise_for_status()
        return json.loads(dict1.text)
    
    def updatechannel(self,channel,status,game):
        channel = checkstring(channel)
        status = checkstring(status)
        game = checkstring(game)
        params = {'status':status,'game':game}
        time.sleep(waittime)
        requests.put(baseurl + 'channels/' + channel, headers = self.headers, params = params).raise_for_status()
    
    def startcommercial(self,length,channel):
        length = checkint(length)
        channel = checkstring(channel)
        parms = {'channel_commercial':length}
        time.sleep(waittime)
        requests.post(baseurl + 'channels/' + channel + '/commercial', headers = self.headers, parms = parms).raise_for_status()
    
    def resetstreamkey(self,channel):
        channel = checkstring(channel)
        time.sleep(waittime)
        requests.delete(baseurl + 'channels/' + channel + '/stream_key', headers = self.headers).raise_for_status()
    
 
def checktoken(token):
    token = checkstring(token)
    headers = {'Authorization':'OAuth ' + token,'Accept':'application/vnd.twitchtv.v2+json'}
    time.sleep(waittime)
    dict1 = requests.get(baseurl + 'user', headers = headers)
    if requests.codes.ok == dict1.status_code: #@UndefinedVariable
        return True
    else:
        return False

def gettokenweb():
    import webbrowser
    from urlparse import urlparse
    webbrowser.open(
                    "https://api.twitch.tv/kraken/oauth2/authorize" +
                    "?response_type=token" +
                    "&client_id=3kfp6al05voejvv7ofmpc94g4jga0tb" +
                    "&redirect_uri=http://httpbin.org/" +
                    "&scope=user_read" +
                    "+user_blocks_edit" +
                    "+user_follows_edit" +
                    "+channel_editor" +
                    "+channel_commercial" +
                    "+channel_stream" +
                    "+channel_subscriptions" +
                    "+channel_check_subscription" +
                    "+user_blocks_read" +
                    "+channel_read"
                    )
    return (urlparse(raw_input('Enter the url:')).fragment).split("&")[0][13:] 

def gettoken():
    import os
    os.close(os.open("tokendata.dat",os.O_CREAT))
    with open("tokendata.dat", "r+") as tokenfile:
        spot = tokenfile.read()
        if checktoken(spot):
            validtoken = spot
        else:
            validtoken = None
           
    if validtoken == None:
        with open("tokendata.dat", "a+") as tokenfile:
            webtoken = gettokenweb()
            tokenfile.write(webtoken + os.linesep)
            return webtoken
    else:
        return validtoken
        
def checkstring(string):
    if not isinstance(string, str) or not string:
        try:
            string = str(string)
        except:
            raise Exception
        else:
            return string
    else:
        return string
    

def checkint(intger):
    if not isinstance(intger, int) or not intger:
        try:
            intger = int(intger)
        except:
            raise Exception
        else:
            return intger
    else:
            return intger
