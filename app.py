from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/Repairs.html')
def repairs():
    return render_template("Repairs.html")


@app.route('/Refurbished.html')
def refurbished():
    return render_template("Refurbished.html")


@app.route('/Contact.html')
def contact():
    return render_template("Contact.html")


@app.route('/FAQ.html')
def faq():
    return render_template("FAQ.html")


@app.route('/Reviews.html')
def reviews():
    return render_template("Reviews.html")


@app.route('/google.html')
def google():
    return render_template("google.html")


@app.route('/iphone.html')
def iphone():
    return render_template("iphone.html")


@app.route('/lg.html')
def lg():
    return render_template("lg.html")


@app.route('/samsung.html')
def samsung():
    return render_template("samsung.html")


@app.route('/about.html')
def about():
    return render_template("About.html")


if __name__ == '__main__':
    app.run(debug=True)
