from flask import *
from flask_mail import *

app = Flask(__name__)

# Flask mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'harsh.rathi99999@gmail.com'
app.config['MAIL_PASSWORD'] = 'khatushyam'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

# instantiate the Mail class
mail = Mail(app)


# configure the Message class object and send the mail from a URL
@app.route('/')
def index():
    msg = Message('subject', sender='admin@gmail.com', recipients=['harsh.rathi20001@gmail.com'])
    msg.body = 'hi, this is the mail sent by using the flask web application'
    return "Mail Sent, Please check the mail id"


if __name__ == '__main__':
    app.run(debug=True)