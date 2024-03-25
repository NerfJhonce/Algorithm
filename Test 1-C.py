class Solution(object):
    def mergeSimilarItems(self, items1, items2):
        """
        :type items1: List[List[int]]
        :type items2: List[List[int]]
        :rtype: List[List[int]]
        """

        mp = defaultdict(int)

        for value, weight in items1 + items2:
            mp[value] += weight

        A = list(mp.items())
        A.sort(key=lambda x: x[0])

        return [[v, w] for v, w in A]
