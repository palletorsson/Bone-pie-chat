from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie import fields

from chat.models import Chat 

class ChatResource(ModelResource): 
    class Meta:
        queryset = Chat.objects.all() 
        resource_name = 'chat'
        fields = ('message', 'user',)
        ordering = ["timestamp"] 
        limit = '100'
        authorization = Authorization()
        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get']
