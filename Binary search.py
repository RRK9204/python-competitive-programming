import math
import pdb
def binary_search(li, le, ri, qu):
    global Found
    Found = 0
    if(le == ri):
        if(qu == li[ri]):
            Found += 1
            print('The query {0} is found at {1} position' .format(li[ri], ri+1))
            return(li[ri])
    elif(le == 0) & (ri == 1):
        if(qu == li[le]):
            Found += 1
            print('The query {0} is found at {1} position' .format(li[le], le+1))
        elif(qu == li[ri]):
            Found += 1
            print('The query {0} is found at {1} position' .format(li[ri], ri+1))
        
    else:
        midEle = math.ceil((le + ri)/2)
        print(midEle)
        if(qu == li[midEle]):
            Found += 1
            print('The query {0} is found at {1} position' .format(li[midEle], midEle+1))
            return(li[midEle])
        
        elif(qu > li[midEle]):
            le = midEle 
            return(binary_search(li, le, ri, qu))
        elif(qu < li[midEle]):
            ri = midEle
            return(binary_search(li, le, ri, qu))
    

#li = li(range(100))
li = []
inputli = input('Enter the elements of list separated by comma: ')
strli = inputli.split(',')
for ele in strli:
    li.append(int(ele))
le = 0
ri = len(li) - 1
li.sort()
print(li)

qu = int(input('Enter the element to be found: '))
binary_search(li, le, ri, qu)
if(Found == 0):
    print('The query {0} is not found' .format(qu))