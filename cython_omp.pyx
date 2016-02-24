from cython.parallel cimport prange

def xcopy(double[:] a, double[:] c):
    cdef int stream_array_size = a.shape[0]
    cdef int j
    for j in prange(stream_array_size, nogil=True):
        c[j] = a[j]

def xscale(double[:] b, double[:] c, double scalar):
    cdef int stream_array_size = b.shape[0]
    cdef int j
    for j in prange(stream_array_size, nogil=True):
        b[j] = scalar*c[j]

def xadd(double[:] a, double[:] b, double[:] c):
    cdef int stream_array_size = a.shape[0]
    cdef int j
    for j in prange(stream_array_size, nogil=True):
        c[j] = a[j]+b[j]

def xtriad(double[:] a, double[:] b, double[:] c, double scalar):
    cdef int stream_array_size = a.shape[0]
    cdef int j
    for j in prange(stream_array_size, nogil=True):
        a[j] = b[j]+scalar*c[j]
