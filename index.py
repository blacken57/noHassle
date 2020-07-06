from flask import Flask, redirect, url_for, request, render_template
import create_face
import svmcamera
import joblib
app = Flask(__name__)

name = ""
index = -1

@app.route('/buy/<name>')
def buy(name):
   dict = joblib.load("catalogue")
   res = []
   for a in dict:
      res.append(a)
   h = svmcamera.person()
   return render_template('money.html', colours=res, name = h[0])

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      create_face.create_face_website(user)
      
      return redirect(url_for('buy',name = user))
   else:
      user = request.args.get('nm')
      create_face.create_face_website(user)
      return redirect(url_for('success',name = user))





if __name__ == '__main__':
   app.run(debug = True)
