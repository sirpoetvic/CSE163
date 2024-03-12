# Student Class, CP4, Lesson 13
class Student():
    def __init__(self, student_number, file_name):
        """
        Args:
            student_number (int): ID #
            classes (dict): classes as key, credit # as value
        """
        self.student_number = student_number
        self.name = file_name
        self.classes = {}
        with open(file_name) as file:
            f = file.readlines()
            for line in f:
                key, value = line.strip().split()
                self.classes[key] = value

    def get_name(self):
        # seperates by \\, takes last element by doing [-1]
        relative_path = self.name.split('\\')[-1]
        # removes last 4 letters of the file name (.txt)
        self.name = relative_path[:-4]
        return self.name

    def get_student_number(self):
        return self.student_number

    def get_credits_for(self, class_name):
        # use the class code (class_name)
        credit_list = []
        for key, value in self.classes.items():
            if class_name in key:
                credit_list.append(value)
        if len(credit_list) == 0:
            # textbook says assign 0, canvas says None
            return 0
        else:
            # assumes only one class code is passed only
            return credit_list[0]

    def get_classes(self):
        class_list = []
        for key in self.classes:
            class_list.append(self.classes[key])
        return class_list
