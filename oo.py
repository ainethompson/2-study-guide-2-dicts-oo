# Create your classes here

class Student(object):

    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Question():

    def __init__(self, question, correct_answer):
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


