

from timeit import Timer

if __name__ == '__main__':

    def diag_gen(length):
        points = [(0.25, 0.25)]
        for _ in range(1, length + 1):
            points.append((points[-1][0] + 1, points[-1][1]))
            points.append((points[-1][0], points[-1][1] + 1))
        points.append((points[-1][0], points[-1][1] + 1))
        points.append((points[-1][0] - 1, points[-1][1]))
        points.append((points[-1][0], points[-1][1] - 1))
        for _ in range(1, length):
            points.append((points[-1][0] - 1, points[-1][1]))
            points.append((points[-1][0], points[-1][1] - 1))
        points.append((0.25, 0.25))

        return points

    def test_diag_gen(points):
        res = 0
        for point in points:
            assert abs(point[0] + point[1] - res) <= 1
            res = point[0] + point[1]
        assert points[0] == points[-1]
    test_diag_gen(diag_gen(200));

    def area(points):
        acc = 0
        for i in xrange(len(points) - 1):
            acc += points[i][0] * points[i + 1][1] - points[i + 1][0] * points[i][1]
        return abs(acc) / 2

    assert area(diag_gen(32)) == 64.0
    assert area([(-x, -y) for x, y in diag_gen(32)]) == 64.0

    regpoly = diag_gen(2*10**5)

    ta = Timer('area(regpoly)', 'from __main__ import area, regpoly')
    print "ta:\t", round(min(ta.repeat(3, 10)), 6), "s"

    try:
        import numpy
        import numpy as np
        np_arr = numpy.array(regpoly, dtype=numpy.float64)


        def area_np(arr):
            return abs((arr[:-1,0] * arr[1:,1] - arr[:-1,1] * arr[1:,0]).sum()) * 0.5
        assert area_np(np_arr) == 4.*10**5

        regpoly_np = numpy.array(diag_gen(2*10**5))

        tanp = Timer('area_np(regpoly_np)', 'from __main__ import area_np, regpoly_np')
        print "tanp:\t", round(min(tanp.repeat(3, 10)), 6), "s"
    except Exception, e:
        print "No numpy :("
        print e, type(e)

