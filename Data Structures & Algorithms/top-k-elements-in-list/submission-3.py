class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        # Going through each value that we counted & appending it to the arr
        for n, c in count.items():
            # Check this syntax: freq(c) compared to freq[c]
            freq[c].append(n)

        res = []
        # Need to go in desc order
        for i in range(len(freq) -1, 0, -1):
            for n in freq[i]:
                res.append(n)

            if len(res) == k:
                return res