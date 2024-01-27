from flask import  render_template,request,Blueprint,jsonify, session, url_for
from jinja2 import TemplateNotFound



FUNCTION_NAME="home"
home=Blueprint(FUNCTION_NAME,__name__,url_prefix="/"+FUNCTION_NAME,template_folder="templates",static_folder="./static")

@home.route("/",methods=["GET"])
def index():
    return render_template(FUNCTION_NAME+"/home.html",message="")


