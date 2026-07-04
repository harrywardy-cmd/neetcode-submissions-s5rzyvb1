class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        gas_amount = 0
        result = 0

        for i in range(len(cost)):
            gas_amount = (gas_amount + gas[i]) - cost[i]

            if gas_amount < 0:
                result = i + 1
                gas_amount = 0
            
        return result
            


      


        