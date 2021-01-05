import configparser
import ast
import logging

logger = logging.getLogger()


class Config:
    """
    Load data from config file
    """

    def __init__(self, file="config.ini"):

        c = configparser.ConfigParser()
        c.read(file)

        # self.modules - dict of social media websites to post
        # Eg: {'instagram':True, 'facebook':False}
        self.modules = {str(a): ast.literal_eval(b) for a, b in dict(c["post"]).items()}

        # credentials for all social media profiles
        # {'instagram':{'username':'@username', 'password':'PASSWORD'}}
        self.credentials = dict()
        for module, should_post in self.modules.items():
            if should_post is True:
                self.credentials[module] = {
                    a: ast.literal_eval(b) for a, b in dict(c[module]).items()
                }

        self.subreddits = ast.literal_eval(c["reddit"]["subreddits"])
        self.sub_category = ast.literal_eval(c["reddit"]["category"])

    def check_data(self):

        print("Subreddits Loaded: ", ",".join(self.subreddits))
        for module, should_post in self.modules.items():
            logger.debug(module, "Loaded" if should_post is True else "Not Loaded")
            if should_post is True:
                logger.debug("Credentials:")
                for key, value in self.credentials[module].items():
                    logger.debug(key, value)
