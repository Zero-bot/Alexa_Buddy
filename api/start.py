import flask
from flask import jsonify
from controls.pi import Devices 
from controls.pi import Pi
from controls.pi import State

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route("/", methods=["GET"])
def home():
	return str({"page": "home"})


@app.route("/pi", methods = ["GET"])
def fauxmo_request():
	device = str.upper(flask.request.args["device"])
	operation = str.lower(flask.request.args["operation"])
	if device == 'ALL' and operation != 'status':
		return raspberry_pi.all_device(State[str.upper(operation)])
	if device == 'ALL' and operation == 'status':
		return raspberry_pi.status(device)
	if operation == 'on':
		return raspberry_pi.switch_on(Devices[device])
	if operation == 'off':
		return raspberry_pi.switch_off(Devices[device])
	if operation == 'status':
		return raspberry_pi.status(Devices[device])


if __name__ == '__main__':
	raspberry_pi = Pi()
	app.run(host='0.0.0.0')