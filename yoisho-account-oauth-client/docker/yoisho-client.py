import os, json
import requests
from bottle import route, run, request

# The Yoisho OAuth server
# oauth_url="http://localhost:8080"
# Example:
# export oauth_url="http://localhost:8091"

# Client app run details
# app_port=8080
# app_url="http://localhost:8080"

try:
    oauth_url=os.environ['oauth_url']
except:
    print("ERROR: please set the oauth_url environment variable!")
    exit(1)

try:
    oauth_url_serverside=os.environ['oauth_url_serverside']
except:
    print("ERROR: please set the oauth_url_serverside environment variable!")
    exit(1)

try:
    app_url=os.environ['app_url']
except:
    print("ERROR: please set the app_url environment variable!")
    exit(1)

# Yoisho client credentials
client_id="7b6fc8ed5127b0b2f076d"
client_secret="724e6890757b0ae624684b70e111b705fe6b050c"



@route('/client')
def index():
    outp=""
    try:
        code=request.query['code']
    except:
        code=""

    outp=outp + "<b>My Money Managing App (Yoisho Client)</b><br>"

    if code == "":
        outp=outp + "Please login <a href='" + oauth_url + "/authorize?redirect_uri=" + app_url + "/client&client_id="+client_id + "'>here</a><br>"
    else:
        url = oauth_url_serverside + '/access_token?code='+ code +'&client_id=' + client_id + '&client_secret=' + client_secret
        headers = {'Content-Type': "application/json; charset=UTF-8", 'Accept': "application/json"}
        res = requests.get(url, headers=headers)

        accesstoken_response=res.text

        j=json.loads(res.text)

        access=j["access_token"]

        url = oauth_url_serverside + '/balance'
        headers = {'Content-Type': "application/json; charset=UTF-8", 'Accept': "application/json", "Authorization": "Bearer " + access}
        res = requests.get(url, headers=headers)

        j=json.loads(res.text)

        user=j["account_owner"]
        balance=j["account_balance"]

        outp=outp + "Hello " + str(user) + ", your current account balance with Yoisho is: " + balance
    return outp

run(host='0.0.0.0', port=8080)
