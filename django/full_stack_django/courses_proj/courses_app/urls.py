from django.urls import path
from . import views

urlpatterns = [
    path('',views.new),
    path('create',views.create),
    path('courses/destroy/<int:course_id>',views.destroy),
    path('delete/<int:course_id>',views.delete),
]