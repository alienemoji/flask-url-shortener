# flask-url-shortener
A simple URL shortener made with Flask. hCaptcha integrated to reduce spam. URLs are stored in a SQLite database.

To use locally, first set environment variables in your OS for your hCaptcha keys:
`export HCAPTCHA_SECRET=xxxxxxxxxxxxxxxxxxxxxxxxxxx`
`export HCAPTCHA_SITEKEY=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`

In app.py, set SERVERN = yourdomain.com

Then run the app and point your browser to localhost:5000. It will create an SQLite database named links.db

To-do:

- Add some better validation+sanitization to input
- Create feature to add an advertisement to shortlinks before redirecting, a la adfly
- Edit templates to use semantic HTML tags wherever relevant
- Create some themes in the form of CSS stylesheets
- Login + user accounts
