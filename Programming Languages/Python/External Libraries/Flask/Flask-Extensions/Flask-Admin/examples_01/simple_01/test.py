from flask import Flask
import flask_admin as admin


app = Flask(__name__)

my_admin = admin.Admin(app)

print(my_admin._set_admin_index_view)