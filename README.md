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

## Python

```
Function    Best Rate MB/s  Avg time     Min time     Max time
Copy:              97.8     1.719613     1.635737     1.852122
Scale:             68.3     2.479552     2.344122     2.895374
Add:               76.9     3.703595     3.121796     7.633055
Triad:             62.6     3.947682     3.836731     4.174377
```
