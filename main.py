
#rotation of current face
def cur_rot(k,decide):
    l=list(d[k])
    temp1=l[2]
    temp2=l[8]
    temp3=l[6]
    if decide==1:
        l[2]=l[0]
        l[8]=temp1
        l[6]=temp2
        l[0]=temp3
        #inner layer
        temp1=l[5]
        temp2=l[7]
        temp3=l[3]
        l[5]=l[1]
        l[7]=temp1
        l[3]=temp2
        l[1]=temp3
    else:
        l[6]=l[0]
        l[8]=temp3
        l[2]=temp2
        l[0]=temp1
        #inner layer
        temp1=l[5]
        temp2=l[7]
        temp3=l[3]
        l[3]=l[1]
        l[7]=temp3
        l[5]=temp2
        l[1]=temp1
    s=''
    for i in range(len(l)):
        s+=l[i]
    d[k]=s




#rotation of other faces

def other_faces_clk(k):
    list1=list(d['FRONT'])
    list2=list(d['DOWN'])
    list3=list(d['BACK'])
    list4=list(d['UP'])
    list5=list(d['RIGHT'])
    list6=list(d['LEFT'])
    if k=='LEFT':
        s1='036'
        s2='258'


        for i in range(len(s1)):
            list2[int(s1[i])]=d['FRONT'][int(s1[i])]
            list3[int(s2[i])]=d['DOWN'][int(s1[len(s1)-1-i])]
            list4[int(s1[i])]=d['BACK'][int(s2[len(s2)-1-i])]
            list1[int(s1[i])]=d['UP'][int(s1[i])]
    elif k=='RIGHT':

        s2='258'
        s1='036'

        for i in range(len(s2)):
            list4[int(s2[i])]=d['FRONT'][int(s2[i])]
            list3[int(s1[i])]=d['UP'][int(s2[len(s2)-1-i])]
            list2[int(s2[i])]=d['BACK'][int(s1[len(s1)-1-i])]
            list1[int(s2[i])]=d['DOWN'][int(s2[i])]
    elif k=='UP':
        s1='012'


        for i in range(len(s1)):
            list3[int(s1[i])]=d['LEFT'][int(s1[i])]
            list5[int(s1[i])]=d['BACK'][int(s1[i])]
            list1[int(s1[i])]=d['RIGHT'][int(s1[i])]
            list6[int(s1[i])]=d['FRONT'][int(s1[i])]
    elif k=='DOWN':
        s1='678'

        for i in range(len(s1)):
            list1[int(s1[i])]=d['LEFT'][int(s1[i])]
            list5[int(s1[i])]=d['FRONT'][int(s1[i])]
            list3[int(s1[i])]=d['RIGHT'][int(s1[i])]
            list6[int(s1[i])]=d['BACK'][int(s1[i])]
    elif k=='FRONT':
        s1='258'
        s2='678'
        s3='012'
        s4='036'

        for i in range(len(s1)):
            list4[int(s2[i])]=d['LEFT'][int(s1[len(s1)-1-i])]
            list5[int(s4[i])]=d['UP'][int(s2[i])]
            list2[int(s3[i])]=d['RIGHT'][int(s4[len(s4)-1-i])]
            list6[int(s1[i])]=d['DOWN'][int(s3[i])]
    elif k=='BACK':
        s1='258'
        s2='678'
        s3='012'
        s4='036'

        for i in range(len(s1)):
            list2[int(s2[i])]=d['LEFT'][int(s4[i])]
            list5[int(s1[i])]=d['DOWN'][int(s2[len(s2)-1-i])]
            list4[int(s3[i])]=d['RIGHT'][int(s1[i])]
            list6[int(s4[i])]=d['UP'][int(s3[len(s3)-1-i])]


    s1=''
    s2=''
    s3=''
    s4=''
    s5=''
    s6=''
    for i in range(len(list1)):
        s1+=list1[i]
        s2+=list2[i]
        s3+=list3[i]
        s4+=list4[i]
        s5+=list5[i]
        s6+=list6[i]
    d['FRONT']=s1
    d['DOWN']=s2
    d['BACK']=s3
    d['UP']=s4
    d['RIGHT']=s5
    d['LEFT']=s6


