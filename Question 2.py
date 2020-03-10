# Modification from https://www.geeksforgeeks.org/search-a-word-in-a-2d-grid-of-characters/

class Engine: 
	  
	def __init__(self): 
		self.R = None
		self.C = None
		self.direction = [[1, 0], [1, -1], [0, -1], [-1, -1],
							[-1, 0], [-1, 1], [0, 1], [1, 1]
							] 
					  
	def searching(self, grid, row, col, word):
		result = 0

		if grid[row][col] != word[0]: 
			return result
			  
		for x, y in self.direction: 
			  
			# print("Direction: {0},{1}".format(x,y))
			rd, cd = row + x, col + y 
			# print("Position: {0},{1}".format(rd,cd))

			flag = True

			for k in range(1, len(word)): 
				if (0 <= rd <self.R and 
					0 <= cd < self.C and 
					word[k] == grid[rd][cd]): 
					  
					rd += x 
					cd += y 
				else: 
					flag = False
					# print("not")
					break
	   
			if flag: 
				result += 1
		return result
		  

	def wordSearch(self, grid, word): 
		result = 0

		self.R = len(grid) 
		self.C = len(grid[0]) 

		for row in range(self.R): 
			for col in range(self.C): 
				temp = self.searching(grid, row, col, word)
				result = result + temp
		return result

if __name__ == '__main__':
	f=open("input.in", "r")
	grid_list = []
	letters_list = []
	word_list = []
	# T = int(input())
	T = int(f.readline())
	for x in range (T):
		# N = int(input())
		# M = int(input())
		N = int(f.readline())
		M = int(f.readline())
	
		for y in range(N):
			#letters = input()
			letters = (f.readline())[:-1]
			letters_list.append(letters)
		grid_list.append(letters_list)
		letters_list = []
		# W = input("")
		W = (f.readline())[:-1]
		word_list.append(W)
		
	engine = Engine()
	for x in range(T):
		result = engine.wordSearch(grid_list[x], word_list[x]) 
		print("Case {0}: {1}".format(x+1,result))


