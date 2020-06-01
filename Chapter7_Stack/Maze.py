from myarray2 import Array2D
from liststack import MyStack

class Maze(object):

    MAZE_WALL = '*'
    PATH_MARK = 'X'
    TRIED_MARK = 'o'

    def __init__(self, maze_file_path):

        self._maze = None
        self.start_cell = None
        self.end_cell = None
        self._initialize_maze(maze_file_path)

    def _initialize_maze(self, maze_file_path):

        with open(maze_file_path) as maze_file:
            num_rows, num_cols = self._read_value_pair(maze_file)
            start_row, start_col = self._read_value_pair(maze_file)
            end_row, end_col = self._read_value_pair(maze_file)

            self._maze = Array2D(num_rows, num_cols)
            self._maze.clear(' ')

            self.start_cell = _MazeCell(start_row - 1, start_col - 1)
            self.end_cell = _MazeCell(end_row - 1, end_col - 1)

            for row in range(self.num_rows):
                line = maze_file.readline()
                for col in range(self.num_cols):
                    if line[col] == '*':
                        self._set_wall(row, col)

    def draw_maze(self):

        for i in range(self.num_rows):
            print()
            for j in range(self.num_cols):
                if i == self.start_cell.row and j == self.start_cell.col:
                    print('S', end='\t')

                elif i == self.end_cell.row and j == self.end_cell.col:
                    print('E', end='\t')
                else:
                    print(self._maze[i, j], end='\t')

        print('\n\n')

    def _read_value_pair(self, file):
        line = file.readline()
        num1, num2 = line.split()
        return int(num1), int(num2)

    def _set_wall(self, row, col):
        self._maze[row, col] = self.MAZE_WALL

    def _set_path(self, row, col):
        self._maze[row, col] = self.PATH_MARK

    def _set_tried(self, row, col):
        self._maze[row, col] = self.TRIED_MARK

    @property
    def num_rows(self):
        return self._maze.num_rows()

    @property
    def num_cols(self):
        return self._maze.num_cols()

    def _valid_move(self, row, col):
        return self._maze[row, col] == ' '

    def _is_exit(self, row, col):
        return row == self.end_cell.row and col == self.end_cell.col

    def _next_nodes(self, row, col):
        if (row - 1) < self.num_rows and self._valid_move(row - 1, col):
            return _MazeCell(row - 1, col)

        if (row + 1) < self.num_rows and self._valid_move(row + 1, col):
            return _MazeCell(row + 1, col)

        if (col - 1) < self.num_cols and self._valid_move(row, col - 1):
            return _MazeCell(row, col - 1)

        if (col + 1) < self.num_cols and self._valid_move(row, col + 1):
            return _MazeCell(row, col + 1)

        return None

    def find_path(self):
        path = MyStack()

        current_cell = _MazeCell(self.start_cell.row, self.start_cell.col)
        path.push(current_cell)

        while not self._is_exit(current_cell.row, current_cell.col):
            #self.draw_maze()
            next_cell = self._next_nodes(current_cell.row, current_cell.col)

            if next_cell is not None:
                current_cell = next_cell
                self._set_path(current_cell.row, current_cell.col)
                path.push(current_cell)

            else:
                self._set_tried(current_cell.row, current_cell.col)
                path.pop()
                if path.is_empty():
                    return False
                else:
                    current_cell = path.peek()


        self.draw_maze()
        return True

class _MazeCell(object):
    def __init__(self, row, col):
        self.row = row
        self.col = col



def main():
    maze_file_path = "maze_file.txt"
    maze = Maze(maze_file_path)
    maze.draw_maze()
    print('\n\n')
    path = maze.find_path()
    print("Find path") if path else print("no path found")

if __name__ == "__main__":
    main()