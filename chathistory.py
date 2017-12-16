from microsoftbotframework import MongodbState, Config

class DataStore:
    """A simple example class"""

    def get_history(self):
        mongodb_state = MongodbState(config=Config())
        info = mongodb_state.get_activities(count=10)
        return info

    def get_lastchat(self):
        mongodb_state = MongodbState(config=Config())
        info = mongodb_state.get_activities(count=3)
        return info
    def get_lastnumberofchats(self, x):
        mongodb_state = MongodbState(config=Config())
        info = mongodb_state.get_activities(count=x)
        return info    
    def get_name(self):
        mongodb_state = MongodbState(config=Config())
        data = mongodb_state.get_user_data()
        return data
    # def set_name(self):
    #     mongodb_state = MongodbState(config=Config())
    #     mongodb_state.set_user_data(values, user_id=None, bot=False, fill=None)
