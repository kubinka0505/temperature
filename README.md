temperature
===
This module allows to convert following temperature units to:
* Celsius
* Fahrenheit
* Kelvin
---
Changelog
---
* `1.0` *(13.05.2018)*: **Initial Release.**
* `1.1` *(24.05.2018)*:

#### Added:
* `float` numbers handling while converting.
* `str` returns of conversion:
##### Example Use:
1. Without `String` argument usage:
```python
>>> Fahrenheit(25).to_Kelvin()
269.2611111111111 K
```
2. With `String` argument usage:
```python
>>> Kelvin(37.5).to_Celsius(True)
'-235.64999999999998°C'
```
#### Fixed:
* Alternative installation for `git` users.
* Name `Celcius` to `Celsius`.
#### Updated:
* `doc-strings`
* `type hints`.
---
Installation
---
`git` is required, although installation can be done by copying files from archive downloadable above.
```python
python -m pip install git+https://github.com/kubinka0505/temperature
```