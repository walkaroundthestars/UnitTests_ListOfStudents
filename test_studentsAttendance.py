import pytest

from studentsAttendance import import_students, add_student, remove_student, export_students, check_students, edit_students


def test_import_students():
    #want
    filePath = 'Students_test.txt'
    want = {"Jan Kowalski": True, "Agata Malinowska": True}
    #got
    result = import_students(filePath)
    #when
    assert result == want

def test_add_student():
    #want
    name = "Agnieszka Kowalska"
    students = {}
    filePath = "students.txt"
    #got
    students = add_student(students, filePath, name)
    #when
    assert name in students

def test_remove_student():
    #want
    name = "Agnieszka Kowalska"
    filePath = "students.txt"
    students = import_students(filePath)
    #got
    remove_student(filePath,students, name)
    #when
    assert name not in students

def test_export_students():
    #want
    file_path = 'studentsAttendanceTest.txt'
    students = {"Agnieszka Kowalska": True, "Janko Muzykant": False}

    #got
    export_students("studentsAttendanceTest.txt", students)
    with open(file_path, "r") as file:
        studentsFile = file.read()

    #when
    assert "Agnieszka Kowalska" in studentsFile
    assert "Janko Muzykant" in studentsFile


def test_check_students(monkeypatch):
    #want
    inputs = iter(["T", "N"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    #got
    students = {"Jan Kowalski": False, "Maria Nowak": False}
    check_students(students)
    #when
    assert students["Jan Kowalski"] is True
    assert students["Maria Nowak"] is False


def test_edit_students(monkeypatch):

    #want
    inputs = iter(["Jan Kowalski", "T"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    name = "Jan Kowalski"
    students = {name : False}
    attendance = "T"

    #got
    edit_students(students, name, attendance)

    #when
    assert students["Jan Kowalski"] == True
