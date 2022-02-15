from flask import Flask


###### App setup
app = Flask(__name__)
app.config.from_pyfile('settings.py')
app.secret_key='555'

###### Pages
## Homepage
from pages.home.home import home
app.register_blueprint(home)

## About
from pages.about.about import about
app.register_blueprint(about)

## Menu
from pages.menu.menu import menu
app.register_blueprint(menu)

## Cart
from pages.cart.cart import cart
app.register_blueprint(cart)

## Contact Us
from pages.contact_us.contact_us import contact_us
app.register_blueprint(contact_us)

## Events
from pages.events.events import events
app.register_blueprint(events)


## Events Cart
from pages.payment.payment import payment
app.register_blueprint(payment)

## Signup
from pages.signup.signup import signup
app.register_blueprint(signup)

## Profile
from pages.profile.profile import profile
app.register_blueprint(profile)


###### Components
## Header
from components.header.header import header
app.register_blueprint(header)

## Footer
from components.footer.footer import footer
app.register_blueprint(footer)

## Header
from components.loader.loader import loader
app.register_blueprint(loader)

## Header
from components.popSign.popSign import popSign
app.register_blueprint(popSign)

if __name__ == '__main__':
    app.run(debug=True)
