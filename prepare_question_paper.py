import pickle
d={}
a=open('question_template.txt','r')
b=a.read()
a.close()
c=1
b=b.split('!@#')
for i in b:
    d[c]=i
    c=c+1
    
#dumping    







   
e=open('question_file','w')   
pickle.dump(d,e)
e.close()
#dumping the whole dictionary
raw_input('\nQUESTION PAPER LOADING COMPLETE')
