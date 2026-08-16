class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        primes = [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 
        43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]

        windowSize = len(s1)
        if windowSize > len(s2): return False

        l = 0
        r = windowSize - 1

        s = 1
        for i in s1:
            index = ord(i) - ord("a")
            s *= primes[index]
        
        ws = 1
        for x in s2[0:windowSize]:
            index = ord(x) - ord("a")
            ws *= primes[index]
        
        while r < len(s2) - 1:
            if s == ws:
                return True
            r += 1
            rindex = ord(s2[r]) - ord("a")
            ws *= primes[rindex]

            lindex = ord(s2[l]) - ord("a")
            ws //= primes[lindex]

            l += 1
        
        if s == ws:
            return True

        return False

