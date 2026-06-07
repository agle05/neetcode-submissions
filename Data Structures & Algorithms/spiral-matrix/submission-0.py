class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        output = []
        top, bottom = 0, len(matrix)-1
        left, right = 0, len(matrix[0])-1

        while top <= bottom and left <= right:
            # Go right along top row
            for col in range(left, right+1):
                output.append(matrix[top][col])
            top += 1

            # Go down along far col
            for row in range(top, bottom+1):
                output.append(matrix[row][right])
            right -= 1

            # Go left along bottom row
            if top <= bottom:
                for col in range(right, left-1, -1):
                    output.append(matrix[bottom][col])
                bottom -= 1

            # Go up along close col
            if left <= right:
                for row in range(bottom, top-1, -1):
                    output.append(matrix[row][left])
                left += 1

        return output