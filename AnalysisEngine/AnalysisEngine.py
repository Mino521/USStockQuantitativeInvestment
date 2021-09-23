from http import server
import importlib
from flask import Flask
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
import Config
from DatabaseUtil import app
import json
import os
import DatabaseUtil


@app.route("/runAlgorithm",methods = ['POST'])
def runAlgorithm():
    try:
        AlgorithmFile = importlib.import_module("AlgorithmLib."+request.args.get("Algorithmname"))
        func = getattr(AlgorithmFile,request.args.get("Algorithmname"))
        result = func(json.loads(request.get_data()))
    except BaseException as e:
        print(e)
        return str(e)
    else:
        return jsonify(result) 
@app.route("/test",methods = ['POST'])
def test():
    try:
        print(request.values.get("AlgorithmName"))
        return "success"
    except BaseException as e:
        print(e)
        return str(e)
@app.route("/uploadFile",methods = ['POST'])
def uploadFile():
    try:
        f = request.files['PythonFile']
        f.filename = secure_filename(f.filename)
        print(os.path.join(os.path.abspath(__file__) +'\\AlgorithmLib'))
        f.save(os.path.join(os.path.dirname(os.path.abspath(__file__)) +"\\AlgorithmLib\\"+f.filename))
        data = DatabaseUtil.AlgorithmLib.query.filter_by(AlgorithmName= f.filename)
        if data:
            data.update({'Description':request.values.get("AlgorithmName"),'Parameter': request.values.get("Parameter"),'Output' : request.values.get("Output")})
        else:
            role = DatabaseUtil.AlgorithmLib(AlgorithmName= f.filename,Description = request.values.get("AlgorithmName"),Parameter = request.values.get("Parameter"),Output = request.values.get("Output"))
            DatabaseUtil.db.session.add(role)
            DatabaseUtil.db.session.commit()
    except BaseException as e:
        print(e)
        return str(e)
    else:
        return "SUCCESS"
@app.route('/getAlgorithmList',methods = ['GET'])
def getAlgorithmList():
    
    Alist = DatabaseUtil.AlgorithmLib.query.all()
    
    return  jsonify(DatabaseUtil.model_list_to_dict_list(Alist))
if __name__ == '__main__':
    app.debug =True
    app.run(host='0.0.0.0',port=5000)

    
