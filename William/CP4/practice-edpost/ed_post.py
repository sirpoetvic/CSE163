# Write your solution here!
class EdPost:
    def __init__(self, title, tag='General', comments=None):
        self._title = title
        self._tag = tag
        # from lecture, look into how it works more!
        if comments is None:
            self._comments = []

    def get_title(self):
        return self._title

    def get_tag(self):
        return self._tag

    def add_comment(self, comments):
        self._comments.append(comments)

    def display(self):
        print(f'{self.get_title()} ({self.get_tag()})')
        print('Comments:')
        for i in self._comments:
            print('  ' + i)
