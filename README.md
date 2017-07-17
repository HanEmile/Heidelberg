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

### Workflow:

- on local:
  - modify gen.py
  - `$ git add gen.py`
  - `$ git commit -m "..."`
  - `$ git push`
- on cosmo5:
  - `$ git pull`
  - `$ ./submit_stars.sh freie_rechner.dat`
- (optional) on remote:
  - `$ top`
- on local:
  - `$ ./get_results.sh <name><x>`
  - modify mesh.py to use the name x data
  - `$ blender startup.blend --python mesh.py`

### Workflow (kang):

- on local:
  - modify gen.py
  - `$ git add gen.py`
  - `$ git commit -m "..."`
  - `$ git push`
- on cosmo5:
  - `$ git pull`
  - `$ ./submit_stars_12core.sh kang`
- (optional) on kang:
  - `$ top`
- on local:
  - `$ ./get_results_kang.sh kang<x>`
  - modify mesh.py to use the kang<x> data
  - `$ blender startup.blend --python mesh.py`

---
![process](https://github.com/HanEmile/Heidelberg/blob/master/visuals/process1.jpg)
---

[Blender](https://www.blender.org),
[Python](https://www.python.org/),
[more...](markdown/notes.md)

###### THE END
