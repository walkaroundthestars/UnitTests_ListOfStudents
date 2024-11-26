import pytest

from unittest.mock import patch, mock_open
from studentsAttendance import import_students, add_student, remove_student, export_students, check_students, edit_students


# Test funkcji import_students
def test_import_students(self):
    #want
    want = {"Jan Kowalski": True, "Maria Antonina": True, "Stanisław Dziąsło": True}
    #got
    result = import_students("students.txt")
    #when
    assert result == want

# Test funkcji add_student
def test_add_student(self):
    #want
    studentName = "Agnieszka Kowalska"
    students = {}
    filePath = "students.txt"
    #got
    students = add_student(studentName, filePath)
    #when


# Test funkcji remove_student
def test_remove_student(self):
    pass


# Test funkcji export_students
def test_export_students(monkeypatch):
    m = mock_open()
    monkeypatch.setattr("builtins.open", m)

    students = {"Jan Kowalski": True, "Maria Nowak": False}
    export_students("studentsAttendance.txt", students)

    m().write.assert_any_call("Jan Kowalski                   - obecny\n")
    m().write.assert_any_call("Maria Nowak                    - nieobecny\n")


# Test funkcji check_students
def test_check_students(monkeypatch):
    inputs = iter(["T", "N"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    students = {"Jan Kowalski": False, "Maria Nowak": False}
    check_students(students)

    assert students["Jan Kowalski"] is True
    assert students["Maria Nowak"] is False


# Test funkcji edit_students
def test_edit_students(monkeypatch):
    inputs = iter(["Jan Kowalski", "T"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    students = {"Jan Kowalski": False}
    edit_students(students)

    assert students["Jan Kowalski"] is True
