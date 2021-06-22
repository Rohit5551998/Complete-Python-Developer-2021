#nonlocal Scope

def outer():
	x = "local"
	def inner():
		nonlocal x
		x = "nonlocal"
		print(f"inner: {x}")

	inner()
	print(f"outer: {x}")

outer()