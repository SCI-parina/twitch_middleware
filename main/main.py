import twitch
#import keypresser
#import keyholder
#import client
import credentials
import socket
#from _socket import SHUT_RDWR

t = twitch.Twitch();
#k = keypresser.Keypresser();
 
username = credentials.username;
key = credentials.key;
t.twitch_connect(username, key);

while True:
    new_messages = t.twitch_recieve_messages();
    if not new_messages:
        continue
    else:
        for message in new_messages:
            print "Message received!"
            msg = message['message'].lower();
            username = message['username'].lower();
            print(username + ": " + msg);
            soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            soc.connect(("127.0.0.1", 1337))
            if msg == "block 1": soc.sendall("1");
            if msg == "block 2": soc.sendall("2");
            if msg == "block 3": soc.sendall("3");
            if msg == "block 4": soc.sendall("4");
            if msg == "block 5": soc.sendall("5");
            if msg == "block 6": soc.sendall("6");
            if msg == "block 7": soc.sendall("7");
            if msg == "block 8": soc.sendall("8");
            if msg == "block 9": soc.sendall("9");
            soc.shutdown(socket.SHUT_RDWR)
            soc.close()
        new_message = ""
