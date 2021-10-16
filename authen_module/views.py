from datetime import date
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from authen_module.models import Customer
from authen_module.models import Loan
from authen_module.models import User
from authen_module.serializers import CustomerSerializer
from authen_module.serializers import LoanSerializer
from authen_module.serializers import UserSerializer
import random
import string

from authen_module.library_module import CustomerValidation
from authen_module.library_module import LoanValidation
from authen_module.library_module import UserValidation

# InputUrl:http://127.0.0.1:8000/authen_module/create-customer
# InputJson:
# {"name":"tester5", "dob":"1998-01-01", "age":"20" , "relation":"brother",  "nominee":"ncustomers nominee" , "current_address":"123,current address, karur " ,
# "permanent_address":"123, permanent address, karur " ,"landmark":"bypass " , "pincode":" 639117" , "city":"Karur" , "id_proof_type":"Adhar " ,
# "id_proof_no":" 987654321000000" , "mobile_no":"9876543215 " , "alternative_no":" 9123456789" , "customer_photo":"  img-customer_photo" ,
# "id_proof_photo":"img-id_proof_photo " , "created_by":"tester5", "updated_by":"tester5"}


@api_view(['POST'])
def create_customer(request):
    validation_result = CustomerValidation().validation_for_customer(request=request)
    if validation_result == True:
        entry_exist = Customer.objects.filter(
            mobile_no=request.data['mobile_no'], is_active=True)
        if entry_exist:
            return ({"status": False, "message": "Customer's mobile number is  already exists"})
        customer_id = ''.join(random.choice(string.digits) for _ in range(5))
        entry = Customer.objects.create(customer_id=customer_id, name=request.data['name'],
                                        dob=request.data['dob'], age=request.data['age'],
                                        relation=request.data['relation'], nominee=request.data['nominee'],
                                        current_address=request.data['current_address'],
                                        permanent_address=request.data['permanent_address'],
                                        landmark=request.data['landmark'], pincode=request.data['pincode'],
                                        city=request.data['city'], id_proof_type=request.data['id_proof_type'],
                                        id_proof_no=request.data['id_proof_no'], mobile_no=request.data['mobile_no'],
                                        alternative_no=request.data['alternative_no'],
                                        customer_photo=request.data['customer_photo'], id_proof_photo=request.data['id_proof_photo'],
                                        created_by=request.data['created_by'], updated_by=request.data['updated_by'])
        return Response({"status": True, "message": "Employee Created Successfully"})
    else:
        return Response(validation_result)

# Input url:http://127.0.0.1:8000/authen_module/view-customer


@api_view(['GET'])
def view_customer(request):
    entry_exist = Customer.objects.filter(is_active=True)
    if not entry_exist:
        return Response({"status": False, "message": "Customer's not Exist"})
    serial = CustomerSerializer(entry_exist, many=True)
    return Response({"status": True, "message": "Customer's  Data list", "data": serial.data})

# Input url:http://127.0.0.1:8000/authen_module/sortbyphno_customer?mobile_no=


@api_view(['GET'])
def sortbyphno_customer(request):
    mobile_no = request.GET.get('mobile_no', False)
    if not mobile_no:
        return Response({"status": False, "message": "Customer's mobile number is Required"})
    entry_exist = Customer.objects.filter(mobile_no=mobile_no, is_active=True)
    if not entry_exist:
        return Response({"status": False, "message": "This mobile number not Exist"})
    serial = CustomerSerializer(entry_exist, many=True)
    return Response({"status": True, "message": "Customer datas under this mobile number", "data": serial.data})


# InputUrl:http://127.0.0.1:8000/authen_module/create-loan
# InputJson:
# {"loan_name":"test loan", "created_by":"tester5", "updated_by":"tester5"}
@api_view(['POST'])
def create_loan(request):
    validation_result = LoanValidation().validation_for_loan(request=request)
    if validation_result == True:
        entry = Loan.objects.create(loan_name=request.data['loan_name'],
                                    created_by=request.data['created_by'], updated_by=request.data['updated_by'])
        return Response({"status": True, "message": "New loan is  Created Successfully"})
    else:
        return Response(validation_result)

# Input url:http://127.0.0.1:8000/authen_module/view-loan


@api_view(['GET'])
def view_loan(request):
    entry_exist = Loan.objects.filter(is_active=True)
    if not entry_exist:
        return Response({"status": False, "message": "Loan's not Exist"})
    serial = LoanSerializer(entry_exist, many=True)
    return Response({"status": True, "message": "Various loan  Data list", "data": serial.data})


