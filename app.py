from flask import Flask, render_template,redirect, url_for


from blueprints.home.views import home
from blueprints.analysisMethod.differenceMethod.views import differenceMethod
from blueprints.analysisMethod.classification.views import classification
from blueprints.analysisMethod.summaryMethod.views import summaryMethod


app = Flask(__name__)
app.config["SECRET_KEY"] = "9c1c9ac6-4525-4cf4-8708-f66887ae7641"

app.register_blueprint(home)
app.register_blueprint(differenceMethod)
app.register_blueprint(classification)
app.register_blueprint(summaryMethod)


@app.route("/")
def index():
    return redirect(url_for('home.index'))

if __name__ == "__main__":
    app.run(debug=True)


        
        

        


        


     
