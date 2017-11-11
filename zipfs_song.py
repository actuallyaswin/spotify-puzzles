n, k = map(int, raw_input().strip().split(' '))
for j in [i[1] for i in sorted([(lambda (a,b): [int(a)*(1 - 1./(i+1)),b])(raw_input().strip().split(' ')) for i in range(n)])[::-1][:k]]:
	print(j)