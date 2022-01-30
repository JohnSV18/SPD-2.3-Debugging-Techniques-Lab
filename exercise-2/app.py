import os
import requests

from datetime import datetime, timedelta
from dotenv import load_dotenv
from flask import Flask, render_template, request, send_file


################################################
## SETUP
################################################

app = Flask(__name__)

load_dotenv()
API_KEY = os.getenv('API_KEY')


################################################
## ROUTES
################################################

@app.route('/')
def home():
    """Displays the homepage with forms for current or historical data."""
    context = {
        'min_date': (datetime.now() - timedelta(days=5)),
        'max_date': datetime.now()
    }
    return render_template('home.html', **context)

def get_letter_for_units(units):
    """Returns a shorthand letter for the given units."""
    return 'F' if units == 'imperial' else 'C' if units == 'metric' else 'K'

@app.route('/results', methods=['GET'])
def results():
    """Displays results for current weather conditions."""
    city = request.args.get('users_city')
    units = request.args.get('units')

    url = 'http://api.openweathermap.org/data/2.5/find?q='+city+'&units='+units+'&appid='+API_KEY

    result_json = requests.get(url).json()
  
    context = {
        'date': datetime.now(),
        'city': result_json['list'][0]['name'],
        'description': result_json['list'][0]['weather'][0]['description'],
        'temp': result_json['list'][0]['main']['temp'],
        'humidity': result_json['list'][0]['main']['humidity'],
        'wind_speed': result_json['list'][0]['wind']['speed'],
        'units_letter': get_letter_for_units(units)
    }

    return render_template('results.html', **context)


if __name__ == '__main__':
    app.run()
