from django.urls import path,re_path 
from .views import home_view
# home_detail_view, home_list_view

urlpatterns = [ 
    path('', home_view, name='contact-create'),  
    #path('renovation/', home_list_view),
    #path('renovation/<int:blog_id>', home_detail_view),
]