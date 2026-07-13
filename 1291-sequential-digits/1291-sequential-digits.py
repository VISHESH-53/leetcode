class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        digits = "123456789"

        length = len(str(low))

        while length <= len(str(high)):
            num = int(digits[:length])
            jump = int("1" * length)

            while num <= high and len(str(num)) == length:
                if num >= low and str(num) in digits:
                    ans.append(num)

                num += jump

            length += 1

        return ans