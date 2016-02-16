def xcopy(a, c):
    STREAM_ARRAY_SIZE = len(a)
    for j in range(STREAM_ARRAY_SIZE):
        c[j] = a[j]

def xscale(b, c, scalar):
    STREAM_ARRAY_SIZE = len(b)
    for j in range(STREAM_ARRAY_SIZE):
        b[j] = scalar*c[j]

def xadd(a, b, c):
    STREAM_ARRAY_SIZE = len(a)
    for j in range(STREAM_ARRAY_SIZE):
        c[j] = a[j]+b[j]

def xtriad(a, b, c, scalar):
    STREAM_ARRAY_SIZE = len(a)
    for j in range(STREAM_ARRAY_SIZE):
        a[j] = b[j]+scalar*c[j]
