class Queue():
	def __init__(self,*args):    #argument can only be list and integers
		if type(args[0]) == list:
			if all([type(i)==int for i in args[0]]):
				self.list = [i for i in args[0]]
			else:
				raise TypeError('Argument must be integers and list')
		
		else:
			if all([type(i)==int for i in args]) == True:
				self.list = list(args)
			else:
				raise TypeError('Argument must be integers and list')

	def __repr__(self):
		return f'Queue({self.list})'	

	def STORE(self,num):
		self.list.append(num)

	def RETRIEVE(self):
		var = self.list[0]
		del self.list[0]
		return var


if __name__ == '__main__':
	q = Queue(2,3,4,5,6)
	print(q)
	q.STORE(8)
	print(q)
	a = q.RETRIEVE()
	print(q)
	print(a)
