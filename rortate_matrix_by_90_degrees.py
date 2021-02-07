# The matrix should be a square matrix
def rotate_90(org_mat):
    # 1st step: make the transpose of the matrix
    # 2nd step: swap the elements of the columns barring the middle one
    print(len(org_mat))
    org_mat = [[org_mat[j][i] for j in range(len(org_mat))] for i in range(len(org_mat[0]))]
    i = 0
    print(org_mat)
    while(i < len(org_mat)):
      c = 0
      j = len(org_mat)-1
      while(c<=j):
        org_mat[i][c] , org_mat[i][j] =  org_mat[i][j] , org_mat[i][c] 
        #print(i,c,j)
        c += 1
        j -= 1
      i += 1   

    return org_mat

r = rotate_90(
             [[1,2,3],
              [4,5,6],
              [7,8,9]]             
             )
print(r)  