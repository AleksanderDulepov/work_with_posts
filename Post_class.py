class Post:
    all_id = []

    def __init__(self, picture, description):
        self.picture = picture
        self.description = description
        self.init_id()

    # автоматическая простановка id
    def init_id(self):
        if not self.all_id:
            self.id = 1
        else:
            self.id = self.all_id[-1] + 1
        self.all_id.append(self.id)
