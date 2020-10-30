import csv
import datetime
from os import times
from flask import Flask, jsonify, request
from flask_cors import CORS


# configs

DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable cors
CORS(app, resources={r'/*': {'origins': '*'}})

# sanity check route


@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


def read_data():
    # post_data = request.get_json()
    # csv_file = post_data.get('upload_file')
    return_obj = {}

    with open('spread.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in range(6, 7):
            # complete_times = []
            # complete_times.append(datetime.strptime(row['Completion Time'], '%d/%m/%y %H:%M:%S'))
            # latest_time = max(complete_times)
            latest_time = row['Completion Time']
            latest_balance = row['Balance']
            return_obj['latest_time'] = latest_time
            return_obj['latest_balance'] = latest_balance
    return return_obj


# check if this is the main module
if __name__ == '___main__':
    app.run()
