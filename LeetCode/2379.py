#2379. Minimum Recolors to Get K Consecutive Black Blocks
#You are given a 0-indexed string blocks of length n, where blocks[i] is either 'W' or 'B', representing the color of the ith block. The characters 'W' and 'B' denote the colors white and black, respectively.
#You are also given an integer k, which is the desired number of consecutive black blocks.
#In one operation, you can recolor a white block such that it becomes a black block.
#Return the minimum number of operations needed such that there is at least one occurrence of k consecutive black blocks.

#1st Кожен раз будуеться новий підрядок
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        res = blocks[:k].count('W')
        for i in range(1, len(blocks) - k + 1):
            tres = blocks[i: i + k].count('W')
            if tres < res:
                res = tres
        return res
        
#2nd Рухома рамка
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        string = blocks[:k]
        res = string.count('W')
        tres = res

        for i in range(k, len(blocks)):
            if string[0] == 'W':
                tres -= 1
            if blocks[i] == 'W':
                tres += 1
            if tres < res:
                res = tres
            string = string[1:] + blocks[i]
        return res
