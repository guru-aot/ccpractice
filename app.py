

from flask import Flask,g
from flask_oidc import OpenIDConnect


app = Flask(__name__)

app.config.update({
    'SECRET_KEY': 'foiclientapp',
    'TESTING': True,
    'DEBUG': True,
    'OIDC_CLIENT_SECRETS': 'client_secrets.json',
    'OIDC_ID_TOKEN_COOKIE_SECURE': False,
    'OIDC_REQUIRE_VERIFIED_EMAIL': False,
    'OIDC_USER_INFO_ENABLED': True,
    'OIDC_SCOPES': ['openid', 'email', 'profile'],
    'OIDC_INTROSPECTION_AUTH_METHOD': 'client_secret_post',
    'OIDC_TOKEN_TYPE_HINT': 'access_token'
})

oidc = OpenIDConnect(app)

@app.route('/')
def home():
    if oidc.user_loggedin:
        return("Hello,%s"%oidc.user_getfield('email'))
    else:
        return 'Welcome, please <a href="/dashboard">Login</a>'

@app.route('/dashboard')
@oidc.require_login
def dashboard():
    userinfo = oidc.user_getinfo(['email','preferred_username','sub'])

    username = userinfo.get('preferred_username')
    email  = userinfo.get('email')
    userid = userinfo.get('sub')

    return("This is your dashboard, %s and your email is %s! and UserId is %s"%(username,email,userid))


if __name__ == '__main__':
    app.run('0.0.0.0', 5000, debug=True)