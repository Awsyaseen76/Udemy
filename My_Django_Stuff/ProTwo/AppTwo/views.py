from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import Topic, Webpage, AccessRecord, Users

# Create your views here.
def index(request):
    return HttpResponse('<em>My Second App </em>')

def app_two_index(request):
    # return HttpResponse('<h1>This is from the AppTwo<h2>')
    # Create the content to inject
    my_dict = {'insertToIndex':'This content are dynamically injected on the view from my_dict'}
    return render(request, 'AppTwo/index.html', context=my_dict)

def helpMe(request):
    help_content = {
        'help_1': 'for any further help go to https://www.udemy.com'
        }
    return render(request, 'AppTwo/help.html', context=help_content)

def pictures(request):
    return render(request, 'AppTwo/pictures.html')

def access_records_list(request):
    acc_rec = AccessRecord.objects.order_by('date')
    date_dic = {'access_records': acc_rec}
    return render(request, 'AppTwo/access_records.html', context=date_dic)

def users_list(request):
    users = Users.objects.order_by('email')
    users_dict = {'users': users}
    return render(request, 'AppTwo/users_list.html', context=users_dict)