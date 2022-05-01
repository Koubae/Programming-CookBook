import json 

class ComplexEncoder(json.JSONEncoder):
    def default(self, z):
        if isinstance(z, complex):
            return (z.real, z.imag)
        else:
            return super().default(z)

print(json.dumps(2 + 5j, cls=ComplexEncoder))