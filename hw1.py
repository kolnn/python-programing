def get_radius(prompt) :
  r = int(input(prompt))
  return r
def get_circle_area(n) :
  resolve= 3.14*n*n
  return resolve

prompt= '넓이를 구하고자 하는 원의 반지름은?'
result= get_radius(prompt)
print('반지름이', result, '인 원의 넓이 = 3.14*',result,'*',result,'=', end= ' ')
value= get_circle_area(result)
print(value)