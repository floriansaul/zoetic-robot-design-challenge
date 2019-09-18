import Config
from Motion import *


# assuming 10ms between samples
class TouchDetector:
	input_history = []
	motions = []

	def __init__(self):
		self.motions = [Tapping(), Flicking(), Rubbing()]

	# Run every timestep
	def loop(self, input_sample):
		ret = ""
		self.input_history.append(input_sample)

		# Dont pass things in until some history has been built up
		if len(self.input_history) < 3:
			return ret

		for motion in self.motions:
			response = motion.detect(self.input_history)
			if response:
				ret += response

		return ret
