from microsoftbotframework import MongodbState, Config

class DataStore:
    """A simple example class"""

    def get_history(self):
        mongodb_state = MongodbState(config=Config())
        info = mongodb_state.get_activities(count=10)
        return info