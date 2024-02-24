# ?11? x ?1 x ?1 = 192465
n = 192465
l = []
a = 0
w = ""
for i in range(11,192465): 
	k = n//i
	if n%i == 0:
		if int(str(k)[0]) > 0 and len(str(k))  > 3:
			if "11" in str(k):
				a = k
				l.append(k)
for i in range(1,100,10):
	if n//a == i:
		if str(i)[-1] =="1":
			w = str(i)
			l.append(i)
for i in range(1,100,10):
	if int(w) % i == 0:
		if str(i)[-1] =="1":
			l.append(i)
lst = []
for i in l:
	if len(str(i)) == 4:
		lst.append(str(i)[0])
		lst.append(str(i)[-1])
	elif i == 1:
		lst.append(0) 
	elif len(str(i)) != 0:
		lst.append(str(i)[0])
print(lst)