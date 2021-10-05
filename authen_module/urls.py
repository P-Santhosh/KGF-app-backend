
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^create-customer$', views.create_customer, name='index1'),
    #url(r'^edit-employee$',views.edit_employee, name='index1'),
    #url(r'^get-employee$', views.get_employee, name='index1'),
    #url(r'^delete-employee$', views.delete_employee, name='index1'),
    #url(r'^view-employee$', views.view_employee, name='index1'),
    #url(r'^viewage-employees$', views.viewage_employees, name='index1'),
    #url(r'^viewbyemail-employee$', views.viewbyemail_employee, name='index1'),
    #url(r'^login-employee$', views.login_employee, name='index1'),
    #url(r'^viewbyname-employees$', views.viewbyname_employees, name='index1'),
    #url(r'^view-employees$', views.view_employees, name='index1'),
    #url(r'^imgupload-employee$', views.imgupload_employee, name='index1'),
]
#pipenv
#pip install pipenv
#pipenv --python 3.9.5
#pipenv shell
#pipenv install django
#pipenv install 
#python manage.py runserver

