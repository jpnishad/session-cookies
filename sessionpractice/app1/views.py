from django.shortcuts import render


# Create your views here.
def setSession(request):
    request.session['name'] = 'jay'
    request.session['lname'] = 'prakash'
    return render(request, 'app1/setSession.html')


def getSession(request):
    # name = request.session['name']
    name = request.session.get('name', default='guest')
    lname = request.session.get('lname')
    keys = request.session.items()
    # age = request.session.setdefault('age', '26')
    return render(request, 'app1/getSession.html', {'name': name, 'keys': keys})


def delSession(request):
    # if 'name' in request.session:
    #     del request.session['name']
    #     del request.session['lname']
    request.session.flush()
    request.session.clear_expired()
    return render(request, 'app1/delSession.html')
