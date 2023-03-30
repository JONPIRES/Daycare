from django.shortcuts import render, redirect
# you need to implement the code below to be able to add the Class Based View(CBV)
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from .models import Kids, Feeding
from .forms import FeedingForm


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
# the kid_id is defined on the urls.py path for kids_detail. similar to req.params and does not need a ','

def kids_detail(req, kid_id):
    kid = Kids.objects.get(id=kid_id)
    feeding_form = FeedingForm()
    return render(req,'kids/detail.html', {
        'kid': kid, 'feeding_form': feeding_form
        })

class KidCreate(CreateView):
#this will add all the field in the cat model or you can create a list to add only the keys you want in this model
# Also, insteade of redirecting the page from here, we can use a dunder method inside the class model(Kids) the get_absolute_url
    model = Kids
    fields = '__all__'

class KidUpdate(UpdateView):
    # for this CBV to be accessed it needs to in a folder with the same name as your app, inside templates
    # in this case is templates/main_app, and have a file with the name model_form.html, in this case (kids_form.html)
    model = Kids
    fields = ['description','nickname', 'age' ]

class KidDelete(DeleteView):
# the same file, as the above example, needs to be created for the delete CBV but with the name 'model_confirm_delete.html', because the delete button on the detail.html is only a 
# get request, so it needs a file to render the form. but if i wanted to make the delete button functional, 
# I would need to wrap the button in a form directly.
    model = Kids
    success_url = '/kids'

def add_feeding(req, kid_id):
    # req.POST is like the req.body in express. it gives you wtv is in the form from the post method
    form = FeedingForm(req.POST)
    if form.is_valid():
        # in this case, I can't save automatically, because the req.POST that is comming in, does not have a kid_id yet. because in the forms.py I only pass, date and meal.
        # so I add 'commit=False' to save so it doesn't commit to the DB, and then I add the kid_id to the object before saving.
        new_feeding=form.save(commit=False)
        new_feeding.kid_id = kid_id
        new_feeding.save()
        # redirect works simmilar to express, but you don't need {} to pass arguments.
        return redirect('detail', kid_id=kid_id)

