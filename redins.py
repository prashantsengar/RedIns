import json
import os as __os
import requests as __requests
from InstagramAPI import InstagramAPI as __ig
import random as __random
import time as __time
import twitter

user = "" ##Enter Instagram username
passw = "" ##Add Instagram password

consumer_key="" ##Add twitter consumer key
consumer_secret="" ##Add twitter consumer secret key
access_token_key=""#Add twitter 
access_token_secret=""##Add twitter


##Edit captions named cap1, cap2, cap3 for Instagram
##Edit captions named cap11, cap22, cap33 for Twitter
cap1 = """Follow @einteresting
        .
        .
        .
        .
        .
        #dankmemes #memes #dank #meme #funny #funnymemes #lol
        #edgymemes #lmao #memesdaily #dankmeme #offensivememes
        #comedy #offensive #follow #like #funnyvideos #fortnitememes
        #haha #oof
        """

cap2 = """Follow @einteresting
        .
        .
        .
        .
        #meme #memes #funny #dankmemes #dank #lol
        #memesdaily #lmao #funnymemes #follow
        #fortnite #like #edgy #dankmeme #edgymemes
        #comedy #cringe #humor #funnyvideos #lmfao
        #instagram #hilarious #oof #savage"""

cap3 = """Follow @einteresting
        .
        .
        .
        .
        .
        #laugh #gaming #minecraft #cancer #music #f #funnymeme #instagood #kpop #edgymeme #love #roblox #joke #viral #lit #memepage #ifunny #lilpump #rofl #life #donaldtrump
        """
cap4 = """Follow @einteresing
        .
        .
        .
        .
        #funny #funnymeme #funnymemes #memes #meme #funnytext #funnyvideos
        #hilarious #crazy #humor #epic #instafun
        """
cap = [cap1, cap2, cap3, cap4]

cap11 = "Follow @E__interesting for more #funny #lol #memes #follow"
cap22 = "Follow @E__interesting for more #follow #dankmemes #reddit"
cap33= "Follow @E__interesting for more #lmao #edgymemes #comedy #retweet"
caps = [cap11,cap22,cap33]


img=[]

def check_folder():
    
    try:
        if not __os.path.exists(f'{__os.getcwd()}\\red_media'):
            __os.mkdir(f'{__os.getcwd()}\\red_media')
            return True
        return True
    except:
        return False

hashh = '123'

def get_links():
    global img
    file = open(f'{__os.getcwd()}\\meme.json')
    meme = json.loads(file.read())
    n = meme['data']['dist']

    for i in range(n):
        img.append(meme['data']['children'][i]['data']['preview']['images'][0]['source']['url'])

    print("I got links")
    file.close()



def write_meme():
    global img

    memes = {'data':'[]'}
    memes['data'] = img

    file = open('meme.txt', 'w+')
    data = json.dumps(memes)
    file.write(data)
    file.close()

    print("Wrote json")

def dload():
    get_links()
    write_meme()
    file = open('meme.txt')
    data = file.read()
    data = json.loads(data)

    links = data['data']

    if len(links)==0:
        print("No links")
    else:

        if check_folder():
            __os.chdir(f'{__os.getcwd()}\\red_media')
            i=0
            print(__os.getcwd())
            for link in links:
                try:
                    print(link)
                    link = link.replace('amp;','')
                    f = __requests.get(link)

                    m_file = open(f'{__os.getcwd()}\\red_media\\{i}.jpg', 'wb')

                    for chunk in f.iter_content(100000):
                        m_file.write(chunk)
                    m_file.close()
                    print("Downloaded")
                    __os.chdir('..')
                    i+=1
                except Exception as e:
                    print(e)

        else:
            raise Exception('There has been an error')


def uload(num):
    i = __ig(user, passw)
    i.login()


    a = twitter.Api(consumer_key=consumer_key, consumer_secret=consumer_secret, access_token_key=access_token_key, access_token_secret=access_token_secret)
    #__os.chdir('\\red_media')

    dirs = __os.listdir(f'{__os.getcwd()}\\red_media')



    for j in range(num):
        try:
            files = __random.choice(dirs)
            files = f'{__os.getcwd()}\\red_media\\' + files
            i.uploadPhoto(files, caption=__random.choice(cap))
            print("insta upload")
            a.PostUpdate(__random.choice(caps), files)
            
            print("Uploaded..")
            __os.remove(files)
            __time.sleep(10)
        except Exception as e:
            print("Error occured {}" .format(str(e)))
            
        

    i.logout()
    print("Logged out")


if __name__=='__main__':

    __os.chdir(f'{__os.getcwd()}')

    
    if check_folder():
        get_links()
        write_meme()
        dload()
        uload(input("Enter the number of files to be uploaded: "))
    else:
        print("Error creating file")
