from flask import Flask, redirect, url_for, request
import create_face
app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      create_face.create_face_website(user)
      
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      create_face.create_face_website(user)
      return redirect(url_for('success',name = user))

if __name__ == '__main__':
   app.run(debug = True)
