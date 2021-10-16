from datetime import date, datetime
#from typing_extensions import Required
#from typing_extensions import Required
# Create your models here.
from mongoengine import Document, fields
from django.db import models
#from cloudinary.models import CloudinaryField


class Customer(Document):
    customer_id = fields.StringField(required=True)
    name = fields.StringField(required=True)
    dob = fields.StringField(required=True)
    age = fields.StringField(required=True)
    relation = fields.StringField(required=True)
    nominee = fields.StringField(required=True)
    current_address = fields.StringField(required=True)
    permanent_address = fields.StringField(required=True)
    landmark = fields.StringField(required=True)
    pincode = fields.StringField(required=True)
    city = fields.StringField(required=True)
    id_proof_type = fields.StringField(required=True)
    id_proof_no = fields.StringField(required=True)
    mobile_no = fields.StringField(required=True)
    alternative_no = fields.StringField(required=True)
    customer_photo = fields.StringField(required=True)
    id_proof_photo = fields.StringField(required=True)
    is_active = fields.BooleanField(default=True)
    created_at = fields.DateTimeField(default=datetime.now)
    updated_at = fields.DateTimeField(default=datetime.now)
    created_by = fields.StringField()
    updated_by = fields.StringField()


class Loan(Document):
    loan_name = fields.StringField(required=True)
    is_active = fields.BooleanField(default=True)
    created_at = fields.DateTimeField(default=datetime.now)
    updated_at = fields.DateTimeField(default=datetime.now)
    created_by = fields.StringField()
    updated_by = fields.StringField()


class User(Document):
    user_name = fields.StringField(required=True)
    position = fields.StringField(required=True)
    user_id = fields.StringField(required=True)
    password = fields.StringField(required=True)
    is_active = fields.BooleanField(default=True)
    created_at = fields.DateTimeField(default=datetime.now)
    updated_at = fields.DateTimeField(default=datetime.now)
    created_by = fields.StringField()
    updated_by = fields.StringField()
