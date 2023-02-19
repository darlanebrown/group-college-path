# group-college-path
## Perpare for Railway deployment

* Prereq: [You have Pipenv installed.
  ](https://github.com/kickstartcoding/pipenv-getting-started) You have Pipenv
  installed globally (Ubuntu GNU/Linux,
  type `sudo apt-get install python3-pip -y && sudo pip3 install pipenv`)

1. Assuming `group-college-path` is the name of your project, 

2. Go into the newly created project, and use `pipenv` to get your virtualenv
setup:
```
cd group-college-path
wsl
sudo apt-get install python3-pip -y && sudo pip3 install pipenv
pipenv shell
pipenv install
```
3. install gunicorn
```
pip install gunicorn
```
4. create requirements
```
pip freeze > requirements
```
5. Create runtime.txt
Railway needs to know the version of python you used for your project, to know the version used type `python --version` in your terminal copy, paste and save the version inside your runtime.txt `python -3.10.6`
6. Next, we need to make some adjustments to our settings.py file
Look for the line that has
```
ALLOWED_HOST = [ ]
```
and change it to
```
ALLOWED_HOST = ['*']
```
7. Add following line `/cservices/views.py` import section
```
from django.views.decorators.csrf import csrf_exempt
```
Then add `@csrf_exempt` decorator as following
```
@csrf_exempt
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
```
8. Still on your settings.py file add the following lines of codes in your static section, so your static files can be properly rendered
```
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT =os.path.join(BASE_DIR, 'staticfiles')
```
9. Lastly, we collect our static files into one folder using the following command
```
python manage.py collectstatic
```
10. Next, we push our project to our Github account where we’ll be deploying our project from. Use the following git syntax to add, commit and push your code.
```
git status
git add .
git commit -m ‘Railwayready’
git push
```

Now, we move to our railway app account that was created

### Running locally

1. This starter project *does not* include migrations. Make migrations as such:
```
python manage.py makemigrations
```

2. Run the migrations to actually create the SQLite database:
```
python manage.py migrate
```

3. Get the server running:
```
python manage.py runserver
```