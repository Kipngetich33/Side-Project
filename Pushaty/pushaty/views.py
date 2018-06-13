from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# from africastalking.africasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException
from django.http import HttpResponse,response
from . models import Chat
from django.http import JsonResponse

# Create your views here.

@login_required(login_url='/accounts/login/')
def home(request):
    c = Chat.objects.all() 
    return render(request,'home.html',{'chat':c})

def messages(request):
    c = Chat.objects.all()
    return render(request,'messages.html',{'chat':c})

def post(request):
    if request.method == 'POST':
        msg = request.POST.get('msgbox',None)
        c = Chat(user = request.user, message = msg)
        if msg != '':
            c.save()
            return JsonResponse({'msg':msg, 'user' : c.user.username})
    else:
        return HttpResponse('Request must be POST')


# the view below is for sending text messages with Africa's talking API

def send_message(request):
    username = username1
    apiKey = apikey1

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

