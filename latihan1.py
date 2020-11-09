n=int(input("Masukan nilaim N :"))

import random

for x in list(range(1, n+1, 1)):
    print(f"Data ke : {x} ->",random.uniform(0,0.5))

print()