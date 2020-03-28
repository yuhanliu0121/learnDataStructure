from mymatrix import Matrix;

m1 = Matrix(2,3)
m2 = Matrix(3,2)

m1[0,0] = 3
m1[0,1] = 2
m1[0,2] = 4
m1[1,0] = 1
m1[1,1] = 2
m1[1,2] = 3

m2[0,0] = 1
m2[0,1] = 2
m2[1,0] = 3
m2[1,1] = 4
m2[2,0] = 5
m2[2,1] = 6

print('m1 =  ')
m1.show()
print('\n')

print('m2 =  ')
m2.show()
print('\n')

print('m1 * m2 = ')
(m1 * m2).show()