# Heidelberg

Display a Galaxy in Blender using a custom Star density function.

##### Generate data with:
```
cd clean/
python3 gen.py
```

##### Multiple PCs:
```
cd clean/
./submit_stars.sh <host> <host> <host> ...
```

##### View Data in 3D:
```
cd clean/
blender startup.blend --python mesh.py
```

---
![process](https://github.com/HanEmile/Heidelberg/blob/master/visuals/process1.jpg)

---

[Blender](https://www.blender.org),
[Python](https://www.python.org/),
[more...](markdown/notes.md)
