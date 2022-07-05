from models import User

@app.route("/layout")
def layout():
    return render_template("layout.html")

@app.route("/")
@app.route("/dashboard")
def dashboard():
    return render_template("pages/dashboard.html", title="Dashboard")

@app.route("/register", methods=['GET','POST'])
def register():
    form = registration_form()
    if form.validate_on_submit():
        flash(f'Account created for {form.first_name.data} {form.last_name.data}', 'success')
        return redirect(url_for('dashboard'))
    return render_template("pages/register.html", title = 'Register', form=form)

@app.route("/login", methods=['GET','POST'])
def login():
    form = login_form()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Login unsuccessful, please check username and password','danger')
    return render_template("pages/login.html", title = 'Login', form=form)