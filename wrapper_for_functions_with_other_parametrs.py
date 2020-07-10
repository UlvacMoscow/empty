a = {"a" : 1}
b = {"b" : 2}
c = {"c" : 3}

def change_mode(a=0, b=0, c=0, name_t=""):
	print(name_t)
	return print(a + b + c) 

def gen_name(name):
	return "func_{}".format(name)

def test_gen(chr_t):
	nm = gen_name([*chr_t.keys()][0])
	change_mode(**chr_t, name_t=nm)


test_gen(a)
test_gen(b)
test_gen(c)

