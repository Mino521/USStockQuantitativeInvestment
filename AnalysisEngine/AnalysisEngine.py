from http import server
import importlib
from flask import Flask
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
import json
import os
app= Flask(__name__)
@app.route("/runAlgorithm",methods = ['POST'])
def runAlgorithm():
    try:
        AlgorithmFile = importlib.import_module("AlgorithmLib."+request.args.get("Algorithmname"))
        func = getattr(AlgorithmFile,request.args.get("Algorithmname"))
        result = func(json.loads(request.get_data()))
    except BaseException:
        return "ERROR"
    else:
        return jsonify(result) 

@app.route("/uploadFile",methods = ['POST'])
def uploadFile():
    try:
        f = request.files['the_file']
        print(type(f))
        f.save(os.path.abspath("./") +"/AlgorithmLib/"+ secure_filename(f.filename))
    except BaseException:
        return "ERROR"
    else:
        return "SUCCESS"

if __name__ == '__main__':
    app.debug =True
    app.run(port=5000)

    
