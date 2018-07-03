# STREAM-python

This is the STREAM benchmark in Python.

See https://github.com/jeffhammond/STREAM or http://www.cs.virginia.edu/stream/ref.html

As-is, pure Python is (expectedly) much slower (see below).  But this allows drop in *tuned* versions.

# How to Use

To build, first modify the compilers in `setup.py`.  Then,

```
python3 setup.py build_ext --inplace
```

To run all tests execute

```
python3 stream.py
```

# Example Output

## Pybind11 reference implementation
```
Function    Best Rate GB/s  Avg time     Min time     Max time
Copy:              16.4     0.010284     0.009751     0.012376
Scale:             16.8     0.010431     0.009506     0.011880
Add:               18.6     0.013835     0.012874     0.014829
Triad:             18.9     0.013772     0.012685     0.015681
```

## Pure Python using numpy operators
```
Function    Best Rate GB/s  Avg time     Min time     Max time
Copy:               6.0     0.029801     0.026692     0.032265
Scale:              4.0     0.040900     0.039674     0.042740
Add:                7.3     0.035303     0.032998     0.037195
Triad:              6.2     0.039500     0.038498     0.042056
```

## Cython, optimized
```
Function    Best Rate GB/s  Avg time     Min time     Max time
Copy:              17.0     0.009997     0.009432     0.012239
Scale:             16.5     0.010243     0.009689     0.012858
Add:               18.1     0.013701     0.013236     0.014630
Triad:             18.7     0.013168     0.012830     0.013439
```

## Pure Python using loops
```
Function    Best Rate GB/s  Avg time     Min time     Max time
Copy:               0.1     1.581430     1.574763     1.609038
Scale:              0.1     2.207595     2.189903     2.265473
Add:                0.1     3.129348     3.067971     3.382861
Triad:              0.1     3.874135     3.701047     5.069734
```

## Pure Python vectorized
```
Function    Best Rate GB/s  Avg time     Min time     Max time
Copy:              18.8     0.009319     0.008493     0.010320
Scale:              4.7     0.035854     0.034254     0.036897
Add:                6.8     0.037315     0.035284     0.039581
Triad:              5.8     0.043582     0.041380     0.044829
```

## Cython, a reference implementation
```
Function    Best Rate GB/s  Avg time     Min time     Max time
Copy:               0.4     0.460282     0.447972     0.476385
Scale:              0.2     0.977194     0.950572     1.003137
Add:                0.2     1.282081     1.262743     1.335770
Triad:              0.1     1.791226     1.752691     1.867340
```
