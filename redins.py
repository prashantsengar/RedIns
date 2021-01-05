from config import Config
import os as __os
import requests as __requests
from InstagramAPI import InstagramAPI as __ig
import random
import time
import twitter
from RedPy import Redpy
from captions import Caption
import facebook
import glob

img = []
curr_dir = __os.path.dirname(__file__)


class RedIns:

    def __init__(self, user_agent=None):
        self.delay = 10
        self.config = Config()
        self.caption = Caption()
        if user_agent:
            self.redpy = Redpy(user_agent)
        else:
            self.redpy = Redpy('web:redpy:v2.1 (by u/myusername)')
        self.instagram = self.config.modules["instagram"]
        self.facebook = self.config.modules["facebook"]
        self.twitter = self.config.modules["twitter"]
        self.login()

    def check_access_token(self, access_token):
        try:
            # print("checking user access token validity")
            r = __requests.get(
                url="https://graph.facebook.com/me",
                params={
                    "access_token": access_token
                }
            )
            r.json()["id"]
            return True
        except KeyError:
            print("Invalid access token.Your access token is "
                  "invalid or has expired.Please refresh your access "
                  "tokens through the Graph API Explorer.")

    def get_long_access_token(self, app_id, app_secret, user_access_token):
        try:
            # print("getting long lived access token")
            r = __requests.get(
                url="https://graph.facebook.com/v5.0/oauth/access_token",
                params={
                    "grant_type": "fb_exchange_token",
                    "client_id": app_id,
                    "client_secret": app_secret,
                    "fb_exchange_token": user_access_token
                })
            llt = r.json()["access_token"]
            print("Long lived access token is :", llt)
            return llt
        except KeyError:
            print("unable to get long lived access token")

    def get_page_access_token(self, app_id, long_lived_token):
        try:
            # print("Getting Page access Token")
            URL = "https://graph.facebook.com/v5.0/"+app_id
            r = __requests.get(
                url=URL,
                params={
                    "fields": "access_token",
                    "access_token": long_lived_token
                })
            # print(r.json())
            page_access_token = r.json()["access_token"]
            return page_access_token
        except KeyError:
            print("Invalid page access token."
                  "Please check your user access tokens")

    def login(self):
        if self.twitter:
            tcreds = self.config.creds["twitter"]
            self.twitter_client = twitter.Api(
                consumer_key=tcreds["consumer_key"],
                consumer_secret=tcreds["consumer_secret"],
                access_token_key=tcreds["access_token_key"],
                access_token_secret=tcreds["access_token_secret"])
        if self.instagram:
            insta_creds = self.config.creds["instagram"]
            self.instagram_client = __ig(
                insta_creds["username"], insta_creds["password"])
            self.instagram_client.login()
        if self.facebook:
            facebook_creds = self.config.creds["facebook"]
            page_access_token = facebook_creds["page_access_token"]
            user_access_token = facebook_creds["user_access_token"]
            app_id = facebook_creds["app_id"]
            app_secret = facebook_creds["app_secret"]
            if self.check_access_token(page_access_token):
                self.facebook_client = facebook.GraphAPI(
                    access_token=page_access_token,
                    version="3.0")
            elif self.check_access_token(user_access_token):
                long_lived_token = self.get_long_access_token(
                    app_id, app_secret, user_access_token)
                page_access_token = self.get_page_access_token(
                    app_id, long_lived_token)
                self.facebook_client = facebook.GraphAPI(
                    access_token=page_access_token,
                    version="3.0")
            else:
                print("Invalid token found for Facebook." +
                      "Will not post on Facebook.")
                self.facebook = False

    def logout(self):
        if self.instagram:
            self.instagram_client.logout()

    def upload_to_twitter(self, file):
        try:
            self.twitter_client.PostUpdate(
                random.choice(self.caption.twitter_caps), file)
            print(f"Uploaded {file} to Twitter..")
        except Exception as e:
            print("Error occured {}" .format(str(e)))

    def upload_to_ig(self, file):
        try:
            self.instagram_client.uploadPhoto(
                file, caption=random.choice(self.caption.insta_caps))
            print(f"Uploaded {file} to Instagram..")
        except Exception as e:
            print("Error occured {}" .format(str(e)))

    def upload_to_fb(self, file):
        try:
            photo = open(file, "rb")
            self.facebook_client.put_photo(
                image=photo,
                message=random.choice(self.caption.facebook_caps),
            )
            photo.close()
            print(f"Uploaded {file} to Facebook..")
        except Exception as e:
            print("Error occured: {}" .format(str(e)))

    def start_upload(self, file):
        if self.instagram:
            self.upload_to_ig(file)
        if self.twitter:
            self.upload_to_twitter(file)
        if self.facebook:
            self.upload_to_fb(file)

    def main(self):
        self.redpy.createFolder()
        files_to_upload = glob.glob('*.jpg')
        local_upload = True
        num_of_upload = int(
            input("Enter the number of files to be uploaded: "))
        if len(files_to_upload) == 0:
            for sub in self.config.subreddits:
                files_to_upload = self.redpy._getImages(
                    self.redpy._generateJSON(
                        sub, self.config.sub_category), num_of_upload)
            local_upload = False
        random.shuffle(files_to_upload)
        max_limit = len(files_to_upload)
        if num_of_upload > max_limit:
            print("Files insufficient")
            print("Setting upload limit to ", max_limit)
            num_of_upload = max_limit
        files_to_upload = files_to_upload[:num_of_upload]
        print('Starting upload')
        for index, file in enumerate(files_to_upload):
            print("Upload Count: ", index)
            if local_upload:
                self.start_upload(file)
            else:
                self.redpy._DownloadFiles([file])
                self.start_upload(__os.path.join(curr_dir,
                                                 'red_media', '0.jpg'))
            time.sleep(self.delay)
        self.logout()
        print("Upload completed")


if __name__ == '__main__':
    RedIns().main()
