from flask import Flask
from views import my_url

app = Flask(__name__)

app.register_blueprint(my_url)

app.run(debug=True)