#anticlockwise other face rotation
def other_faces_aclk(k):
    list1=list(d['FRONT'])
    list2=list(d['DOWN'])
    list3=list(d['BACK'])
    list4=list(d['UP'])
    list5=list(d['RIGHT'])
    list6=list(d['LEFT'])
    if k=='LEFT':
        s1='036'
        s2='258'

        for i in range(len(s1)):
            list4[int(s1[i])]=d['FRONT'][int(s1[i])]
            list3[int(s2[i])]=d['UP'][int(s1[len(s1)-1-i])]
            list2[int(s1[i])]=d['BACK'][int(s2[len(s2)-1-i])]
            list1[int(s1[i])]=d['DOWN'][int(s1[i])]
    elif k=='RIGHT':

        s2='258'
        s1='036'
        for i in range(len(s2)):
            list2[int(s2[i])]=d['FRONT'][int(s2[i])]
            list3[int(s1[i])]=d['DOWN'][int(s2[len(s2)-1-i])]
            list4[int(s2[i])]=d['BACK'][int(s1[len(s1)-1-i])]
            list1[int(s2[i])]=d['UP'][int(s2[i])]
    elif k=='UP':
        s1='012'


        for i in range(len(s1)):
            list1[int(s1[i])]=d['LEFT'][int(s1[i])]
            list5[int(s1[i])]=d['FRONT'][int(s1[i])]
            list3[int(s1[i])]=d['RIGHT'][int(s1[i])]
            list6[int(s1[i])]=d['BACK'][int(s1[i])]
    elif k=='DOWN':
        s1='678'


        for i in range(len(s1)):
            list3[int(s1[i])]=d['LEFT'][int(s1[i])]
            list5[int(s1[i])]=d['BACK'][int(s1[i])]
            list1[int(s1[i])]=d['RIGHT'][int(s1[i])]
            list6[int(s1[i])]=d['FRONT'][int(s1[i])]
    elif k=='FRONT':
        s1='258'
        s2='678'
        s3='012'
        s4='036'

        for i in range(len(s1)):
            list2[int(s3[i])]=d['LEFT'][int(s1[i])]
            list5[int(s4[i])]=d['DOWN'][int(s3[len(s3)-1-i])]
            list4[int(s2[i])]=d['RIGHT'][int(s4[i])]
            list6[int(s1[i])]=d['UP'][int(s2[len(s2)-1-i])]
    elif k=='BACK':
        s1='258'
        s2='678'
        s3='012'
        s4='036'

        for i in range(len(s1)):
            list4[int(s3[i])]=d['LEFT'][int(s4[len(s4)-1-i])]
            list5[int(s1[i])]=d['UP'][int(s3[i])]
            list2[int(s2[i])]=d['RIGHT'][int(s1[len(s1)-1-i])]
            list6[int(s4[i])]=d['DOWN'][int(s2[i])]
    s1=''
    s2=''
    s3=''
    s4=''
    s5=''
    s6=''
    for i in range(len(list1)):
        s1+=list1[i]
        s2+=list2[i]
        s3+=list3[i]
        s4+=list4[i]
        s5+=list5[i]
        s6+=list6[i]

    d['FRONT']=s1
    d['DOWN']=s2
    d['BACK']=s3
    d['UP']=s4
    d['RIGHT']=s5
    d['LEFT']=s6

test_case=int(input())
for z in range(test_case):
    #accept the dictionary
    d={}
    for i in range(6):
        s=input()
        d[s]=input()

    keys_list=list(d.keys())


    #accept the list
    n = int(input())
    arr = input()
    r_list = list(map(str,arr.split(' ')))

    #CUBE rotation
    for i in range(len(r_list)):
        for j in range(len(keys_list)):
            if r_list[i][0]==keys_list[j][0]:
                if(len(r_list[i])==1):
                    cur_rot(keys_list[j],1)
                    other_faces_clk(keys_list[j])
                else:
                    cur_rot(keys_list[j],-1)
                    other_faces_aclk(keys_list[j])
    l=['UP','FRONT','LEFT','RIGHT','BACK','DOWN']
    for i in range(len(l)):
        print(l[i])
        print(d[l[i]])
