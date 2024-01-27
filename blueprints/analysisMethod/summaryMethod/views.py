from flask import  redirect, render_template,request,Blueprint,jsonify, session, url_for
from jinja2 import TemplateNotFound



FUNCTION_NAME="summaryMethod"
summaryMethod=Blueprint(FUNCTION_NAME,__name__,url_prefix="/"+FUNCTION_NAME,template_folder="templates",static_folder="./static")


@summaryMethod.route('/cluster-analysis')
def clusterAnalysis():
    return render_template(FUNCTION_NAME+"/login.html",message="")


@summaryMethod.route('/latent-class-analysis')
def latentClassAnalysis():
    return render_template(FUNCTION_NAME+"/login.html",message="")



