def reverse_list(given_list,start, end):
    while start < end:
        given_list[start], given_list[end] = given_list[end] , given_list[start]
        start += 1
        end -= 1
    return given_list
        
a = reverse_list([3,1,5,6,2,45], 0, 5)     
print(a)