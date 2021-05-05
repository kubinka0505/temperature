# !/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from sys import version as Python_Version

#-----#

"""Temperature units conversion.

Available Units:
- Celsius
- Fahrenheit
- Kelvin

Example Use:
	```python
	>>> Celsius(12.5).to_Fahrenheit()
	54.5{0}F
	```

Changelog:
	`1.0` (13.05.2018):
		Initial Release.
	`1.1` (24.05.2018):
		Added:
			- `float` numbers handling.
			- `str` returns of conversion:
				Example Use:
					Without `String` argument usage:
						```python
						>>> Fahrenheit(25).to_Kelvin()
						269.2611111111111 K
						```
					With `String` argument usage:
						```python
						>>> Kelvin(37.5).to_Celsius(True)
						'-235.64999999999998{0}C'
						```
		Fixed:
			- Alternative installation for `git` users.
			- Renamed `Celcius` to `Celsius`.
		Updated:
			- `doc-strings`
			- `type hints`""".format(u"\xb0")

#-----#

__version__ = "1.1"
__date__ = "25.05.2018"
__author__ = "kubinka0505"

#-----#

class Celsius(object):
	"""`Celsius` Temperature section."""
	def __init__(self, Temperature):
		# type: (int or float)
		"""Initializes `self` and `Celsius` Temperature used in conversion."""
		if isinstance(Temperature, int) or isinstance(Temperature, float): self.Temperature = Temperature
		else: raise ValueError("`Temperature` should be `{0}` or `{1}`, not `{2}`.".format(int.__class__.__name__, float.__class__.__name__, Temperature.__class__.__name__))

	def to_Fahrenheit(self, String = False):
		# type: (bool)
		# return: Fahrenheit
		"""Converts `Celsius` to `Fahrenheit`."""
		if isinstance(String, bool):
			if String == True:
				return u"{0}\xb0F".format((self.Temperature*9/5)+32)
			elif String == False:
				return print(u"{0}\xb0F".format((self.Temperature*9/5)+32))
		else: raise ValueError("`String` should be `{0}`, not `{1}`.".format(bool.__class__.__name__, String.__class__.__name__))

	def to_Kelvin(self, String = False):
		# type: (bool)
		# return: Kelvin or str
		"""Converts `Celsius` to `Kelvin`."""
		if isinstance(String, bool):
			if String == True:
				return "{0} K".format(self.Temperature+273.15)
			elif String == False:
				return print("{0} K".format(self.Temperature+273.15))
		else: raise ValueError("`String` should be `{0}`, not `{1}`.".format(bool.__class__.__name__, String.__class__.__name__))

#-----#

class Fahrenheit(object):
	"""`Fahrenheit` Temperature section."""
	def __init__(self, Temperature):
		# type: (int or float)
		"""Initializes `self` and `Fahrenheit` Temperature used in conversion."""
		if isinstance(Temperature, int) or isinstance(Temperature, float): self.Temperature = Temperature
		else: raise ValueError("`Temperature` should be `{0}` or `{1}`, not `{2}`.".format(int.__class__.__name__, float.__class__.__name__, Temperature.__class__.__name__))

	def to_Celsius(self, String = False):
		# type: (bool)
		# return: Celsius
		"""Converts `Fahrenheit` to `Celsius`."""
		if isinstance(String, bool):
			if String == True:
				return u"{0}\xb0C".format((self.Temperature-32)*5/9)
			elif String == False:
				return print(u"{0}\xb0C".format((self.Temperature-32)*5/9))
		else: raise ValueError("`String` should be `{0}`, not `{1}`.".format(bool.__class__.__name__, String.__class__.__name__))

	def to_Kelvin(self, String = False):
		# type: (bool)
		# return: Kelvin
		"""Converts `Fahrenheit` to `Kelvin`."""
		if isinstance(String, bool):
			if String == True:
				return "{0} K".format((self.Temperature+459.67)*5/9)
			elif String == False:
				return print("{0} K".format((self.Temperature+459.67)*5/9))
		else: raise ValueError("`String` should be `{0}`, not `{1}`.".format(bool.__class__.__name__, String.__class__.__name__))

#-----#

class Kelvin(object):
	"""`Kelvin` Temperature section."""
	def __init__(self, Temperature):
		# type: (int or float)
		"""Initializes `self` and `Kelvin` Temperature used in conversion."""
		if isinstance(Temperature, int) or isinstance(Temperature, float): self.Temperature = Temperature
		else: raise ValueError("`Temperature` should be `{0}` or `{1}`, not `{2}`.".format(int.__class__.__name__, float.__class__.__name__, Temperature.__class__.__name__))

	def to_Celsius(self, String = False):
		# type: (bool)
		# return: Celsius
		"""Converts `Kelvin` to `Celsius`."""
		if isinstance(String, bool):
			if String == True:
				return u"{0}\xb0C".format(self.Temperature-273.15)
			elif String == False:
				return print(u"{0}\xb0C".format(self.Temperature-273.15))
		else: raise ValueError("`Temperature` should be `{0}` or `{1}`, not `{2}`.".format(int.__class__.__name__, float.__class__.__name__, Temperature.__class__.__name__))

	def to_Fahrenheit(self, String = False):
		# type: (bool)
		# return: Fahrenheit
		"""Converts `Kelvin` to `Fahrenheit`."""
		if isinstance(String, bool):
			if String == True:
				return u"{0}\xb0F".format((self.Temperature*9/5)-459.67)
			elif String == False:
				return print(u"{0}\xb0F".format((self.Temperature*9/5)-459.67))
		else: raise ValueError("`Temperature` should be `{0}` or `{1}`, not `{2}`.".format(int.__class__.__name__, float.__class__.__name__, Temperature.__class__.__name__))

# Annotations #
if Python_Version.split(".")[0] == "3":
	# Celsius #
	Celsius.__init__.__annotations__ = {"Temperature": __import__("typing").Union[int, float] if Python_Version.split(".")[1] <= "5" else int}
	Celsius.to_Fahrenheit.__annotations__ = {"String": bool, "return": Fahrenheit}
	Celsius.to_Kelvin.__annotations__ = {"String": bool, "return": Kelvin}
	# Fahrenheit #
	Fahrenheit.__init__.__annotations__ = {"Temperature": __import__("typing").Union[int, float] if Python_Version.split(".")[1] <= "5" else int}
	Fahrenheit.to_Celsius.__annotations__ = {"String": bool, "return": Celsius}
	Fahrenheit.to_Kelvin.__annotations__ = {"String": bool, "return": Kelvin}
	# Kelvin #
	Kelvin.__init__.__annotations__ = {"Temperature": __import__("typing").Union[int, float] if Python_Version.split(".")[1] <= "5" else int}
	Kelvin.to_Celsius.__annotations__ = {"String": bool, "return": Celsius}
	Kelvin.to_Fahrenheit.__annotations__ = {"String": bool, "return": Fahrenheit}

del print_function, Python_Version