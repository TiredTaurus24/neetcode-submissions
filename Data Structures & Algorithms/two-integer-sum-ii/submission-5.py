class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num_dict = defaultdict(int)
        for i in range(len(numbers)):
            complement = target - numbers[i]
            if num_dict[complement]:
                return [num_dict[complement], i+1]
            num_dict[numbers[i]] = i + 1
        return []
        