from flask import Flask, render_template,redirect, url_for


from blueprints.home.views import home
from blueprints.analysisMethod.classification.views import classification


app = Flask(__name__)
app.config["SECRET_KEY"] = "9c1c9ac6-4525-4cf4-8708-f66887ae7641"

app.register_blueprint(home)
app.register_blueprint(classification)


@app.route("/")
def index():
    return redirect(url_for('home.index'))

if __name__ == "__main__":
    app.run(debug=True)


        
        

        


        


     
