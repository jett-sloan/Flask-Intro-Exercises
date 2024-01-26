"""Basic math operations."""
def string_to_num(x):
    x = int(x)
    return x

def add(a, b):
    """Add a and b."""
    a = string_to_num(a,0)
    b = string_to_num(b,0)
    return str(a + b)

def sub(a, b):
    """Substract b from a."""
    a = string_to_num(a,0)
    b = string_to_num(b,0)
    return str(a - b)


def mult(a, b):
    """Multiply a and b."""
    a = string_to_num(a,0)
    b = string_to_num(b,0)
    return str(a * b)

    

def div(a, b):
    """Divide a by b."""
    a = string_to_num(a,0)
    b = string_to_num(b,0)
    return str(a / b)
    
