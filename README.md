# STREAM-python

This is the STREAM benchmark translated to Python.

See https://github.com/jeffhammond/STREAM or http://www.cs.virginia.edu/stream/ref.html

As-is, pure Python is (expectedly) much slower (see below).  But this allows drop in *tuned* versions.

## C

```
Function    Best Rate MB/s  Avg time     Min time     Max time
Copy:           13111.6     0.013130     0.012203     0.016650
Scale:          12595.3     0.013449     0.012703     0.016654
Add:            13158.6     0.018974     0.018239     0.020934
Triad:          13603.9     0.018147     0.017642     0.018999
```

## Python using loops

```
Function    Best Rate MB/s  Avg time     Min time     Max time
Copy:              97.8     1.719613     1.635737     1.852122
Scale:             68.3     2.479552     2.344122     2.895374
Add:               76.9     3.703595     3.121796     7.633055
Triad:             62.6     3.947682     3.836731     4.174377
```

## Python using `a[:]`

```
Function    Best Rate MB/s  Avg time     Min time     Max time
Copy:           15473.9     0.010647     0.010340     0.011041
Scale:           4163.6     0.039474     0.038428     0.043061
Add:             5522.9     0.044784     0.043455     0.046903
Triad:           3345.9     0.073444     0.071729     0.076359
```

## Python using mostly numpy operations

```
Function    Best Rate MB/s  Avg time     Min time     Max time
Copy:            6170.5     0.027514     0.025930     0.029193
Scale:           4592.4     0.036794     0.034840     0.039469
Add:             7175.9     0.035378     0.033445     0.037374
Triad:           5650.4     0.045002     0.042475     0.051588
```

## Python using loops and Cython

```
Function    Best Rate MB/s  Avg time     Min time     Max time
Copy:             327.6     0.497223     0.488426     0.504358
Scale:            156.0     1.114992     1.025804     1.713871
Add:              192.6     1.341248     1.246336     1.710788
Triad:            131.9     2.561911     1.819383     8.202087
```
