class Solution:
    def hasArrayTwoCandidates(self, arr, x):
        # sort the array
        arr = sorted(arr)
        left, right = 0, len(arr) - 1
        while left < right:
            if arr[left] + arr[right] < x:
                left += 1
            elif arr[left] + arr[right] > x:
                right -= 1
            else:
                return 'true'
        return 'false'

# Provided array and target sum
arr = [335, 501, 170, 725, 479, 359, 963, 465, 706, 146, 282, 828, 962, 492, 996, 943, 828, 437, 392, 605, 903, 154, 293, 383, 422, 717, 719, 896, 448, 727, 772, 539, 870, 913, 668, 300, 36, 895, 704, 812, 323, 334]
x = 468

# Create an instance of Solution and call the method
solution = Solution()
result = solution.hasArrayTwoCandidates(arr, x)

print(result)  # Output should be 'true' or 'false' based on the array and target sum
