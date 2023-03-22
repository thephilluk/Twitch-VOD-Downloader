import requests
import json
import sys
from datetime import datetime, timedelta
import subprocess

user = "" # Target Username

client_id = "" # Twitch Application Client ID
client_secret = "" # Twitch Application Client Secret

if(client_id == ""):
    sys.exit("Client ID is not set! Please create a Twitch application and add it in this file")
if(client_secret == ""):
    sys.exit("Client Secret is not set! Please create a Twitch application and add it in this file")
if(user == ""):
    sys.exit("Target username is not set! Please add it in this file")


print("Getting Access Token")
response = requests.post("https://id.twitch.tv/oauth2/token",data={"client_id":client_id, "client_secret":client_secret, "grant_type":"client_credentials"} , headers={"Content-Type":"application/x-www-form-urlencoded"})
token = json.loads(response.text)["access_token"]
print("Got Access Token! ending with '" + token[-5:] + "'")

print("---------")

print("Getting User Data")
s = requests.Session()
s.headers.update({"Authorization":"Bearer " + token, "Client-Id":client_id})
userData = s.get("https://api.twitch.tv/helix/users?login=" + user)
if(userData.status_code != 200 or len(json.loads(userData.text)["data"]) == 0):
    print(userData.text)
    sys.exit("error getting User Data")

userData = json.loads(userData.text)["data"][0]
print("Got userdata for " + str(userData["id"]) + ":" + userData["display_name"])

print("---------")

doLoop = True
first = True
vidList = []
lastDate = None
try:
    with open("last.txt", "r") as file2:
        read_content = file2.read()
        if(read_content != ""):
            lastDate = datetime.strptime(read_content, "%d.%m.%Y")
except:
    print("File not found")
if(lastDate == None):
    lastDate = datetime.strptime("01.01.1970", "%d.%m.%Y")
    
print("Getting Videos before: " + lastDate.strftime("%d.%m.%Y"))
while doLoop:
    if(first):
        userVideosOrg = s.get("https://api.twitch.tv/helix/videos?user_id="+userData["id"]+"&type=archive&first=1")
    else:
        userVideosOrg = s.get("https://api.twitch.tv/helix/videos?user_id="+userData["id"]+"&type=archive&after=" + cursor)
    if(userVideosOrg.status_code != 200 or len(json.loads(userVideosOrg.text)["data"]) == 0):
        print(json.loads(userVideosOrg.text)["error"])
        sys.exit(json.loads(json.loads(userVideosOrg.text)["message"])["error"])    
    userVideos = json.loads(userVideosOrg.text)["data"]
    for vid in userVideos:
        if(datetime.strptime(vid["created_at"], '%Y-%m-%dT%H:%M:%SZ') <= lastDate + timedelta(days=1)):
            doLoop = False
            break
        vidList.append({"id":vid["id"],"title":vid["title"], "created": datetime.strptime(vid["created_at"], '%Y-%m-%dT%H:%M:%SZ'), "length":vid["duration"]})
    cursor = json.loads(userVideosOrg.text)["pagination"]["cursor"]
    if(len(userVideos) != 20 and not(first)):
        break
    first = False


if(len(vidList) == 0):
    print("No new Videos for " + userData["display_name"] + " found, exiting")
    sys.exit()
print("Got " + str(len(vidList)) + " Videos from " + userData["display_name"])
for vid in vidList:
    print(vid["id"] + ": " + vid["title"] + "; " + vid["created"].strftime("%d.%m.%Y") + "; " + vid["length"])

if(len(vidList) != 0):
    with open("last.txt", 'w') as file:
        file.write(vidList[0]["created"].strftime("%d.%m.%Y"))


i = 0
for vid in vidList:
    print("Downloading " + vid["title"])
    process = subprocess.Popen("TwitchDownloaderCLI.exe videodownload --id " + str(vid["id"]) + " -o " + vid["created"].strftime("%d.%m.%Y") + "-" + str(i) + ".mp4")
    process.wait()
    if(process.returncode != 0):
        sys.exit("Fatal Error while Downloading Video File!")
    print("Downloading Chat data for " + vid["title"])
    rint("TwitchDownloaderCLI.exe chatdownload --id " + "1760160246" + " -o " + vid["created"].strftime("%d.%m.%Y") + "-" + str(i) + ".json -E")
    process = subprocess.Popen("TwitchDownloaderCLI.exe chatdownload --id " + str(vid["id"]) + " -o '" + vid["created"].strftime("%d.%m.%Y") + "-" + str(i) + ".json' -E")
    process.wait()  
    #print(process.returncode)
    if(process.returncode != 0):
        sys.exit("Fatal Error while Downloading Chat File!")
    print("renaming and moving to Subdirectory")
    process = subprocess.Popen("cmd.exe /C move /Y ^'" + vid["created"].strftime("%d.%m.%Y") + "-" + str(i) + ".json^' " + vid["created"].strftime("%d.%m.%Y") + "-" + str(i) + ".json")
    process.wait()  
    if(process.returncode != 0):
        sys.exit("Fatal Error moving Downloading Chat File!")
        
    process = subprocess.Popen("cmd.exe /C mkdir " + vid["created"].strftime("%d.%m.%Y"))
    process.wait()  
    if(process.returncode != 0):
        sys.exit("Fatal Error making subdir!")
        print("cmd.exe /C move /Y " + vid["created"].strftime("%d.%m.%Y") + "* " + vid["created"].strftime("%d.%m.%Y"))
    process = subprocess.Popen("cmd.exe /C move /Y " + vid["created"].strftime("%d.%m.%Y") + "* " + vid["created"].strftime("%d.%m.%Y"))
    process.wait()  
    if(process.returncode != 0):
        sys.exit("Fatal Error moving Downloading Chat File!")
    i = i + 1
    print("Done with " + vid["title"])
print("Done with all Downloads, exiting")
sys.exit()
