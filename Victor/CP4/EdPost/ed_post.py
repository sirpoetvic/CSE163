class EdPost:
    def __init__(self, title: str, tag="General") -> None:
        self._title = title
        self._tag = tag
        self._comments = []

    def get_title(self):
        return self._title

    def get_tag(self):
        return self._tag

    def add_comment(self, comment: str):
        """adds comment to the comment list

        Args:
            comment (str): comment to be added
        """
        self._comments.append(comment)

    def display(self):
        """Displays the information for the specific EdPost"""
        print(f"{self._title} ({self._tag})")
        print("Comments:")
        for comment in self._comments:
            print(f"  {comment}")
