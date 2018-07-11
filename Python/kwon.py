fhand = open('C:/Users/oyun/Desktop/kwon.txt')
di = dict()
for line in fhand:
    line = line.rstrip()
    wds = line.split()
    for w in wds:
        di[w] = di.get(w,0)+1
largest = 0
for a,b in di.items():
    if b>largest:
        largest = b
    print(a, b)
print('가장큰 값은', largest)
