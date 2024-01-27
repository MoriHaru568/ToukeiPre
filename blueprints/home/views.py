from flask import  redirect, render_template,request,Blueprint,url_for





FUNCTION_NAME="home"
home=Blueprint(FUNCTION_NAME,__name__,url_prefix="/"+FUNCTION_NAME,template_folder="templates",static_folder="./static")



@home.route("/",methods=["GET"])
def index():
    return render_template(FUNCTION_NAME+"/home.html",message="")

@home.route('/chi-square-test')
def chi_square_test():
    return redirect(url_for('classification.chiSquareTest'))

@home.route('/t-test')
def t_test():
    return render_template('classification.tTest')

@home.route('/variance')
def anova():
    return render_template('classification.variance')

# @home.route('/factor-test')
# def anova():
#     return render_template('anova.html')

# @home.route('/principal-component')
# def anova():
#     return render_template('anova.html')

# @home.route('/multidimensional-scaling-test')
# def anova():
#     return render_template('anova.html')

# @home.route('/correspondence-analysis')
# def anova():
#     return render_template('anova.html')

# @home.route('/quantification-test')
# def anova():
#     return render_template('anova.html')

# @home.route('/cluster-analysis')
# def anova():
#     return render_template('anova.html')

# @home.route('/latent-class-analysis')
# def anova():
#     return render_template('anova.html')

