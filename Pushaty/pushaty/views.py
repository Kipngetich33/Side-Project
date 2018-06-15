from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from africastalking.AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException
from django.http import HttpResponse,response
from . models import Chat
from django.http import JsonResponse

# Create your views here.

def home(request):
    c = Chat.objects.all() 
    current_user = request.user
    return render(request,'home.html',{'chat':c,"current_user":current_user}) 

@login_required(login_url='/accounts/login/')
def messages(request):
    c = Chat.objects.all()
    current_user = 'Vincent'
    return render(request,'messages.html',{'chat':c,"current_user":current_user})

def post(request):
    if request.method == 'POST':
        # msg = request.POST.get('msgbox',None)
        msg = request.POST.get('chat-msg')
        print(msg)
        c = Chat(user = request.user, message = msg)
        if msg != '': 
            c.save()
            return JsonResponse({'msg':msg, 'user' : c.user.username})
    else:
        return HttpResponse('Request must be POST')


# the view below is for sending text messages with Africa's talking API

def send_message(request):

    # the username and apiKey below does not belong to me i should change it
    username = 'Nanda'
    apiKey = 'ccd6a5c49876e24e7408a7f2d5f8d6e04a3a8d56f00d9920874ec94ff656d36b'

    to = '0712567583'
    message = 'Test Message'
    gateway = AfricasTalkingGateway(username, apiKey)

    try:
        # That's it, hit send and we'll take care of the rest.
        results = gateway.sendMessage(to, message)

        for recipient in results:
            # status is either "Success" or "error message"
            print('number=%s;status=%s;messageId=%s;cost=%s' % (recipient['number'],
                                                                recipient['status'],
                                                                recipient['messageId'],
                                                                recipient['cost']))

    except AfricasTalkingGatewayException as e:
        print('Encountered an error while sending: %s' % str(e))


    return HttpResponse(response, content_type='text/plain')



# the views below are for the profile creation
def update_profile(request):
    return render(request,'update_profile.html')