from flask import Flask, render_template
import requests

app = Flask(__name__)

def get_blockchain_chart_data():
    # Make a request to the Blockchain Charts API
    chart_name = 'transactions-per-second'
    timespan = '5weeks'
    rolling_average = '8hours'
    format_type = 'json'

    url = f'https://api.blockchain.info/charts/transactions-per-second?timespan=5weeks&rollingAverage=8hours&format=json'
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        return response.json()
    else:
        # Handle errors as needed
        return None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/home')
def index():
    # Fetch Blockchain Charts data
    chart_data = get_blockchain_chart_data()

    # Render the HTML page and pass the chart data
    return render_template('home.html', chart_data=chart_data)

if __name__ == "__main__":
    app.run(debug=True)