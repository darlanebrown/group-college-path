from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth.models import User
from django.contrib import auth



from cservices.models import Application



class NewApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = [
            'first_name',
            'last_name',
            'email',
            'phone',
            'current_education',
            'desired_interest',
            'desired_major',
        ]
        
        
class EditApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = [
            'first_name',
            'last_name',
            'email',
            'phone',
            'current_education',
            'desired_interest',
            'desired_major',
        ]
        
def formpage(request):
    if request.method == 'POST':
    
        form = NewApplicationForm(request.POST) 

        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            current_education = form.cleaned_data['current_education']
            desired_interest = form.cleaned_data['desired_interest']
            desired_major = form.cleaned_data['desired_major']
            
            user = form.save()

            # As soon as our new user is  created, we make this user be
            # instantly "logged in".
            #auth.login(request, user)
            return redirect('https://calendly.com/nadiabc/collegepath')

    else:
        # if a GET we'll create a blank form
        form = NewApplicationForm()

    context = {
        'form': form,
    }
    
   
    return render(request, 'form.html', context)

#admin/counselor should login here
#def employees_only(request):

    # Check if the user is logged in.
#    if not request.user.is_authenticated:

        # Use Django's built-in "messages" system to us send the user a message
        # that appears on whatever next page they visit (but goes away when
        # they go to a new page)
#        messages.warning(request, "You need to log in to view Employee's Only")
#        return redirect('/')

#    all_users = User.objects.all()
#    registrations = Registration.objects.all()
#    context = {
#        'users': all_users,
#        'registrations': registrations,
#    }

#    return render(request, 'employees_only.html', context)

# below specifies the homepage 

def homepage(request):
    context = {
    }
    return render(request, 'index.html', context)

# def about(request):
#        context = {
#            'about',
#        }
#        return render(request, 'base.html', context)

#def services(request):
        #context = {
            #'services',
        #}
        #return render(request, 'base.html', context)

#def admin_login(request):
        #context = {
            #'admin_login',
        #}
        #return render(request, 'base.html', context)

# def contact(request):
#        context = {
#            'contact',
#        }
#        return render(request, 'base.html', context)


