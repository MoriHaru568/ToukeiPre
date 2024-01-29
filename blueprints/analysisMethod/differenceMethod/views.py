from flask import  render_template,request,Blueprint,jsonify, session, url_for
from jinja2 import TemplateNotFound



FUNCTION_NAME="differenceMethod"
differenceMethod=Blueprint(FUNCTION_NAME,__name__,url_prefix="/"+FUNCTION_NAME,template_folder="templates",static_folder="./static")

@differenceMethod.route("/chi-square-test",methods=["GET"])
def chiSquareTest():
    return render_template(FUNCTION_NAME+"/chi-square-test.html",message="")


@differenceMethod.route("/t-test",methods=["GET"])
def tTest():
    return render_template(FUNCTION_NAME+"/t-test.html",message="")


@differenceMethod.route("/variance",methods=["GET"])
def variance():
    return render_template(FUNCTION_NAME+"/variance.html",message="")


