class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 0
        store = set(nums)
        for num in store:
            temp = set()
            temp.add(num)
            pref = num-1
            suf = num+1
            
            while pref not in temp or suf not in temp:
                print(f"{pref} {suf}")
                if pref in store:
                    temp.add(pref)
                    pref+=1
                elif suf in store:
                    temp.add(suf)
                    suf+=1
                else:
                    break                    
            count = max(len(temp), count)
        
        return count            