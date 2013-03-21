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
            self.token = token
            self.headers = {'Accept':'application/vnd.twitchtv.v2+json'}
            self.name = None
        elif checktoken(token):
            self.token = token
            self.headers = {'Authorization':'OAuth ' + token,'Accept':'application/vnd.twitchtv.v2+json'}
            time.sleep(waittime)
            dict1 = requests.get(baseurl + 'user', headers = self.headers)
            dict1.raise_for_status()
            self.name = json.loads(dict1.text) ['name']
        else:
            raise Exception
        
    def returnauthtoken(self):
        return self.token
       
    def getblocklist(self,limit = 25,offset = 0):
        limit = checkint(limit) 
        offset = checkint(offset)
        params = {'limit':limit,"offset":offset}
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
    
    def getchannelvideos(self,channel):
        channel = checkstring(channel)
        time.sleep(waittime)
        dict1 = requests.get(baseurl + 'channels/' + channel +'/videos', headers = self.headers)
        dict1.raise_for_status()
        return json.loads(dict1.text)
    
    def getchannelfollowers(self,channel):
        channel = checkstring(channel)
        time.sleep(waittime)
        dict1 = requests.get(baseurl + 'channels/' + channel +'/follows', headers = self.headers)
        dict1.raise_for_status()
        return json.loads(dict1.text)
    
    def getchanneleditors(self,channel):
        channel = checkstring(channel)
        time.sleep(waittime)
        dict1 = requests.get(baseurl + 'channels/' + channel +'/editors', headers = self.headers)
        dict1.raise_for_status()
        return json.loads(dict1.text)
    
    def getchannelvideos(self,limit = 25,offset = 0,broadcasts = False,channel = None):
        limit = checkint(limit)
        offset = checkint(offset)
        broadcasts = bool(broadcasts)
        time.sleep(waittime)
        params = {"limit":limit,"offset":offset,"broadcasts":broadcasts}
        if channel == None:
            dict1 = requests.get(baseurl + 'channels/' + self.name + '/videos', headers = self.headers, params = params)
            dict1.raise_for_status()     
            return json.loads(dict1.text)       
        else:
            channel = checkstr(channel)
            dict1 = requests.get(baseurl + 'channels/' + channel +'/videos', headers = self.headers, params = params)
            dict1.raise_for_status()
            return json.loads(dict1.text)
        
    
    def updatechannel(self,channel,status,game):
        channel = checkstring(channel)
        status = checkstring(status)
        game = checkstring(game)
        params = {'status':status,'game':game}
        time.sleep(waittime)
        requests.put(baseurl + 'channels/' + channel, headers = self.headers, params = params).raise_for_status()
    
    def resetstreamkey(self,channel):
        channel = checkstring(channel)
        time.sleep(waittime)
        requests.delete(baseurl + 'channels/' + channel + '/stream_key', headers = self.headers).raise_for_status()
    
    def startcommercial(self,length,channel):
        length = checkint(length)
        channel = checkstring(channel)
        parms = {'channel_commercial':length}
        time.sleep(waittime)
        requests.post(baseurl + 'channels/' + channel + '/commercial', headers = self.headers, parms = parms).raise_for_status()
    
    def getchannelfollowers(self,channel,limit = 25,offset = 0):
        limit = checkint(limit)
        offset = checkint(offset)
        channel = checkstr(channel)
        params = {"limit":limit,"offset":offset}
        time.sleep(waittime)
        dict1 = requests.get(baseurl + 'channels/' + channel + '/follows', headers = self.headers, parms = parms)
        dict1.raise_for_status()
        return json.loads(dict1.text)
    
    def getusefollowing(self,limit = 25,offset = 0):
        limit = checkint(limit)
        offset = checkint(offset)
        params = {"limit":limit,"offset":offset}
        time.sleep(waittime)
        dict1 = requests.get(baseurl + 'users/' + self.name + '/follows/channels', headers = self.headers, parms = parms)
        dict1.raise_for_status()
        return json.loads(dict1.text)
    
    def follow(self,target):
        target = checkstr(target)
        time.sleep(waittime)
        dict1 = requests.put(baseurl + 'users/' + self.name + '/follows/channels/' + target, headers = self.headers).raise_for_status()
        
    def unfollow(self,target):
        target = checkstr(target)
        time.sleep(waittime)
        dict1 = requests.delete(baseurl + 'users/' + self.name + '/follows/channels/' + target, headers = self.headers).raise_for_status()
        
    def gettopgames(self,limit = 25,offset = 0):
        limit = checkint(limit)
        offset = checkint(offset)
        params = {"limit":limit,"offset":offset}
        time.sleep(waittime)
        dict1 = requests.get(baseurl + "games/top", headers = self.headers, parms = parms)
        dict1.raise_for_status()
        return json.loads(dict1.text)
    
    def getingests(self):
        time.sleep(waittime)
        dict1 = requests.get(baseurl + "ingests/", headers = self.headers)
        dict1.raise_for_status()
        return json.loads(dict1.text)
        
    def gettokeninfo(self):
        time.sleep(waittime)
        dict1 = requests.get(baseurl, headers = self.headers)
        dict1.raise_for_status()
        return json.loads(dict1.text)
    
    def searchstreams(self,query,limit = 25,offset = 0):
        query = checkstr(query)
        limit = checkint(limit)
        offset = checkint(offset)
        parms = {"query":query,"limit":limit,"offset":offset}
        time.sleep(waittime)
        dict1 = requests.get(baseurl + "search/streams", parms = parms, headers = self.headers)
        dict1.raise_for_status()
        return json.loads(dict1.text)
    
    def searchgames(self,query,type,live = False):
        query = checkstr(query)
        type = checkstr(type)
        live = bool(live)
        parms = {"query":query,"type":type,"live":live}
        time.sleep(waittime)
        dict1 = requests.get(baseurl + "search/games", parms = parms, headers = self.headers)
        dict1.raise_for_status()
        return json.loads(dict1.text)
        
    def getstream(self,channel):
        channel = checkstr(channel)
        time.sleep(waittime)
        dict1 = requests.get(baseurl + "streams/" + channel, headers = self.headers)
        dict1.raise_for_status()
        return json.loads(dict1.text)
    
    def getstreams(self,game,channel,limit = 25,offset = 0,embeddable = False,hls = False):
        game = checkstr(game)
        channel = checkstr(channel)
        limit = checkint(limit)
        offset = checkint(offset)
        embeddable = bool(embeddable)
        hls = bool(hls)
        parms = {"game":game,"channel":channel,"limit":limit,"offset":offset,"embeddable":embeddable,"hls":hls}
        time.sleep(time.waittime)
        dict1 = requests.get(baseurl + "streams/", headers = self.headers, parms = parms)
        dict1.raise_for_status()
        return json.loads(dict1.text)
    
    def getfeaturedstreams(self,limit = 25,offset = 0,hls = False):
        limit = checkint(limit)
        offset = checkint(offset)
        hls = bool(hls)
        parms = {"limit":limit,"offset":offset,"hls":hls}
        time.sleep(waittime)
        dict1 = requests.get(baseurl + "streams/featured", headers = self.headers, parms = parms)
        dict1.raise_for_status()
        return json.loads(dict1.text)
    
    def getstreamsummary(self,limit = 25,offset = 0,hls = False):
        limit = checkint(limit)
        offset = checkint(offset)
        hls = bool(hls)     
        parms = {"limit":limit,"offset":offset,"hls":hls}     
        time.sleep(waittime)
        dict1 = requests.get(baseurl + "streams/summary", headers = self.headers, parms = parms)
        dict1.raise_for_status()
        return json.loads(dict1.text)
    
    def getstreamsfollowing(self):
        time.sleep(waittime)
        dict1 = requests.get(baseurl + "streams/followed", headers = self.headers)
        dict1.raise_for_status()
        return json.loads(dict1.text)
        
    def getsubscribers(self,channel,limit = 25, offset = 0,direction = "asc"):
        channel = checkstr(channel)
        limit = checkint(limit)
        offset = checkint(offset)
        direction = checkstr(direction)
        parms = {"limit":limit,"offset":offset,"direction":direction}
        time.sleep(waittime)
        dict1 = requests.get(baseurl + "channels/" + channel + "/subscriptions", headers = self.headers, parms = parms)
        dict1.raise_for_status()
        return json.loads(dict1.text)        
    
    def checksubscription (self,channel,user):
        channel = checkstr(channel)
        user = checkstr(user)
        time.sleep(waittime)
        dict1 = requests.get(baseurl + "channels/" + channel + "/subscriptions/" + user, headers = self.headers)
        dict1.raise_for_status()
        return json.loads(dict1.text)        
    
    def getteams(self):
        time.sleep(waittime)
        dict1 = requests.get(baseurl + "teams/", headers = self.headers)
        dict1.raise_for_status()
        return json.loads(dict1.text)
    
    def getteaminfo(self,team):
        team = checkstr(team)
        time.sleep(waittime)
        dict1 = requests.get(baseurl + "teams/" + team, headers = self.headers)
        dict1.raise_for_status()
        return json.loads(dict1.text)
        
    def getuserinfo(self,user):
        user = checkstr(user)
        time.sleep(waittime)
        dict1 = requests.get(baseurl + "users/" + user, headers = self.headers)
        dict1.raise_for_status()
        return json.loads(dict1.text)
    
    def getvideoinfo(self,id):
        id = checkstr(id)
        time.sleep(waittime)
        dict1 = requests.get(baseurl + "videos/" + id, headers = self.headers)
        dict1.raise_for_status()
        return json.loads(dict1.text)
    

