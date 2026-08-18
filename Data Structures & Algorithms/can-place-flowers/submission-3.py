class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        count = 0

        temp = []
        temp.append(0)
        for t in flowerbed:
            temp.append(t)
        
        temp.append(0)
        for i in range(1,len(temp)-1,1):
            if temp[i] == 0:
                if temp[i-1] == 0 and temp[i+1] ==0:
                    count +=1
                    temp[i] = 1

        return count >= n