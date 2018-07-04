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


## Pure Python using loops
```
Function    Best Rate GB/s  Avg time     Min time     Max time
Copy:               0.1     1.814840     1.609796     2.458325
Scale:              0.1     2.446591     2.256223     3.267892
Add:                0.1     3.338355     3.132576     4.177105
Triad:              0.1     4.176528     3.781108     6.688463
```

## Pure Python vectorized
```
Function    Best Rate GB/s  Avg time     Min time     Max time
Copy:              18.5     0.010163     0.008665     0.011690
Scale:              4.3     0.042002     0.037561     0.045683
Add:                6.1     0.042635     0.039430     0.044133
Triad:              5.3     0.049778     0.045096     0.060804
```

## Pure Python using numpy operators
```
Function    Best Rate GB/s  Avg time     Min time     Max time
Copy:               6.4     0.030766     0.024966     0.033695
Scale:              4.9     0.040577     0.032601     0.045119
Add:                8.1     0.035203     0.029726     0.037902
Triad:              6.0     0.042509     0.040308     0.046051
```

## Cython, a reference implementation
```
Function    Best Rate GB/s  Avg time     Min time     Max time
Copy:               0.4     0.477003     0.455385     0.497927
Scale:              0.2     1.006159     0.970726     1.104747
Add:                0.2     1.324193     1.286940     1.365401
Triad:              0.1     1.856771     1.816768     1.924070
```

## Cython, optimized
```
Function    Best Rate GB/s  Avg time     Min time     Max time
Copy:              17.5     0.010997     0.009135     0.015010
Scale:             17.7     0.010571     0.009035     0.014827
Add:               19.8     0.013058     0.012091     0.014440
Triad:             19.7     0.013359     0.012155     0.017599
```

## Pybind11 reference implementation
```
Function    Best Rate GB/s  Avg time     Min time     Max time
Copy:              16.5     0.011123     0.009713     0.013151
Scale:             16.6     0.011012     0.009626     0.012199
Add:               17.4     0.014351     0.013810     0.014967
Triad:             17.6     0.015052     0.013604     0.017705
```
