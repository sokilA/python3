#!/usr/bin/python3

class Note():
    def __init__(self, title: str, todo: str, done: bool = False):
        self._title = title.replace('\n', '')
        self._todo = todo
        self._done = done

    @property
    def get_title(self):
        return self._title

    @property
    def get_todo(self):
        return self._todo

    @property
    def is_done(self):
        return self._done


class Model():
    def __init__(self):
        self.filename = 'todolist.txt'

    def add_note(self, note) -> None:
        self.del_note(note.get_title)
        is_done = '+' if note.is_done else '-'
        with open(self.filename, 'a') as f:
            data = note.get_title + ' ' + is_done + '\n' + \
                   note.get_todo + '\n'
            f.write(data)
            f.flush()

    def get_note(self, title: str) -> Note:
        note = None
        with open(self.filename, 'r') as f:
            for line in f:
                if line == str(title) + ' ' + '-' + '\n' or \
                        line == str(title) + ' ' + '+' + '\n':
                    todo = f.__next__().replace('\n', '')
                    is_done = line[-2] == '+'
                    note = Note(title, todo, is_done)
                    break
        return note

    def get_notes(self) -> list:
        with open(self.filename, 'r') as f:
            is_title = True
            for line in f:
                if is_title:
                    title = line[:-3]
                    is_done = line[-2] == '+'
                    is_title = False
                else:
                    is_title = True
                    yield Note(title, line[:-1], is_done)

    def del_note(self, title: str) -> None:
        lines = ''
        with open(self.filename, 'r') as f:
            lines = f.readlines()
        with open(self.filename, 'w') as f:
            is_prev_deleted = False
            for line in lines:
                if is_prev_deleted:
                    is_prev_deleted = False
                    continue
                if not (line == str(title) + ' ' + '-' + '\n' or \
                        line == str(title) + ' ' + '+' + '\n'):
                    f.write(line)
                else:
                    is_prev_deleted = True

    def modify_title(self, old_title: str, new_title: str) -> None:
        note = self.get_note(old_title)
        if not self.get_note(new_title) and note:
            self.del_note(old_title)
            self.add_note(Note(new_title, note.get_todo, note.is_done))
        else:
            pass

    def modify_todo(self, title: str, todo: str) -> None:
        note = self.get_note(title)
        if note:
            self.del_note(title)
            self.add_note(Note(title, todo, note.is_done))
        else:
            pass

    def modify_done(self, title: str) -> None:
        note = self.get_note(title)
        self.del_note(title)
        self.add_note(Note(title, note.get_todo, not note.is_done))


class View():
    def input_choice(self) -> int:
        welcome_text = "1.Add note\n2.Show note\n3.Show all\n" + \
                       "4.Delete note\n5.Modify note\n0.Quit"
        print(welcome_text)
        return int(input())

    def input_modify_choice(self) -> int:
        welcome_text = "1.Modify title\n2.Modify todo\n3.Modify done"
        print(welcome_text)
        return int(input())

    def input_note(self) -> Note:
        title = self.input_title()
        todo = self.input_todo()
        return Note(title, todo)

    def input_title(self, newer: str = '') -> str:
        title = input("Input {0}note`s title: ".format(newer))
        return title

    def input_todo(self, newer: str = '') -> str:
        title = input("Input {0}note`s todo: ".format(newer))
        return title

    def output_note(self, note) -> None:
        if note:
            print("Title:", note.get_title)
            print("Todo:", note.get_todo)
            print("Is done:", note.is_done)
        else:
            print("Note not exists")

    def output_notes(self, notes: list) -> None:
        for note in notes:
            self.output_note(note)
            print()


class Controller():
    def __init__(self):
        self.model = Model()
        self.view = View()

    def run(self) -> None:
        while (True):
            choice = self.view.input_choice()
            if choice == 0: break
            if choice == 1:
                self.model.add_note(self.view.input_note())
            elif choice == 2:
                self.view.output_note(self.model.get_note(
                    self.view.input_title()))
            elif choice == 3:
                self.view.output_notes(self.model.get_notes())
            elif choice == 4:
                self.model.del_note(self.view.input_title())
            elif choice == 5:
                modify_choice = self.view.input_modify_choice()
                if modify_choice == 1:
                    self.model.modify_title(self.view.input_title(),
                                            self.view.input_title('new '))
                elif modify_choice == 2:
                    self.model.modify_todo(self.view.input_title(),
                                           self.view.input_todo('new '))
                elif modify_choice == 3:
                    self.model.modify_done(self.view.input_title())
                else:
                    pass
            else:
                raise ValueError("Incorrect choice")


def main():
    controller = Controller()
    controller.run()


main()
