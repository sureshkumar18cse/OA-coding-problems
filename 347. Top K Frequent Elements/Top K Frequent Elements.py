# 1. Optimal — Bucket Sort O(n) ✅
class Solution:
    def topKFrequent(self, nums, k):
        # Step 1: Count frequency
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        # Step 2: Create buckets
        buckets = [[] for _ in range(len(nums) + 1)]

        # Step 3: Put each number into its frequency bucket
        for num, freq in count.items():
            buckets[freq].append(num)

        # Step 4: Traverse from highest frequency
        answer = []

        for freq in range(len(nums), 0, -1):
            for num in buckets[freq]:
                answer.append(num)

                if len(answer) == k:
                    return answer


# # 2. HashMap + Sorting — O(n log n)
# class Solution:
#     def topKFrequent(self, nums, k):
#         count = {}

#         for num in nums:
#             count[num] = count.get(num, 0) + 1

#         frequencies = list(count.items())

#         frequencies.sort(key=lambda x: x[1], reverse=True)

#         answer = []

#         for i in range(k):
#             answer.append(frequencies[i][0])

#         return answer

# # 3. Brute Force — O(n²)
# class Solution:
#     def topKFrequent(self, nums, k):
#         n = len(nums)
#         visited = set()
#         frequencies = []

#         for num in nums:
#             if num in visited:
#                 continue

#             count = 0

#             for x in nums:
#                 if x == num:
#                     count += 1

#             visited.add(num)
#             frequencies.append((num, count))

#         answer = []

#         for _ in range(k):
#             max_index = 0

#             for i in range(len(frequencies)):
#                 if frequencies[i][1] > frequencies[max_index][1]:
#                     max_index = i

#             answer.append(frequencies[max_index][0])
#             frequencies.pop(max_index)

#         return answer
