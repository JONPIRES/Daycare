from django.shortcuts import render
from .models import Kids

# Create your views here.

# kids = [
#     {'name':'Julio', 'age': 2, 'nickname': 'Bud', 'description':"rascal"},
#     {'name':'William', 'age': 4, 'nickname': 'Willy', 'description':"chill"}
# ]

def home(req):
    return render(req, 'home.html')

def about(req):
    return render(req,'about.html')

def kids_index(req):
    kids = Kids.objects.all()
    return render(req,'kids/index.html',{'kids':kids})
# the kid_id is defined on the urls.py path for kids_detail. similar to req.params
def kids_detail(req, kid_id):
    kid = Kids.objects.get(id=kid_id)
    return render(req,'kids/detail.html', {'kid': kid})