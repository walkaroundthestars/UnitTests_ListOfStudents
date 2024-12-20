from datetime import datetime


def menu():
    print("Wybierz opcję:")
    print("1. Importuj studentów z pliku")
    print("2. Dodaj nowego studenta")
    print("3. Zaznacz obecność studenta")
    print("4. Edytuj obecność studenta")
    print("5. Usuń studenta z bazy")
    print("6. Zapisz listę studentów do pliku")
    print("7. Wyjdź")
    wybor = input("Wybierz opcję: ")
    return wybor


def import_students(file_path, students_list=None):
    if students_list is None:
        students_list = {}
    try:
        with open(file_path, "r") as file:
            for line in file:
                students = line.strip().split(",")
                for student in students:
                    if student != "":
                        students_list[student.strip()] = True
                    elif student == "":
                        pass
                    elif student.count(" ") == 0:
                        print("Zły format studenta!")
            print("Lista studentów zaimportowana pomyślnie.")
    except FileNotFoundError:
        print("Plik nie istnieje. Zaczynamy z pustą listą.")
    return students_list


def add_student(students_list, file_path, name):
    with open(file_path, "a") as file:
        if name.count(" ") == 0:
            print("Zły format studenta!")
        else:
            students_list[name.strip()] = True
            file.write(name + ",")
    print("Student został dodany pomyślnie")
    return students_list


def remove_student(file_path, students_list, name):
    if name in students_list:
        students_list.pop(name)
    else:
        print("Takiego studenta nie ma w bazie")
    with open(file_path, "w") as file:
        for student in students_list.keys():
            file.write(student + ",")
    print("Student został usunięty")


# TODO: checking if TODO is working correctly
def export_students(file_path2, students_list):
    with open(file_path2, "a") as file:
        file.write(str(datetime.now()) + "\n")
        for student, attendance in students_list.items():
            if attendance:
                file.write(f"{student:30} - obecny\n")
            else:
                file.write(f"{student:30} - nieobecny\n")
    print("Lista studentów zapisana pomyślnie.")


# TODO: another todo
def check_students(students_list, name, attendance):
    if attendance.upper() == "T":
        students_list[name] = True
    elif attendance.upper() == "N":
        students_list[name] = False
    else:
        raise Exception("Nieprawidłowa obecność. Edytuj póżniej.")


# TODO: and another todo
def edit_students(students_list, name, attendance):
    if attendance.upper() == "T":
        students_list.update({name: True})
    elif attendance.upper() == "N":
        students_list.update({name: False})
    else:
        raise Exception("Nieprawidłowa obecność.")


# TODO: if potato can become vodka, I can learn CI
# Issue URL: https://github.com/walkaroundthestars/UnitTests_ListOfStudents/issues/4
def main():
    file_path = "students.txt"
    file_path2 = "studentsAttendance.txt"
    students_list = {}

    while True:
        wybor = menu()
        if wybor == "1":
            students_list = import_students(file_path)
        elif wybor == "2":
            name = input("Podaj imię i nazwisko studenta do dodania: ")
            add_student(students_list, file_path, name)
        elif wybor == "3":
            for student in students_list:
                print(f"czy {student} jest obecny? ")
                attendance = input("T/N: ")
                check_students(students_list, student, attendance)
        elif wybor == "4":
            name = input("Podaj imię studenta: ")
            attendance = input("Czy był obecny? T/N: ")
            edit_students(students_list, name, attendance)
        elif wybor == "5":
            name = input("Podaj imię i nazwisko studenta do usunięcia: ")
            remove_student(file_path, students_list, name)
        elif wybor == "6":
            export_students(file_path2, students_list)
        elif wybor == "7":
            exit()
        else:
            print("Błędny wybór")


if __name__ == "__main__":
    main()
