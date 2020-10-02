from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, HiddenField, SelectField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed
from flask_uploads import IMAGES


class AddProduct(FlaskForm):
    
    name = StringField('Name')
    price = IntegerField('Price')
    stock = IntegerField('Stock')
    description = TextAreaField('Description')
    image = FileField('Image', validators=[FileAllowed(IMAGES, 'Only images are accepted!')])


class AddToCart(FlaskForm):
    
    id =  HiddenField('ID')
    quantity = IntegerField('Quantity')
    

class Checkout(FlaskForm):
    
    first_name = StringField('First Name', validators=[DataRequired('Enter a name')])
    last_name = StringField('Last Name', validators=[DataRequired('Enter a surname')])
    phone_number = IntegerField('Phone Number')
    email = StringField('Email', validators=[DataRequired('Please enter your email address.')])
    address = StringField('Address', validators=[DataRequired('Enter a valid address')])
    city = StringField('City', validators=[DataRequired('Enter a city!')])

    state = SelectField('State', choices=[('IT', 'Italy'), ('ES', 'Spain'), ('FR', 'France'), ('UK', 'UnitedKindom'), ('GR', 'Germany')], validators=[DataRequired('Select a state')])
    
    payment_type = SelectField('Payment Type', choices=[('CK', 'Check'), ('WT', 'Wire Transfer')], validators=[DataRequired('Select a form of payment')])


class Rejct_Or_Fetch(FlaskForm):
    
    reject = SubmitField('Reject Order')
    fetch = SubmitField('Fetch Order')


class Add_Item_Admin(FlaskForm):

    name = StringField('Name')
    price = IntegerField('Price')
    stock = IntegerField('Stock')
    description = TextAreaField('Description')
    submit =  SubmitField('Add Product')