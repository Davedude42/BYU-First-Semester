
def is_valid(lst):
	return sum(lst[0:4]) == sum(lst[3:7]) and sum(lst[3:7]) == sum(lst[6:10]) + lst[0]

def not_ftf(n):
	return n != 5 and n != 4 and n != 2

all_n = [1, 3, 6, 7, 8, 9]

lst_indices = [-1, -1, -1, -1, -1, -1]
for i in range(6):
	for ii in range(6):
		for iii in range(6):
			for iv in range(6):
				for v in range(6):
					for vi in range(6):
						if len([i, ii, iii, iv, v, vi]) == len(set([i, ii, iii, iv, v, vi])):
							lst = [all_n[i], all_n[ii], 2, all_n[iii], all_n[iv], 4, all_n[v], all_n[vi], 5]
							if is_valid(lst):
								print(lst)
