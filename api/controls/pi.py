import RPi.GPIO as GPIO
from enum import Enum
from time import sleep

class Devices(Enum):
	TV = 7
	DTH = 11
	FIRESTICK = 13
	FAN = 15

class State(Enum):
	ON = 'on'
	OFF = 'off'

class Pi(object):
	_DEVICES_STATE = {}

	def __init__(self):
		GPIO.setmode(GPIO.BOARD)
		for device in Devices:
			GPIO.setup(device.value, GPIO.OUT)
			GPIO.output(device.value, GPIO.HIGH)
			self._DEVICES_STATE[device] = State.OFF
			self._DEVICES_STATE['ALL'] = State.OFF

	def switch_on(self, device: Devices) -> str:
		if self._DEVICES_STATE[device] is not State.ON:
			GPIO.output(device.value, GPIO.LOW)
			self._DEVICES_STATE[device] = State.ON
		return State.ON.value

	def switch_off(self, device: Devices) -> str:
		if self._DEVICES_STATE[device] is not State.OFF:
			GPIO.output(device.value, GPIO.HIGH)
			self._DEVICES_STATE[device] = State.OFF
		return State.OFF.value

	def status(self, device) -> str:
		if device == 'ALL':
			return self._DEVICES_STATE['ALL'].value
		return self._DEVICES_STATE[device].value

	def all_device(self, state: State) -> str:
		if state is State.ON:
			for device in Devices:
				if self._DEVICES_STATE[device] is not State.ON:
					GPIO.output(device.value, GPIO.LOW)
			self._DEVICES_STATE['ALL'] = state
		elif state is State.OFF:
			for device in Devices:
				if self._DEVICES_STATE[device] is not State.OFF:
					GPIO.output(device.value, GPIO.HIGH)
			self._DEVICES_STATE['ALL'] = state
		return state.value


	def destroy(self):
		for device in Devices:
			GPIO.output(device.value, GPIO.HIGH) 
		GPIO.cleanup()	



# raspi = Pi()
# raspi.switch_on(Devices.TV)
# print(raspi.status(Devices.TV))
# sleep(3)
# raspi.switch_off(Devices.TV)
# print(raspi.status(Devices.TV))
# raspi.destroy()
