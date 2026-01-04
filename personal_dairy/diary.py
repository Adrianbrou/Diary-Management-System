from datetime import datetime


class DiaryEntry:
    def __init__(self, title, content, date, tags):
        self.title = title
        self.content = content
        self.date = tuple(date)
        self.tags = set(tags)
        self.created_at = datetime.now().isoformat()

    def to_dict(self):
        return {
            "title": self.title,
            "content": self.content,
            "date": self.date,
            "tags": list(self.tags),
            "created_at": self.created_at
        }
