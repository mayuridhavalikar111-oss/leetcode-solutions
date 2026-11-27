class Solution(object):
    def commonFactors(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        x, y = a, b
        while y:
            x, y = y, x % y
        g = x  

        count = 0
        for i in range(1, g + 1):
            if g % i == 0:
                count += 1
                
        return count




        