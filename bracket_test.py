def search(code):
    for i in range(len(code)):
        if code[i]=='=':
            return i

def autocorrect(x):
    for i in range(len(x)):
        code=x[i]
        #indetation
        print (code)
        if '(' in code and ')' not in code and code[-1]==':':
            c = code[0:len(code)-1]
            d = code[-1]
            x[i]= c+')'+d
        
        elif ')' in code and '(' not in code and code[-1]==':':
            for i in range(len(code)):
                try:
                    if (code[i]+code[i+1])=='in':
                        part1=code[0:i+3]
                        part2=code[i+2:len(code)]
                        x[i]=part1+'(' + part2                   
                except:
                    pass
    for i in range(len(x)):
        code=x[i]
        #indetation
        print (code)
        if '[' in code and ']' not in code and code[-1]==':':
            c = code[0:len(code)-1]
            d = code[-1]
            x[i]= c+']'+d
        
        elif ']' in code and '[' not in code and code[-1]==':':
            for i in range(len(code)):
                try:
                    if (code[i]+code[i+1])=='in':
                        part1=code[0:i+3]
                        part2=code[i+2:len(code)]
                        x[i]=part1+'[' + part2                   
                except:
                    pass
    for i in range(len(x)):
        code=x[i]
        #indetation
        print (code)
        if '{' in code and '}' not in code and code[-1]==':':
            c = code[0:len(code)-1]
            d = code[-1]
            x[i]= c+'}'+d
        
        elif '}' in code and '{' not in code and code[-1]==':':
            for i in range(len(code)):
                try:
                    if (code[i]+code[i+1])=='in':
                        part1=code[0:i+3]
                        part2=code[i+2:len(code)]
                        x[i]=part1+'{' + part2                   
                except:
                    pass
        #general
        elif '(' in code and ')' not in code :
            x[i]= code+')'

        elif ')' in code and '(' not in code :
            part1=code[0:search(code)+1]
            part2=code[search(code):len(code)]
            x[i]=part1+'('+part2    
        elif '[' in code and ']' not in code :
            x[i]= code+']'

        elif ']' in code and '[' not in code:
            part1=code[0:search(code)+1]
            part2=code[search(code):len(code)]
            x[i]=part1+'['+part2    

        elif '{' in code and '}' not in code :
            x[i]= code+'}'

        elif '}' in code and '{' not in code:
            part1=code[0:search(code)+1]
            part2=code[search(code):len(code)]
            x[i]=part1+'{'+part2      
