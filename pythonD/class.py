#Class

#データ処理をまとめるためのえっけいずです。

class Charcter:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
    def attack(self):
        print(f"{self.name}が攻撃しました！")


class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
    def introduce(self):
        print(f"私の名前は{self.name}です。年齢は{self.age}歳です。")
    def show_score(self):
        print(f"{self.name}の点数は{self.score}点です。")
    def pass_exam(self):
        if self.score >= 60:
            print(f"{self.name}は合格です。")
        else: 
            print(f"{self.name}は不合格です。")

#student1 = Student("Alice",20,75)
#student2 = Student("Bob", 19, 55)
#student3 = Student("Charlie", 21, 90)

#student1.introduce()
#student1.show_score()
#student1.pass_exam()

#student2.introduce()
#student2.show_score()
#student2.pass_exam()

#student3.introduce()
#student3.show_score()
#student3.pass_exam()

students = [
Student("Alice",20,75),
Student("Bob", 19, 55),
Student("Charlie", 21, 90)
]


for student in students:
    student.introduce()
    student.show_score()
    student.pass_exam()
    print("------------")