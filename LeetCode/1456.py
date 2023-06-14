#1456. Maximum Number of Vowels in a Substring of Given Length
#Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.
#Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

#1st 
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        res = 0
        for i in range(len(s) - k + 1):
            pres = 0
            for j in s[i:i + k]:
                if j in 'aeiou':
                    pres += 1
            if pres > res:
                res = pres
        return res
        
#2nd Бінарний пошук
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l = len(s)
        tres = 0
        string = s[:k]
        for i in string:
            if i in 'aeiou':
                tres += 1
        res = tres

        for i in range(k, l):
            if string[0] in 'aeiou':
                tres -= 1
            if s[i] in 'aeiou':
                tres += 1
            if tres > res:
                res = tres
            string = string[1:] + s[i]
        return res