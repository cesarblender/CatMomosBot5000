import os
import facebook

BOT_POST_FREQUENCY = 120 * 3 # Each 3 hours

def getGraphAPI() -> facebook.GraphAPI:
    token = os.getenv("TOKEN")

    return facebook.GraphAPI(token)
