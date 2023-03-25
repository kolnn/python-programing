def get_fixed_price(prompt) :
    d= int(input(prompt))
    a= int(input(ana))
    b= int(input(anb))
    pa= (100*a)/(100 - d)
    print('A 상품의 정가는 ', pa, '원')
    pb= (100*b)/(100 - d)
    print('B 상품의 정가는 ', pb, '원')

prompt='할인율은? '
ana='A 상품의 할인된 가격은? '
anb='B 상품의 할인된 가격은? '
get_fixed_price(prompt)