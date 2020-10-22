from flask import Flask
import adminFunctions as adminFunctions
import CommonVariables
import Tools

app = Flask(__name__)


@app.route("/")     
def index():
    return "flask app Admin"


@app.route("/DOWNLOADALL")   
def download_all():
    adminFunctions.download_all_scan()
    return CommonVariables.RETURN_STATEMENT

@app.route("/UPDATESCAN")   
def updateScan():
    adminFunctions.updateScan()
    return CommonVariables.RETURN_STATEMENT

@app.route("/MALMANGADATAUPDATE")   
def MAL_manga_data_update():
    adminFunctions.MAL_manga_data_update()
    return CommonVariables.RETURN_STATEMENT

@app.route("/MANGAWEHAVEUPDATE") 
def Manga_we_have_update():
    adminFunctions.Manga_we_have_update()
    return CommonVariables.RETURN_STATEMENT

if __name__ == "__main__":
    #Tools.commandLineSetup()
    app.run(host ='0.0.0.0', port = 5000, debug = True)