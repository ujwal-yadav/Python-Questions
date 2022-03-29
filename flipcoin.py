def nof(N, S):
	if (S < N):
		return 0
	if (N == 1 or N == S):
		return 1
	return (nof(N - 1, S - 1) +
			nof(N - 1, S - 2))

if __name__ == '__main__':
	N, S = 3, 4
	print (nof(N, S))
