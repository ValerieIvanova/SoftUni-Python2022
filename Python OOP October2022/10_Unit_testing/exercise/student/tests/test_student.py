from unittest import TestCase, main

from student import Student


class TestStudent(TestCase):
    def setUp(self) -> None:
        self.student = Student('Name')
        self.student_with_course = Student('Name2', {'math': ['notes']})

    def test_correct_initialization(self):
        self.assertEqual('Name', self.student.name)
        self.assertEqual({}, self.student.courses)
        self.assertEqual({'math': ['notes']}, self.student_with_course.courses)

    def test_add_notes_to_existing_course(self):
        result = self.student_with_course.enroll('math', ['first', 'second'])
        self.assertEqual(['notes', 'first', 'second'], self.student_with_course.courses['math'])
        self.assertEqual("Course already added. Notes have been updated.", result)

    def test_add_notes_to_non_existing_course_without_third_param(self):
        result = self.student.enroll('python', ['python is cool'])
        self.assertEqual(['python is cool'], self.student.courses['python'])
        self.assertEqual("Course and course notes have been added.", result)

    def test_add_notes_to_non_existing_course_with_third_param_Y(self):
        result = self.student.enroll('python', ['python is cool'], 'Y')
        self.assertEqual(['python is cool'], self.student.courses['python'])
        self.assertEqual("Course and course notes have been added.", result)

    def test_add_new_course_without_adding_the_notes(self):
        result = self.student.enroll('python', ['python is cool'], 'n')
        self.assertEqual([], self.student.courses['python'])
        self.assertEqual("Course has been added.", result)

    def test_add_notes_on_existing_course(self):
        result = self.student_with_course.add_notes('math', 'new note')
        self.assertEqual(['notes', 'new note'], self.student_with_course.courses['math'])
        self.assertEqual("Notes have been updated", result)

    def test_add_notes_to_non_existing_course(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes('math', 'n')
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_existing_course(self):
        result = self.student_with_course.leave_course('math')
        self.assertEqual({}, self.student_with_course.courses)
        self.assertEqual("Course has been removed", result)

    def test_leave_non_existing_course_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student_with_course.leave_course('java')
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))



if __name__ == '__main__':
    main()