from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
from models import User, Post

app = Flask(__name__)
app.config['SECRET_KEY'] = 'f8a70a7047b74e561d4b60f38763557d'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

# with app.app_context():
#     db.create_all()


posts = [
    {
        'author': 'musawir',
        'title': 'Blog',
        'content': "lorem ipsum s simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
        'date_posted': 'june 10'

    },
    {
        'author': 'abdul',
        'title': 'Blog smple',
        'content': 'lorem ipsum',
        'date_posted': 'june 15'

    }


]


@ app.route("/")
@ app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@ app.route("/about")
def about():
    return render_template('about.html', title='About')


@ app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@ app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in   :)', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unseccussful. Please check username and password', 'danger')

    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
