
#Problem: Solving system of linear equations using Gaussian Elimination Method

#calculates determinant of matrix A
def find_det(A):
    n = len(A)
    #if the size of matrix is 1x1, then prints the element
    if n == 1:
        return A[0][0]
    #if size is not 1x1, then calculates determinant
    else:
        det = 0
        for i in range(n):
          for j in (A[:i] + A[i+1:]):
            minor = [j[:i] + j[i+1:]]
          det2 = ((-1)**i) * A[0][i] * find_det(minor)
          det = det + det2
        return det

#determines if system is singular or not
def solvable(A):
    # if det = 0, then the system is singular and not solvable
    determinant = find_det(A)
    if determinant == 0:
        print("The system is not solvable.")
        return False
    else:
        print("The system is solvable.")
        return True

#implements gaussian elimination method
def gaussian_elimination(A, b):
    n = len(A)

    #forms upper triangular matrix
    for k in range(n):
        for i in range(k+1, n):
            factor = A[i][k] / A[k][k]
            for j in range(k,n):
                A[i][j] -= factor * A[k][j]
            b[i] -= factor * b[k]

    #back substitution
    x = []
    for i in range(n):
      x.append(0)
    for i in range(n-1, -1, -1):
        sum_ax = 0
        for j in range(i+1, n):
            sum_ax += A[i][j] * x[j]
        x[i] = (b[i] - sum_ax) / A[i][i]

    return x


def main():

    dimension = int(input("Enter the Dimension of the Matrix (n):"))
    matrix = []

    print("Enter the Coefficient Matrix (A):")
    for i in range(dimension):
      m_element = input().split()
      j = []
      for k in m_element:
        #appends element to row
        j.append(float(k))
      #appends row to matrix
      matrix.append(j)

    print("Enter the Vector (b):")
    v_element = input().split()
    vector = []
    for k in v_element:
      vector.append(float(k))

    #if solvable is true, then calculate using gaussian elimination
    if solvable(matrix):
        x = gaussian_elimination(matrix, vector)
        print("The solution is:", end="[ ")
        for value in x:
          print("{:.10f}".format(value),end=" ")
        print("]")

if __name__ == '__main__':
    main()

