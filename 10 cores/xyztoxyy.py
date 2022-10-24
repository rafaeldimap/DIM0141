import csv
with open('XYZ.csv',newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for i in reader:
        #print(i)
        freq, X, Y, Z = int(i[0]), float(i[1]), float(i[2]), float(i[3])
        S = X+Y+Z
        x, y, z = X/S, Y/S, Z/S
        print(f'{freq},{x},{y},{z},{Y}')
