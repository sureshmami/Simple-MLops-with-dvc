from logging import debug, error
from re import template
from flask import Flask, config, render_template, request, jsonify
import os
import joblib
from werkzeug.wrappers import response
import yaml
import numpy as np

from prediction_service import prediction

params_path = "params.yaml"
webapp_root = "webapp"

static_dirs = os.path.join(webapp_root, "static")
template_dirs = os.path.join(webapp_root,"templates")

app = Flask(__name__,static_folder=static_dirs,template_folder=template_dirs)

def read_params(config_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

def predict(data):
    config = read_params(params_path)
    model_dir_path = config["webapp_model_dir"]
    model = joblib.load(model_dir_path)
    prediction = model.predict(data)
    return "{0:.2f}".format(prediction[0])

def api_response(request):
    try:
        data = np.array([list(request.json.values())])
        response = predict(data)
        response = {"response":response}
        return response
    except Exception as e:
        print(e)
        error = {"error":"Something went wrong, try again!!"}
        return error


@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        try:
            if request.form:
                data = dict(request.form).values()
                data = [list(map(float, data))]
                response = predict(data)
                return render_template("index.html", response=response)
            elif request.json:
                response = api_response(request)
                return jsonify(response)
                
            
        except Exception as e:
            print(e)
            error = {"error":"Something went wrong, try again!!"}
            return render_template("404.html", error=error) 
    else:
        return render_template("index.html")
if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)

