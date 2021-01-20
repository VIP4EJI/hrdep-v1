from flask import Flask
from flaskext.mysql import MySQL

app = Flask(__name__)

app.config['MYSQL_DATABASE_HOST'] = 'VIP4EJI.mysql.pythonanywhere-services.com'
app.config['MYSQL_DATABASE_USER'] = 'VIP4EJI'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Qwerty_1988'
app.config['MYSQL_DATABASE_DB'] = 'VIP4EJI$hrdep_db'

mysql = MySQL()
mysql.init_app(app)