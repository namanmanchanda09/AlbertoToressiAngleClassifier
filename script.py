import random, os
l = os.listdir('globalCheck/shoe')
random.shuffle(l)
ll = len(l)
new = l[0:ll- 800]
for i in new:
    os.remove('globalCheck/shoe/' + i)
    


    
