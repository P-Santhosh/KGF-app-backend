from authen_module.models import Customer
from authen_module.serializers import CustomerSerializer
from authen_module.models import Loan
from authen_module.serializers import LoanSerializer
from authen_module.models import User
from authen_module.serializers import UserSerializer

class CustomerValidation:
    @staticmethod
    def validation_for_customer(request):
        # If u want u can add min,max length and special character validations here..
        name = request.data.get('name', False)
        if not name:
            return ({"status": False, "message": "Customer's Name is Required"})
        dob = request.data.get('dob', False)
        if not dob:
            return ({"status": False, "message": "Customer's Date of birth  is Required"})
        age = request.data.get('age', False)
        if not age:
            return ({"status": False, "message": "Customer's Age  is Required"})
        relation = request.data.get('relation', False)
        if not relation:
            return ({"status": False, "message": "Customer's Relation  is Required"})
        nominee = request.data.get('nominee', False)
        if not nominee:
            return ({"status": False, "message": "Customer Nominee is Required"})
        current_address = request.data.get('current_address', False)
        if not current_address:
            return ({"status": False, "message": "Customer's Current address is Required"})
        permanent_address = request.data.get('permanent_address', False)
        if not permanent_address:
            return ({"status": False, "message": "Customer's Permanent address is Required"})
        landmark = request.data.get('landmark', False)
        if not landmark:
            return ({"status": False, "message": " Customer's  Landmark  is Required"})
        pincode = request.data.get('pincode', False)
        if not pincode:
            return ({"status": False, "message": "Customer's Pincode  is Required"})
        city = request.data.get('city', False)
        if not city:
            return ({"status": False, "message": " Customer's  City is Required"})
        id_proof_type = request.data.get('id_proof_type', False)
        if not id_proof_type:
            return ({"status": False, "message": "Customer's type of Id proof is Required"})
        id_proof_no = request.data.get('id_proof_no', False)
        if not id_proof_no:
            return ({"status": False, "message": "Customer's Id proof number  is Required"})
        mobile_no = request.data.get('mobile_no', False)
        if not mobile_no:
            return ({"status": False, "message": "Customer's Mobile number is Required"})
        alternative_no = request.data.get('alternative_no', False)
        if not alternative_no:
            return ({"status": False, "message": "Customer's Alternative number  is Required"})
        customer_photo = request.data.get('customer_photo', False)
        if not customer_photo:
            return ({"status": False, "message": "Customer's  photo  is Required"})
        id_proof_photo = request.data.get('id_proof_photo', False)
        if not id_proof_photo:
            return ({"status": False, "message": "Customer's  Id proof photo  is Required"})
        created_by = request.data.get('created_by', False)
        if not created_by:
            return ({"status": False, "message": "Created By is Required"})
        updated_by = request.data.get('updated_by', False)
        if not updated_by:
            return ({"status": False, "message": "Updated By is Required"})
        if name and dob and age and relation and nominee and current_address and permanent_address and landmark and pincode and city and id_proof_type and id_proof_no and mobile_no and alternative_no and customer_photo  and id_proof_photo and created_by and updated_by:
            return True

class LoanValidation:
    @staticmethod
    def validation_for_loan(request):
        # If u want u can add min,max length and special character validations here..
        loan_name = request.data.get('loan_name', False)
        if not loan_name:
            return ({"status": False, "message": "Customer's Loan Name is Required"})
        created_by = request.data.get('created_by', False)
        if not created_by:
            return ({"status": False, "message": "Created By is Required"})
        updated_by = request.data.get('updated_by', False)
        if not updated_by:
            return ({"status": False, "message": "Updated By is Required"})
        if loan_name  and created_by and updated_by:
            return True

class UserValidation:
    @staticmethod
    def validation_for_user(request):
        # If u want u can add min,max length and special character validations here..
        user_name = request.data.get('user_name', False)
        if not user_name:
            return ({"status": False, "message": "User's Name is Required"})
        position = request.data.get('position', False)
        if not position:
            return ({"status": False, "message": "User's position is Required"})
        user_id = request.data.get('user_id', False)
        if not user_id:
            return ({"status":False,"message":"User's Id  is Required"})
        password = request.data.get('password', False)
        if not password:
            return ({"status":False,"message":"Password is Required"})
        created_by = request.data.get('created_by', False)
        if not created_by:
            return ({"status": False, "message": "Created By is Required"})
        updated_by = request.data.get('updated_by', False)
        if not updated_by:
            return ({"status": False, "message": "Updated By is Required"})
        if user_name and position and user_id and password and   created_by and updated_by:
            return True
