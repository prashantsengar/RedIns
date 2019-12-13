import json
import os as __os
import requests as __requests
from InstagramAPI import InstagramAPI as __ig
import random as __random
import time as __time
import twitter
from JSONs import *
from caps import *

user = ""  # Enter Instagram username
passw = ""  # Add Instagram password

consumer_key = ""  # Add twitter consumer key
consumer_secret = ""  # Add twitter consumer secret key
access_token_key = ""  # Add twitter
access_token_secret = ""  # Add twitter

img = []


def check_folder():

    try:
        if not __os.path.exists(path.join(path.dirname(__file__), red_media)):
            __os.mkdir(path.join(path.dirname(__file__), red_media))
            return True
        return True
    except:
        return False


def get_links(__JSON):
    global img
    file = open(path.join(path.dirname(__file__), __JSON)
    meme=json.loads(file.read())
    n=meme['data']['dist']

    for i in range(n):
        img.append(meme['data']['children'][i]['data']['preview']['images'][0]['source']['url'])

    print("I got links")
    file.close()


def write_meme():
    global img

    memes={'data': '[]'}
    memes['data']=img

    file=open('meme.txt', 'w+')
    data=json.dumps(memes)
    file.write(data)
    file.close()

    print("Wrote json")


def dload(JSON):
    get_links(JSON)
    write_meme()
    file=open('meme.txt')
    data=file.read()
    data=json.loads(data)

    links=data['data']

    if len(links) == 0:
        print("No links")
    else:

        if check_folder():
            __os.chdir(path.join(path.dirname(__file__), red_media))
            i=0
            print(__os.getcwd())
            for link in links:
                try:
                    print(link)
                    link=link.replace('amp;', '')
                    f=__requests.get(link)

                    m_file=open(path.join(path.dirname(__file__), red_media, f'{i}.jpg'), 'wb')

                    for chunk in f.iter_content(100000):
                        m_file.write(chunk)
                    m_file.close()
                    print("Downloaded")
                    __os.chdir('..')
                    i += 1
                except Exception as e:
                    print(e)

        else:
            raise Exception('There has been an error')


def uload(num):
    i=__ig(user, passw)
    i.login()

    a=twitter.Api(consumer_key=consumer_key, consumer_secret=consumer_secret,
                    access_token_key=access_token_key, access_token_secret=access_token_secret)
    # __os.chdir('\\red_media')

    dirs=__os.listdir(path.join(path.dirname(__file__), red_media))

    for j in range(num):
        try:
            files=__random.choice(dirs)
            files=path.join(path.dirname(__file__), red_media, files)
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


if __name__ == '__main__':

    __os.chdir(path.join(path.dirname(__file__))

    if check_folder():
        for j in JSONs:
            get_links(j)
            write_meme()
            dload(j)
            uload(input("Enter the number of files to be uploaded: "))
    else:
        print("Error creating file")
