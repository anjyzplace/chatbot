from microsoftbotframework import MongodbState, Config

config=Config()
arry = config._get_yaml_config('config.yaml')

def MONGO_URI():
    value = arry['mongodb']['uri']
    return value
