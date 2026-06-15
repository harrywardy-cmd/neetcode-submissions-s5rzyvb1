class Solution:
    def confusingNumber(self, n: int) -> bool:

        validNum = {"0":"0", "1":'1', "6":"9", "8":"8", "9":"6"}
        rotated_number = []

        for char in str(n):
            if char not in validNum:
                return False
            
            rotated_number.append(validNum[char])
        rotated_number = "".join(rotated_number)
            
        return int(rotated_number[::-1]) != n
                
        