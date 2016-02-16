import numpy as np
from time import time

mysecond = time


def checkSTREAMresults():
    pass


def checktick():
    M = 20
    timesfound = np.empty((M,))

    for i in range(M):

        t1 = mysecond()
        t2 = mysecond()
        while (t2 - t1) < 1e-6:
            t2 = mysecond()
        t1 = t2
        timesfound[i] = t1

    minDelta = 1000000
    Delta = (1e6 * np.diff(timesfound)).astype(np.int)
    minDelta = Delta.min()
    return minDelta


def main(args):

    STREAM_ARRAY_SIZE = args.STREAM_ARRAY_SIZE
    NTIMES = args.NTIMES
    OFFSET = args.OFFSET
    STREAM_TYPE = args.STREAM_TYPE

    HLINE = "-------------------------------------------------------------"
    MIN = min
    MAX = max

    a = np.empty((STREAM_ARRAY_SIZE+OFFSET,), dtype=STREAM_TYPE)
    b = np.empty((STREAM_ARRAY_SIZE+OFFSET,), dtype=STREAM_TYPE)
    c = np.empty((STREAM_ARRAY_SIZE+OFFSET,), dtype=STREAM_TYPE)

    avgtime = np.zeros((4,), dtype='double')
    maxtime = np.zeros((4,), dtype='double')
    FLT_MAX = np.finfo('single').max
    mintime = np.array([FLT_MAX, FLT_MAX, FLT_MAX, FLT_MAX])

    label = ["Copy:      ", "Scale:     ", "Add:       ", "Triad:     "]

    tbytes = np.array([2 * np.nbytes[STREAM_TYPE] * STREAM_ARRAY_SIZE,
                       2 * np.nbytes[STREAM_TYPE] * STREAM_ARRAY_SIZE,
                       3 * np.nbytes[STREAM_TYPE] * STREAM_ARRAY_SIZE,
                       3 * np.nbytes[STREAM_TYPE] * STREAM_ARRAY_SIZE],
                      dtype='double')

    quantum = 0
    BytesPerWord = 0
    times = np.zeros((4, NTIMES))

    # --- SETUP --- determine precision and check timing ---
    print(HLINE)
    print("pySTREAM version 0.01")
    print(HLINE)
    BytesPerWord = np.nbytes[STREAM_TYPE]
    print("This system uses %d bytes per array element." % BytesPerWord)

    print(HLINE)
    print("Array size = %d (elements), Offset = %d (elements)" %
          (STREAM_ARRAY_SIZE, OFFSET))
    print("Memory per array = %.1f MiB (= %.1f GiB)." %
          (BytesPerWord * (STREAM_ARRAY_SIZE / 1024.0 / 1024.0),
           BytesPerWord * (STREAM_ARRAY_SIZE / 1024.0 / 1024.0 / 1024.0)))
    print("Total memory required = %.1f MiB (= %.1f GiB)." %
          (3.0 * BytesPerWord * (STREAM_ARRAY_SIZE / 1024.0 / 1024.0),
           3.0 * BytesPerWord * (STREAM_ARRAY_SIZE / 1024.0 / 1024.0 / 1024.)))
    print("Each kernel will be executed %d times." % NTIMES)
    print(" The *best* time for each kernel (excluding the first iteration)")
    print(" will be used to compute the reported bandwidth.")

    # Get initial value for system clock.
    for j in range(STREAM_ARRAY_SIZE):
        a[j] = 1.0
        b[j] = 2.0
        c[j] = 0.0

    print(HLINE)

    quantum = checktick()
    if quantum >= 1:
        print("Your clock granularity/precision appears to be " +
              "%d microseconds." % quantum)
    else:
        print("Your clock granularity appears to be "
              "less than one microsecond.")
        quantum = 1

    t = mysecond()
    for j in range(STREAM_ARRAY_SIZE):
        a[j] = 2.0 * a[j]
    t = 1.0e6 * (mysecond() - t)

    print("Each test below will take on the order"
          " of %d microseconds." % int(t))
    print("   (= %d clock ticks)" % int(t/quantum))
    print("Increase the size of the arrays if this shows that")
    print("you are not getting at least 20 clock ticks per test.")

    print(HLINE)

    print("WARNING -- The above is only a rough guideline.")
    print("For best results, please be sure you know the")
    print("precision of your system timer.")
    print(HLINE)

    # --- MAIN LOOP --- repeat test cases NTIMES times ---

    test = 'strange'
    scalar = 3.0
    for k in range(NTIMES):

        if test == 'reference':
            times[0][k] = mysecond()
            for j in range(STREAM_ARRAY_SIZE):
                c[j] = a[j]
            times[0][k] = mysecond() - times[0][k]

            times[1][k] = mysecond()
            for j in range(STREAM_ARRAY_SIZE):
                b[j] = scalar*c[j]
            times[1][k] = mysecond() - times[1][k]

            times[2][k] = mysecond()
            for j in range(STREAM_ARRAY_SIZE):
                c[j] = a[j]+b[j]
            times[2][k] = mysecond() - times[2][k]

            times[3][k] = mysecond()
            for j in range(STREAM_ARRAY_SIZE):
                a[j] = b[j]+scalar*c[j]
            times[3][k] = mysecond() - times[3][k]

        if test == 'vector':
            times[0][k] = mysecond()
            c[:] = a[:]
            times[0][k] = mysecond() - times[0][k]

            times[1][k] = mysecond()
            b[:] = scalar * c[:]
            times[1][k] = mysecond() - times[1][k]

            times[2][k] = mysecond()
            c[:] = a[:] + b[:]
            times[2][k] = mysecond() - times[2][k]

            times[3][k] = mysecond()
            a[:] = b[:] + scalar * c[:]
            times[3][k] = mysecond() - times[3][k]

        if test == 'strange':
            times[0][k] = mysecond()
            c = a.copy()
            times[0][k] = mysecond() - times[0][k]

            times[1][k] = mysecond()
            c *= scalar
            b = c.copy()
            times[1][k] = mysecond() - times[1][k]

            times[2][k] = mysecond()
            c = a + b
            times[2][k] = mysecond() - times[2][k]

            times[3][k] = mysecond()
            c *= scalar
            a = b + c
            times[3][k] = mysecond() - times[3][k]

    # --- SUMMARY ---

    for k in range(1, NTIMES):  # note -- skip first iteration
        for j in range(4):
            avgtime[j] = avgtime[j] + times[j][k]
            mintime[j] = MIN(mintime[j], times[j][k])
            maxtime[j] = MAX(maxtime[j], times[j][k])

    print("Function    Best Rate MB/s  Avg time     Min time     Max time")
    for j in range(4):
        avgtime[j] = avgtime[j] / float(NTIMES-1)

        print("%s%12.1f  %11.6f  %11.6f  %11.6f" %
              (label[j],
               1.0e-06 * tbytes[j]/mintime[j],
               avgtime[j],
               mintime[j],
               maxtime[j]))

    print(HLINE)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='pystream')
    parser.add_argument('--STREAM_ARRAY_SIZE', action='store',
                        dest='STREAM_ARRAY_SIZE', type=int,
                        default=10000000)
    parser.add_argument('--NTIMES', action='store', dest='NTIMES', type=int,
                        default=10)
    parser.add_argument('--OFFSET', action='store', dest='OFFSET', type=int,
                        default=0)
    parser.add_argument('--STREAM_TYPE', action='store', dest='STREAM_TYPE',
                        default='double')

    args = parser.parse_args()
    main(args)
    checktick()
