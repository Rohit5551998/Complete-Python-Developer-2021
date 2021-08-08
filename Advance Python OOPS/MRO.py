#MRO - Method Order Resolution

class A:
	num = 10

class B(A):
	pass

class C(A):
	num = 1

class D(B, C):
	pass

d = D()
print(D.mro())