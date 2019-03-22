from django.shortcuts import render
from django import forms


from cservices.models import Application



class NewApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = [
            'first_name',
            'last_name',
            'email',
            'phone',
            'education',
            'username',
            'password'
        ]
        
        
class EditApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = [
            'first_name',
            'last_name',
            'email',
            'phone',
            'education',
            'username',
            'password'
        ]
        


def formpage(request):
    if request.method == 'POST':
    
        form = NewApplicationForm(request.POST) 

        if form.is_valid():
            user = form.save()

            # As soon as our new user is  created, we make this user be
            # instantly "logged in".
            auth.login(request, user)
            return redirect("/")

    else:
        # if a GET we'll create a blank form
        form = NewApplicationForm()

    context = {
        'form': form,
    }
    
   
    return render(request, 'form.html', context)


# team the pages below will be added after


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


