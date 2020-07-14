def csvWriter(name,code,reason,header,text):

    data=[name,'@',code,'@',reason,'@',header,'@',text]

    with open ('Result.txt','a') as f:
        for row in data:
            f.write( row )
        f.write('\n')