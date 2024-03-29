# Write your solution to main.py here!
from student import Student


def main():
    pablo = Student(1551515,
                    'William\\CP4\\practice_student_class\\pablo.txt')
    arlo = Student(1231231,
                   'William\\CP4\\practice_student_class\\arlo.txt')
    nicole = Student(1234567,
                     'William\\CP4\\practice_student_class\\nicole.txt')

    print(pablo.get_name(),
          pablo.get_student_number(),
          pablo.get_credits_for('CSE163'))

    print(arlo.get_name(),
          arlo.get_student_number(),
          arlo.get_credits_for('CSE163'))

    print(nicole.get_name(),
          nicole.get_student_number(),
          nicole.get_credits_for('CSE390HA'))


if __name__ == '__main__':
    main()
