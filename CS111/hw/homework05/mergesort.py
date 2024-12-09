import sys

def mergeSort(lst):
	if len(lst) == 1:
		return lst

	leftSorted = mergeSort(lst[:(len(lst) // 2)])
	rightSorted = mergeSort(lst[(len(lst) // 2):])

	return merge(leftSorted, rightSorted)

def merge(left, right):
	ret = []
	i = 0
	j = 0

	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			ret.append(left[i])
			i += 1
		else:
			ret.append(right[j])
			j += 1

	ret = ret + left[i:] + right[j:]

	return ret

def main():
	numbers = []
	with open(sys.argv[1], 'r') as inputFile:
		numbers = [int(n) for n in inputFile.readlines()]

	numbers = mergeSort(numbers)
	
	with open(sys.argv[2], 'w') as outputFile:
		outputFile.writelines([str(n).zfill(3) + '\n' for n in numbers])


if __name__ == '__main__':
	main()