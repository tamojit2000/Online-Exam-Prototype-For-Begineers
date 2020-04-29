print'\n\t\tEXAM TAKING SOFTWARE\n\n'
print'\t\t====================\n\n\n'
name=raw_input('Please Enter Your Name - ').title()
print
choice=raw_input('(Do you need the instructions ? (Y/N)) ')
if choice.upper()=='Y':
    
    print'''
    INSTRUCTIONS
    ____________


    1. This is MCQ type CBT exam.
    2. One or more option may be correct.
    3. Examinee just enter the correct option.
    4. There are two turns of answering, if we want to rectify the answer then
        changes need to be done in second turn as final answer, otherwise it may be left empty.
    5. One can skip the question just pressing enter.
    6. There will be only one chance to answer, question once answered cannot be changed.
    7. There is Marksheet arranged for your view with all your entries an the answerkey.
    8. Your Score remains stored in memory with date,time and name.
    9. Extra time if taken leads to deduction of one forth for a min.
    10. Partial marking scheme is there as Rule of JEE Advanced.

    
    -------------------------------------X----------------------------------------------


    '''
print


################################
def create_set(d):
    ld=len(d)
    l=[x for x in range(1,ld+1)]
    import random
    za=[]
    while len(l)>0:
        a=random.randint(0,len(l)-1)
        za.append(l[a])
        del  l[a]
    return za

def give_datetime():
    import datetime
    a=datetime.datetime.now().date()
    b=datetime.datetime.now().time()
    return [a,b]

def time_diff(a,b):
    #a,b are time objects
    x=a.hour-b.hour
    y=a.minute-b.minute
    z=a.second-b.second
    q=(x*60)+y+(z/60)
    return q

def option_rearrange(x):
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

def multiple_check(x,y):
    b=list(y)
    b.sort()
    z=0
    for i in x:
        if i in b:
            z+=1
        if i not in b:
            z=0
            break
    return z
        

#################################

print'\n\n\t\tYOUR EXAM STARTS NOW.'
raw_input('\n\t\tPRESS ENTER TO START YOUR EXAM.\n')

print'\n\n\n\n\n\n\n'
          
a=open('question_file','r')   # name of the file in which whole dict dumped
import pickle
question_dictionary=pickle.load(a)#
a.close
question_set=create_set(question_dictionary)#
a=open('answer_file','r')  # name of file answer key dumped
answer_key=pickle.load(a)#
a.close()
marks=0.0

date1=give_datetime()[0]
time1=give_datetime()[1]

print '\n\tStarting Time - ',time1,'\t\tStarting Date - ',date1
print

alloted_time=len(question_dictionary)*(0.5)

print'\n\n\t\tYour alloted time is ',alloted_time,' min.\n\t\tNo of questions ',len(question_dictionary),'\n\n'

print'=======================X=======================\n'
print'\n\n\n\n\n\n\n'


response={}
for i in range(len(question_dictionary)):
    print '\nQUESTION ',i+1,'))','\n'
    print question_dictionary[question_set[i]]
    print
    response[question_set[i]]=raw_input('\tYour Answer - ').upper()
    response2=raw_input('\tYour Final Answer - ').upper()
    if response2!='':
        response[question_set[i]]=response2
    response[question_set[i]]=option_rearrange(response[question_set[i]])     #only options are taken by option_rearrange function
    
    
    if len(response[question_set[i]])>1:     
        aqss=multiple_check(response[question_set[i]],answer_key[question_set[i]].strip())
        if aqss>0 and response[question_set[i]]!=answer_key[question_set[i]].strip():
            marks+=0.25*aqss
        if aqss>0 and response[question_set[i]]==answer_key[question_set[i]].strip():
            marks+=1
        if aqss==0:
            marks-=0.25
    elif response[question_set[i]]==answer_key[question_set[i]].strip() and len(response[question_set[i]])==1:
        marks+=1
    elif response[question_set[i]]=='':
        marks+=0
    else:
        marks-=0.25
    #print marks
    #print response[question_set[i]],'tat'
    #print answer_key[question_set[i]].rstrip()
    print'\n=======================X==========================\n'
