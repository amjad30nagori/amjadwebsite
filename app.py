from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('./index.html')

@app.route('/.well-known/pki-validation/7FBF967CD2041427C74FB9D71D3E7013.txt')
def certificate():
    return render_template('/.well-known/pki-validation/7FBF967CD2041427C74FB9D71D3E7013.txt')

@app.route('/<string:page_name>')
def htmlpage(page_name):
    return render_template(page_name)

def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_file = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_file.writerow([email, subject, message])

# def write_to_file(data):
#     with open('database.txt', mode='a') as database:
#         email = data["email"]
#         subject = data["subject"]
#         message = data["message"]
#         file = database.write(f'\n{email},{subject},{message}')

@app.route('/submit_form', methods=["POST", "GET"])
def submit_form():
    if request.method == "POST":
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect("./thankyou.html")
    else:
        return "something went wrong"


