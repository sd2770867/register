from Flask import Flask,request,render_template
  
app = Flask(__name__)
@app.route('/register',methods=['GET','POST'])
def register():
    if request.method=='POST':
        name =request.form['name']
        email=request.form['email']
        password=requst.form['password']
        #store the user data in a database or file
return render_temple('success.html')
return render_temple('register.html')
if __name__=='_main_':
    app.run(host='0.0.0.0')
