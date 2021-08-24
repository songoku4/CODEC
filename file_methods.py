def save(x,path,name):
    f=open(path+'\\'+name+'( rectified).py','w')
    for i in range(len(x)):
        print (type(x[i]))
        f.write(x[i]+'\n')
    f.close()
