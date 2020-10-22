from flask import Flask
import Tools
import usersFunctions

app = Flask(__name__)

@app.route('/')
def hello():
    return "Flask app client"

@app.route("/SIGNUP")   #  http://localhost:5000/SIGNUP?pseudo=snoozy&password=deadoralive
def signup():
    return usersFunctions.signup()

@app.route('/GETALL')   # localhost:5000/GETALL?limit=10
def getall():
    return usersFunctions.getAllManga()

@app.route('/TEST') # localhost:5000/TEST
def test():
    img = usersFunctions.testImage()
    return  "<img src='{}'>".format(img)

#if __name__ == "__main__":
    #Tools.commandLineSetup()
    #Tools.setupLOCALDATA()
    #app.run(host ='localhost', port = 5000, debug = True)