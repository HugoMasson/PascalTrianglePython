#################################################
#												#
#		Hugo.M  pascal  triangle  printer		#
#												#
#				22 october 2021					#
#												#
#################################################

import os


def drawPascalTriangle(n):

	os.system('cls' if os.name == 'nt' else 'clear')
	t  = []
	t2 = []

	print(1)
	for i in range(1, n+1):
		print(1, end=' ')
		t.append(1)
		for j in range(1, i):
			t.append(t2[j-1]+t2[j])
			print(t2[j-1]+t2[j], end=' ')
		t.append(1)
		t2 = t
		t = []
		print(1)


if __name__ == "__main__":
	drawPascalTriangle(10)