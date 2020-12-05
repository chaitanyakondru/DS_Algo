import random

def max_pairwise_product(n,seq):
    first_max_index = -1
    result = 0
    for i in range(n):
        if seq[first_max_index] < seq[i] or first_max_index == -1:
            first_max_index = i
    second_max_index = -1
    for i in range(n):
        if i != first_max_index and (seq[second_max_index] < seq[i] or second_max_index == -1):
            second_max_index = i
    result = seq[first_max_index] * seq[second_max_index]
    return result
def max_pairwise_product_slow(n,seq):
    result = 0
    for i in range(n):
        for j in range(i+1,n):
            if seq[i] * seq[j] > result:
                result = seq[i]*seq[j]
    return result

if __name__ == "__main__":
    traditional = 0
    fast = 0
    while True:
        if traditional == fast:
            n = random.randint(5, 10)
            seq = [random.randint(0, 100) for x in range(n)]
            fast = max_pairwise_product(n, seq)
            traditional = max_pairwise_product_slow(n,seq)
            print(seq, traditional,fast, "OK")
        else:
            print(seq, traditional,fast, "Test failed")
            break

