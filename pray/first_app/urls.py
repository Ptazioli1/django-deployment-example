from django.urls import path
from first_app import views

app_name = 'first_app'

urlpatterns = [
     path('formpage/',views.form_name_view,name='form_name'),
     path('relative/',views.relative,name='relative'),
     path('other/',views.other,name='other'),
     path('register/',views.register,name='register'),
     path('user_login/',views.user_login,name='user_login')
     ]
