class max_pairwise_product:
    def __init__(self,n,seq):
        self.n = int(n)
        self.seq = seq

    def max_pairwise_product_slow(self):
        result = 0
        for i in range(self.n):
            for j in range(i + 1, self.n):
                if self.seq[i] * self.seq[j] > result:
                    result = self.seq[i] * self.seq[j]
        return result

    def max_pairwise_product_optimized(self):
        first_max_index = -1
        result = 0
        for i in range(self.n):
            if self.seq[first_max_index] < self.seq[i] or first_max_index == -1:
                first_max_index = i
        second_max_index = -1
        for i in range(self.n):
            if i != first_max_index and (self.seq[second_max_index] < self.seq[i] or second_max_index == -1):
                second_max_index = i
        result = self.seq[first_max_index] * self.seq[second_max_index]
        return result
