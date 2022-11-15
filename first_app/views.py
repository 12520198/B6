from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages

from .form import NewUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='login')
def show_data(request):
    return render(request, template_name='home.html')


def register_form(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        # print(request.POST)
        print(form.is_valid())
        if form.is_valid():
            print(request.POST)
            form.save()
           
            return HttpResponse('login successful...')
        else:
            return render(request,template_name='register.html',context={'form': form})
                

    else:
        return render(request, template_name='register.html',
                      context={'register_form': NewUserForm()})


# from django.contrib.auth.forms import AuthenticationForm
def login_user(request):
    if request.method == 'POST':
        data = request.POST
        # form = AuthenticationForm(request, data=(request.POST))
        # print(dir(form))
        # if data.is_valid:
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username=username, password=password)
        # print(user)
        if user:
            login(request, user)
            messages.success(request, f"login by {username}")
            print('--------------',(request.session.values()))
            return redirect('homepage')
        else:
            messages.error(request, 'please register first....!')
            return redirect('register')
        # return redirect('homepage')
        
    else:
        return render(request, template_name='login_user.html',
                      context={'login_form': AuthenticationForm()})


# so by logout functionality (predefind) the data will delete from client(cookies) as well as server(sessions)
# from django.contrib.auth import authenticate, login, logout
def logout_user(request):     # IMP
    logout(request)
    print(request.user)
    return redirect('login')


#-----------------------------------------------------------
# django session
# those two functionality to chect the browser accept the cookies or not
# and alternate way to check in setting.py (INSTALLED APP, MIDDLEWARE)
# 1 - set_test_cookie() - to create the test cookie
# 2 - test_cookie_worked() - return bool if browser accept cookie
# 3 - delete_test_cookie() - delete crested cookie


def cookie_session(request):
    request.session.set_test_cookie()
    return HttpResponse('<h1>cookie set suceesfully</h1>')

def cookie_delete(request):
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        return HttpResponse('<h1>set cookie delete succesfully</h1><br>your browser accept cookie')

    else:
        return HttpResponse('cookie not suported')

# --------------------------------------------------------

# create the session ans access the session
def create_session(request):
    request.session['city'] = 'pune'
    request.session['pincode'] = '430013'
    return HttpResponse('<h1>Session</h1><br>the session are set')


def access_session(request):
    responce = '<h1>session data</h1><br>'
    if request.session['city']:
        responce += "city - {}<br>".format(request.session['city']) 
    if request.session['pincode']:
        responce += "pincode - {}".format(request.session['pincode'])

        return HttpResponse(responce)
    else:
        return HttpResponse('sessions are not found')


# ------------------------------------------------------------------

# delete the session
def delete_session(request):
    try:
        del request.session['city']
        del request.session['pincode']

    except KeyError as msg:
        return HttpResponse(msg)

    return HttpResponse('<h1>the session delete successfully</h1>')





