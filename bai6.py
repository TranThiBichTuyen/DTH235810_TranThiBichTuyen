rows=9
cols=9
a=("*********")
for row in range(rows):
    for col in range(cols):
        if row ==0 or row==8:
            if col ==0 or col ==8:
                print (a)