from flask import Flask, redirect, url_for, request, render_template
import create_face
import svmcamera
import joblib
app = Flask(__name__)

name = ""
index = -1
balance = joblib.load("balance")
naam = joblib.load("name.joblib")

@app.route('/buy',methods = ['POST'])
def buy():
   dict = joblib.load("catalogue")
   res = []
   for a in dict:
      res.append(a)
   if request.method == 'POST':
     if request.form['ques'] == 'Yes':
      
      return render_template('products.html')
     elif request.form['ques'] == 'No':
      return render_template('Register.html',methods = ['POST','GET'])

@app.route('/Register',methods = ['POST', 'GET'])
def Register():
   if request.method == 'POST':
      user = request.form['nm']
      create_face.create_face_website(user)      
      #return redirect(url_for('buy',name = user))
      dict = joblib.load("catalogue")
      res = []
      for a in dict:
         res.append(a)
      #names = svmcamera.person()
      #index = names.index(names[1])
      return render_template('Homepage.html')

@app.route('/Home',methods = ['POST', 'GET'])
def Home():
   if request.method == 'POST':
     if request.form['ques'] == 'Buy':
      names = svmcamera.person()      
      return render_template('buy.html',person = names[0],methods = ['POST'])
     elif request.form['ques'] == 'Register':
      return render_template('Register.html',methods = ['POST','GET'])
     elif request.form['ques'] == 'Balance':
      names = svmcamera.person()#names = [name, index]; names[1] = index
      return "Hello, Balance is: "+str(balance[names[1]]) + " and your name is: "+names[0]

# @app.route('/Balance',methods = ['POST', 'GET'])
# def Balance():
#   if request.method == 'POST':
#     user = request.form['nm']
#     money = int(user)





if __name__ == '__main__':
   app.run(debug = True)