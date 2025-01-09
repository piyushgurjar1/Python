class MathOperations:
    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply_matrices(self, matrix1, matrix2):
        result = []
        for i in range(len(matrix1)):  
            row = []
            for j in range(len(matrix2[0])):  
                sum = 0
                for k in range(len(matrix2)):  
                    sum += matrix1[i][k] * matrix2[k][j]
                row.append(sum)
            result.append(row)
        return result

def display(matrix):
    for row in matrix:
        print(row)