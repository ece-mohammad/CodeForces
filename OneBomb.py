#http://codeforces.com/problemset/problem/699/B

import logging as log

def filter_by_column(column, distribution):
	#return a modified dist with elemnts that don't have 
	#column == column ex:
	#filter_by_column(1, [(0,1),(0,0),(0,2)]) >> [(0,0),(0,2)]
	temp = []
	for cell in distribution:
		if cell[1] != column:
			temp.append(cell)
	return temp


def filter_by_row(row, distribution):
	#return a modified dist with elemnts that don't have 
	#row == row ex:
	#filter_by_row(0, [(0,1),(0,0),(0,2)]) >> []
	temp = []
	for cell in distribution:
		if cell[0] != row:
			temp.append(cell)
	return temp


def same_row(distribution):
	
	#if dist is not empty
	if distribution:
		length = len(distribution)
		#loop over dist and return False if dist[index][0] != dist[index+1][0]
		for index in range(length - 1):
			if distribution[index][0] != distribution[index+1][0]:
				return False
	
	#return True if dist is empty
	return True

def same_column(distribution):
	
	#if dist is not empty
	if distribution:
		length = len(distribution)
		#loop over dist and return False if dist[index][1] != dist[index+1][1]
		for index in range(length - 1):
			if distribution[index][1] != distribution[index+1][1]:
				return False
	
	#return True if dist is empty
	return True



def OneBomb():
	
	log.basicConfig(level=log.DEBUG)
	
	wall = '*'
	
	n_rows, n_columns = map(int, input().split())
	
	rows_density = [0]*n_rows
	columns_density = [0]*n_columns
	wall_distribution = []
	
    #clacultae the row_density, columns_density and wall_distribution
    #by iterating over every cell in each row
	for row in range(n_rows):
		
		current_row = input().strip()
		rows_density[row] += current_row.count(wall)
		log.debug("current_row string: {}".format(current_row))
		for column in range(n_columns):
			log.debug('column index: {}'.format(column))
			if current_row[column] == wall:
				columns_density[column] += 1
				wall_distribution.append((row+1, column+1))
	
	log.info('distribution: {}\nrow_density: {}\ncolumns_density:{}'.format(wall_distribution, rows_density, columns_density))
	
	#the column, row containing most walls
	max_column_density = columns_density.index(max(columns_density))+1
	max_row_density = rows_density.index(max(rows_density))+1
	log.info('max_column_density:{}\nmax_row_density:{}'.format(max_column_density, max_row_density))
	
	
	#check if walls are aligned more vertically than horizontally
	#more walls in the same column than walls in the same row
	if max(columns_density) > max(rows_density):
		#if walls are vertical, remove 
		mod_density = filter_by_column(max_column_density, wall_distribution)
		log.info("mod_density:",*mod_density)
		if same_row(mod_density):
			print('YES')
			if mod_density:
				print(mod_density[0][0], max_column_density)
			else:
				print(1, max_column_density)
		else:
			print('NO')
	
	else:
		mod_density = filter_by_row(max_row_density, wall_distribution)
		if same_column(mod_density):
			print('YES')
			if mod_density:
				print(max_row_density, mod_density[0][1])
			else:
				print(max_row_density, 1)
		else:
			print('NO')


if __name__ == '__main__':
	OneBomb()
