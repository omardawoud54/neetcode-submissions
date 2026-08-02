class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # def sort(x):
        #     x = list(x)
        #     x_len = len(x)
        #     for i in range(x_len):
        #         for j in range(0, x_len - i - 1):
        #             if x[j] > x[j + 1]:
        #                 x[j], x[j + 1] = x[j + 1], x[j]
        #     return x
        
        return sorted(s) == sorted(t)