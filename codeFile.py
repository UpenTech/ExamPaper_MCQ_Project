from typing import Iterable


def createDictionary(ques_: dict) -> None:
    """Reads from a data file and 
    creates a dictionary containing questions along with its
    answers

    :param ques_: empty dictionary
    :type ques_: dict
    :return: dictionary
    """
    with open("data.txt") as sou:
        retrive = sou.readline()
        retrive = sou.readline()

        while retrive:
            var = retrive
            _ , state, capital, _ = var.split("\t") 
            ques_[state] = capital
            retrive = sou.readline()

ques_ = {}

createDictionary(ques_)
for a in ques_.items():
    print(a)