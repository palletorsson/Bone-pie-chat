from tastypie.api import Api
from resources import ChatResource # Tweets

v1 = Api("v1")
v1.register(ChatResource()) # Tweets
