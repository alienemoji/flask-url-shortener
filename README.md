# flask-url-shortener
A simple URL shortener made with Flask. URLs are stored in a SQLite database. Uses hCaptcha to reduce spam.

To use locally, first set environment variables in your OS for your hCaptcha keys:
-   HCAPTCHA_SECRET
-   HCAPTCHA_SITEKEY

In app.py, set SERVERN = yourdomain.com

Then run the app. It will create an SQLite database named links.db

To-do:

- Add some better validation+sanitization to input
- Create feature to add an advertisement to shortlinks before redirecting, a la adfly
- Edit templates to use semantic HTML tags wherever relevant
- Create some themes in the form of CSS stylesheets
- Login page + user accounts
- Add config file and ability to use either SQLite or MySQL
- Improve code style and readability