print'\n--------------------------------------------end--------------------------------\n'
print('\n\nEXAM COMPLETE PRESS ENTER TO VIEW YOUR SCORE')

date2=give_datetime()[0]
time2=give_datetime()[1]

print'\n\n\t','Ending Time - ',time2,'\t\tEnding Date - ',date2
print'\n'

time_taken=time_diff(time2,time1)
time_error=0
if time_taken>alloted_time:
    time_error=time_taken-alloted_time
    
if time_error>0:
    marks-=(time_error*0.25)

raw_input()

Nm=name.replace(' ','_')
z=open(Nm+'_score.txt','a')
z.write('\n-----------------------------------X----------------------------\n'+'\t\tEXAM SUMMARY\n')
print
print'\n\tYour Name - ',name
z.write('\n\tYour Name - '+str(name))
print'\n\tStarting Date: ',str(date1),'\t\tStarting Time- ',str(time1)
z.write('\n\tStarting Date: '+str(date1)+'\t\tStarting Time- '+str(time1))
print'\n\tEnding Date: ',str(date2),'\t\tEnding Time- ',str(time2)
z.write('\n\tEnding Date: '+str(date2)+'\t\tEnding Time- '+str(time2))

if time_error>0:
    print'\n\tExtra Time Taken - ',time_error,' min. '
    z.write('\n\tExtra Time Taken - '+str(time_error)+' min. ')

print'\n\tYour marks - ',marks,'out of',len(question_dictionary)
z.write('\n\tYour marks - '+str(marks)+' out of '+str(len(question_dictionary)))
if time_error>0:
    print '\n\n\tExtra time taken so deduction of ',time_error,' marks.\n'

print'\n\n\t\tMARKSHEET\n'
z.write('\n\tMARKSHEET\n')
print '  YOUR RESPONSE\t\tCORRECT KEY\t\tACHIVEMENT\n'
z.write('  YOUR RESPONSE\t\tCORRECT KEY\t\tACHIVEMENT\n')

for i in range(len(question_dictionary)):
    print
    print '\n',i+1,'>',
    z.write('\n'+str(i+1)+'>')
    if response[question_set[i]].strip()==answer_key[question_set[i]].strip() and len(response[question_set[i]].strip())==1:
        aqs='+1'
    elif response[question_set[i]].strip()=='':
        aqs='Zero'
        response[question_set[i]]='~'
    elif len(response[question_set[i]].strip())>1:
        aqss=multiple_check(response[question_set[i]],answer_key[question_set[i]].strip())
        if aqss>0 and response[question_set[i]]!=answer_key[question_set[i]].strip():
            aqs=str(0.25*aqss)
        if aqss>0 and response[question_set[i]]==answer_key[question_set[i]].strip():
            aqs='+1'
        if aqss==0:
            aqs='-0.25'
        
    elif response[question_set[i]].strip()!=answer_key[question_set[i]].strip() and len(response[question_set[i]].strip())==1:
        aqs='-0.25'

    print '\t\t',response[question_set[i]].strip(),'\t\t',answer_key[question_set[i]].strip(),'\t\t',aqs
    z.write('\t\t'+str(response[question_set[i]].strip())+'\t\t'+str(answer_key[question_set[i]].strip())+'\t\t'+str(aqs))
print "\n '~' denotes that no option was declared."
if time_error>0:
    print '\n\n\tExtra time taken so deduction of ',time_error*0.25,' marks.\n'

z.write("\n '~' denotes that no option was declared.")
if time_error>0:
    z.write('\nExtra time taken so negative marking of '+str(time_error*0.25)+' marks')
z.write('\n----------------------------------X-----------------------------------\n')
z.close()
print'\n\n======================='
print'\n\nBy Tamojit....'
print'\n\n=======================\n'
raw_input('end')    
    
