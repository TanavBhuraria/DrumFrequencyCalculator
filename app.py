from flask import Flask, render_template, request
import math
import os

app = Flask(__name__)

@app.route('/')
def landing():
    return render_template('index.html')

@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    freq = None

    if request.method == 'POST':
        try:
            r = float(request.form['radius']) / 100  # cm to meters
            tension_values = {"low": 400, "medium": 800, "high": 1200}
            density_values = {"thin": 0.1, "medium": 0.2, "thick": 0.3}

            tension = tension_values[request.form['tension'].lower()]
            density = density_values[request.form['thickness'].lower()]

            f = 0.382767638 / r * math.sqrt(tension / density)
            freq = round(f, 2)
        except Exception as e:
            freq = "Error: Invalid input."

    return render_template('calculator.html', freq=freq)

@app.route('/instructions')
def instructions():
    return render_template('instructions.html')

@app.route('/how-it-works')
def howitworks():
    return render_template('how-it-works.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))
