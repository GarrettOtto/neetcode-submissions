class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Hash map to count the occurances of each value
        count = {}

        # This array is the same size as the input array
            # This code creates the number of empty arrays inside the freq array
                # for i in range(len(nums) + 1)
            # The index is the frequency of an element
            # The value is going to be the list of all elements with that specific frequency
        freq = [[] for i in range(len(nums) + 1)]

        # Go through every value in nums and count how many times it occurs
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        # This will return each key value pair we have in our dictionary
            # n is number
            # c is count
        for n, c in count.items():
            freq[c].append(n)

        # Creating a result output array
        res = []
        # Looping through the list and getting the highest k most frequesnt elements
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res