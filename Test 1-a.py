class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        n = len(candies)
        result = [False]*n
        maxCandies = max(candies)
        for i in range(n):
            if candies[i] + extraCandies >= maxCandies:
                result[i] = True
        return result
