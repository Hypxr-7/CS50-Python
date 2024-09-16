def determinant(matrix):
    """
    Calculate the determinant of a square matrix.
    Args:
        matrix (list of list of int/float): A square matrix represented as a list of lists.
    Returns:
        int/float: The determinant of the matrix.
    Raises:
        TypeError: If the input is not a list of lists.
        ValueError: If the matrix is not square.
    Examples:
        >>> determinant([[1, 2], [3, 4]])
        -2
        >>> determinant([[1]])
        1
        >>> determinant([[2, 5, 3], [1, -2, -1], [1, 3, 4]])
        -20
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("Matrix must be a list of lists")
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    if rows != cols:
        raise ValueError("Matrix must be square")

    if rows == 1:
        return matrix[0][0]

    if rows == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for c in range(cols):
        minor_matrix = [row[:c] + row[c+1:] for row in matrix[1:]]
        det += ((-1) ** c) * matrix[0][c] * determinant(minor_matrix)
    
    return det

def test_determinant():
    # Test 1x1 matrix
    assert determinant([[5]]) == 5

    # Test 2x2 matrix
    assert determinant([[1, 2], 
                        [3, 4]]) == -2

    # Test 3x3 matrix
    assert determinant([[1, 2, 3], 
                        [4, 5, 6], 
                        [7, 8, 9]]) == 0
    
    assert determinant([[2, 5, 3], 
                        [1, -2, -1], 
                        [1, 3, 4]]) == -20

    # Test 4x4 matrix
    assert determinant([[1, 0, 2, -1], 
                        [3, 0, 0, 5], 
                        [2, 1, 4, -3], 
                        [1, 0, 5, 0]]) == 30

    # Test non-square matrix (should raise ValueError)
    try:
        determinant([[1, 2, 3], 
                     [4, 5, 6]])
    except ValueError as e:
        assert str(e) == "Matrix must be square"
    else:
        assert False, "Expected ValueError"

    # Test invalid matrix type (should raise TypeError)
    try:
        determinant("not a matrix")
    except TypeError as e:
        assert str(e) == "Matrix must be a list of lists"
    else:
        assert False, "Expected TypeError"

if __name__ == "__main__":
    test_determinant()
    print("All tests passed")