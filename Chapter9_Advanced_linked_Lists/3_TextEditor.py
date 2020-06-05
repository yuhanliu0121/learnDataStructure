#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Yuhan Liu
# @E-mail  : yxl1837@miami.edu
# @File    : 3_TextEditor.py
# @Software: PyCharm


class EditBuffer(object):

    def __init__(self):
        self._first_line = _EditBufferNode(text=['\n'])
        self._last_line = self._first_line
        self._current_line = self._first_line
        self._current_column_index = 0
        self._current_line_index = 0
        self._num_lines = 1
        self._insert_mode = True

    # Returns the number of lines in the text buffer.
    def num_lines(self):
        return self._num_lines

    # Returns the length of the current line that includes the newline character
    def num_chars(self):
        return len(self._current_line.text)

    # Returns the line index of the line containing the cursor. The first line has an index of 0
    def line_index(self):
        return self._current_line_index

    # Returns the column index of the cursor within the current line. The first position in each line has an index of 0
    def column_index(self):
        return self._current_column_index

    # Sets the entry mode to either insert or overwrite based on the value of the boolean argument insert.
    # True: insert mode
    # False: overwrite mode
    def set_entry_mode(self, insert=True):
        self._insert_mode = insert

    # Toggles the entry mode to either insert ot overwrite based on the current mode.
    def toggle_entry_mode(self):
        self._insert_mode = not self._insert_mode

    # Returns true if the current entry mode is set to insert and false otherwise
    def in_insert_mode(self):
        return self._insert_mode is True

    # Returns the character at the current cursor position
    def get_char(self):
        return self._current_line.text[self._current_column_index]

    # Returns the contents of the current line as a string that includes the newline character
    # If show_mode is True, the string will also include the position of the cursor
    def get_line(self, show_mode=False):
        if not show_mode:
            return ''.join(self._current_line.text)
        else:
            cursor_str_list = [' ' for i in range(self._current_column_index)]
            cursor_str_list.append('^\n')
            return ''.join(self._current_line.text) + ''.join(cursor_str_list)

    # Moves the cursor up num lines. The cursor is kept at the same character position unless the new line is shorter,
    # in which case the cursor is placed at the end of the new lin, The num us negative, and the cursor position is not changed.
    def move_up(self, num=1):
        if num > self._current_line_index:
            num = self._current_line_index
        self._current_line_index -= num

        for _ in range(num):
            self._current_line = self._current_line.prev

        if len(self._current_line.text) - 1 < self._current_column_index:
            self._current_column_index = len(self._current_line.text) - 1

    # The same as move_up() except the cursor is moved down
    def move_down(self, num=1):
        if num > (self._num_lines - 1) - self._current_line_index:
            num = (self._num_lines - 1) - self._current_line_index
        self._current_line_index += num

        for _ in range(num):
            self._current_line = self._current_line.next

        if len(self._current_line.text) - 1 < self._current_column_index:
            self._current_column_index = len(self._current_line.text) - 1

    # Moves the cursor to the document's home position, which is the first line and first character position in that line.
    def move_doc_home(self):
        self._current_line = self._first_line
        self._current_line_index = 0
        self._current_column_index = 0

    # Moves the cursor to the document's end position, which is the last line and first character position in that line
    def move_doc_end(self):
        self._current_line = self._last_line
        self._current_line_index = self._num_lines - 1
        self._current_column_index = 0

    # Moves the cursor to the left one position. The cursor is warpped to the end ot hte previous line if it is currently at the front of a line.
    def move_left(self):
        if self._current_column_index == 0:
            if self._current_line is not self._first_line:
                self._current_line = self._current_line.prev
                self._current_line_index -= 1
                self._current_column_index = len(self._current_line.text) - 1
        else:
            self._current_column_index -= 1

    # Moves the cursor to the right one position. The cursor is warpped to the beginning of the next line if  it is currently positioned at the end of a line.
    def move_right(self):
        if self._current_column_index == len(self._current_line.text) - 1:
            if self._current_line is not self._last_line:
                self._current_line = self._current_line.next
                self._current_line_index += 1
                self._current_column_index = 0
        else:
            self._current_column_index += 1

    # Moves the cursor to the front of the current line at the first character position
    def move_line_home(self):
        self._current_column_index = 0

    # Moves the cursor the end of the current line.
    def move_line_end(self):
        self._current_column_index = len(self._current_line.text) - 1

    # Starts a new line at the cursor position. A newline character is inserted at the current position and all
    # chatacters following are moved to a new line. the new line is inserted immediately following the current line
    # and the cursor is adjusted to be at the first position of the new line.
    def break_line(self):
        new_line = _EditBufferNode(text=['\n'])

        new_line.prev = self._current_line
        new_line.next = self._current_line.next

        if self._current_line.next is not None:
            self._current_line.next.prev = new_line
        self._current_line.next = new_line

        if self._current_line is self._last_line:
            self._last_line = new_line

        self._current_line = new_line

        self._current_column_index = 0
        self._current_line_index += 1

        self._num_lines += 1

    # Removes the entire line containing the cursor. The cursor is then moved to the front of the next line. If the
    # line being deleted is the last line, the cursor is moved to the front of the previous line.
    def delete_line(self):
        if self._num_lines != 1:
            if self._current_line is self._first_line:
                self._current_line.next.prev = None
                self._current_line = self._current_line.next
                self._num_lines -= 1
                self._current_column_index = 0

                self._first_line = self._current_line

            elif self._current_line is self._last_line:
                self._current_line.prev.next = None
                self._current_line = self._current_line.prev
                self._current_column_index = 0
                self._current_line_index -= 1
                self._num_lines -= 1

                self._last_line = self._current_line
            else:
                self._current_line.prev.next = self._current_line.next
                self._current_line.next.prev = self._current_line.prev
                self._current_line = self._current_line.next
                self._current_column_index = 0
                self._num_lines -= 1

    # Removes all of the characters at the end of the current line starting at the cursor position.
    # the newline character is not removed and the cursor is left at the end of the current line.
    def truncate_line(self):
        new_text = [ch for ch in self._current_line.text[:self._current_column_index + 1]]
        new_text.append('\n')

        self._current_line.text = new_text

    # Inserts the given character into the buffer at the current position. If the current entry mode is insert,
    # the character is inserted and the following characters on that line are shifted down; in overwrite mode,
    # the character at the current position is replaced. If the cursor is currently at a newline character and the
    # entry mode is overwrite, the new character is inserted at the end of the line. The cursor is advanced one
    # position. If ch is the newline character, then a line break occurs, which is the same as calling break_line()
    def add_char(self, ch):
        if ch == '\n':
            self.break_line()

        else:
            if self._insert_mode:
                self._current_line.text.insert(self._current_column_index, ch)

            elif self._current_line.text[self._current_column_index] == '\n':
                self._current_line.text.insert(-1, ch)
            else:
                self._current_line.text[self._current_column_index] = ch

            self._current_column_index += 1

    # Removes the character at the current position and leaves the cursor at the same position
    def delete_char(self):
        self._current_line.text.pop(self._current_column_index)

    # Removes the character preceding the current position and moves the cursor left one position. If the cursor is
    # currently at teh front of the line, the newline character on teh preceding line is removed and teh current line
    # and the preceding line are merged in to a single line
    def robout_char(self):
        if self._current_column_index == 0 and self._current_line is not self._first_line:
            self._current_line.prev.text.pop(-1)
            self._current_column_index = len(self._current_line.prev.text) - 1
            self._current_line.prev.text.extend(self._current_line.text)

            self.delete_line()
            if self._current_line is not self._last_line:
                self.move_up(1)
        else:
            new_text = self._current_line.text[self._current_column_index:]
            self._current_line.text = new_text
            self._current_column_index = 0

    # Deletes the entire contents of the buffer and resets it to the same state as in the constructor
    def delete_all(self):
        self.__init__()

    # Show the entire contents of the buffer
    def show_all(self):
        current_line_temp = self._first_line
        loop_count = 0
        while current_line_temp is not None:
            if loop_count == self._current_line_index:
                print(self.get_line(True),end='')
            else:
                print(''.join(current_line_temp.text),end='')
            loop_count += 1
            current_line_temp = current_line_temp.next


