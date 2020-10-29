from poly_seq_1 import Polygon, Polygons, FIGURES


poly_1 = Polygon(3, 5)
print(poly_1.edge_length)
poly_2 = Polygon(3, 5)
print(poly_1 == poly_2)
poly_3 = Polygon(3, 10)
print(poly_1 == poly_3)
poly_4 = Polygon(5, 5)
print(poly_1 == poly_4)

print('===' * 15)
print('Poly 1 is Greater than Poly 2', '=> ', (poly_1 > poly_2))
print('Poly 1 is Greater than Poly 3', '=> ', (poly_1 > poly_3))
print('Poly 3 is Greater than Poly 4', '=> ', (poly_3 > poly_4))
print('Poly 1 is Greater than Poly 4', '=> ', (poly_1 > poly_4))
print('Poly 4 is Greater than Poly 1, 2 & 3?', '=> ', (poly_4 > poly_1 and
                                                       poly_4 > poly_2 and
                                                       poly_4 > poly_3))

poly_1.edges = 4
print(poly_1)
print(poly_1.edge_length)
print(poly_1.R)
print(poly_1)
print(poly_1.edge_length)

poly_1 = Polygon(4, 5)
print(poly_1)
print(poly_1.edge_length)
print(poly_1.interior_angle)
print(poly_1.perimeter)
print(poly_1.apothem)
print(poly_1.area)

print(poly_1.get_type())
print(poly_1.__name__)
print(poly_1.__dict__)

seq_poly = Polygons(5, 5)
print(seq_poly.polygons)
for i in seq_poly:
    print(i)
print(len(seq_poly))

poly_2 = Polygon(4, 5)
print(poly_2.__name__)

seq_poly2 = Polygons(10, 10)
for i in seq_poly2:
    print(i.name, '>>> ', i)


print(seq_poly[1])

print(len(seq_poly))
print('==='*15)
print(seq_poly[:])
#
# print(any(x.name for x in seq_poly))
print('sQuAre' in seq_poly)
print('==='*15)
print('==='*15)
print(seq_poly.max_area_per_ratio)
