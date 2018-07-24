import json
import requests
from bottle import route, run, request

# Yoisho client credentials
client_id="7b6fc8ed5127b0b2f076d"
client_secret="724e6890757b0ae624684b70e111b705fe6b050c"

# Client app run details
port=8050
app_url="http://localhost:8050"

# The Yoisho OAuth server
oauth_url="http://localhost:8091"

@route('/client')
def index():
    outp=""
    try:
        code=request.query['code']
    except:
        code=""

    outp=outp + "<b>My Money Managing App (Yoisho Client)</b><br>"

    if code == "":
        outp=outp + "Please login <a href='" + oauth_url + "/authorize?redirect_uri=http://localhost:8050/client&client_id="+client_id + "'>here</a><br>"
    else:
        url = oauth_url + '/access_token?code='+ code +'&client_id=' + client_id + '&client_secret=' + client_secret
        headers = {'Content-Type': "application/json; charset=UTF-8", 'Accept': "application/json"}
        res = requests.get(url, headers=headers)

        accesstoken_response=res.text

        j=json.loads(res.text)

        access=j["access_token"]

#        headers = {'Content-Type': "application/json; charset=UTF-8", 'Accept': "application/json"}
#        data = {"client_id": client_id, "client_secret":client_secret, "code": code}
#        res = requests.post(url, json=data, headers=headers)

        url = oauth_url + '/balance'
        headers = {'Content-Type': "application/json; charset=UTF-8", 'Accept': "application/json", "Authorization": "Bearer " + access}
        res = requests.get(url, headers=headers)

        j=json.loads(res.text)

        user=j["account_owner"]
        balance=j["account_balance"]

        outp=outp + "Hello " + str(user) + ", your current account balance with Yoisho is: " + balance
    return outp


run(host='0.0.0.0', port=port)