# Input url:http://127.0.0.1:8000/authen_module/sortbyname_loan?loan_name=


@api_view(['GET'])
def sortbyname_loan(request):
    loan_name = request.GET.get('loan_name', False)
    if not loan_name:
        return Response({"status": False, "message": "Loan name  is Required"})
    entry_exist = Loan.objects.filter(loan_name=loan_name, is_active=True)
    if not entry_exist:
        return Response({"status": False, "message": "This loan name  not Exist"})
    serial = LoanSerializer(entry_exist, many=True)
    return Response({"status": True, "message": "Loan datas under this loan name ", "data": serial.data})

# Input url:http://127.0.0.1:8000/authen_module/delete-loan?loan_name=12345


@api_view(['GET'])
def delete_loan(request):
    loan_name = request.GET.get('loan_name', False)
    if not loan_name:
        return Response({"status": False, "message": "Loan name is Required"})
    entry_exist = Loan.objects.filter(loan_name=loan_name, is_active=True)
    if not entry_exist:
        return Response({"status": False, "message": "This loan  not Exist"})
    loan_entry = Loan.objects.get(loan_name=loan_name, is_active=True)
    loan_entry['is_active'] = False
    loan_entry.save()
    serial = LoanSerializer(entry_exist, many=True)
    return Response({"status": True, "message": "This loan  Deleted Successfully", "data": serial.data})


# InputUrl:http://127.0.0.1:8000/authen_module/create-user
# InputJson:
# {"user_name":"tester", "position":"tester position", "user_id":"Test_id" , "password":"123456","created_by":"tester", "updated_by":"tester"}
@api_view(['POST'])
def create_user(request):
    validation_result = UserValidation().validation_for_user(request=request)
    if validation_result == True:
        entry_exist = User.objects.filter(
            user_id=request.data['user_id'], is_active=True)
        if entry_exist:
            return ({"status": False, "message": "User's Id  is  already exists"})
        entry = User.objects.create(user_name=request.data['user_name'], position=request.data['position'],
                                    user_id=request.data['user_id'], password=request.data['password'],
                                    created_by=request.data['created_by'], updated_by=request.data['updated_by'])
        return Response({"status": True, "message": "User is  Created Successfully"})
    else:
        return Response(validation_result)

# Input url:http://127.0.0.1:8000/authen_module/view-user


@api_view(['GET'])
def view_user(request):
    entry_exist = User.objects.filter(is_active=True)
    if not entry_exist:
        return Response({"status": False, "message": "User's not Exist"})
    serial = UserSerializer(entry_exist, many=True)
    return Response({"status": True, "message": "User's  Data list", "data": serial.data})

# Input url:http://127.0.0.1:8000/authen_module/sortbyname_user?user_name=


@api_view(['GET'])
def sortbyname_user(request):
    user_name = request.GET.get('user_name', False)
    if not user_name:
        return Response({"status": False, "message": "Userr name  is Required"})
    entry_exist = User.objects.filter(user_name=user_name, is_active=True)
    if not entry_exist:
        return Response({"status": False, "message": "This user  name  not Exist"})
    serial = UserSerializer(entry_exist, many=True)
    return Response({"status": True, "message": "User  datas under this  name ", "data": serial.data})

# Input url:http://127.0.0.1:8000/authen_module/delete-user?user_id=Test_id


@api_view(['GET'])
def delete_user(request):
    user_id = request.GET.get('user_id', False)
    if not user_id:
        return Response({"status": False, "message": "User Id is Required"})
    entry_exist = User.objects.filter(user_id=user_id, is_active=True)
    if not entry_exist:
        return Response({"status": False, "message": "User Id   not Exist"})
    user_entry = User.objects.get(user_id=user_id, is_active=True)
    user_entry['is_active'] = False
    user_entry.save()
    serial = UserSerializer(entry_exist, many=True)
    return Response({"status": True, "message": "User is  Deleted Successfully", "data": serial.data})

# login
# Input url:http://127.0.0.1:8000/authen_module/login-user
# InputJson:
# {"user_id":"Test_id" , "password":"123456"}


@api_view(['POST'])
def login_user(request):
    entry_exist = User.objects.filter(
        user_id=request.data['user_id'], password=request.data['password'], is_active=True)
    entry = User.objects.filter(
        user_id=request.data['user_id'], password=request.data['password'])
    serial = UserSerializer(entry_exist, many=True)
    if entry_exist:
        return Response({"status": True, "message": "User logged in succesfully", "data": serial.data})
    if not entry_exist:
        return Response({"status": False, "message": "User's not Exist"})
