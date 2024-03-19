from product import Product

def test_calculate_total():
    pdt = Product("x",12,2)
    result = pdt.calculate_total()
    assert(result) == 24

def test_zero_quantity():
    pdt = Product("x",0,1)
    try:
        pdt.calculate_total()
        return False, f"No ValueError raised for input: {pdt}"
    except ValueError:
        return f"ValueError correctly raised for input: {pdt}"

def test_negative_quantity():
    pdt = Product('x',-1,5)
    try:
        pdt.calculate_total()
        return False, f"No ValueError raised for input: {pdt}"
    except ValueError:
        return f"ValueError correctly raised for input: {pdt}"

def test_negative_price():
    pdt = Product('x',9,-1)
    try:
        pdt.calculate_total()
        return False, f"No ValueError raised for input: {pdt}"
    except ValueError:
        return f"ValueError correctly raised for input: {pdt}"



print(test_calculate_total())
print(test_negative_price())
print(test_negative_quantity())
print(test_zero_quantity())