class Solution:
    def isPalindrome(self, s: str) -> bool:
        compact = "".join(x if x.isalnum() else '' for x in s)
        sz = len(compact)
        left = 0
        right = 0
        midpoint = sz//2
        left, right = midpoint-1, midpoint+1 if sz%2 else midpoint
        print(f"{compact} {midpoint}")
        

        while left >= 0 and right< sz:
            if compact[left].lower()!=compact[right].lower():
                print(f"{compact[left]} {compact[right]}")
                return False
            left-=1
            right+=1

        return True
     