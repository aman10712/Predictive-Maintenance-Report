from flask import Flask, render_template, request
from model import mal_function_pred
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/result',methods=["GET","POST"])
def results_page():

     if request.method == "POST":
          dev_cap = int(request.form["dev_cap"])
          dev_pre = int(request.form["dev_pre"])
          dev_temp = int(request.form["dev_temp"])
          day = int(request.form["day"])
          mon = int(request.form["mon"])
          year = int(request.form["year"])
          loc = request.form["loc"]
          dates=mal_function_pred(dev_cap,dev_pre,dev_temp,loc,day,mon,year)
          return render_template("results.html",mal_date = str(dates[0]),serv= str(dates[1]))
    
     return 'Contact Page'


@app.route('/about_us')
def abus():
    
    return 'This is About Page'

app.run(debug=True)