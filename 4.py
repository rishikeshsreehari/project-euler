'''
Problem 4:

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
Find the largest palindrome made from the product of two 3-digit numbers.


'''

import time

start_time = time.time()

max_product = 0
max = 999
min = 99

for i in range(max,min,-1):
    for j in range(max,min,-1):
        product = i * j
        if product < max_product:
            break
        elif(str(product)) == (str(product))[::-1]:
            max_product = product
                
print(f"The maximum palindrome is {max_product}")

end_time = time.time()

elapsed_time = end_time - start_time
print(f"Time taken: {elapsed_time} seconds")

            
            




