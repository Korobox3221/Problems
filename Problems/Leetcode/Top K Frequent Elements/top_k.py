class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        nums.sort(reverse=True)
        res = defaultdict(list)
        for i in nums:
            res[i].append(i)
        l_l = list(res.values())
        k_k = []
        for i in range (len(l_l)):
                k_k.append(len(l_l[i]))
        print(k_k)
        final =[]
        for i in range(k):
            index = k_k.index(max(k_k))
            max_occ = l_l[k_k.index(max(k_k))][0]
            final.append(max_occ)
            k_k.pop(index)
            k_k.insert(index,0)
        final.sort()
        return final
