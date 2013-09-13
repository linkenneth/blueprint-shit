# Members: Jonathan Ho, Rohit Mukherjee, Kenneth lin

class Cube(object):
	def __init__(self, row_list):
		assert len(row_list) == 6
		self.top, self.left, self.front, self.right, self.back, self.bottom = row_list

	def __str__(self):
		s = ','.join(self.top) + '\n'
		s += ','.join(self.left) + '\n'
		s += ','.join(self.front) + '\n'
		s += ','.join(self.right) + '\n'
		s += ','.join(self.back) + '\n'
		s += ','.join(self.bottom) + '\n'
		return s

	def is_same(self, other):
		return str(self) == str(other)

	@classmethod
	def rotate_face(cls, face, direction): # Takes the face of a cube, and rotates it in the direction specified.
		if(direction=='L'):
			for i in range(3):
				face=cls.rotate_face(face,'R') # Just rotates right 3 times, resulting in the equivalent state of a left turn
		elif direction == 'R':
			face = [face[6], face[3], face[0], face[7], face[4], face[1], face[8], face[5], face[2]]
		elif direction == '2':
			face = [face[8], face[7], face[6], face[5], face[4], face[3], face[2], face[1], face[0]]
		else:
			assert False
		return face

	@classmethod
	def _move_front_right(cls, face, face_top, face_left, face_right, face_bottom, face_back): # Rotate the front face of the cube clockwise
		new_face = cls.rotate_face(face,'R')
		new_face_top = [face_top[0], face_top[1], face_top[2], face_top[3], face_top[4], face_top[5], face_left[8], face_left[5], face_left[2]]
		new_face_right = [face_top[6], face_right[1], face_right[2], face_top[7], face_right[4], face_right[5], face_top[8], face_right[7], face_right[8]]
		new_face_left = [face_left[0], face_left[1], face_bottom[0], face_left[3], face_left[4], face_bottom[1], face_left[6], face_left[7], face_bottom[2]]
		new_face_bottom = [face_right[6], face_right[3], face_right[0], face_bottom[3], face_bottom[4], face_bottom[5], face_bottom[6], face_bottom[7], face_bottom[8]]
		return cls([new_face_top, new_face_left, new_face, new_face_right, face_back, new_face_bottom])

	def _move_front(self, s):
		if s == 'right':
			return Cube._move_front_right(self.front, self.top, self.left, self.right, self.bottom, self.back)
		elif s == 'left':
			tmp_cube = self
			for i in range(3):
				tmp_cube = Cube._move_front_right(tmp_cube.front, tmp_cube.top, tmp_cube.left, tmp_cube.right, tmp_cube.bottom, tmp_cube.back)
			return tmp_cube
		else:
			assert False

	def _rotate_cube(self, d): # Reorients the cub, changing which face we consider the "front". For example, reorienting down will make the new front face the old top face
		if d == 'up':
			new_back_face = self.rotate_face(self.top, '2')
			new_bottom_face = self.rotate_face(self.back, '2')
			return Cube((self.front, self.rotate_face(self.left, 'L'), self.bottom, self.rotate_face(self.right, 'R'), new_back_face, new_bottom_face))
		elif d == 'down':
			new_back_face = self.rotate_face(self.top, '2')
			new_bottom_face = self.rotate_face(self.back, '2')
			return Cube((self.rotate_face(self.back, '2'), self.rotate_face(self.left, 'R'), self.top, self.rotate_face(self.right, 'L'), self.rotate_face(self.bottom, '2'), self.front))
		elif d == 'right':
			return Cube((self.rotate_face(self.top, 'L'), self.back, self.left, self.front, self.right, self.rotate_face(self.bottom, 'R')))
		elif d == 'left':
			return Cube((self.rotate_face(self.top, 'R'), self.front, self.right, self.back, self.left, self.rotate_face(self.bottom, 'L')))
		else:
			assert False

	def move(self, s): # A handler function for all the possible changes (rotate right/left, reorient up/down/right/left)
		if s == 'move_R':
			return self._move_front('right')
		elif s == 'move_L':
			return self._move_front('left')
		elif s == 'rotate_U':
			return self._rotate_cube('up')
		elif s == 'rotate_D':
			return self._rotate_cube('down')
		elif s == 'rotate_R':
			return self._rotate_cube('right')
		elif s == 'rotate_L':
			return self._rotate_cube('left')
		else:
			assert False
	VALID_MOVES = ['move_R', 'move_L', 'rotate_U', 'rotate_D', 'rotate_R', 'rotate_L']


	def is_solved(self): # Checks if the cube is solved by making sure that every element in every row's array representation matches the first element (all r's/y's etc)
		def all_same(l):
			x = l[0]
			for i in l:
				if i != x:
					return False
			return True

		return all_same(self.top) and all_same(self.bottom) and all_same(self.left) and all_same(self.right) and all_same(self.front) and all_same(self.back)

input_file = 'input2.txt' # Our cube input

lines = []
with open(input_file, 'r') as f:
	for line in f.readlines():
		lines.append(line.strip())

rows = []
for l in lines:
	rows.append(l.split(','))
print(rows)
print
orig_cube = Cube(rows)
print(orig_cube)
print ('after move_front right')
print(orig_cube._move_front('right'))

print ('after moving right then left')
print (orig_cube._move_front('left')._move_front('right'))

print ('after rotate up')
print (orig_cube._rotate_cube('right'))


print('==================')
#cube = orig_cube._move_front('right')._rotate_cube('up')._move_front('left')

# Breadth-first search over moves
cube = orig_cube
MAX_ITERS = 1000000000000
states = [([cube],[])] # State: ([seen cube states], [moves taken])
seen_states = set()
for i in range(MAX_ITERS):
	curr_state = states[0]
	states = states[1:]

	if curr_state[0][-1].is_solved():
		print('done')
		print("Moves:",i)
		print(list(map(str,curr_state)))
		break
	if curr_state[0][-1] in seen_states:
		continue
	seen_states.add(curr_state[0][-1])

	for m in Cube.VALID_MOVES:
		states.append((curr_state[0] + [curr_state[0][-1].move(m)], curr_state[1] + [m]))

