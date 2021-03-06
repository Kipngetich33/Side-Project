from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from africastalking.AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException
from django.http import HttpResponse,response
from . models import Chat
from . forms import ProfileUpdateForm, HelpForm
from django.http import JsonResponse


# Create your views here.
redirect
def home(request):
    c = Chat.objects.all() 
    current_user = request.user
    return render(request,'home.html',{'chat':c,"current_user":current_user}) 

def help(request):
    current_user = request.user
    if request.method == 'POST':
        form = HelpForm(request.POST)
        if form.is_valid():
            # get and save data here

            return redirect( home)
    else:
        form = HelpForm()

    return render(request,'help.html',{"current_user":current_user,"form":form})

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

    if request.method == 'POST':
        # form = ProfileUpdateForm(request.POST)
        # if form.is_valid():
        #     new_caption = form.cleaned_data['image_caption']
        #     update_image.image_caption = new_caption
        #     update_image.save_image() 

        #     return redirect( more ,image_id)
        pass
    else:
        form = ProfileUpdateForm()

    return render(request,'update_profile.html')

def create_order(request):
    if request.method == 'POST':
        data = request.POST['first-input']
        print(data)
        
        # form1 = Schedule(day = 'Monday', course = 'ct', year1 = '1', year2 ='2' ,year3 = '3' ,year4 = '4',period = '7' ,room1 = '100',room2 = '120',room3 = data,room4 = data1)
        # form1.save()
        return redirect(home)
    return redirect(help)