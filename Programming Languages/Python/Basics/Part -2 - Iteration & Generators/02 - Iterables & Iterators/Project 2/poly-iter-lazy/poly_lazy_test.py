from poly_lazy_iter import Polygon, Polygons
import math


def test_polygon():
    abs_tol = 0.001
    rel_tol = 0.001

    try:
        p = Polygon(2, 10)  # Test Creating Poly with 2 sides
        print(p)
        assert False, ('Creating a Polygon with 2 sides: '
                       'Exception expected, not received')

    except ValueError:
        pass
    ##########
    # TRIANGLE
    ##########
    n = 3
    R = 1
    p = Polygon(n, R)
    assert p.vertices == n, (f'actual: {p.vertices},'
                                   f' expected: {n}')
    assert p.edges == n, f'actual: {p.edges}, expected: {n}'
    assert p.circumradius == R, f'actual: {p.circumradius}, expected: {n}'
    assert p.interior_angle == 60, (f'actual: {p.interior_angle},'
                                    ' expected: 60')

    ##########
    # SQUARE
    ##########
    n = 4
    r = 1
    p = Polygon(n, r)
    assert p.interior_angle == 90, (f'actual: {p.interior_angle}, '
                                    ' expected: 90')
    assert math.isclose(p.area, 2,
                        rel_tol=abs_tol,
                        abs_tol=abs_tol), (f'actual: {p.area},'
                                           ' expected: 2.0')

    assert math.isclose(p.edge_length, math.sqrt(2),
                        rel_tol=rel_tol,
                        abs_tol=abs_tol), (f'actual: {p.edge_length},'
                                           f' expected: {math.sqrt(2)}')

    assert math.isclose(p.perimeter, 4 * math.sqrt(2),
                        rel_tol=rel_tol,
                        abs_tol=abs_tol), (f'actual: {p.perimeter},'
                                           f' expected: {4 * math.sqrt(2)}')

    assert math.isclose(p.apothem, 0.707,
                        rel_tol=rel_tol,
                        abs_tol=abs_tol), (f'actual: {p.perimeter},'
                                           ' expected: 0.707')
    ##########
    # HEXAGON
    ##########
    p = Polygon(6, 2)
    assert math.isclose(p.edge_length, 2,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.apothem, 1.73205,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.area, 10.3923,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.perimeter, 12,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.interior_angle, 120,
                        rel_tol=rel_tol, abs_tol=abs_tol)

    ###########
    # DODECAGON
    ###########
    p = Polygon(12, 3)
    assert math.isclose(p.edge_length, 1.55291,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.apothem, 2.89778,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.area, 27,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.perimeter, 18.635,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.interior_angle, 150,
                        rel_tol=rel_tol, abs_tol=abs_tol)

    #
    p1 = Polygon(3, 10)
    p2 = Polygon(10, 10)
    p3 = Polygon(15, 10)
    p4 = Polygon(15, 100)
    p5 = Polygon(15, 100)

    assert p2 > p1
    assert p2 < p3
    assert p3 != p4
    assert p1 != p4
    assert p4 == p5


if __name__ == '__main__':
    test_polygon()
