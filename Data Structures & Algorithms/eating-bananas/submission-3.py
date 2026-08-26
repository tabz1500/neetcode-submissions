import math
from typing import List


class Solution:

  def minEatingSpeed(self, piles: List[int], h: int) -> int:
    l, r = 1, max(piles)
    res = r

    while l <= r:
      mp = (l + r) // 2

      time = 0
      for i in piles:
        time += math.ceil(i / mp)

      if time <= h:
        res = min(res, mp)
        r = mp - 1
      else:
        l = mp + 1

    return res