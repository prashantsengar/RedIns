# Edit or Add Captions following the examples present below
# For adding Instagram Captions, use self.add_insta_caps(()
# For adding Twitter Captions, use self.add_twitter_caps()
# Please do these below line 19


class Caption:

    def __init__(self):
        self.insta_caps = []
        self.twitter_caps = []
        self.facebook_caps = []

    def add_insta_caps(self, string):
        self.insta_caps.append(string)

    def add_twitter_caps(self, string):
        self.twitter_caps.append(string)

    def add_facebook_caps(self, string):
        self.facebook_caps.append(string)

    def default_add(self):
        self.add_insta_caps("""Follow @einteresting
                .
                .
                .
                .
                .
                #dankmemes #memes #dank #meme #funny #funnymemes #lol
                #edgymemes #lmao #memesdaily #dankmeme #offensivememes
                #comedy #offensive #follow #like #funnyvideos #fortnitememes
                #haha #oof
                """)

        self.add_insta_caps("""Follow @einteresting
                .
                .
                .
                .
                #meme #memes #funny #dankmemes #dank #lol
                #memesdaily #lmao #funnymemes #follow
                #fortnite #like #edgy #dankmeme #edgymemes
                #comedy #cringe #humor #funnyvideos #lmfao
                #instagram #hilarious #oof #savage""")

        self.add_insta_caps("""Follow @einteresting
                .
                .
                .
                .
                .
                #laugh #gaming #minecraft #cancer #music #f #funnymeme
                #instagood #kpop #edgymeme #love #roblox #joke #viral #lit
                #memepage #ifunny #lilpump #rofl #life #donaldtrump
                """)
        self.add_insta_caps("""Follow @einteresing
                .
                .
                .
                .
                #funny #funnymeme #funnymemes #memes #meme #funnytext
                # funnyvideos #hilarious #crazy #humor #epic #instafun
                """)

        self.add_twitter_caps(
            "Follow @E__interesting for more #funny #lol #memes #follow")
        self.add_twitter_caps(
            "Follow @E__interesting for more #follow #dankmemes #reddit")
        self.add_twitter_caps(
            "Follow @E__interesting for more #edgymemes #comedy #retweet")

        self.add_facebook_caps(
            "Follow @SomeGuy for more #funny #lol #memes #follow")
        self.add_facebook_caps(
            "Follow @SomeGuy for more #follow #dankmemes #reddit")
        self.add_facebook_caps(
            "Follow @RandomGuy for more #edgymemes #comedy #retweet")
