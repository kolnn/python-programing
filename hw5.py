def read_single_digit(prompt) :
    a= str(prompt)
    if a == '0' :
        a = '영'
    elif a == '1' :
        a = '일'
    elif a == '2' :
        a = '이'
    elif a == '3' :
        a = '삼'
    elif a == '4' :
        a = '사'
    elif a == '5' :
        a = '오'
    elif a == '6' :
        a = '육'
    elif a == '7' :
        a = '칠'
    elif a == '8' :
        a = '팔'
    else :
        a = '구'
    return a

def read_number(prompt) :
    h = prompt //  100
    t = (prompt // 10) % 10
    n = prompt % 10
    hs = read_single_digit(h)
    ts = read_single_digit(t)
    ns = read_single_digit(n)
    return hs + ts + ns
    
prompt = int(input('세 자리 정수 입력: '))
answer = read_number(prompt)
print(answer)