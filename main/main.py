import twitch
import keypresser
import keyholder
#import client
import credentials
import socket

t = twitch.Twitch();
k = keypresser.Keypresser();
 
username = credentials.username;
key = credentials.key;
t.twitch_connect(username, key);
print("ebin");

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.connect(("127.0.0.1", 1337))


while True:
    new_messages = t.twitch_recieve_messages();
    if not new_messages:
        continue
    else:
        print("ebin");
        for message in new_messages:
            msg = message['message'].lower();
            username = message['username'].lower();
            print(username + ": " + msg);
            '''
            if msg == "up": k.key_press("up");
            if msg == "down": k.key_press(msg);
            if msg == "right": k.key_press(msg);
            if msg == "left": k.key_press(msg);
            if msg == "a": k.key_press("f");
            if msg == "b": k.key_press("d");
            if msg == "start": k.key_press("a");
            if msg == "select": k.key_press("s");
            '''
            if msg == "up": soc.sendall('1');
            if msg == "down": keyholder.holdForSeconds('k', 2);
            if msg == "start": keyholder.holdForSeconds("w", 2);
            if msg == "select": keyholder.holdForSeconds("q", 2);
            if msg == "right": keyholder.holdForSeconds('l', 2);
            if msg == "left": keyholder.holdForSeconds("j", 2);
            if msg == "a": keyholder.holdForSeconds(msg, 2);
            if msg == "b": keyholder.holdForSeconds(msg, 2);