class Channel():
    def __init__(self,token = None,channel = None):
        if token != None and checktoken(token):
            self.headers = {"Authorization":"OAuth " + token,"Accept":"application/vnd.twitchtv.v2+json"}
            time.sleep(waittime)
            dict1 = requests.get(baseurl, headers = self.headers)
            dict1.raise_for_status()
            self.channel = json.loads(dict1.text) ["token"] ["user_name"] 
            self.scope = json.loads(dict1.text) ["token"] ["authorization"] ["scopes"]
            self.authed = True
        elif channel != None:
            self.channel = checksrt(channel)
            self.headers = {"Accept":"application/vnd.twitchtv.v2+json"}
            self.scope = None
            self.authed = False
        else:
            raise Exception
    
    def getchannelinfo(self):
        if self.authed:
            time.sleep(waittime)
            dict1 = requests.get(baseurl + "channel/", headers = self.headers)
            dict1.raise_for_status()
            return json.loads(dict1.text)   
        elif not self.authed:
            time.sleep(waittime)
            dict1 = requests.get(baseurl + 'channels/' + self.channel, headers = self.headers)
            dict1.raise_for_status()
            return json.loads(dict1.text)
        
    def getchannelvideos(self, limit = 25, offset = 0, broadcasts = False):
        limit = checkint(limit)
        offset = checkint(offset)
        broadcasts = bool(broadcasts)
        parms = {"limit":limit, "offset":offset, "broadcasts":broadcasts}
        time.sleep(waittime)
        dict1 = requests.get(baseurl + 'channels/' + self.channel +'/videos', headers = self.headers, parms = parms)
        dict1.raise_for_status()
        return json.loads(dict1.text)
    
    def getchannelfollowers(self,limit = 25, offset = 0):
        limit = checkint(limit)
        offset = checkint(offset)
        parms = {"limit":limit,"offset":offset}
        time.sleep(waittime)
        dict1 = requests.get(baseurl + 'channels/' + self.channel +'/follows', headers = self.headers, parms = parms)
        dict1.raise_for_status()
        return json.loads(dict1.text)
    
    def getchanneleditors(self):
        if channel_read not in self.scope:
            raise errors.HigherScopeRequired ("channel_read")
        time.sleep(waittime)
        dict1 = requests.get(baseurl + 'channels/' + self.channel +'/editors', headers = self.headers)
        dict1.raise_for_status()
        return json.loads(dict1.text)
    
    def updatechannel(self,status,game):
        if channel_editor not in self.scope:
            raise errors.HigherScopeRequired ("channel_editor")
        status = checkstring(status)
        game = checkstring(game)
        params = {'status':status,'game':game}
        time.sleep(waittime)
        requests.put(baseurl + 'channels/' + self.channel, headers = self.headers, params = params).raise_for_status()
        
    def resetstreamkey(self):
        if channel_stream not in self.scope:
            raise errors.HigherScopeRequired ("channel_stream")
        time.sleep(waittime)
        requests.delete(baseurl + 'channels/' + self.channel + '/stream_key', headers = self.headers).raise_for_status()
        
    def startcommercial(self,length):
        if channel_commercial not in self.scope:
            raise errors.HigherScopeRequired ("channel_commercial")
        length = checkint(length)
        parms = {'channel_commercial':length}
        time.sleep(waittime)
        requests.post(baseurl + 'channels/' + self.channel + '/commercial', headers = self.headers, parms = parms).raise_for_status()
    
    def getsubscribers(self,limit = 25, offset = 0, direction = "asc"):
        if channel_subscriptions not in self.scope:
            raise errors.HigherScopeRequired ("channel_subscriptions")
        limit = checkint(limit)
        offset = checkint(offset)
        direction = checkstr(direction)
        parms = {"limit":limit,"offset":offset,"direction":direction}
        time.sleep(waittime)
        dict1 = requests.get(baseurl + "/channels/" + self.channel + "/subscriptions", headers = self.headers, parms = parms)
        dict1.raise_for_status()
        return json.loads(dict1.text)
        
                
        
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
    try:
        string = str(string)
    except:
        raise errors.InvalidInput
    else:
        return string
    

def checkint(intger):
    try:
        intger = int(intger)
    except:
        raise errors.InvalidInput
    else:
        return intger