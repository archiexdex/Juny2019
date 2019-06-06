n = 15
print(len(list(filter(lambda x: (not x%15) or (x%3 and x%5), range(1, n+1)))))
