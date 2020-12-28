# RedIns
Get images from Reddit and upload to Instagram, Twitter and FaceBook

- Join our Telegram group via the link given [below](#community)
- Read about it on my [blog](https://prashants.in/blog/redins-post-to-social-media-from-reddit/)


## Clone from repository
`git clone https://github.com/prashantsengar/RedIns`

## Install requirements
`pip install -r requirements.txt`


## Configuration
- Rename config_example.ini to config.ini
- Open config.ini and add the required API keys (see the next secyion to see how to get them) 
- Set `Instagram = True` if you want to post to Instagram. Similarly, set True or False for other accounts
- Set captions in `cap.py`

## Getting API keys
- To learn how to get Facebook `app_id` and `app_secret`, visit this [page](https://theonetechnologies.com/blog/post/how-to-get-facebook-application-id-and-secret-key)
To get `page access token`, see this [page](https://elfsight.com/blog/2017/10/how-to-get-facebook-access-token/)
- To learn how to get Twitter API keys, visit this [page](https://themepacific.com/how-to-generate-api-key-consumer-token-access-key-for-twitter-oauth/994/)

### How to use
- Open Command prompt or terminal
- Go to Reddit.com and download the JSON of any subreddit and save it in the 'JSONS.py' file and follow the instruction there.
- Edit or Add captions to be used in 'caps.py' by following the instructions present there.
- Type `python redins.py` or `python3 redins.py`
- Enter the number of files to be uploaded

#### How to download JSON of a subreddit
- Let us say you want to get data of the subreddit /r/memes
- Go to https://reddit.com/r/memes.json
- Save the web page as memes.json in the directory of the project
- Open `JSONs.py` and write `new_JSON('memes.json')` after line 5

*Note:* Due to recent changes in Instagram's private API, Instagram posting might not work. It will be updated to use the new Graph API


## Community 

Read the [contributing guide](./CONTRIBUTING.md)

Join the Telegram group for support and contributing. If you want to contribute, joining the group helps us all a lot because you can get instant feedback.

[<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Telegram_logo.svg/1024px-Telegram_logo.svg.png" alt="mTracker Telegram Group" width="150" height="150">](https://t.me/joinchat/INDdLhNoG-yYqLb-sf8Rlg)
