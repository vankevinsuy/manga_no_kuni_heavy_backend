from flask import Flask,request
import Tools
from usersFunctions import UserFunctions
app = Flask(__name__)

@app.route('/')
def hello():
    return "Flask app client"

@app.route('/GETALL')   # localhost:5000/GETALL?pseudo=snoozy&password=deadoralive&limit=10
def getall():
    pseudo = request.args.get('pseudo')
    password = request.args.get('password')
    return UserFunctions(pseudo, password).getAllManga()

@app.route('/TEST') # localhost:5000/TEST?pseudo=snoozy&password=deadoralive
def test():
    pseudo = request.args.get('pseudo')
    password = request.args.get('password')
    img = UserFunctions(pseudo, password).testImage()
    return  "<img src='{}'>".format(img)

if __name__ == "__main__":
    #Tools.commandLineSetup()
    #Tools.setupLOCALDATA()
    app.run(host ='localhost', port = 5000, debug = True)