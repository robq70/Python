import requests
import html


class Question:
    def __init__(self, category, questionStr, correctAnswerFlag):
        self.category = category
        self.questionStr = questionStr
        self.correctAnswerFlag = correctAnswerFlag


class Quiz:
    def __init__(self, numQuestions):
        self.apiUrl = "https://opentdb.com/api.php?difficulty=easy&type=boolean&amount="
        self.numQuestions = numQuestions
        self.questionsList = []
        self.loadQuestions(numQuestions)

    def loadQuestions(self, numQuestions):
        response = requests.get(self.apiUrl + str(numQuestions))
        # {'response_code': 0, 'results': [{'type': 'boolean', 'difficulty': 'easy', 'category': 'History', 'question': 'Thomas Crapper was a plumber who invented the flushing toilet.', 'correct_answer': 'False', 'incorrect_answers': ['True']}, {'type': 'boolean', 'difficulty': 'easy', 'category': 'Entertainment: Video Games', 'question': 'Faust is a playable character in &quot;Guilty Gear Xrd Revelator&quot;.', 'correct_answer': 'True', 'incorrect_answers': ['False']}
        if response.ok:
            # print(response.json())
            data = response.json()
            results = data["results"]
            for q in results:
                category = q["category"]
                questionType = q["type"]
                difficulty = q["difficulty"]
                questionStr = html.unescape(q["question"])
                print(questionStr)
                correctAnswerFlag = q["correct_answer"].lower() in ["true", "1", "yes"]

                qObj = Question(category, questionStr, correctAnswerFlag)
                self.questionsList.append(qObj)

    def startQuiz(self):
        print("\nWelcome in Quiz!")
        numCorrectUserAnswers = 0
        n = 0
        numQuestions = len(self.questionsList)

        while n < numQuestions:
            q = self.questionsList[n]
            print("Question number" + str(n) + ": ", q.questionStr)
            print("Answer flag: ", q.correctAnswerFlag)

            answer = input("Give correct answer y/n")
            answerBool = False
            if answer == "y":
                answerBool = True
            if answerBool == q.correctAnswerFlag:
                print("Correct!")
                numCorrectUserAnswers += 1
            else:
                print("Not correct!")
            n += 1
        print(
            "Number of correct answers: ",
            numCorrectUserAnswers,
            " from ",
            len(self.questionsList),
            " questions ",
        )


quiz = Quiz(10)
quiz.startQuiz()
