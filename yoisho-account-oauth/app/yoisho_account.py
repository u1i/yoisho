from bottle import Bottle, request, response, view, redirect
from datetime import datetime
import json
import random, string

app = Bottle()

@app.get('/home')
@view('index')
def home():
    """Renders the home page."""
    return dict()

@app.get('/authorize')
@view('login')
def ylogin():
    """Renders the login page."""
    len=128
    dummy_token=""

    try:
        login_message = request.query['login_message']
    except:
        login_message = "Please login using your banking credentials"

    for _ in range(len):
	       dummy_token += random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)

    redirect = request.query['redirect_uri']
    return dict(redirect_uri=redirect, token=dummy_token, login_message=login_message)

@app.get('/loggedin')
def ylogin():
    user = request.query['uname']
    redirect_uri = request.query['redirect']
    accounts={"dave":"10,187.91", "jane":"981,719.23"}

    code1 = str(random.randint(11111,99999))

    # Dave's codes start with 4, Jane's with 6

    if user == "dave":
            code = "4" + code1
    else:
            code = "6" + code1

    if user in accounts.keys():
        redirect(redirect_uri + "?code=" + str(code))
    else:

        redirect("/authorize?login_message=invalid%20login&redirect_uri="+redirect_uri)


@app.get('/balance')
def getbalance():
    return 0
