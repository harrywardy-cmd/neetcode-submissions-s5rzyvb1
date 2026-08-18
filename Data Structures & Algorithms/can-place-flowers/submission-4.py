class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        temp = [0] + flowerbed + [0]
        
        for i in range(1,len(temp)-1):
            if temp[i] == 0:
                if temp[i-1] == 0 and temp[i+1] ==0:
                    count +=1
                    temp[i] = 1

        return count >= n