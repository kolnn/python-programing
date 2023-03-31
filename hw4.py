def rep_char( nstr) :
    print('-'*nstr )

def announce() :
    name = input('Input his/her name: ')
    msg1 = f'Hello {name},' 
    msg2 = 'Welcome to Seoul,'    
    nstr = len(msg1)if(len(msg1)> len(msg2))else len(msg2)
    rep_char(nstr)
    print(f'{msg1}\n{msg2}')
    rep_char(nstr)
 
announce()