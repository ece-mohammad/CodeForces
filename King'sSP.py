

class ChessPos(object):
	
	trans_1 = {k:v for v,k in enumerate("abcdefgh",1)}
	trans_2 = {k:v for k,v in enumerate("abcdefgh",1)}
	
	def __init__(self, square):
		self.x = ChessPos.trans_1[square[0]]
		self.y = int(square[1])
	
	def __sub__(self, other):
		return (self.x - other.x, self.y - other.y)
	
	def __str__(self):
		return "{}{}:({},{})".format(ChessPos.trans_2[self.x],self.y,self.x, self.y)


isPos = lambda x: x > 0
isNeg = lambda x: x < 0


def cross_direction(delta):
	
	if isPos(delta[0]):
		if isPos(delta[1]):		#(+ve, +ve)
			return "RU"
		elif isNeg(delta[1]):	#(+ve, -ve)
			return "RD"
			
	elif isNeg(delta[0]):
		if isPos(delta[1]):		#(-ve, +ve)
			return "LU"
		elif isNeg(delta[1]):	#(-ve, -ve)
			return "LD"


def str8_direction(delta):
	
	if isPos(delta[0]):
		return "R"
	elif isNeg(delta[0]):
		return "L"
	elif isPos(delta[1]):
		return "U"
	elif isNeg(delta[1]):
		return "D"


def KingSP():
	start = ChessPos(input())
	end = ChessPos(input())
	delta = end - start
	abs_delta = abs(delta[0]), abs(delta[1])

	steps = max(abs_delta)
	cross = abs(min(abs_delta))
	norm_delta = abs_delta[0] - cross, abs_delta[1] - cross
	
	#print('start:',start)
	#print('end:',end)
	#print('delta:',delta)
	#print('steps:', steps)
	#print('cross:', cross)
	#print('abs_delta:',abs_delta)
	#print('norm_delta:',norm_delta)
	
	print(steps)
	
	while(isPos(abs_delta[0]) and isPos(abs_delta[1])):
		print(cross_direction(delta))
		abs_delta = abs_delta[0]-1, abs_delta[1]-1
	
	delta = abs_delta[0]*((-1)**isNeg(delta[0])), abs_delta[1]*((-1)**isNeg(delta[1]))
	
	while(isPos(abs_delta[0]) or isPos(abs_delta[1])):
		print(str8_direction(delta))
		abs_delta = abs_delta[0] -1, abs_delta[1]-1
	
	
	
if __name__ == '__main__':
	
	KingSP()
