# OAuth client for Yosiho Account - Python implementation

You can run this using a [docker container](https://github.com/u1i/yoisho/tree/master/yoisho-account-oauth-client/docker), or alternatively. natively on your local box:

## 1 - Run Yoisho Account Balance OAuth Service

We're using a different port (8091) here as 8080 is often taken by other services.

`docker run --rm -d -p 8091:8080 u1ih/yoisho-account:latest`

## 2 - Run the app

Create a virtualenv and do a `pip install bottle` 

Run the app with `python yoisho-client.py`

## 3 - Open Client App

Open `http://localhost:8050/client` in your browser

![](https://raw.githubusercontent.com/u1i/yoisho/master/resources/yc-1.png)

## 4 - Login into Bank Account

A click on should bring you to the sign-in dialogue. Valid login names are 'dave' and 'jane'. Any passwords will be accepted.

![](https://raw.githubusercontent.com/u1i/yoisho/master/resources/yc-2.png)

![](https://raw.githubusercontent.com/u1i/yoisho/master/resources/yc-3.png)


## 5 - Magic happens

The OAuth flow will happen in the background - the app will receive the code, use it to request an access token and trigger an API call using this token.

![](https://raw.githubusercontent.com/u1i/yoisho/master/resources/yc-4.png)