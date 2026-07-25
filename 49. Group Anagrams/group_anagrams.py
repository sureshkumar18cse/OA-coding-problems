class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            key = "".join(sorted(word))

            if key not in groups:
                groups[key] = []

            groups[key].append(word)

        return list(groups.values())



# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         visited = [False] * len(strs)
#         ans=[]

#         for i in range(len(strs)):
#             if visited[i]:
#                 continue

#             curr = [strs[i]]
#             visited[i] = True

#             for j in range(i + 1, len(strs)):
#                 if not visited[j] and sorted(strs[i]) == sorted(strs[j]):
#                     curr.append(strs[j])
#                     visited[j] = True
#             ans.append(curr)
#         return ans   #its brute force and exceed time limit



# from typing import List
# from collections import defaultdict

# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         anagrams = defaultdict(list)

#         for word in strs:
#             key = "".join(sorted(word))
#             anagrams[key].append(word)

#         return list(anagrams.values())
