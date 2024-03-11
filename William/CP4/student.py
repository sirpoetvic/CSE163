# Student Class, CP4, Lesson 13
# need to redo this, logic is wrong.
# specifically on the init.
class Student():
    def __init__(self, student_number, file_name):
        """
        Args:
            student_number (int): ID #
            classes (dict): classes as key, credit # as value
        """
        self.student_number = student_number
        self.name = file_name[:-4]  # removes last 4 letters of the file name
        self.classes = {}

    def get_name(self):
        return self.name

    def get_student_number(self):
        return self.student_number

    def get_credits_for(self, file_name):
        self.classes = file_name.split[1]
        credit = 0
        for key, value in self.classes:
            credit = value
            if credit != 0:
                return credit
        return None

    def get_classes(self, file_name):
        self.classes = file_name.split[0]
        class_id = ''
        for key, value in self.classes:
            class_id = key
        return class_id
