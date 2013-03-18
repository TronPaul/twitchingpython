twitchingpython
===============

Twitching Python (a Twitch.tv API wrapper for python) (a work in progress) (for python 2.7x)

Run it by placing main.py somewhere in the PYTHONPATH and importing it.

You can also install this using pip like this:

    pip install twitchingpython

Then to use it you need to import it:

    import twitchingpython
    
and create the main API object and auth yourself if you want to:

    t = twitchingpython.TwitchingWrapper()
    
Inside the brackets you will have to place the twitch.tv API auth token if you want to be auth'ed. You can get it here:

    https://api.twitch.tv/kraken/oauth2/authorize?response_type=token&client_id=3kfp6al05voejvv7ofmpc94g4jga0tb&redirect_uri=http://httpbin.org/&scope=user_read+user_blocks_edit+user_follows_edit+channel_editor+channel_commercial+channel_stream+channel_subscriptions+channel_check_subscription+user_blocks_read+channel_read
    
Or you can use the built in method to get the auth token:

    t = twitchingpython.TwitchingWrapper(twitchingpython.gettoken())

It will open a web browser and ask you to sign in to Twitch.Tv, after the sign in it will redirect you to a url, copy and paste it into the python promt. After this everytime you use this method twitchingpython will remember this token and use it. 
