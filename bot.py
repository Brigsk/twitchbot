import config
import utils
import re
import time
import _thread
from time import sleep
import socket


def main():
    s = socket.socket()
    s.connect((config.HOST, config.PORT))
    s.send("PASS {}\r\n".format(config.PASS).encode("utf-8"))
    s.send("NICK {}\r\n".format(config.NICK).encode("utf-8"))
    s.send("JOIN {}\r\n".format(config.CHAN).encode("utf-8"))

    chat_message = re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")
    utils.mess(s,"Sup, superhumans")

    _thread.start_new_thread(utils.fill0pList, ())
    while True:
        response = s.recv(1024).decode("utf-8")
        if response == "PING :tmi.twitch.tv\r\n":
            s.send("POND  :tmi.twitch.tv\r\n".encode("utf-8"))
        else:
            username = re.search(r"\w+", response).group(0)
            message = chat_message.sub("", response)
            print(response)

            if message.strip() == "!time":
                utils.mess(s, "it's currently " + time.strftime("%I:%M %p %Z on %A %B %d %Y"))
            if message.strip() == "!messages":
                utils.mess(s, "Do something ubermenshen!")
                utils.mess(s, "Go cry over a horse")
        sleep(1)

if __name__ == "__main__":
    main()