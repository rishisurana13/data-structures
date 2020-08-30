class Priv:

	def __say_hello(self):
		print('Hello World!')
	def say_hello(self):
		print('hi world!')

	def priv(self):
		self.__say_hello()

