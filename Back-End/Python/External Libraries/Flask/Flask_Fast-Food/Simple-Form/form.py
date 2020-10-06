from flask import Flask, request, render_template, url_for
from wtforms import SubmitField, Form, FloatField, validators


app = Flask(__name__)


def mul(A,B):
    return  A*B
def add(A,B):
    return  A+B

# Form
class InputForm(Form):
    A = FloatField(
        label='A', default=0,
        validators=[validators.InputRequired()])
    B = FloatField(
        label='B', default=0,
        validators=[validators.InputRequired()])  
       
       
@app.route('/comp', methods=['GET', 'POST'])
def comp():
   
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        if request.form['btn'] == 'Add':
            result = add(form.A.data, form.B.data)
       
        elif request.form['btn'] == 'Multiply':
            result = mul(form.A.data, form.B.data)
   
    else:
        result = None
    return render_template('view.html', form=form, result=result)

@app.route('/')
def index():
    return '<h1> Hello World </h1>'



if __name__ == '__main__':
    app.run(debug=True)