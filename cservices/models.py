from django.db import models
from django import forms

import hashlib

BEST_TIME= [
    ('morning before 10am', 'Morning before 10am'),
    ('morning after 10am', 'morning after 10am'),
    ('afternoon', 'Afternoon'),
    ('late afternoon', 'Late-Afternoon after 4pm'),
    ]

# Create your models here.

class Application(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    email = models.EmailField(max_length=120)
    phone = models.CharField(max_length=127)
    current_education = models.CharField(max_length=127)
    desired_interest  = models.CharField(max_length=127)
    desired_major = models.CharField(max_length=127)




# we could add 
# def get_gravatar(self):
        # This is the example code found online for Gravatar, which will
        # randomly generate avatars based on email (we'll use username in this
        # case).
#        email = self.username
#        encoded = hashlib.md5(email.encode('utf8')).hexdigest()
#        gravatar_url = "http://www.gravatar.com/avatar/%s?d=identicon" % encoded
#        return gravatar_url    

# check admin panel to see how information is ported over.
#   def __str__(self):
#        return () 
    
#class ApplicationTime(models.Model):    
#   best_time = models.CharField(label='Prefered time frame?') 
#   widget = models.RadioSelect(choices=BEST_TIME)
