class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        foo = defaultdict(list) # string sum : array
        for string in strs:
            freq = [0] * 26
            for i in string:
                freq[ord(i) - ord('a')] += 1
            
            foo[tuple(freq)].append(string)
            
        return list(foo.values())