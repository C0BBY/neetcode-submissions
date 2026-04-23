class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def isAnagram(original, subject)->bool:
            if len(original) != len(subject):
                return False

            checker = {}            
            for c in original:
                checker[c] = checker.get(c, 0)+1

            for c in subject:
                if c not in checker:
                    return False
                
                checker[c]-=1                
                if checker[c] == 0:
                    checker.pop(c)                    
            
            return not checker                 
        
        visited = []
        master_list = []
        
        for i in range(len(strs)):
            if i in visited:
                continue
            visited.append(i)
            anagrams = [strs[i]]
            for j in range(i+1, len(strs)):
                if j in visited:
                    continue
                if isAnagram(strs[i], strs[j]):
                    visited.append(j)
                    anagrams.append(strs[j])
            master_list.append(anagrams)
        
        print(master_list)
        return master_list
