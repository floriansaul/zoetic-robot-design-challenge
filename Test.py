from TouchDetector import TouchDetector

tests = [
	{"name": "Flick Test",
	 "data": [[0, 0, 0, 0, 0, 0], [0, 4000, 0, 0, 0, 0], [0, 4000, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]],
	 "output": "Flick detected on sensor B\n"},
	{"name": "Tap Test",
	 "data": [[0, 0, 0, 0, 0, 0], [0, 0, 0, 4000, 0, 0], [0, 0, 0, 4000, 0, 0], [0, 0, 0, 4000, 0, 0],
	          [0, 0, 0, 4000, 0, 0], [0, 0, 0, 4000, 0, 0], [0, 0, 0, 4000, 0, 0], [0, 0, 0, 1200, 0, 0]],
	 "output": "Tap detected on sensor D\n"},
	{"name": "Rub Test", "data": [[0, 0, 2500, 2500, 0, 0] for n in range(50)], "output": "Rub detected\n"},
]


def assert_equals(a, b, test_case):
	if a == b:
		print(test_case["name"] + " passes")
	else:
		print(test_case["name"] + " fails")


for test in tests:
	touch_detector = TouchDetector()
	output = ""
	for sample in test["data"]:
		output += touch_detector.loop(sample)
	assert_equals(test["output"], output, test)
