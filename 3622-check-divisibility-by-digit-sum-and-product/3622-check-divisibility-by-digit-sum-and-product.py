class Solution:
    def checkDivisibility(self, n: int) -> bool:
        # Handle 0 explicitly to prevent zero division
        if n == 0:
            return False
            
        temp = abs(n)  # Handles negative numbers safely
        digit_sum = 0
        digit_prod = 1
        
        # Extract digits mathematically
        while temp > 0:
            digit = temp % 10
            digit_sum += digit
            digit_prod *= digit
            temp //= 10
            
        # Prevent division by zero
        divisor = digit_prod + digit_sum
        if divisor == 0:
            return False
            
        return n % divisor == 0


