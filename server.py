from flask import Flask, render_template, url_for, request, redirect
import csv 

app = Flask(__name__)


@app.route('/')
def home():
	return render_template("index.html")

@app.route('/<string:page_name>')
def html_page(page_name):
	return render_template(page_name)

@app.route('/index.html')
def index():
	return render_template("index.html")

@app.route('/contact.html')
def contact():
	return render_template("contact.html")

def write_to_file(data):
	with open('database.txt', mode='a') as database:
		firstname = data["firstname"]
		subject = data["subject"]
		email = data["email"]
		message = data["message"]
		file = database.write(f'\n{firstname},{subject},{email},{message}')

def write_to_csv(data):
	with open('database.csv', newline='', mode='a') as database2:
		firstname = data["firstname"]
		subject = data["subject"]
		email = data["email"]
		message = data["message"]
		csv_writer = csv.writer(database2, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([firstname, subject, email, message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		data = request.form.to_dict()
		write_to_file(data)
		return redirect('/thankyou.html')
		
	else:
		return "Something went wrong, try again"