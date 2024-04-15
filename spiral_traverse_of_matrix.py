'''
Idea 
- Remove the first row 
- take transpose of the remaining matrix 
- rotate 90 degree in the clock wise direction and repeat process 
'''

def spiral_traverse(matrix):
    result = []
    while matrix:
        result += matrix[0]  # Add the first row to the result
        row_removed_matrix = matrix[1:]
        print("Row removed matrix ", row_removed_matrix)
        convert_zip = zip(*matrix[1:])
        convert_in_list = list(zip(*matrix[1:])) # transpose of matrix 
        print("Transpose of matrix ", convert_in_list)
        rotate_matrix = convert_in_list[::-1]
        print("Rotated matrix at the end ", rotate_matrix)
        matrix = list(zip(*matrix[1:]))[::-1]  # Rotate the remaining matrix counter-clockwise
    return result

# Example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
result = spiral_traverse(matrix)
print(result)  # Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]
