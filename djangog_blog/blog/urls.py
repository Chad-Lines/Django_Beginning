from django.urls import path
from . import views             # '.' indicates the current directory

urlpatterns = [
    # path('', views.post_list, name='post_list')
    path(
        '',                 # This is the root URL (127.0.0.1:8000)
        views.post_list,    # This is the post_list view in the views.py file
        name='post_list'    # This is the name of the URL used to identify the view
    ),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),  # Path for a dedicated post view
    path('post_new', views.post_new, name='post_new'),
]