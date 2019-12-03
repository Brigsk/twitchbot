import config
import urllib.request
import json
import time
import _thread
from time import sleep


def mess(sock, message):
    sock.send("PRIVMSG #{} :{}\r\n".format(config.CHAN, message))

def ban(sock, user):
    mess(sock, "*.ban {}".format(user))

def timeout(sock, user, seconds = 500):
    mess(sock, "*.timeout {}".format(user, seconds))

#http://tml.twitch.tv/group/user/loltyler1/chatters
def fill0pList():
    while True:
        try:
            url = "http://tmi.twitch.tv/group/user/loltyler1/chatters"
            req = urllib.Request(url, headers={"accept": "*/*"})
            res = urllib.urlopen(req.read())
            if res.find("502 bad gateway") == -1:
                    config.oplist.clear()
            data = json.loads(res)
            for p in data["chatters"]["moderators"]:
                config.oplist[p] = "mod"
            for p in data["chatters"]["global_mod"]:
                config.oplist[p] = "global_mod"
            for p in data["chatters"]["staff"]:
                config.oplist[p] = "staff"
        except:
                print("Something went wrong...do nothing")
        sleep(5)

def is0p(user):
    return user in config.oplist