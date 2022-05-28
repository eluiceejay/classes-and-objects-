class Student:
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

    def change_name(self, name):
        self.name = name
        print("My name is now" + " " + name)

    def change_age(self, age):
        self.age = age
        print("My age is now ", + age)

    def add_tracks(self, tracks):
        self.tracks = tracks
        print("My track is now" + " " + tracks)

    def get_score(self, score):
        self.score = score
        print("My score is now ", + score)


Bob = Student("Bob", 26, ["FE", "BE"], 20.90)


Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_tracks("UI/UX")
Bob.get_score(40.59)
