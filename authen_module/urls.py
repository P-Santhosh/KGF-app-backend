
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^create-customer$', views.create_customer, name='index1'),
    url(r'^view-customer$', views.view_customer, name='index1'),
    url(r'^sortbyphno_customer$', views.sortbyphno_customer, name='index1'),
    url(r'^create-loan$', views.create_loan, name='index1'),
    url(r'^view-loan$', views.view_loan, name='index1'),
    url(r'^sortbyname_loan$', views.sortbyname_loan, name='index1'),
    url(r'^delete-loan$', views.delete_loan, name='index1'),
    url(r'^create-user$', views.create_user, name='index1'),
    url(r'^view-user$', views.view_user, name='index1'),
    url(r'^sortbyname_user$', views.sortbyname_user, name='index1'),
    url(r'^delete-user$', views.delete_user, name='index1'),
    url(r'^login-user$', views.login_user, name='index1'),
 
]
#pipenv 
#pip install pipenv
#pipenv --python 3.9.5
#pipenv shell
#pipenv install django
#pipenv install 
#python manage.py runserver

