from flask import  redirect, render_template,request,Blueprint,url_for





FUNCTION_NAME="home"
home=Blueprint(FUNCTION_NAME,__name__,url_prefix="/"+FUNCTION_NAME,template_folder="templates",static_folder="./static")



@home.route("/",methods=["GET"])
def index():
    return render_template(FUNCTION_NAME+"/home.html",message="")

@home.route('/chi-square-test')
def chiSquareTest():
    return redirect(url_for('differenceMethod.chiSquareTest'))

@home.route('/t-test')
def tTest():
    return redirect(url_for('differenceMethod.tTest'))

@home.route('/variance')
def variance():
    return redirect(url_for('differenceMethod.variance'))

@home.route('/factor-test')
def factorTest():
    return redirect(url_for('classification.factorTest'))

@home.route('/principal-component')
def principalComponent():
    return redirect(url_for('classification.principalComponent'))

@home.route('/multidimensional-scaling-test')
def multidimensionalScalingTest():
    return redirect(url_for('classification.multidimensionalScalingTest'))

@home.route('/correspondence-analysis')
def correspondenceAnalysis():
    return redirect(url_for('classification.correspondenceAnalysis'))

@home.route('/quantification-test')
def quantificationTest():
    return redirect(url_for('classification.quantificationTest'))

@home.route('/cluster-analysis')
def clusterAnalysis():
    return redirect(url_for('summaryMethod.clusterAnalysis'))

@home.route('/latent-class-analysis')
def latentClassAnalysis():
    return redirect(url_for('summaryMethod.latentClassAnalysis'))

