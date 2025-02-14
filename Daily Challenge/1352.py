from typing import List

class ProductOfNumbers:

    def __init__(self):
        self.prefix_sum = [1]
        self.size = 0


    def add(self, num: int) -> None:
        if num ==0:
            self.prefix_sum = [1]
            self.size = 0
        else:
            self.prefix_sum.append(self.prefix_sum[self.size]*num)
            self.size+=1
        return

    def getProduct(self, k: int) -> int:
        if k > self.size:
            return 0
        return (
            self.prefix_sum[self.size] // self.prefix_sum[self.size-k]
        )

