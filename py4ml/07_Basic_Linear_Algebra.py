# vector 간 덧셈 또는 뺄셈 연산을 할 때, 연산이 가능한 사이즈인지를 확인하여 가능 여부를 True 또는 False로 반환함
def vector_size_check(*vector_variables):
    return all(len(vector_variables[0]) == x for x in [len(vector) for vector in vector_variables[1:]])

# vector간 덧셈을 실행하여 결과를 반환함, 단 입력되는 vector의 갯수와 크기는 일정하지 않음
def vector_addition(*vector_variables):
    if vector_size_check(*vector_variables) == False :
        raise ArithmeticError
    return [sum(elements) for elements in zip(*vector_variables)]

# vector간 뺄셈을 실행하여 결과를 반환함, 단 입력되는 vector의 갯수와 크기는 일정하지 않음
def vector_subtraction(*vector_variables):
    if vector_size_check(*vector_variables) == False:
        raise ArithmeticError
    return [elements[0]*2-sum(elements) for elements in zip(*vector_variables)]

# 하나의 scalar 값을 vector에 곱함, 단 입력되는 vector의 크기는 일정하지 않음
def scalar_vector_product(alpha, vector_variable):
    return [alpha * element for element in vector_variable]

# matrix 간 덧셈 또는 뺄셈 연산을 할 때, 연산이 가능한 사이즈인지를 확인하여 가능 여부를 True 또는 False로 반환함
def matrix_size_check(*matrix_variables):
    return all([len(set(len(matrix[0]) for matrix in matrix_variables)) == 1]) and
        all([len(matrix_variables[0]) == len(matrix) for matrix in matrix_variables])

# 비교가 되는 n개의 matrix가 서로 동치인지 확인하여 True 또는 False를 반환함
def is_matrix_equal(*matrix_variables):
    return None

# matrix간 덧셈을 실행하여 결과를 반환함, 단 입력되는 matrix의 갯수와 크기는 일정하지 않음
def matrix_addition(*matrix_variables):
    if matrix_size_check(*matrix_variables) == False:
        raise ArithmeticError
    return None

# matrix간 뺄셈을 실행하여 결과를 반환함, 단 입력되는 matrix의 갯수와 크기는 일정하지 않음
def matrix_subtraction(*matrix_variables):
    if matrix_size_check(*matrix_variables) == False:
        raise ArithmeticError
    return None

# matrix의 역행렬을 구하여 결과를 반환함, 단 입력되는 matrix의 크기는 일정하지 않음
def matrix_transpose(matrix_variable):
    return None

# 하나의 scalar 값을 matrix에 곱함, 단 입력되는 matrix의 크기는 일정하지 않음
def scalar_matrix_product(alpha, matrix_variable):
    return None

# 두 개의 matrix가 입력 되었을 경우, 두 matrix의 곱셈 연산의 가능 여부를 True 또는 False로 반환함
def is_product_availability_matrix(matrix_a, matrix_b):
    return None

# 곱셈 연산이 가능한 두 개의 matrix의 곱셈을 실행하여 반환함
def matrix_product(matrix_a, matrix_b):
    if is_product_availability_matrix(matrix_a, matrix_b) == False:
        raise ArithmeticError
    return None
