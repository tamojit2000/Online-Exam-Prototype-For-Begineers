
def option_rearrange2(x):
    z=''
    if 'A' in x:
        z=z+'A'
    if 'B' in x:
        z=z+'B'
    if 'C' in x:
        z=z+'C'
    if 'D' in x:
        z=z+'D'
    
    return z


import pickle
d={}
a=open('answer_template.txt','r')
b=a.read()
a.close()
c=1
b=b.split('!@#')
for i in b:
    i=i.upper()
    i=option_rearrange2(i)
    d[c]=i
    c=c+1
    
#dumping    







   
e=open('answer_file','w')   
pickle.dump(d,e)
e.close()
#dumping the whole dictionary
raw_input('\nANSWER SHEET LOADING COMPLETE')
