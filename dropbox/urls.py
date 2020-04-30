from django.urls import path

from . import views

urlpatterns = [
    	#path('', views.Form, name='Form'),
		path('form/', views.Form, name = 'Form'),
		path('upload/', views.Upload, name = 'Upload'),
]
