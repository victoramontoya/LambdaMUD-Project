from rest_framework import serializers, viewsets
from .models import Conversation, Player

# class ConversationSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Conversation
#         fields = ('user', 'message')

#     def create(self, validated_data):
#         current_user = self.context['request'].user
        
#         current_player = Player.objects.get(user = current_user)

#         chat = Conversation.objects.create( player=current_player, **validated_data)
#         return chat