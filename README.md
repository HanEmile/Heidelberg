# Heidelberg

Display an elliptical Galaxy in Blender using a custom Star density function.

##### Dependencies:
- [math](https://docs.python.org/3/library/math.html)
- [matplotlib.pyplot](http://matplotlib.org/api/pyplot_api.html)
- [numpy](http://www.numpy.org/)
- [scipy](https://www.scipy.org/)
- [scipy.interpolate.InterpolatedUnivariateSpline](https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.InterpolatedUnivariateSpline.html)

##### Custom Dependencies:
Name | File | Function
--- | --- | ---
Variables | `variables.py` | stores general variables
Constants | `constants.py` | stores constants
Heidelberg | `Heidelberg.py` | stores functions

##### Generate data with:
`python3 main.py`

##### Draw Histogram with:
`python3 draw.py`

##### Blender foo (WIP):
`blender <blender-file> --python <python-file> 

[Blender](https://www.blender.org),
[more...](markdown/notes.md)
