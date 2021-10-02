from flask import Flask, request, redirect, render_template
import os
import random
import string
import sqlite3
import html #for escape
import requests #for hCaptcha
import json #to help with hCaptcha data

app = Flask(__name__)
app.config["SECRET_KEY"] = str(os.urandom(24));
SERVERN = "localhost" # should change this to find hostname automatically
# get hCaptcha site keys from environment variables
hcaptcha_secret = os.environ.get('HCAPTCHA_SECRET')
hcaptcha_site_key = os.environ.get('hcaptcha_sitekey')

#initialize database
conn = sqlite3.connect("urls.db")
c = conn.cursor()
c.execute("""
        CREATE TABLE IF NOT EXISTS urls
        (id INTEGER PRIMARY KEY, url TEXT);
""")
conn.commit()
conn.close()

#define routes
@app.route('/')
def index():
    return render_template("index.html", HCAPTCHA_SITEKEY = hcaptcha_site_key)

@app.route('/shorten', methods = ["POST"])
def shorten():
    #hcaptcha request
    hcaptcha_token = request.form['h-captcha-response']
    api_endpoint = 'https://hcaptcha.com/siteverify'
    hc_data = {'response':hcaptcha_token,'secret':hcaptcha_secret}
    r = requests.post(url = api_endpoint, data = hc_data)
    answer = r.text
    result = json.loads(r.text)
    if result['success'] != bool(1):
        return render_template("index.html", notificationFail = "Please complete the captcha correctly")
    else:
        url = request.form['url']
        conn = sqlite3.connect("urls.db")
        c = conn.cursor()
        c.execute("INSERT INTO urls VALUES (NULL, ?);", (url,))
        conn.commit()
        id = c.lastrowid
        shortlink = f'http://{SERVERN}/{id}'
        conn.close()
        return render_template("index.html", HCAPTCHA_SITEKEY = hcaptcha_site_key, notification = f'Your shortened URL:\n{shortlink}')

@app.route('/<id>')
def go(id):
    conn = sqlite3.connect("urls.db")
    c = conn.cursor()
    c.execute("SELECT * FROM urls WHERE id=?;", (id,))
    url = c.fetchone()
    conn.close()
    try:
        destination = url[1]
    except:
        return render_template("index.html", notificationFail = "Invalid ID")
    return redirect(destination)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug = False, host = "0.0.0.0")
