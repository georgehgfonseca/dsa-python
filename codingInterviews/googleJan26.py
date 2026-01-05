
ilhas - lagos

clica na ilha, retorna numero de lagos

'''
    0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19
0   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .
1   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .
2   .   .   X   X   X   .   .   .   .   .   *   .   .   .   .   .   .   .   .   .
3   .   .   .   .   .   .   .   .   .   .   *   X   X   X   X   X   X   .   .   .
4   .   .   .   .   .   X   X   X   .   .   *   X   *   X   *   *   X   .   .   .
5   .   .   .   .   .   X   .   X   .   .   *   X   X   X   X   X   X   .   .   .
6   .   .   .   .   .   X   X   X   .   .   *   *   *   .   .   .   .   .   .   .
7   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .

count_lakes(image, (2,2)) → 0
count_lakes(image, (6,6)) → 1
count_lakes(image, (12,5)) → 2

'''

# water doesn't connect diagonally
# a piece of water whose dfs doesn't reach the border belongs to a lake
# pre-compute connect components (cc) (one is the ocean the others are lakes) (do i need it?)
# when receiving a coord -> dfs from that coord and check/count which water cells (connect components) it touches minus the cc of the ocean

def count_lakes(image: List[List[char]], coord: Tuple[int]):
  # t O(n * m) s O(n * m)
  n, m = len(image), len(image[0])
  LAND = "X"
  NOT_COMPUTED = -1
  
  waterComponent = dict()
  
  # from land points
  visited = set()
  def dfs(coord): # O(n * m) number of cells
    visited.add(coord)
    left = (coord[0], coord[1] - 1)
    right = (coord[0], coord[1] + 1)
    top = (coord[0] + 1, coord[1])
    bottom = (coord[0] - 1, coord[1])
    neighs = [left, right, top, bottom]
    
    for neigh in neighs:
      offBounds = neigh[0] < 0 or neigh[0] >= n or neigh[1] < 0 or neigh[1] >= m 
      if not offBounds and neigh not in visited:
        if image[neigh[0]][neigh[1]] == LAND:
          dfs(neigh)
        else:
          # hit water, save to compute/check connected component later
          waterComponent[neigh] = NOT_COMPUTED
          
  component = -1
  
  def connectComponent(coord):  # O(n * m) number of cells
    waterComponent[coord] = component
    # to do improve code
    left = (coord[0], coord[1] - 1)
    right = (coord[0], coord[1] + 1)
    top = (coord[0] + 1, coord[1])
    bottom = (coord[0] - 1, coord[1])
    neighs = [left, right, top, bottom]
    for neigh in neighs:
      offBounds = neigh[0] < 0 or neigh[0] >= n or neigh[1] < 0 or neigh[1] >= m 
      if not offBounds and neigh in waterComponent and waterComponent[neigh] == NOT_COMPUTED:
        connectComponent(neigh)
      
    
  for water in waterComponent:
    if waterComponent[water] == NOT_COMPUTED:
      component += 1
      connectComponent(water)
      
  return component
