class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        for i in strs:
            out += f"{len(i)}#{i}"
        
        return out

    def decode(self, s: str) -> List[str]:
        out = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            
            print(s[i:j])
            length = int(s[i:j])
            out.append(s[j + 1: j + length + 1])

            i = j + length + 1
        return out
