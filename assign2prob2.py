'''
CMPSC465
Assignment2 Problem2
Authors: Jillian Haffner, Rachael Owens, Kevin O'Connor
Sept. 20, 2020
'''

def main():
	n = int(input()) - 1
	p = []
	for i in range(0, n):
		p.append(input().split())
	# sort P: edit code to take array of 2 elements as the 
	s = []
	s = push(s, p_star[0])
	s = push(s, p_star[1])
	s = push(s, p_star[2])
	s = graham_scan_core(p, s, n)


def graham_scan_core(arr, stack, n):
	for k in range(3, n):
		while len(stack) > 0:
			if (arr[k-1][0] * arr[k][1] - arr[k][0] * arr[k-1][1]) < 0:
				stack = pop(stack)
				continue
			else:
				break
		push(stack, arr[k])
	return stack

def pop(stack):
	if len(stack) <= 0:
		return 0
	else:
		return stack.pop()

def push(stack, x):
	if len(stack <= 0):
		return 0
	else:
		return stack.append(x)

def CHDC(p):
	n = len(p)
	if n <= 3: return p
	c1 = CHDC(p[: n/2])
	c2 = CHDC(p[n/2 + 1 :])
	return combine(c1, c2)

def combine(c1, c2):
	small = c1[0][0]
	for i in range(1, len(c1)):
		if small > c1[i][0]:
			small = c1[i][0]
	count = 0
	for j in range(0, len(c2)):
		if small > c2[j][0]:
			count = count + 1
	if count >= 1:
		temp = c1
		c1 = c2
		c2 = temp
	# sort c1 with code from prob1