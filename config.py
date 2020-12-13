import configparser
import ast


class Config:
    """
    Load data from config file
    """

    def __init__(self, file='config.ini'):

        c = configparser.ConfigParser()
        c.read(file)

        self.modules = {a: ast.literal_eval(b)
                        for a, b in dict(c["post"]).items()}
        self.creds = dict()
        for module, status in self.modules.items():
            if status:
                self.creds[module] = {a: ast.literal_eval(b)
                                      for a, b in dict(c[module]).items()}

        self.subreddits = ast.literal_eval(c['reddit']['subreddits'])
        self.sub_category = ast.literal_eval(c['reddit']['category'])

    def check_data(self):

        print("Subreddits Loaded: ", ",".join(self.subreddits))
        for module, status in self.modules.items():
            print(module, "Loaded" if status else "Not Loaded")
            if status:
                print("Credentials:")
                for key, value in self.creds[module].items():
                    print("\t", key, ": ", value)
