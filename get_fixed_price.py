d = 0
def get_fixed_price(percent) : 
    global d
    d = percent
def A(A) : 
    return (100*A)/(100 - d)
def B(B) :
    return (100*B)/(100 - d)