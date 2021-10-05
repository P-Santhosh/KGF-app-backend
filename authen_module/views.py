from datetime import date
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from authen_module.models import Customer
from authen_module.serializers import CustomerSerializer
import random
import string

from authen_module.library_module import CustomerValidation

# InputUrl:http://127.0.0.1:8000/authen_module/create-customer
# InputJson:
# {"name":"tester1", "dob":"1998-01-01", "age":"20" , "relation":"brother",  "nominee":"ncustomers nominee" , "current_address":"123,current address, karur " ,
#"permanent_address":"123, permanent address, karur " ,"landmark":"bypass " , "pincode":" 639117" , " city":"Karur" , "id_proof_type":"Adhar " ,
#"id_proof_no":" 987654321000000" , "mobile_no":"9876543210 " , "alternative_no":" 9123456789" , "customer_photo":"  img-customer_photo" ,
#"id_proof_photo":"img-id_proof_photo " , "created_by":"tester1", "updated_by":"tester1"}

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
