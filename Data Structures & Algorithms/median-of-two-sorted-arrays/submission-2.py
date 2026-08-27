class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:   
        A, B = nums1, nums2
        if len(A) > len(B):
            A,B = B,A
        
        total = len(A) + len(B)
        half = total // 2

        l, r = 0, len(A)

        while l <= r:
            i = (l + r) // 2
            j = half - i

            leftA = A[i - 1] if i > 0 else float("-inf")
            rightA = A[i] if i < len(A) else float('inf')
            leftB = B[j - 1] if j > 0 else float("-inf")
            rightB = B[j] if j < len(B) else float('inf')

            if leftA <= rightB and leftB <= rightA:
                if total % 2 == 0:
                    return (max(leftA, leftB) + min(rightA, rightB)) / 2
                else:
                    return min(rightB, rightA)

            elif leftA > rightB:
                r = i - 1
            else:
                l = i + 1