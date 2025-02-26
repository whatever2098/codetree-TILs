product_name, product_code = input().split()
product_code = int(product_code)

class Product:
    def __init__(self, product_name, product_code):
        self.pn = product_name
        self.pc = product_code

product1 = Product("codetree", 50)
product2 = Product(product_name, product_code)

print("product", product1.pc, "is", product1.pn)
print("product", product2.pc, "is", product2.pn)