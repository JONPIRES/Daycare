from django.shortcuts import render

# Create your views here.

kids = [
    {'name':'Julio', 'age': 2, 'nickname': 'Bud'},
    {'name':'William', 'age': 4, 'nickname': 'Willy'}
]

def home(req):
    return render(req, 'home.html')

def about(req):
    return render(req,'about.html')

def kids_index(req):
    return render(req,'kids/index.html',{
        'kids':kids
    })