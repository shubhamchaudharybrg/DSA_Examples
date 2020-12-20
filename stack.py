class Stack():
	def __init__(self,*args):    # Argument can only be list or integer
		if type(args[0]) == list:
			if all([type(i) == int for i in args[0]])==True:
				self.list = [i for i in args[0]]
			else:
				raise TypeError('Argument must be integers or list.')
		elif type(args[0]) != list:
			if all([type(i) == int for i in args])==True:
				self.list = list(args)
			else:
				raise TypeError('Argument must be integers or list.')
	
	def __repr__(self):
		return f'Stack({self.list})'
	
	def PUSH(self,num):
		self.list.append(num)
	
	def POP(self):
		var = self.list.pop()
		return var


if __name__ == '__main__':
	s = Stack([(2,3,4,5,6)])
	print(s)
	s.PUSH(8)
	print(s)
	s.POP()
	print(s)
