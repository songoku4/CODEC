def data_set_test(code):
    k=0
    a=0
    for i in range(len(code)):
        if code[i]=='(' or code[i]=='{' or code[i]=='[':
            k=i
    tokens=code.split(' ')
    for i in tokens:
        if 'while' in tokens:
            a=code.find('while')
        elif 'if' in tokens:
            a=code.find('if')
        elif 'elif' in tokens:
            a=code.find('elif')
        elif 'else' in tokens:
            a=code.find('else')
        elif 'for' in tokens:
            a=code.find('for')
        elif 'try' in tokens:
            a=code.find('try')
        elif 'except' in tokens:
            a=code.find('except')
    if a<k:
        r='test_passed'
    else:
        r='test_failed'
def string_test(code):
    k=0
    a=0
    b=0
    for i in range(len(code)):
        if code[i]=='"' or code[i]=="'" or code[i]=='"""':
            k=i
    tokens=code.split(' ')
    for i in tokens:
        if 'while' in tokens:
            a=code.find('while')
        elif 'if' in tokens:
            a=code.find('if')
        elif 'elif' in tokens:
            a=code.find('elif')
        elif 'else' in tokens:
            a=code.find('else')
        elif 'for' in tokens:
            a=code.find('for')
        elif 'try' in tokens:
            a=code.find('try')
        elif 'except' in tokens:
            a=code.find('except')
    if a<k:
        r='test_passed'
    else:
        r='test_failed'

def complex_loop_test(code):
    k=0
    a=0
    for i in range(len(code)):
        if code[i]=='[':
            k=i
    tokens=code.split(' ')
    for i in tokens:
        if 'while' in tokens:
            a=code.find('while')
        elif 'if' in tokens:
            a=code.find('if')
        elif 'elif' in tokens:
            a=code.find('elif')
        elif 'else' in tokens:
            a=code.find('else')
        elif 'for' in tokens:
            a=code.find('for')
        elif 'try' in tokens:
            a=code.find('try')
        elif 'except' in tokens:
            a=code.find('except')
    if a<k:
        r='test_passed'
    else:
        r='test_failed'
        
def complete_check(code):
    marks=0

    if complex_loop_test(code)=='test_passed':
        marks+=1

    if string_test(code)=='test_passed':
        marks+=1

    if data_set_test(code)=='test_passed':
        marks+=1
    return marks
def only_keyword(code):
    tokens=code.split(' ')
    for i in tokens:
        r='only keyword'
        if 'while' in tokens:
            return r
        elif 'if' in tokens:
            return r
        elif 'elif' in tokens:
            return r
        elif 'else' in tokens:
            return r
        elif 'for' in tokens:
            return r
        elif 'try' in tokens:
            return r
        elif 'except' in tokens:
            return r
        

def indent_block_test_main(x):
    try:
        for i in range(len(x)):
            code=x[i]
            if code[-1]==':':
                pass
            elif complete_check(code)==3:
                x[i]=code+':'
            elif only_keyword(code)=='only keyword':
                x[i]=code+':'

            else :
                pass
    except:
        pass




