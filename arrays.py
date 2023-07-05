import array as arr
import random
numbers = arr.array("i", [6,7,8,9,10,11,12,13,14,15])
answer = numbers[random.randint(0, 9)]*10
print(answer)
