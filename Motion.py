import Config


class Motion:

	def detect(self, input_history):
		pass


class Tapping(Motion):
	# let's call a "tap" a touch between .05 and .5 sec duration ending now
	def detect(self, input_history):
		ret = ""
		for sensor, current_sensor_value in enumerate(input_history[-1]):
			if current_sensor_value < Config.touch_threshold:
				minimum_condition = all([sample[sensor] > Config.touch_threshold for sample in input_history[-6:-1]])
				maximum_condition = any([sample[sensor] < Config.touch_threshold for sample in input_history[-51:-6]])

				if minimum_condition and maximum_condition:
					ret += "Tap detected on sensor " + Config.sensors[sensor] + "\n"
		return ret


class Flicking(Motion):
	# let's call a "flick" a touch between .01 and .05 sec duration ending now
	def detect(self, input_history):
		ret = ""
		for sensor, current_sensor_value in enumerate(input_history[-1]):
			if current_sensor_value < Config.touch_threshold:
				minimum_condition = input_history[-2][sensor] > Config.touch_threshold
				maximum_condition = any([sample[sensor] < Config.touch_threshold for sample in input_history[-6:-1]])

				if minimum_condition and maximum_condition:
					ret += "Flick detected on sensor " + Config.sensors[sensor] + "\n"
		return ret


class Rubbing(Motion):
	# let's call a "rub" a touch on 2+ sensors for .5+ seconds
	def detect(self, input_history):
		if all(self.fulfills_rub_criteria(sample) for sample in input_history[-50:]):
			return "Rub detected\n"
		return False

	def fulfills_rub_criteria(self, sample):
		count = 0
		for sensor_value in sample:
			if sensor_value > Config.resting_finger_threshold:
				count += 1
		return count >= 2
