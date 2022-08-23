# # When you build this, please make sure that your program meets the following criteria:

# http://localhost:8000 - have this display a nice looking HTML form.  The form should be submitted to '/result'
# http://localhost:8000/result - have this display a html template with the information that was submitted by POST
# Don't forget that any inputs we want to be able to access from the form submission need to have a name!

# It's always a good idea to print request.POST to see if the form is delivering all the information you need in your routing method.

#  Create a new Django application  Have the root route ("/") show a page with the form  
# Have the "/result" route display the information from the form on a new HTML page  
# NINJA BONUS: Use a CSS framework to style your form  
# NINJA BONUS: Include a set of radio buttons on your form  
# SENSEI BONUS: Include a set of checkboxes on your form

from django.urls import path, include


urlpatterns = [
    path('', include('dojoSurvey.urls')),
]
 