from flask import Flask, render_template, url_for, request, redirect
import csv 
import numpy as np

import pickle

model=pickle.load(open('model.pkl','rb'))

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


@app.route('/predict', methods=["POST"])
def predict():
    # get values of the form
    city = request.values.get("city")
    basement = request.values.get("choice_basement")
    renovated = request.values.get("choice_renovated")
    floors = request.values.get("floors")
    waterfront = request.values.get("choice_waterfront")
    view = request.values.get("view")
    condition = request.values.get("condition")
    bedrooms  = request.values.get("bedrooms")
    bathrooms  = request.values.get("bathrooms")
    living  = request.values.get("living")
    lot  = request.values.get("lot")
    above = request.values.get("above")
    
    inputs = np.array([[bedrooms,bathrooms,living,lot,floors,waterfront,view,condition,above,basement,renovated,city]])

    prediction = model.predict(inputs)
    
    output='{0:.{1}f}'.format(prediction[0], 0)

    # print prediction
    return render_template('estimation.html', 
                           city='{}$'.format(output))


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
    
if __name__=="__main__":
    app.run(port=5000, debug=True)