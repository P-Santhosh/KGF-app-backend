# InputUrl:http://127.0.0.1:8000/authen_module/edit-employee
# InputJson:{"employee_name":"Sindhu", "email":"saveetha@gmail.com", "password":"saveetha" ,
#  "created_by":"sangeetha", "updated_by":"sangeetha", "id":"60bc7162a7d34e079cba9ee5"}
'''@api_view(['POST'])
def edit_employee(request):
    id = request.data.get('id', False)
    if not id:
        return Response({"status":False,"message":"Employee id is Required"})
    entry_exist=Employee.objects.filter(id=id,is_active=True)
    if not entry_exist:
        return Response({"status":False,"message":"Employee not Exist"})
    entry_exist=Employee.objects.filter(email=request.data['email'],is_active=True,id__nin=[id])
    if entry_exist:
        return Response({"status":False,"message":"Email already exists"})
    validation_result=EmployeeValidation().validation_for_employee(request=request)
    if validation_result==True:
        employee_entry=Employee.objects.get(id=id,is_active=True)
        employee_entry['employee_name'] =request.data['employee_name']
        employee_entry['age'] =request.data['age']
        employee_entry['dob']=request.data['dob']
        employee_entry['address']=request.data['address']
        employee_entry['contact_no']=request.data['contact_no']
        
        employee_entry['password']=request.data['password']
        employee_entry.save()
        return Response({"status":True,"message":"Employee Updated Successfully"})
    else:
        return Response(validation_result)
# Input url:http://127.0.0.1:8000/authen_module/get-employee?id=60bc7162a7d34e079cba9ee5
@api_view(['GET'])
def get_employee(request):
    id = request.GET.get('id',False)
    if not id:
        return Response({"status":False,"message":"Id is Required"})
    entry_exist=Employee.objects.filter(id=id,is_active=True)
    if not entry_exist:
        return Response({"status":False,"message":"Employee not Exist"})
    serial=EmployeeSerializer(entry_exist,many=True)
    return Response({"status":True,"message":"Employee Updated Successfully", "data":serial.data})
# Input url:http://127.0.0.1:8000/authen_module/delete-employee?employee_id=12345
@api_view(['GET'])
def delete_employee(request):
    employee_id = request.GET.get('employee_id',False)
    if not employee_id:
        return Response({"status":False,"message":"Employee id is Required"})
    entry_exist=Employee.objects.filter(employee_id=employee_id,is_active=True)
    if not entry_exist:
        return Response({"status":False,"message":"Employee not Exist"})
    employee_entry=Employee.objects.get(employee_id=employee_id,is_active=True)
    employee_entry['is_active']=False
    employee_entry.save()
    serial=EmployeeSerializer(entry_exist,many=True)
    return Response({"status":True,"message":"Employee Deleted Successfully","data":serial.data})
# Input url:http://127.0.0.1:8000/authen_module/view-employee
@api_view(['GET'])
def view_employee(request):
    entry_exist=Employee.objects.filter(is_active=True)
    if not entry_exist:
        return Response({"status":False,"message":"Employee not Exist"})
    serial=EmployeeSerializer(entry_exist,many=True)
    return Response({"status":True,"message":"Employee Datalist", "data":serial.data})

# Input url:http://127.0.0.1:8000/authen_module/viewage-employees?age=22
@api_view(['GET'])
def viewage_employees(request):
    age = request.GET.get('age',False)
    if not age:
        return Response({"status":False,"message":"Age is Required"})
    entry_exist=Employee.objects.filter(age=age,is_active=True)
    if not entry_exist:
        return Response({"status":False,"message":"Employee not Exist"})
    serial=EmployeeSerializer(entry_exist,many=True)
    return Response({"status":True,"message":"Employee Datalist", "data":serial.data})
    # Input url:http://127.0.0.1:8000/authen_module/viewbyemail-employee?email=
@api_view(['GET'])
def viewbyemail_employee(request):
    email = request.GET.get('email',False)
    if not email:
        return Response({"status":False,"message":"Email is Required"})
    
    entry_exist=Employee.objects.filter(email=email,is_active=True) 
    if not entry_exist:
        return Response({"status":False,"message":"Employee not Exist"})
    serial=EmployeeSerializer(entry_exist,many=True)
    return Response({"status":True,"message":"Employee Datalist", "data":serial.data})
@api_view(['POST'])
def login_employee(request):
    entry_exist=Employee.objects.filter(email=request.data['email'],password=request.data['password'], is_active=True)
    entry=Employee.objects.filter(
    email=request.data['email'],password=request.data['password'])
    serial=EmployeeSerializer(entry_exist,many=True)
    if entry_exist:
        return Response({"status":True,"message":"login in succesfully", "data":serial.data} )
    if not entry_exist:
        return Response({"status":False,"message":"Employee not Exist"})
    
email = request.GET.get('email',False)
    if not email:
        return Response({"status":False,"message":"email is Required"})
    password = request.GET.get('password',False)
    if not password:
        return Response({"status":False,"message":"password is Required"})
    entry_exist=((Employee.objects.filter(email=email  , is_active=True)) and (Employee.objects.filter(password=password , is_active=True)))
    if not entry_exist:
        return Response({"status":False,"message":"Employee not Exist"})
    serial=EmployeeSerializer(entry_exist,many=True)
    return Response({"status":True,"message":"Employee Updated Successfully", "data":serial.data})
# InputUrl:http://127.0.0.1:8000/authen_module/create-employee
# InputJson:
# {"employee_name":"Sindhu", "email":"saveetha@gmail.com", "password":"saveetha" ,
#  "created_by":"sangeetha", "updated_by":"sangeetha"}
@api_view(['POST'])
def create_employee(request):
    validation_result=EmployeeValidation().validation_for_employee(request=request)
    if validation_result==True:
        entry_exist=Employee.objects.filter(email=request.data['email'],is_active=True)
        if entry_exist:
            return ({"status":False,"message":"Email already exists"})
        #employee_id =  ''.join(random.choice(string.digits) for _ in range(5))
        entry=Employee.objects.create(name=request.data['name'],
        email=request.data['email'],desc=request.data['desc'],
        created_by=request.data['created_by'],updated_by=request.data['updated_by'],
        date=request.data['date'],org=request.data['org'],address=request.data['address'],
        contact_no=request.data['contact_no'],file=request.data['file'])
        return Response({"status":True,"message":"Employee Created Successfully"})
    else:
        return Response(validation_result)

# Input url:http://127.0.0.1:8000/authen_module/viewbyname-employees?name=
@api_view(['GET'])
def viewbyname_employees(request):
    
    name = request.GET.get('name',False)
    if not name:
        return Response({"status":False,"message":"Name is Required"})
    entry_exist=Employee.objects.filter(name=name,is_active=True)
    if not entry_exist:
        return Response({"status":False,"message":"Name not Exist"})
    serial=EmployeeSerializer(entry_exist,many=True)
    return Response({"status":True,"message":"Employee Datalist", "data":serial.data})
# Input url:http://127.0.0.1:8000/authen_module/view-employees   
@api_view(['GET'])
def view_employees(request):
    entry_exist=Employee.objects.filter(is_active=True)
    if not entry_exist:
        return Response({"status":False,"message":"Employee not Exist"})
    serial=EmployeeSerializer(entry_exist,many=True)
    return Response({"status":True,"message":"Employee Datalist", "data":serial.data})
    

@api_view(['POST'])
def imgupload_employee(request):
  
        entry=Employee.objects.upload(file=request.data['file'])
        return Response({"status":True,"message":"Employee Image upload Successfully"})'''
  


  #### urls
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