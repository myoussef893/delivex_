from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, DateField,EmailField,SelectField
from wtforms.validators import DataRequired


egyptian_cities = [
    "Cairo",
    "Alexandria",
    "Giza",
    "Shubra El Kheima",
    "Port Said",
    "Suez",
    "Luxor",
    "El-Mahalla El-Kubra",
    "Tanta",
    "Asyut",
    "Ismailia",
    "Fayyum",
    "Zagazig",
    "Aswan",
    "Damietta",
    "Damanhur",
    "Minya",
    "Beni Suef",
    "Qena",
    "Sohag",
    "6th of October City",
    "Shibin El Kom",
    "Banha",
    "Kafr el-Sheikh",
    "Arish",
    "Mallawi",
    "10th of Ramadan City",
    "Bilbeis",
    "Marsa Matruh",
    "Edfu",
    "Mit Ghamr",
    "Al-Hawamidiyya",
    "Desouk",
    "Qalyub",
    "Abu Kabir",
    "Kafr el-Dawwar",
    "Girga",
    "Akhmim",
    "El Matareya",
    "Hurghada",
    "Rosetta",
    "Juhaynah",
    "Baltim",
    "Al Obour City",
    "Natrun Valley",
    "Fayed",
    "Al Jamaliyah",
    "El-Mahmoudeya",
    "Abnub",
    "Tahta",
    "Samalut",
    "Bush",
    "Hawsh Isa",
    "Munuf",
    "Ashmun",
    "Manfalut",
    "Isna",
    "Al Qusiyah",
    "Al Jammaliyah",
    "Dayrut",
    "Al Kharijah",
    "Toukh",
    "Al Manzalah",
    "Awsim",
    "Al Fashn",
    "Fuwwah",
    "Faqus",
    "Al Khankah",
    "Mersa Matruh",
    "Al Qurayn",
    "Abu Qurqas",
    "Al Manshah",
    "Kousa",
    "Kawm Umbu",
    "Faraskur",
    "Bani Mazar",
    "Minyat an Nasr",
    "Shibin al Qanatir",
    "Al Qanatir al Khayriyah",
    "Basyun",
    "Samannud",
    "Shirbin",
    "Dishna",
    "Farshut",
    "Diyarb Najm",
    "At Tall al Kabir",
    "Tala",
    "Ibshaway",
    "Al Balyana",
    "Ash Shuhada'",
    "Sidi Salim",
    "Juhaynah",
    "Tamiyah",
    "Mashtul as Suq",
    "Al Hamul",
    "Ain Sukhna",
    "Itsa",
    "Matay",
    "Al Badari",
    "Hihya",
    "Al Qanayat",
    "Quwaysina",
    "Madinat Sittah Uktubar",
    "Abu al Matamir",
    "Naja' Hammadi",
    "Dayr Mawas",
    "Ad Dilinjat",
    "Az Zarqa",
    "As Saff",
    "`Izbat al Burj",
    "Al Wasitah",
    "Sumusta as Sultani",
    "Kawm Hamadah",
    "Al Bajur",
    "Kafr Saqr",
    "Al `Ayyat",
    "Aja",
    "Al Ibrahimiyah",
    "Safaga",
    "Ras Gharib",
    "Al Qusayr",
    "Qutur",
    "Al Bawiti",
    "El Gouna",
    "El-Tor",
    "Sharm el-Sheikh",
    "Siwa Oasis",
    "Taba",
    "Dahab",
    "Marsa Alam",
    "New Administrative Capital"
]
## Login 
class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


## Signup 
class SignupForm(FlaskForm): 
    full_name = StringField('Full Name', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])
    phone = IntegerField('Phone',validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Signup')


## New Package 
class NewPackageForm(FlaskForm): 
    pickup_address = StringField('Pickup Address', validators=[DataRequired()])
    pickup_city = SelectField('Pickup City', choices=egyptian_cities, validators=[DataRequired()])
    
    delivery_address = StringField('Delivery Address', validators=[DataRequired()])
    delivery_city = SelectField('Delivery City',choices=egyptian_cities, validators=[DataRequired()])

    sender_name = StringField('Sender Name', validators=[DataRequired()])
    receiver_name = StringField('Receiver Name', validators=[DataRequired()])
    
    sender_phone = IntegerField('Sender Phone', validators=[DataRequired()])
    receiver_phone = IntegerField('Receiver Phone', validators=[DataRequired()])
    
    special_notes = StringField('Notes/Comment')
    
    courier_type = SelectField('Select Courier Type', choices=['Foot','Car','Truck','Motor Cycle'], validators=[DataRequired()])

    package_weight = IntegerField('Package Weight', validators=[DataRequired()])
    
    submit = SubmitField('Submit')
    
    
    

## Inquiry 


