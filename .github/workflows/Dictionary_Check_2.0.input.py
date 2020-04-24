import enchant
from itertools import permutations
#318 at 4:03 pm
#361 at 4:06 pm
#381 at 4:09 pm
# I get 22 every 2 mins
#426 at 4:16 pm

user_letter_set = input("Enter your letters:")
#letter_set = ["v","i","a","l","s","u"]
letter_set = user_letter_set

for n in range(3, len(letter_set)+1):
    for perm in permutations(letter_set, n): 
        d = enchant.Dict("en_US")
        a = d.check("".join(perm))
        if a == True:
            print ("".join(perm))
    


