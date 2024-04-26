class Solution(object):
    def generate(self, numRows):
        triangle = []
        for i in range(numRows):
            row = [1] * (i + 1)  # Initialize each row with 1s
            for j in range(1, i):  # Update inner elements using n-1Cr-1 approach
                row[j] = self.nCr(i, j)
            triangle.append(row)
        return triangle

    def nCr(self, n, r):
        res = 1
        for i in range(r):
            res = res * (n - i) / (i + 1)
        return int(res)
    

        def generate(self, numRows):
        
            triangle = []

            for i in range(1, numRows+1):
                triangle.append(self.generateRows(i))
            return triangle



    def nCr(self, n, r):
        res = 1

        for i in range(r):
            res = res * (n - i) / (i + 1)


#Optimal solution

    def generateRows(self, row):

        res = 1
        ansRow = [1]

        for col in range(1,row):
            res = res * (row-col)/col
            ansRow.append(res)

        return ansRow

# Example usage
solution = Solution()
print(solution.generate(5))  # Output the Pascal's triangle with 5 rows
