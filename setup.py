from setuptools import setup

setup(
	name = "temperature",
	version = "1.1",
	author = "kubinka0505",
	description = "Temperature units conversion.",
	long_description = \
"""\
Temperature Conversion.

Conversion of Temperature units. (Celsius, Fahrenheit, Kelvin)
	""",
	classifiers = [
		"Programming Language :: Python :: 2",
		"Programming Language :: Python :: 3"
		"License :: OSI Approved :: MIT License",
		"Development Status :: 5 - Production/Stable",
		"Intended Audience :: Science/Research",
		],
	url = "http://github.com/kubinka0505/temperature",
	license = "MIT",
	py_modules = [r"temperature\__init__"],
)
