def find_middle_ele(A,B,C):
    if (A-B) * (A-C) < 0:
        return A
    elif (B-C) * (B-A) < 0:
        return B
    else:
        return C

def find_max_ele(A,B,C):
    mid = find_middle_ele(A,B,C)
    if A > mid:
        #print('Max element is :', A)
        return A
    elif B > mid:
        #print('Max element is :', B)
        return B
    else:
        print('Max ele is : ', C)

def find_min_ele(A,B,C):
    mid = find_middle_ele(A, B, C)
    min = find_max_ele(A,B,C)
    if A<mid:
        return A
    elif B<mid:
        return B
    else:
        return C

mid_ele = find_middle_ele(123, 500, 21)
min_ele = find_min_ele(123, 500, 21)
max_ele = find_max_ele(123, 500, 21)
print(min_ele,mid_ele, max_ele)