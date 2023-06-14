#744. Find Smallest Letter Greater Than Target

#1st Брут
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for i in letters:
            if i > target:
                return i

        return letters[0]

#2nd Бінарний пошук
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        lb, rb = 0, len(letters)
        while lb < rb:
            mid = (lb + rb) // 2
            if letters[mid] > target:
                rb = mid
            else:
                lb = mid + 1
        
        return letters[r] if rb < len(letters) else letters[0]  