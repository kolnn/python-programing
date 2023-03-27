import get_fixed_price as f

per = int(input("할인율은? "))
f.get_fixed_price(per)

A = int(input('A 상품의 할인된 가격은?'))
B = int(input("B 상품의 할인된 가격은?"))
print('A 상품의 정가는',f.A(A),'원')
print('B 상품의 정가는',f.B(B),'원')
