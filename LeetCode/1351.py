#1351 Count Negative Numbers in a Sorted Matrix
#Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

#1st По строці з початку до першого негативного
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        res = 0
        for i in range(len(grid)):
            k = 0
            for j in range(len(grid[i])):
                if grid[i][j] < 0:
                    break
                else:
                    k += 1
            res += len(grid[i]) - k
    
        return res
        
#2nd По строці з початку до першого негативного
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        l = len(grid[0])
        res = 0
        for i in grid:
            k = 0
            for j in i:
                if j < 0:
                    break
                else:
                    k += 1
            res += l - k
    
        return res
        
#3rd По строці з кінця до першого позитивного
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for i in grid:
            for j in range(-1, -len(i)-1, -1):
                if i[j] < 0:
                    count += 1
                else:
                    break
        return count
        
#4th Пошук середини бінарним способом через окрему функцію
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        res = 0
        lrow, lcol = len(grid), len(grid[0])
        
        for i in range(lrow):
            res += self.search(grid[i], lcol)
        
        return res

    def search(self, row, n):
        lb, rb = 0, n - 1

        while lb <= rb:
            mid = (start + end) // 2
            
            if row[mid] >= 0:
                start = mid + 1
            else:
                end = mid - 1
        
        return n - start  

        
#5th Пошук середини бінарним способом через рекурсію
