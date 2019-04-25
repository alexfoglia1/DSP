import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
tn = int(sys.argv[3])

u = 1
v = 0
u1 = 0
v1 = 1
   
while b != 0:
	q = int(a / b)
	rs, us, vs, a, u, v = a, u, v, b, u1, v1
	b = rs - q *b
	u1 = us - q*u
	v1 = vs - q*v1

x = (u*tn)/a
y = (v*tn)/a

print("x = {} y = {}".format(x,y))
