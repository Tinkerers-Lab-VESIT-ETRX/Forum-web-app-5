from django.contrib import admin
from django.urls import path
# from Discussion_Forum.views import *
from django.contrib import admin

from django.urls import include, path
# import views from
# from '../Discussion_Forum'
from Discussion_Forum import views

admin.site.site_header = "Login to Ashwini Gawhale"
admin.site.site_title = "Welcome to Ashwini's Portal"
admin.site.index_title = "WELCOME TO THIS PORTAL"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('addInForum/',views.addInForum,name='addInForum'),
    path('addInDiscussion/',views.addInDiscussion,name='addInDiscussion'),
]
