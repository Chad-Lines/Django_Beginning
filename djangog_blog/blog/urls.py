from django.urls import path
from . import views             # '.' indicates the current directory

urlpatterns = [
    path(
        '',                 # This is the root URL (127.0.0.1:8000)
        views.post_list,    # This is the post_list view in the views.py file
        name='post_list'    # This is the name of the URL used to identify the view
    ),
]