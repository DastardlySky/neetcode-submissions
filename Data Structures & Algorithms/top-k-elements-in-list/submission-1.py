class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        max_frequency = 0

        for num in nums:
            count[num] += 1
            max_frequency = max(max_frequency, count[num])

        buckets = [[] for i in range(max_frequency + 1)]

        for num, frequency in count.items():
            buckets[frequency].append(num)

        res = []

        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
