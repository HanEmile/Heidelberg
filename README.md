# Heidelberg

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/630b24cb270f41a384c7c357ae03f11e)](https://www.codacy.com/app/HanEmile/Heidelberg?utm_source=github.com&utm_medium=referral&utm_content=HanEmile/Heidelberg&utm_campaign=badger)

Display an elliptical Galaxy in Blender using a custom Star density function.

##### Custom Dependencies:
Name | File | Function
--- | --- | ---
Variables | `variables.py` | stores general variables
Constants | `constants.py` | stores constants
Heidelberg | `Heidelberg.py` | stores functions

##### Generate data with:
```
cd clean/
python3 main.py
```

##### Draw Histogram with:
```
cd clean/
python3 draw.py
```

##### Generate 3D-Data:
```
cd clean/3D/
python3 gen_3D.py
```

##### Display 3D-Data in Blender:
```
cd clean/3D/
blender startup.blend --python read_3D.py
```

---
![process](https://github.com/HanEmile/Heidelberg/blob/master/visuals/process.jpg)
---

[Blender](https://www.blender.org),
[Python](https://www.python.org/),
[more...](markdown/notes.md)
