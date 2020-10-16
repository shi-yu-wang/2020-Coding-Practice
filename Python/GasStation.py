class Solution:
    """
    @param gas: An array of integers
    @param cost: An array of integers
    @return: An integer
    """
    def canCompleteCircuit(self, gas, cost):
        
        n = len(gas)
        # write your code here
        tolGas = 0
        curGas = 0
        start = 0
        for i in range(n):
            # total gas secures that we can d a circle
            tolGas += gas[i] - cost[i]
            # current gas secures that we can go to next stop
            curGas += gas[i] - cost[i]
            
            if curGas < 0:
                start = i + 1
                curGas = 0
                
        return start if tolGas >= 0 else -1
