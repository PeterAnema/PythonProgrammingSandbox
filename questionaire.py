class AnswerOption:

    def __init__(self,text,code):
        self.__text = text
        self.__code = int(code)

class Item:
    """Single item containing question, answeroptions, selected answer and score"""
    
    def __init__(self):
        """Constructor"""
        self.__question = ""
        self.__options = ()
        self.__answer = None
        self.__score = 0

    def setupItem(self,question,answers):
        self.__question = question
        self.__answers.list(answers)

    def setAnswer(self,answer):
        if answer < len(self.__options):
            self.__answer = int(answer)

    def getScore(self):
        self.__score = self.weights[self.__answer]
        return self.__score
        

class Questions:

    def __init__(self):
        self.items = list()
        self.score = None

    def setItems(self,listOfItems):
        pass

    def berekenScore(self):
        self.score = 0
        for item in self.items:
            self.score += item.score
        

class Test:

    def __init__(self,testname):
        self.name = testname
        self.questions = Questions

    def getName(self):
        return self.name


t = Test("QoL")
print(t.getName())
