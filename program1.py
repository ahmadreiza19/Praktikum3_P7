modal awal = 100000000

for bulan in range(1, 9, 1):
    # mentukan laba pada bulan ke 1 dan 2
    if (bulan >= 1) and (bulan <= 2):
        # laba bulan 1 dan 2 adalah 0%
        laba12 = modalawal * 0
        print(f"laba bulan ke {bulan} : {laba12}")
    if (bulan >= 3) and (bulan <= 4):
        # laba bulan 3 dan 4 adalah 1%
        laba34 = modalawal * 0.1
        print(f"laba bulan ke {bulan} : {laba34}")
    if (bulan >= 5) and (bulan <= 7):
        # laba bulan 5,6,7 adalah 5%
        laba567 = modalawal * 0.05
        print(f"laba bulan ke {bulan} : {laba567}")
    if bulan == 8:
        laba8 = modal awal * 0,03
        print(f"laba bulan ke {bulan} : {laba8}

totallaba = laba12+laba12+laba34+laba567+laba567+laba567+laba8

print(f" \n total laba adalah : {totallaba}" )
print()