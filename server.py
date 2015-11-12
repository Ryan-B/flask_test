from flask import Flask, render_template, request, redirect, session, flash  # Import Flask to allow us to create our app and render_template to allow us to render index.html
app = Flask(__name__)
app.secret_key = "ThisIsSecret"
@app.route('/') # The "@" symbol designates a "decorator" which attaches the following function to the '/' route. This means that whenever we send a request to localhost:5000/ we will run the following "hello_world" function.
def index():
	return render_template('index.html')

@app.route('/success', methods=['post'])
def show_data():
	if len(request.form['name']) < 1:
		flash("Name cannot be empty!")
		return redirect ('/') 
	elif len(request.form['comments']) > 120:
		flash("Your comment is TL;DR please keep it under 120 characters.")
		return redirect ('/')
  	else:
  		session['name'] = request.form['name']
  		session['team'] = request.form['team']
  		session['location'] = request.form['location']
  		session['language'] = request.form['language']
  		session['comments'] = request.form['comments']

	return render_template('success.html')
	
  
app.run(debug=True)
    	
	
		 
  	

