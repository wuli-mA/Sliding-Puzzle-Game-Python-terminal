import random
def print_map(matrix): #To print a randomly disordered matrix.
    random.shuffle(matrix)
    num_of_inverse=0
    try:                #To test whether the 3*3 matrix is solvable.
        if len(matrix)==9: 
            for num in matrix:
                for i in range(matrix.index(num)):
                    if matrix[i]>num:
                        num_of_inverse+=1
            if num_of_inverse%2!=0:
                random.shuffle(matrix)
    except:             #To test whether the 4*4 matrix is solvable.
        if len(matrix)==16: 
            y=(matrix.index(0))//4
            for num in matrix:
                for i in range(matrix.index(num)):
                    if matrix[i]>num:
                        num_of_inverse+=1
            if (num_of_inverse + y)%2==0:
                random.shuffle(matrix)
    for num in matrix:
        num=int(float(num))
        if (matrix.index(num)+1)%(len(matrix)**0.5)==0: #The element is located on the right end.
            if num==0:
                print('  ')
            else:
                print("%2d"%num)
        else:
            if num==0:
                print('  ',end=' ')
            else:
                print("%2d"%num,end=' ')
 
def find_x8(t):   #This function is to find the x-coordinate of the white space in 3-dimension matrix.
    h=(t+1)%3
    if h==0:
        H="right"
    if h==1:
        H="left"
    if h==2:
        H='middle'
    return H

def find_x15(t):   #This function is to find the x-coordinate of the white space in 4-dimension matrix.
    h=(t+1)%4
    if h==0:
        H="right"
    if h==1:
        H="left"
    if h==2:
        H='middle'
    if h==3:
        H="middle"
    return H
def find_y8(t):    #This function is to find the y-coordinate of the white space in 3-dimension matrix.
    v=t//3
    if v==0:
        V="up"
    if v==1:
        V="middle"
    if v==2:
        V="down"
    return V

def find_y15(t):   #This function is to find the x-coordinate of the white space in 4-dimension matrix.
    v=t//4
    if v==0:
        V="up"
    if v==3:
        V="down"
    if v==1:
        V="middle"
    if v==2:
        V="middle"
    return V

def action8(V,H,matrix,u,d,l,r,t,notice):
    notice="Enter your move ("
    if H!="right":
        notice+="left:"+r+','
    if H!='left':
        notice+="right:"+l+','
    if V!= "down":
        notice+="up:"+d+','
    if V!="up":
        notice+="down:"+u+','
    notice+="):"
    move=input(notice)
    if move==u and V!="up":
        temp=matrix[t-3]
        matrix[t-3]=0
        matrix[t]=temp
        t-=3
    elif move==d and V!="down":
        temp=matrix[t+3]
        matrix[t+3]=0
        matrix[t]=temp
        t+=3
    elif move==l and H!="left":
        temp=matrix[t-1]
        matrix[t-1]=0
        matrix[t]=temp
        t-=1
    elif move==r and H!="right":
        temp=matrix[t+1]
        matrix[t+1]=0
        matrix[t]=temp
        t+=1
    for num in matrix:
        num=int(float(num))
        if (matrix.index(num)+1)%(len(matrix)**0.5)==0:
            if num==0:
                print('  ')
            else:
                print("%2d"%num)
        else:
            if num==0:
                print('  ',end=' ')
            else:
                print("%2d"%num,end=' ')

def action15(V,H,matrix,u,d,l,r,t,notice):
    notice="Enter your move ("
    if H!="right":
        notice+="left:"+r+','
    if H!='left':
        notice+="right:"+l+','
    if V!= "up":
        notice+="down:"+u+','
    if V!="down":
        notice+="up:"+d+','
    notice+="):"
    move=input(notice)
    if move==u and V!="up":
        temp=matrix[t-4]
        matrix[t-4]=0
        matrix[t]=temp
        t-=4
    elif move==d and V!="down":
        temp=matrix[t+4]
        matrix[t+4]=0
        matrix[t]=temp
        t+=4
    elif move==l and H!="left":
        temp=matrix[t-1]
        matrix[t-1]=0
        matrix[t]=temp
        t-=1
    elif move==r and H!="right":
        temp=matrix[t+1]
        matrix[t+1]=0
        matrix[t]=temp
        t+=1
    for num in matrix:
        num=int(float(num))
        if (matrix.index(num)+1)%(len(matrix)**0.5)==0: #The element is located on the right end.
            if num==0:
                print('  ')
            else:
                print("%2d"%num)
        else:
            if num==0:
                print('  ',end=' ')
            else:
                print("%2d"%num,end=' ')

state=True
while(state):
    global t, V, H, u,d,l,r,notice1,mode
    mode=input("Please enter the mode you want (8/15):")
    if mode=="8":
        matrix=[1,2,3,4,5,6,7,8,0]
    else:
        matrix=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]
    d=input('Enter the key that you want to represent "up":')
    u=input('Enter the key that you want to represent "down":')#Instruct the user to define movekeys by himself.
    r=input('Enter the key that you want to represent "left":')
    l=input('Enter the key that you want to represent "right":')

    movekey_list=(u,d,l,r)#Create a list that contains re-defined movekeys.
    print(movekey_list)
    notice1="..."
    print_map(matrix) #Print the randomly disorganized matrix
    t=matrix.index(0) 
    count=0
    if mode=="8":
        print("You are using 8 Mode.")
        while True:    
            H=find_x8(t)
            V=find_y8(t)
            action8(V,H,matrix,u,d,l,r,t,notice1) #Move the blank space into the direction that the user instructs.
            count+=1
            print("Step count=",count)
            t=matrix.index(0)
            if matrix==[1,2,3,4,5,6,7,8,0]:
                state=False
                break
        print("Successful. Total step:",count)
    else:
        print("You are using 15 Mode.")
        while True:
            H=find_x15(t)
            V=find_y15(t)
            action15(V,H,matrix,u,d,l,r,t,notice1) #Move the blank space into the direction that the user instructs.
            count+=1
            print("Step count=",count)
            t=matrix.index(0)
            if matrix==[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]:
                break
        print("Successful. Total step:",count)
        final=input("Enter “1” for 8-puzzle, “2” for 15-puzzle or “q” to end the game:")
        if final=="q":
            state=False
            break