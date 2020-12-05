import os
import sys
import random
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src import max_pairwise_product_automatated

# number of tests from the user
test = int(sys.argv[1])
# size of the sequence
n = int(sys.argv[2])
# seed for generating random number
myseed = int(sys.argv[3])


for i in range(test):
    os.system("python generate_test.py" +' '+ str(n) + " " + str(myseed) + " > test_input.txt")
    input = []
    file1 = open('test_input.txt', 'r')
    Lines = file1.readlines()
    # Strips the newline character
    for line in Lines:
        each_line = line.strip()
        input.append(each_line)
    n = int(input[0])
    seq = input[1]
    seq = list(map(int, seq.split(' ')))

    obj = max_pairwise_product_automatated.max_pairwise_product(n, seq)
    result = obj.max_pairwise_product_optimized()
    try:
        assert obj.max_pairwise_product_slow() == obj.max_pairwise_product_optimized()
        print('Test : {} --- passed '.format(i))
        print("Given inputs:\n")
        print("n : {}....sequence:{}".format(n, seq))
    except AssertionError:
        print("For {n} and sequence {seq} Test :{i} failed".format(n, seq, i))
    except Exception as e:
        print(e)
    myseed = myseed + 100



