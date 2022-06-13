
def rotate_image(matrix):
    """
    Given a n x n 2-D matrix representing an image, rotate the image 90 degrees clockwise IN-PLACE

    ex: matrix = [[1,2], [3,4]] -> [[3,1], [4,2]]

        Before:               After:
        1: matrix[0][0]  ->   matrix[0][1]
        2: matrix[0][1]  ->   matrix[1][1]
        3: matrix[1][0]  ->   matrix[0][1]
        4: matrix[1][1]  ->   matrix[1][0]

        matrix = [[1,2,3],[4,5,6],[7,8,9]] -> [[7,4,1],[8,5,2],[9,6,3]]

        Before:               After:
        1: matrix[0][0] -> matrix[0][2] 
        2: matrix[0][1] -> matrix[1][2] 
        3: matrix[0][2] -> matrix[2][2] 
        4: matrix[1][0] -> matrix[0][1] 
        5: matrix[1][1] -> matrix[1][1] 
        6: matrix[1][2] -> matrix[2][1] 
        7: matrix[2][0] -> matrix[0][0] 
        8: matrix[2][1] -> matrix[1][0] 
        9: matrix[2][2] -> matrix[2][0] 

    Runtime: O(n^2) since we have to traverse a 2-D matrix
    Space: O(1) since no extra space must be added
    """

    for i in range(len(matrix)+1):
        print(i)
        for j in range(len(matrix)-1, -1, -1):
            print(j)

    print(matrix)


matrix = [[1, 2], [3, 4]]
rotate_image(matrix)
