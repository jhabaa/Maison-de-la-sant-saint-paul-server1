# MSSP first server 

from flask import Flask
import mysql.connector
from dotenv import load_dotenv
import os
import json


#load environnement variable
_l = load_dotenv()

#Init Flask 
app = Flask(__name__)

#MYSQL config
cnx = mysql.connector.connect(host=os.getenv("MYSQL_HOST"), port=os.getenv("MYSQL_PORT"), user= os.getenv("MYSQL_USER"), password=os.getenv("MYSQL_PWD"))

# Now we'll just create a cursor for each request
@app.route('/')
def empty():
    return "Invalid Request"

@app.route('/getservices')
def get_services():
    # Create a cursor 
    cursor = cnx.cursor()

    #get services
    cursor.execute("SELECT * FROM mssp.services;")
    # result 
    r = cursor.fetchall()
    return json.dumps(r)


