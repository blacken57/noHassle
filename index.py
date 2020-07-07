from flask import Flask, redirect, url_for, request, render_template
import create_face
import svmcamera
import joblib
app = Flask(__name__)

name = ""
index = -1

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
      return render_template('login.html',methods = ['POST','GET'])

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      #create_face.create_face_website(user)      
      #return redirect(url_for('buy',name = user))
      dict = joblib.load("catalogue")
      res = []
      for a in dict:
         res.append(a)
      names = svmcamera.person()
      return render_template('buy.html',person=names[0])
   else:
      user = request.args.get('nm')
      create_face.create_face_website(user)
      return redirect(url_for('success',name = user))





if __name__ == '__main__':
   app.run(debug = True)
