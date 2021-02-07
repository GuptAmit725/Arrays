def find_Kth_smallest_element(list_of_elements):

    '''
    Expected Time Complexity: O(n)
    
    Input:
    The first line of input contains an integer T, denoting the number of testcases. 
    Then T test cases follow. Each test case consists of three lines. 
    First line of each testcase contains an integer N denoting size of the array. 
    Second line contains N space separated integer denoting elements of the array. 
    Third line of the test case contains an integer K.
    
    Output:
    For each testcase, in a newline, print the kth smallest element.
    
    Yout Task:
    Complete kthSmallest and return the kth smallest element.
    '''
    c = 0
    sort_dict = {}
    for ele in list_of_elements:
        sort_dict[ele] = c
        c += 1
    return sort_dict
d = find_Kth_smallest_element([2,6,8,2,3,4,1,5])
print(d)
