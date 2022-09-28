from flask import Flask, jsonify, request

import importlib.util
try:
    importlib.util.find_spec('RPi.GPIO')
    import RPi.GPIO as GPIO
except ImportError:
    """
    import FakeRPi.GPIO as GPIO
    OR
    import FakeRPi.RPiO as RPiO
    """

app = Flask(__name__)


PIN = 4




def switch_on(pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(4, GPIO.OUT) # Turn motor on

def switch_off(pin):
    GPIO.cleanup()# Turn motor off





@app.route("/") 
def index(): 
   return "Hello, World!" 

@app.route('/api/v1/status', methods=['GET'])
def server_status():
    return 'Server is UP', 200

@app.route('/api/v1/power/<state>', methods=['POST'])
def change_state(state):
    if state not in ['on','ON','off','OFF']:
        return 'Wrong state', 400
    elif state in ['on','ON']:
        switch_on(PIN)
        print("State : ON")
        return 'ON', 200
    elif state in ['off','OFF']:
        switch_off(PIN)
        print("State : OFF")
        return 'OFF', 200


if __name__ == '__main__':
    app.run(port=5000, debug=True)

