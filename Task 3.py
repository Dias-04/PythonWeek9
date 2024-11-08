import operator

d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

sorted_d_r = dict(sorted(d.items(), key=operator.itemgetter(1)))
print("Rise: ", sorted_d_r)

sorted_d_d = dict(sorted(d.items(), key=operator.itemgetter(1), reverse=True))
print("Decrease:", sorted_d_d)
