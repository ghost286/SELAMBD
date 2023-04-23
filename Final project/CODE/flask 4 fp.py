from flask import Flask, render_template, request
import my_python_script

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_form', methods=['POST'])
def process_form():
    data = request.form['data']
    result = my_python_script.process_data(data)
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
