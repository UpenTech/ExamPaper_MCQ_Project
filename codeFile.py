import random

ans_ = []
all_options_ = []

def header_(file_) -> None:
    """Creates the header for our ques paper

    :param file_: file
    :type file_: file
    """

    #Header Page of Test Paper
    TITLE ="Class Test".upper().center(80)
    HEAD = "Geography mcq questions".upper().center(80)

    MARKS_F = "Full Marks: 100".rjust(120)
    MARKS_P = "Pass Marks: 35".rjust(120)

    print(TITLE, file=file_)
    print(HEAD, file=file_)
    print(MARKS_F,file=file_)
    print(MARKS_P,  file=file_)

def createDictionary(ques_: dict) -> None:
    """Reads from a data file and 
    creates a dictionary containing questions along with its
    answers

    :param ques_: empty dictionary
    :type ques_: dict
    :return: None
    """
    with open("data.txt") as sou:
        retrive = sou.readline()
        retrive = sou.readline()

        while retrive:
            var = retrive
            _ , state, capital, _ = var.split("\t") 
            ques_[state] = capital
            retrive = sou.readline()


def generateQuestion(ques_: dict) -> list:
    """ Generates 50 MCQ questions based
    on geography from data.txt file

    :type ques_: dict
    :return: None
    """
    options_ = []                                   #Options Container
    global all_options_                             #GodSheet - suffled answersheet
    temp = all_options_.copy()

    with open("MCQ_Questions.txt","a+") as prob_:
        header_(prob_)

        for no in range(1,51):

            all_options_ = temp.copy()
            to_go = random.choice(list(ques_))
            global ans_
            ans_.append(ques_[to_go])               #I want my answers
            options_.append(ques_[to_go])

            print(f"{no}. What is the capital of the state {to_go}?", file=prob_)

            for _ in range(3):
                var = random.choice(all_options_)
                options_.append(var)
                all_options_.remove(var)

            random.shuffle(options_)

            for opt in options_:
                print(opt, file=prob_)

            options_.clear()
            del ques_[to_go]
            print("-" * 55, file=prob_)



ques_dict =  {}

createDictionary(ques_dict)
all_options_ = list(ques_dict.values())
generateQuestion(ques_dict)

with open("Answers.txt", "a+") as soln_:
    print("Solution of MCQ. (numerical order)", file=soln_)
    for _ in ans_:
        print(_, file= soln_)