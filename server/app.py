from flask import Flask, jsonify
from flask_cors import CORS

# configs

DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

#enable cors
CORS(app, resources={r'/*': {'origins': '*'}})

# sanity check route 

@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


# check if this is the main module
if __name__ == '___main__':
    app.run()