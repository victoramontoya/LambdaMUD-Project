from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import json
from pusher import Pusher
# from .models import Conversation
from django.contrib.auth.decorators import login_required

# instantiate pusher
# pusher = Pusher(app_id=u'PUSHER_APP_ID', key=u'PUSHER_APP_KEY', secret=u'PUSHER_APP_SECRET', cluster=u'PUSHER_CLUSTER')
#     # Create your views here.
#     #add the login required decorator, so the method cannot be accessed withour login
# @login_required(login_url='login/')
# def index(request):
#         return render(request,"chat.html")

#     #use the csrf_exempt decorator to exempt this function from csrf checks
# @csrf_exempt
# def broadcast(request):
#         # collect the message from the post parameters, and save to the database
#         message.save()
#         # create an dictionary from the message instance so we can send only required details to pusher
#         message = {'name': message.user.username, 'status': message.status, 'message': message.message, 'id': message.id}
#         #trigger the message, channel and event to pusher
#         pusher.trigger(u'a_channel', u'an_event', message)
#         # return a json response of the broadcasted message
#         return JsonResponse(message, safe=False)

#     #return all conversations in the database
# def conversations(request):
#         data = Conversation.objects.all()
#         # loop through the data and create a new list from them. Alternatively, we can serialize the whole object and send the serialized response 
#         data = [{'name': person.user.username, 'status': person.status, 'message': person.message, 'id': person.id} for person in data]
#         # return a json response of the broadcasted messgae
#         return JsonResponse(data, safe=False)

#     #use the csrf_exempt decorator to exempt this function from csrf checks
# @csrf_exempt
# def delivered(request, id):

#         message = Conversation.objects.get(pk=id)
#         # verify it is not the same user who sent the message that wants to trigger a delivered event
#         if request.user.id != message.user.id:
#             socket_id = request.POST.get('socket_id', '')
#             message.status = 'Delivered'
#             message.save()
#             message = {'name': message.user.username, 'status': message.status, 'message': message.message, 'id': message.id}
#             pusher.trigger(u'a_channel', u'delivered_message', message, socket_id)
#             return HttpResponse('ok')
#         else:
#             return HttpResponse('Awaiting Delivery')

@csrf_exempt
def register(request):
    data = json.loads(request.body)
    username = data['username']
    password1 = data['password1']
    password2 = data['password2']
    user=User(username=username)
    if len(username) < 3:
        response = JsonResponse({"error":"Username must be at least 3 characters."}, safe=True, status=500)
    elif len(password1) < 5:
        response = JsonResponse({"error":"Password must be at least 5 characters."}, safe=True, status=500)
    elif password1 != password2:
        response = JsonResponse({"error":"The two password fields didn't match."}, safe=True, status=500)
    else:
      try:
          user.validate_unique()
      except ValidationError:
          response = JsonResponse({"error":"A user with that username already exists."}, safe=True, status=500)
      else:
          user.set_password(password1)
          user.save()
          response = JsonResponse({"key":str(user.auth_token)}, safe=True, status=201)
    return response

@csrf_exempt
def login(request):
    data = json.loads(request.body)
    username = data['username']
    password = data['password']
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        response = JsonResponse({"error":"User does not exist."}, safe=True, status=500)
    else:
        if user.check_password(password):
            response = JsonResponse({"key":str(user.auth_token)}, safe=True, status=200)
        else:
            response = JsonResponse({"error":"Unable to log in with provided credentials."}, safe=True, status=500)
    return response


