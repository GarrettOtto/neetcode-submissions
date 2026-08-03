class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashTable = {}

        for word in strs:
            key = "".join(sorted(word))

            if key not in hashTable:
                hashTable[key] = []

            hashTable[key].append(word)

        return list(hashTable.values())