class _EditBufferNode(object):
    def __init__(self, prev=None, text=None, next=None):
        self.prev = prev
        self.text = text
        self.next = next


def main():
    print("creat a new EditBuffer")
    edit_buffer = EditBuffer()
    print()
    print("show all: ")
    edit_buffer.show_all()
    print()

    string1 = "def robout_char(self):\n"
    string2 = '    if self._current_column_index == 0 and self._current_line is not self._first_line:\n'
    string3 = '        self._current_line.prev.text.pop(-1)\n'
    string4 = '        self._current_column_index = len(self._current_line.prev.text) - 1\n'
    string5 = '        self._current_line.prev.text.extend(self._current_line.text)\n'
    string6 = '\n'
    string7 = "        self.delete_line()\n"
    string8 = "        if self._current_line is not self._last_line:\n"
    string9 = "        self.move_up(1)\n"

    string_list = [string1, string2, string3, string4, string5, string6, string7, string8, string9]
    print("add characters to the edit buffer")
    for string in string_list:
        # print("now adding the string: %s" % string)
        for char in string:
            # print("now adding: %s" % char)
            edit_buffer.add_char(char)

    print("show all: ")
    edit_buffer.show_all()
    print()

    print("move to the front of the first line and move 20 right:")
    edit_buffer.move_doc_home()
    for _ in range(20):
        edit_buffer.move_right()

    edit_buffer.show_all()
    print()

    print("move down for 2")
    edit_buffer.move_down(2)
    edit_buffer.show_all()
    print()


    print("number of lines: %d" % edit_buffer.num_lines())      # Expected: 10
    print("number of characters: %d" % edit_buffer.num_chars())     # Expected: 45 (44 characters + '\n')
    print("line index: %d " % edit_buffer.line_index())     # Expected: 2
    print("column index: %d" % edit_buffer.column_index())      # Expected: 20
    print()

    print("get character of the current cursor: %s" % edit_buffer.get_char())
    print()
    print("get line: %s " % edit_buffer.get_line())

    print("move 10 right: ")
    for _ in range(10):
        edit_buffer.move_right()
    edit_buffer.show_all()
    print()
    
    print("move up for 100:")
    edit_buffer.move_up(100)
    edit_buffer.show_all()
    print()
    
    print("move down by 2 and move right by 20 :")
    edit_buffer.move_down(2)
    for _ in range(20):
        edit_buffer.move_right()
    edit_buffer.show_all()
    print()
    
    print("move down by 4:")
    edit_buffer.move_down(4)
    edit_buffer.show_all()
    print()
    
    print("move  to the end of the file:")
    edit_buffer.move_doc_end()
    edit_buffer.show_all()
    print()
    
    print("move left:")
    edit_buffer.move_left()
    edit_buffer.show_all()
    print()
    
    print("move right:")
    edit_buffer.move_right()
    edit_buffer.show_all()
    print()
    
    print("move up by 2 and right by 16:")
    edit_buffer.move_up(2)
    for _ in range(16):
        edit_buffer.move_right()
    edit_buffer.show_all()
    print()
    
    print("move line home: ")
    edit_buffer.move_line_home()
    edit_buffer.show_all()
    print()
    
    print("move line end: ")
    edit_buffer.move_line_end()
    edit_buffer.show_all()
    print()  
    
    print("break line: ")
    edit_buffer.break_line()
    edit_buffer.show_all()
    print()

    print("delete line:")
    edit_buffer.delete_line()
    edit_buffer.show_all()
    print()

    print("move up by 6")
    edit_buffer.move_up(6)
    edit_buffer.show_all()
    print()

    print("delete line:")
    edit_buffer.delete_line()
    edit_buffer.show_all()
    print()

    print("move right by 30")
    for _ in range(30):
        edit_buffer.move_right()
    edit_buffer.show_all()
    print()

    print("truncate line: ")
    edit_buffer.truncate_line()
    edit_buffer.show_all()
    print()

    print("move to line home: ")
    edit_buffer.move_line_home()
    edit_buffer.show_all()
    print()

    print("rubout char:")
    edit_buffer.robout_char()
    edit_buffer.show_all()
    print()

    print("move right by 30")
    for _ in range(30):
        edit_buffer.move_right()
    edit_buffer.show_all()
    print()

    print("rubout char: ")
    edit_buffer.robout_char()
    edit_buffer.show_all()
    print()

    print("delete all")
    edit_buffer.delete_all()
    edit_buffer.show_all()
    print()
        

if __name__ == "__main__":
    main()
