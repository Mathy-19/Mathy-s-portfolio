from flask import Flask,render_template
app=Flask(__name__)
@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")
@app.route('/qualification')
def qualification():
    return render_template("qualification.html")
@app.route('/work')
def work():
    return render_template("work.html")
@app.route('/contact')
def contact():
    return render_template("contact.html")


if __name__=="__main__":
 app.run(debug=True)