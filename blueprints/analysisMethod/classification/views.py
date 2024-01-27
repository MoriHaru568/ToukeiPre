from flask import  render_template,request,Blueprint,jsonify, session, url_for
from jinja2 import TemplateNotFound



FUNCTION_NAME="classification"
classification=Blueprint(FUNCTION_NAME,__name__,url_prefix="/"+FUNCTION_NAME,template_folder="templates",static_folder="./static")

@classification.route('/factor-test')
def factorTest():
    return render_template(FUNCTION_NAME+"/login.html",message="")

@classification.route('/principal-component')
def principalComponent():
    return render_template(FUNCTION_NAME+"/login.html",message="")

@classification.route('/multidimensional-scaling-test')
def multidimensionalScalingTest():
    return render_template(FUNCTION_NAME+"/login.html",message="")

@classification.route('/correspondence-analysis')
def correspondenceAnalysis():
    return render_template(FUNCTION_NAME+"/login.html",message="")

@classification.route('/quantification-test')
def quantificationTest():
    return render_template(FUNCTION_NAME+"/login.html",message="")


