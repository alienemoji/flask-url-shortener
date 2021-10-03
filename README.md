# flask-url-shortener
A simple URL shortener made with Flask. URLs are stored in a SQLite database. Uses hCaptcha to reduce spam.

To use locally, first set environment variables in your OS for your hCaptcha keys:
-   HCAPTCHA_SECRET
-   HCAPTCHA_SITEKEY

Then run the app.

Contributions are welcome no matter how small. I don't have any specific rules for contributing, just open an issue first. You are welcome to add any features you feel would be useful in a URL shortener. If you're a Hacktoberfest participant finding this repo, feel free to work on my to-do list below.

To-do:

- Add some better validation+sanitization to input
- Create feature to add an advertisement to shortlinks before redirecting, a la adfly
- Edit templates to use semantic HTML tags wherever relevant
- Create some themes in the form of CSS stylesheets
- Login page
- Add config file and ability to use either SQLite or MySQL
- Improve code style and readability
