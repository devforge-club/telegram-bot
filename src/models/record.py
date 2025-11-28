class Record:
    def to_dict(self):
        pass

    @classmethod
    def from_dict(cls, data: dict):
        return cls()
