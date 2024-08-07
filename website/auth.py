from flask import Blueprint,render_template,request,flash

auth = Blueprint('auth',__name__)

@auth.route("/login", methods=['GET','POST'])
def login():
    return render_template("login.html",boolean=False)

@auth.route('/logout')
def logout():
    return "<p>logout</p>"

@auth.route('/signup',methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstname = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash("Email must be greater than 3 characters",category='error')
        elif len(firstname) < 2:
            flash("FirstName must be greater than 1 character",category='error')
        elif password1 != password2:
            flash("password should be same as confirm password",category='error')
        elif len(password1) < 5:
            flash("The password is too short must be greater than 5",category='error')
        else:
            flash("Account Created",category='Success')


    return render_template("signup.html")