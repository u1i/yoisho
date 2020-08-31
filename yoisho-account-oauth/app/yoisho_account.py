from bottle import Bottle, request, response, view, redirect
from datetime import datetime
import json, time, base64
import random, string

app = Bottle()

# the client details the app must provide
yoisho_client_id = "7b6fc8ed5127b0b2f076d"
yoisho_client_secret = "724e6890757b0ae624684b70e111b705fe6b050c"

# for how many seconds is the access_token valid?
token_expiration_seconds = 30

# our client database with account names and account balance
accounts={"dave":"10,187.91", "jane":"981,719.23"}

@app.get('/home')
@view('index')
def home():
    """Renders the home page."""
    return dict()

@app.get('/authorize')
@view('login')
def ylogin():
    """Renders the login page."""

    try:
        login_message = request.query['login_message']
    except:
        login_message = "Please login using your banking credentials to authorize the app to access your account."

    try:
        redirect = request.query['redirect_uri']
    except:
        response.content_type = "application/json"
        response.status = 400
        return '{"error":"invalid request, missing redirect_uri"}'

    try:
        client_id = request.query['client_id']
    except:
        response.content_type = "application/json"
        response.status = 400
        return '{"error":"invalid request, client_id mising"}'

    # check if client ID is correct
    if client_id != yoisho_client_id:
        response.content_type = "application/json"
        response.status = 400
        return '{"error":"invalid request, client_id is incorrect"}'

    # generate dummy token
    len=128
    dummy_token=""
    for _ in range(len):
	       dummy_token += random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)

    return dict(redirect_uri=redirect, token=dummy_token, login_message=login_message, client_id=client_id)

@app.get('/loggedin')
def ylogin():
    user = request.query['uname']
    redirect_uri = request.query['redirect']
    client_id = request.query['client_id']

    code1 = str(random.randint(112111,999999))

    # Dave's codes start with 4, Jane's with 6

    if user == "dave":
            code = "4" + code1
    else:
            code = "6" + code1

    if user in accounts.keys():
        redirect(redirect_uri + "?code=" + str(code))
    else:

        redirect("/authorize?client_id="+client_id+"&login_message=invalid%20login&redirect_uri="+redirect_uri)

@app.get('/access_token')
def getaccesstoken():

    try:
        client_id = request.query['client_id']
        client_secret = request.query['client_secret']
        code = request.query['code']
    except:
        response.content_type = "application/json"
        response.status = 400
        return '{"error":"invalid request, code, client_id or client_secret mising"}'

    # check if client ID is correct
    if client_id != yoisho_client_id:
        response.content_type = "application/json"
        response.status = 400
        return '{"error":"invalid request, client_id is incorrect"}'

    # check if client secret is correct
    if client_secret != yoisho_client_secret:
        response.content_type = "application/json"
        response.status = 400
        return '{"error":"invalid request, client_secret is incorrect"}'

    len=39
    dummy_token=""
    for _ in range(len):
    	dummy_token += random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)

    catch = 0

    # base64 encode current utime to add to token

    t = base64.urlsafe_b64encode(str(int(time.time())))

    # Dave's codes/tokens start with 4/e, Jane's with 6/f
    if code[0] == "4":
        access_token = "e" + dummy_token + "." + t
        catch = 1

    if code[0] == "6":
        access_token = "f" + dummy_token + "." + t
        catch = 1

    if catch == 1:
        return dict(access_token = access_token, token_type="bearer", scope="read")
    else:
        response.content_type = "application/json"
        response.status = 400
        return '{"error":"invalid access code"}'

@app.get('/balance')
def getbalance():

    try:
        #access_token = request.query['access_token']
        bearer = request.environ.get('HTTP_AUTHORIZATION','')
        access_token=bearer[7:]
    except:
        response.content_type = "application/json"
        response.status = 400
        return '{"error":"invalid request, access_token mising"}'

    # identify which user we have in the token
    catch = 0
    if access_token[0] == "e":
        user = "dave"
        catch = 1

    if access_token[0] == "f":
        user = "jane"
        catch = 1

    if catch == 0:
        response.content_type = "application/json"
        response.status = 400
        return '{"error":"invalid access_token "}'

    token_time = int(base64.urlsafe_b64decode(access_token[41:]))
    current_time=int(time.time())

    if current_time - token_time > token_expiration_seconds:
        response.content_type = "application/json"
        response.status = 400
        return '{"error":"access_token has expired"}'

    return dict(account_owner=user, account_balance=accounts[user])

@app.get('/info')
def getaccinfo():

    try:
        #access_token = request.query['access_token']
        bearer = request.environ.get('HTTP_AUTHORIZATION','')
        access_token=bearer[7:]
    except:
        response.content_type = "application/json"
        response.status = 400
        return '{"error":"invalid request, access_token mising"}'

    # identify which user we have in the token
    catch = 0
    if access_token[0] == "e":
        user = "dave"
        catch = 1
        return_data = {"account_owner": "dave", "fullname": "Dave Thompson", \
        "email": "daveth271@gmail.com", "address": "491-1295, Nishimiyanosawa 6-jo, Teine-ku Sapporo-shi, Hokkaido", \
        "phone": "+8183-977-7817"}

    if access_token[0] == "f":
        user = "jane"
        catch = 1
        user = "jane"
        return_data = {"account_owner": "dave", "fullname": "Jane Hamamoto", \
        "email": "kumori18@yahoo.jp", "address": "376-1062, Machi, Ogawara-machi Shibata-gun, Miyagi", \
        "phone": "+8128-945-7273"}

    if catch == 0:
        response.content_type = "application/json"
        response.status = 400
        return '{"error":"invalid access_token "}'

    token_time = int(base64.urlsafe_b64decode(access_token[41:]))
    current_time=int(time.time())

    if current_time - token_time > token_expiration_seconds:
        response.content_type = "application/json"
        response.status = 400
        return '{"error":"access_token has expired"}'

    return dict(return_data)
