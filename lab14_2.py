#!/usr/bin/env python3

class phone_book_member():
    def __init__(self, first_name: str, second_name: str, phone_number: str):
        self._first_name = first_name
        self._second_name = second_name
        self._phone_number = phone_number

    @property
    def get_name(self):
        return self._first_name

    @property
    def get_fname(self):
        return self._second_name

    @property
    def get_number(self):
        return self._phone_number


class Model():
    def __init__(self):
        self.filename = 'phonebook.txt'

    def add_member(self, member) -> None:
        with open(self.filename, 'a') as f:
            data = member._first_name + ' ' + member._second_name + '\n' + \
                   member.get_number + '\n'
            f.write(data)
            f.flush()

    def get_member(self, first_name: str, second_name: str) -> phone_book_member:
        member = None
        with open(self.filename, 'r') as f:
            for line in f:
                if line == str(first_name) + ' ' + str(second_name) + '\n':
                    phone_number = f.__next__()
                    phone_number = phone_number.replace('\n', '')
                    member = phone_book_member(first_name, second_name, phone_number)
                    break
        return member

    def get_members(self) -> list:
        with open(self.filename, 'r') as f:
            is_name = True
            full_name = []
            for line in f:
                line = line.replace('\n', '')
                if is_name:
                    full_name = line.split(' ')
                    is_name = False
                else:
                    is_name = True
                    yield phone_book_member(full_name[0], full_name[1], line)

    def del_member(self, first_name: str, second_name: str) -> None:
        lines = ''
        with open(self.filename, 'r') as f:
            lines = f.readlines()
        with open(self.filename, 'w') as f:
            is_prev_deleted = False
            for line in lines:
                if is_prev_deleted:
                    is_prev_deleted = False
                    continue
                if line != str(first_name) + ' ' + str(second_name) + '\n':
                    f.write(line)
                else:
                    is_prev_deleted = True

    def del_member_phones(self, phone_number: str) -> None:
        lines = ''
        with open(self.filename, 'r') as f:
            lines = f.readlines()
        with open(self.filename, 'w') as f:
            is_prev_deleted = False
            temp_for_delete = ''
            temp_for_delete2 = ''
            for line in lines:
                temp_for_delete2 = temp_for_delete
                temp_for_delete = line

                if is_prev_deleted:
                    is_prev_deleted = False
                    continue
                if line != str(phone_number) + '\n':
                    f.write(temp_for_delete2)
                else:
                    is_prev_deleted = True
                    temp_for_delete = ''

            if temp_for_delete != str(phone_number) + '\n':
                f.write(temp_for_delete)


class View():
    def input_choice(self) -> int:
        welcome_text = "1.Add member\n2.Show member\n3.Show all\n" + \
                       "4.Delete member\n5.Delete member by phone number\n0.Quit"
        print(welcome_text)
        return int(input())

    def input_member(self) -> phone_book_member:
        first_name = input("Input member`s first_name: ")
        second_name = input("Input member`s second_name: ")
        phone_number = input("Input member`s phone number: ")
        return phone_book_member(first_name, second_name, phone_number)

    def input_name(self) -> tuple:
        first_name = input("Input member`s first_name: ")
        second_name = input("Input member`s second_name: ")
        return (first_name, second_name)

    def input_phone_number(self):
        phone_number = input("Input member`s phone_number: ")
        return phone_number

    def output_member(self, member) -> None:
        if member:
            print("Name:", member._first_name)
            print("FName:", member._second_name)
            print("Phone number:", member._phone_number)
        else:
            print("Member not exists")

    def output_members(self, members: list) -> None:
        for member in members:
            self.output_member(member)
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
                self.model.add_member(self.view.input_member())
            elif choice == 2:
                member_name = self.view.input_name()
                self.view.output_member(self.model.get_member(
                    member_name[0], member_name[1]))
            elif choice == 3:
                self.view.output_members(self.model.get_members())
            elif choice == 4:
                member_name = self.view.input_name()
                self.model.del_member(member_name[0], member_name[1])
            elif choice == 5:
                member_name = self.view.input_phone_number()
                self.model.del_member_phones(member_name)
            else:
                raise ValueError("Incorrect choice")


def main():
    controller = Controller()
    controller.run()


main()
