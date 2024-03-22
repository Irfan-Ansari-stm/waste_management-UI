from flask import Flask, render_template


app = Flask(__name__)

# Initialize Google Maps client with your API key

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/transport')
def transport():
    return render_template('transport.html')

@app.route('/waste')
def waste():
    return render_template('waste.html')

@app.route('/service')
def service():
    return render_template('service.html')

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
