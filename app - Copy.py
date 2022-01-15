from config import CLIENT_SECRET, TOKEN, OAUTH_URL, REDIRECT_URI
from flask import Flask, render_template, redirect, url_for, request, flash, Response, session
from zenora import APIClient

app = Flask(__name__)
app.config["SECRET_KEY"] = "verysecret"
client = APIClient(TOKEN, client_secret=CLIENT_SECRET)


@app.route('/login')
def home():
    if 'token' in session:
        bearer_client = APIClient(session.get('token'), bearer=True)
        current_user = bearer_client.users.get_current_user()
        return render_template("login.html", current_user=current_user)
    return render_template('login.html', oauth_uri=OAUTH_URL)





@app.route("/oauth/callback")
def callback():
    code= request.args['code']
    access_token = client.oauth.get_access_token(code, REDIRECT_URI).access_token
    session['token'] = access_token
    return redirect("/") # redirecting to homepage

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(host = '192.168.1.124', port = 4444)
    app.run(debug=True)
