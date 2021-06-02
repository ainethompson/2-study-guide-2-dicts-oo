# Create your classes here

class Student:

    def __init__(self, first_name, last_name, address):
        """ Initialize a student """

        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Question:

    def __init__(self, question, correct_answer):
        """ Initialize a question """

        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):
        """ Ask user a question and evaluate if their answer is correct """

        print(self.question)
        user_input = input('> ')

        if user_input == self.correct_answer:
            return True
        else:
            return False


class Exam:

    def __init__(self, name):
        """ Initialize an exam """

        self.name = name
        self.questions = []

    def add_question(self, new_question):
        """ Add a question to the exam """
        # new_question = Question instance
        self.questions.append(new_question)

    def administer(self):
        """ Administer exam questions and return score as decimal percentage """

        score = 0

        for question in self.questions:
            if question.ask_and_evaluate() == True:
                score += 1

        return 100 * (score / len(self.questions))


class StudentExam:

    def __init__(self, student, test):
        """ Initialize a student's exam """
        self.student = student
        self.test = test
        self.score = 0

    def take_test(self):
        """ Administer exam and print score """

        self.score = self.test.administer()

        print(f'{self.student.first_name} scored {self.score} on their {self.test.name} exam.')

def exam_example():
    """ example student exam """

    exam = Exam('midterm')

    set_q = Question(
        'What is the method for adding an element to a set?',
        '.add()')
    exam.add_question(set_q)

    pwd_q = Question(
        'What does pwd stand for?',
        'print working directory')
    exam.add_question(pwd_q)

    list_q = Question(
        'Python lists are mutable, iterable, and what?',
        'ordered')
    exam.add_question(list_q)

    aine = Student('Aine', 'Thompson', 1234)

    aine_exam = StudentExam(aine, exam)

    aine_exam.take_test()


class Quiz(Exam):
    
    def administer(self):
        """ Administer Quiz and return score """

        if super().administer() > 50:
            return 1
        else:
            return 0


class StudentQuiz(StudentExam):

    def take_test(self):
        self.score = self.test.administer()

        if self.score == 1:
            result = 'passed'
        elif self.score == 0:
            result = 'failed'

        print(f'{self.student.first_name} {result} their {self.test.name} quiz')


def quiz_example():
    """ Example student quiz """

    quiz = Quiz('Quiz 1')

    set_q = Question(
        'What is the method for adding an element to a set?',
        '.add()')
    quiz.add_question(set_q)

    pwd_q = Question(
        'What does pwd stand for?',
        'print working directory')
    quiz.add_question(pwd_q)

    list_q = Question(
        'Python lists are mutable, iterable, and what?',
        'ordered')
    quiz.add_question(list_q)

    aine = Student('Aine', 'Thompson', 1234)

    aine_quiz = StudentQuiz(aine, quiz)

    aine_quiz.take_test()