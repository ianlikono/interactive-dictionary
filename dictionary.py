import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did You Mean %s instead? Enter Y if yes or N if no " %
                   get_close_matches(word, data.keys())[0])
        yn = yn.upper()
        if yn == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N":
            return "The Word Does Not Exist In English Please Double Check It"
        else:
            return "Please Select A Valid Option"

    else:
        return "The Word Does Not Exist In English Please Double Check It"


word = input("Enter Word: ")

answer = translate(word)

if type(answer) == list:
    for item in answer:
        print(item)

else:
    print(answer)
