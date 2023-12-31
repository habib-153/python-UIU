def str_len(str):
	count = 0
	for i in str:
		count += 1
	return count

def find_substr(a,b):
	if str_len(b) > str_len(a):
		b,a = a,b
	if b in a:
		print("1")
	else:
		print("0")
		
input_str = list(map(str, input().split()))
find_substr(input_str[0], input_str[1])