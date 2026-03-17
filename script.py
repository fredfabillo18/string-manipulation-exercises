v = [0, 10, 20, 15, 0]
dt = 2
distance = 0
for index in range(len(v)-1):
    distance += (dt/2)*(v[index]+v[index+1])
print(distance)