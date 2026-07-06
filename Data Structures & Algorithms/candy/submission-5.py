class Solution:
    def candy(self, ratings: List[int]) -> int:
        

        candies = [1] * (len(ratings))

        for child in range(len(ratings)):
             if child - 1 in range(len(ratings)):
                if ratings[child] > ratings[child-1]:
                    candies[child] = max(candies[child], candies[child-1] + 1)

        for child in range(len(ratings)-1,-1,-1):
            if child +1 in range(len(ratings)):
                if ratings[child] > ratings[child+1]:
                    candies[child] = max(candies[child], candies[child+1]+1)



        return sum(candies)        
            

