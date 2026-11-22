
class Solution:
    def myAtoi(self, s: str) -> int:

        i = 0
        n = len(s)

        # Step 1: Skip leading spaces
        while i < n and s[i] == " ":
            i += 1

        # Step 2: Check sign
        sign = 1

        if i < n and s[i] == "-":
            sign = -1
            i += 1
        elif i < n and s[i] == "+":
            i += 1

        # Step 3: Convert digits
        num = 0

        while i < n and s[i] >= "0" and s[i] <= "9":

            digit = ord(s[i]) - ord("0")

            num = num * 10 + digit

            i += 1

        # Step 4: Apply sign
        num = num * sign

        # Step 5: Handle 32-bit overflow
        INT_MIN = -2147483648
        INT_MAX = 2147483647

        if num < INT_MIN:
            return INT_MIN

        if num > INT_MAX:
            return INT_MAX

        return num
