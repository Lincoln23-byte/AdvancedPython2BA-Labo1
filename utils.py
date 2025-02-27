
from scipy.integrate import quad
def fact(n):
    assert n>= 0
    res = 1
    while n > 0:
        res*=n
        n= n-1
    return res	

def roots(a, b, c):
    delta= b**2 - 4*a*c
    if delta > 0:
        x1= (-b-(delta**0.5))/(2*a)
        x2= (-b+(delta**0.5))/(2*a)
        sol=x1, x2
    if delta == 0:
        x0= -b/(2*a)
        sol=x0
    if delta < 0:
        sol= "No solution"
    return sol

def integrate(function, lower, upper):
	def fun(x):
		return eval(function)
	return quad(fun, lower, upper)[0]

	"""Approximates the integral of a fonction between two bounds
	
	Pre: 'function' is a valid Python expression with x as a variable,
		'lower' <= 'upper',
		'function' continuous and integrable between 'lower‘ and 'upper'.
	Post: Returns an approximation of the integral from 'lower' to 'upper'
		of the specified 'function'.

	Hint: You can use the 'integrate' function of the module 'scipy' and
		you'll probably need the 'eval' function to evaluate the function
		to integrate given as a string.
	"""

if __name__ == '__main__':
	print(fact(5))
	print(roots(1, 0, 1))
	print(integrate('x ** 2 - 1', -1, 1))
