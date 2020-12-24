import configparser

# Instagram
user = ""
passw = ""
IG = False

# Twitter
consumer_key = ""
consumer_secret = ""
access_token_key = ""
access_token_secret = ""
TWITTER = False

# Facebook
page_access_token = ""
fb_app_id = ""
fb_app_secret = ""
long_lived_token = ""
fb_page_id = ""
FB = False


def get_instagram_data(ig_section):
    return ig_section["username"], ig_section["password"]


def get_fb_data(fb_section):
    return (
        fb_section["page_access_token"],
        fb_section["app_id"],
        fb_section["app_secret"],
        fb_section["page_id"],
    )


def get_twitter_data(t_section):
    return (
        t_section["consumer_key"],
        t_section["consumer_secret"],
        t_section["access_token_key"],
        t_section["access_token_secret"],
    )


def get_data():
    """
    Gets data from config file
    """

    c = configparser.ConfigParser()
    c.read("config.ini")

    print(eval(c["Post"]["Instagram"]))
    print(eval(c["Post"]["Facebook"]))
    print(eval(c["Post"]["Twitter"]))

    if eval(c["Post"]["Instagram"]):
        global user, passw, IG
        IG = True
        user, passw = get_instagram_data(c["Instagram"])
    if eval(c["Post"]["Facebook"]):
        global user_access_token, fb_app_id, fb_app_secret, fb_page_id, FB
        FB = True
        print(FB)
        user_access_token, fb_app_id, fb_app_secret, fb_page_id = get_fb_data(
            c["Facebook"]
        )
    if eval(c["Post"]["Twitter"]):
        global consumer_key, consumer_secret, access_token_key, access_token_secret, TWITTER
        TWITTER = True
        (
            consumer_key,
            consumer_secret,
            access_token_key,
            access_token_secret,
        ) = get_twitter_data(c["Twitter"])
