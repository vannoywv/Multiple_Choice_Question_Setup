###
### A multiple choice question setup intended to:
### 1) accept a question prompt and print the prompt to the user
### 2) accept a list of  up to 40 options for the user to choose from and print only available options to user
### 3) accept an input from the user of a or A, b, B, ...
### 4) return the item from the provided list that was selected by the user
### 5) print this response
### 6) query user to finalize the choice
###
class Question():
    def __init__(self, prompt, options, response, output):
        self.prompt= prompt
        self.options= options
        self.response= response
        self.output= output

    @property
    def prompt(self):
        return self._prompt

    @prompt.setter
    def prompt(self, value):
        self._prompt = value

    @property
    def options(self):
        return self._options

    @options.setter
    def options(self, value):
        self._options = value

    @property
    def response(self):
        return self._response

    @response.setter
    def response(self, value):
        self._response = value

    @property
    def output(self):
        return self._output

    @output.setter
    def output(self, value):
        self._output = value

def multich(question):
    print(question.prompt)
    if len(question.options) > 0:
        print(f"A. {question.options[0]}")
    if len(question.options) > 1:
        print(f"B. {question.options[1]}")
    if len(question.options) > 2:
        print(f"C. {question.options[2]}")
    if len(question.options) > 3:
        print(f"D. {question.options[3]}")
    if len(question.options) > 4:
        print(f"E. {question.options[4]}")
    if len(question.options) > 5:
        print(f"F. {question.options[5]}")
    if len(question.options) > 6:
        print(f"G. {question.options[6]}")
    if len(question.options) > 7:
        print(f"H. {question.options[7]}")
    if len(question.options) > 8:
        print(f"I. {question.options[8]}")
    if len(question.options) > 9:
        print(f"J. {question.options[9]}")
    if len(question.options) > 10:
        print(f"K. {question.options[10]}")
    if len(question.options) > 11:
        print(f"L. {question.options[11]}")
    if len(question.options) > 12:
        print(f"M. {question.options[12]}")
    if len(question.options) > 13:
        print(f"N. {question.options[13]}")
    if len(question.options) > 14:
        print(f"O. {question.options[14]}")
    if len(question.options) > 15:
        print(f"P. {question.options[15]}")
    if len(question.options) > 16:
        print(f"Q. {question.options[16]}")
    if len(question.options) > 17:
        print(f"R. {question.options[17]}")
    if len(question.options) > 18:
        print(f"S. {question.options[18]}")
    if len(question.options) > 19:
        print(f"T. {question.options[19]}")
    if len(question.options) > 20:
        print(f"U. {question.options[20]}")
    if len(question.options) > 21:
        print(f"V. {question.options[21]}")
    if len(question.options) > 22:
        print(f"W. {question.options[22]}")
    if len(question.options) > 23:
        print(f"X. {question.options[23]}")
    if len(question.options) > 24:
        print(f"Y. {question.options[24]}")
    if len(question.options) > 25:
        print(f"Z. {question.options[25]}")
    if len(question.options) > 26:
        print(f"AA. {question.options[26]}")
    if len(question.options) > 27:
        print(f"BB. {question.options[27]}")
    if len(question.options) > 28:
        print(f"CC. {question.options[28]}")
    if len(question.options) > 29:
        print(f"DD. {question.options[29]}")
    if len(question.options) > 30:
        print(f"EE. {question.options[30]}")
    if len(question.options) > 31:
        print(f"FF. {question.options[31]}")
    if len(question.options) > 32:
        print(f"GG. {question.options[32]}")
    if len(question.options) > 33:
        print(f"HH. {question.options[33]}")
    if len(question.options) > 34:
        print(f"II. {question.options[34]}")
    if len(question.options) > 35:
        print(f"JJ. {question.options[35]}")
    if len(question.options) > 36:
        print(f"KK. {question.options[36]}")
    if len(question.options) > 37:
        print(f"LL. {question.options[37]}")
    if len(question.options) > 38:
        print(f"MM. {question.options[38]}")
    if len(question.options) > 39:
        print(f"NN. {question.options[39]}")
    question.response=input("Selection:")
    question.response=question.response.upper()
#Checks to see if the response is appropriate, gives the output value based on the provided list.
#Administers question again if inappropriate response given.
    if question.response== "A":
        if len(question.options) > 0:
            print(f"You selected {question.options[0]} ")
            question.output = question.options[0]
        else:
            print("Option not supported. Select again.")
            multich(question=question)
    elif question.response== "B":
        if len(question.options) > 1:
            print(f"You selected {question.options[1]} ")
            question.output = question.options[1]
        else:
            print("Option not supported. Select again.")
            multich(question=question)
    elif question.response== "C":
        if len(question.options) > 2:
            print(f"You selected {question.options[2]} ")
            question.output = question.options[2]
        else:
            print("Option not supported. Select again.")
            multich(question=question)
    elif question.response== "D":
        if len(question.options) > 3:
            print(f"You selected {question.options[3]} ")
            question.output = question.options[3]
        else:
            print("Option not supported. Select again.")
            multich(question=question)
    elif question.response== "E":
        if len(question.options) > 4:
            print(f"You selected {question.options[4]} ")
            question.output = question.options[4]
        else:
            print("Option not supported. Select again.")
            multich(question=question)
    elif question.response== "F":
        if len(question.options) > 5:
            print(f"You selected {question.options[5]} ")
            question.output = question.options[5]
        else:
            print("Option not supported. Select again.")
            multich(question=question)
    elif question.response== "G":
        if len(question.options) > 6:
            print(f"You selected {question.options[6]} ")
            question.output = question.options[6]
        else:
            print("Option not supported. Select again.")
            multich(question=question)
    elif question.response== "H":
        if len(question.options) > 7:
            print(f"You selected {question.options[7]} ")
            question.output = question.options[7]
        else:
            print("Option not supported. Select again.")
            multich(question=question)
    elif question.response== "I":
        if len(question.options) > 8:
            print(f"You selected {question.options[8]} ")
            question.output = question.options[8]
        else:
            print("Option not supported. Select again.")
            multich(question=question)
    elif question.response== "J":
        if len(question.options) > 9:
            print(f"You selected {question.options[9]} ")
            question.output = question.options[9]
        else:
            print("Option not supported. Select again.")
            multich(question=question)
    elif question.response== "K":
        if len(question.options) > 10:
            print(f"You selected {question.options[10]} ")
            question.output = question.options[10]
        else:
            print("Option not supported. Select again.")
            multich(question=question)
    elif question.response== "L":
        if len(question.options) > 11:
            print(f"You selected {question.options[11]} ")
            question.output = question.options[11]
        else:
            print("Option not supported. Select again.")
            multich(question=question)
    elif question.response== "M":
        if len(question.options) > 12:
            print(f"You selected {question.options[12]} ")
            question.output = question.options[12]
        else:
            print("Option not supported. Select again.")
            multich(question=question)
    elif question.response== "N":
        if len(question.options) > 13:
            print(f"You selected {question.options[13]} ")
            question.output = question.options[13]
        else:
            print("Option not supported. Select again.")
            multich(question=question)
    elif question.response== "O":
        if len(question.options) > 14:
            print(f"You selected {question.options[14]} ")
            question.output = question.options[14]
        else:
            print("Option not supported. Select again.")
            multich(question=question)
    elif question.response== "P":
        if len(question.options) > 15:
            print(f"You selected {question.options[15]} ")
            question.output = question.options[15]
        else:
            print("Option not supported. Select again.")
            multich(question=question)
    elif question.response== "Q":
        if len(question.options) > 16:
            print(f"You selected {question.options[16]} ")
            question.output = question.options[16]
        else:
            print("Option not supported. Select again.")
            multich(question=question)
    elif question.response== "R":
        if len(question.options) > 17:
            print(f"You selected {question.options[17]} ")
            question.output = question.options[17]
        else:
            print("Option not supported. Select again.")
            multich(question=question)
    elif question.response== "S":
        if len(question.options) > 18:
            print(f"You selected {question.options[18]} ")
            question.output = question.options[18]
        else:
            print("Option not supported. Select again.")
            multich(question=question)
    elif question.response== "T":
        if len(question.options) > 19:
            print(f"You selected {question.options[19]} ")
            question.output = question.options[19]
        else:
            print("Option not supported. Select again.")
            multich(question=question)
    elif question.response== "U":
        if len(question.options) > 20:
            print(f"You selected {question.options[20]} ")
            question.output = question.options[20]
        else:
            print("Option not supported. Select again.")
            multich(question=question)
    elif question.response== "V":
        if len(question.options) > 21:
            print(f"You selected {question.options[21]} ")
            question.output = question.options[21]
        else:
            print("Option not supported. Select again.")
            multich(question=question)
    elif question.response== "W":
        if len(question.options) > 22:
            print(f"You selected {question.options[22]} ")
            question.output = question.options[22]
        else:
            print("Option not supported. Select again.")
            multich(question=question)
    elif question.response== "X":
        if len(question.options) > 23:
            print(f"You selected {question.options[23]} ")
            question.output = question.options[23]
        else:
            print("Option not supported. Select again.")
            multich(question=question)
    elif question.response== "Y":
        if len(question.options) > 24:
            print(f"You selected {question.options[24]} ")
            question.output = question.options[24]
        else:
            print("Option not supported. Select again.")
            multich(question=question)
    elif question.response== "Z":
        if len(question.options) > 25:
            print(f"You selected {question.options[25]} ")
            question.output = question.options[25]
        else:
            print("Option not supported. Select again.")
            multich(question=question)
    elif question.response== "AA":
        if len(question.options) > 26:
            print(f"You selected {question.options[26]} ")
            question.output = question.options[26]
        else:
            print("Option not supported. Select again.")
            multich(question=question)
    elif question.response== "BB":
        if len(question.options) > 27:
            print(f"You selected {question.options[27]} ")
            question.output = question.options[27]
        else:
            print("Option not supported. Select again.")
            multich(question=question)
    elif question.response== "CC":
        if len(question.options) > 28:
            print(f"You selected {question.options[28]} ")
            question.output = question.options[28]
        else:
            print("Option not supported. Select again.")
            multich(question=question)
    elif question.response== "DD":
        if len(question.options) > 29:
            print(f"You selected {question.options[29]} ")
            question.output = question.options[29]
        else:
            print("Option not supported. Select again.")
            multich(question=question)
    elif question.response== "EE":
        if len(question.options) > 30:
            print(f"You selected {question.options[30]} ")
            question.output = question.options[30]
        else:
            print("Option not supported. Select again.")
            multich(question=question)
    elif question.response== "FF":
        if len(question.options) > 31:
            print(f"You selected {question.options[31]} ")
            question.output = question.options[31]
        else:
            print("Option not supported. Select again.")
            multich(question=question)
    elif question.response== "GG":
        if len(question.options) > 32:
            print(f"You selected {question.options[32]} ")
            question.output = question.options[32]
        else:
            print("Option not supported. Select again.")
            multich(question=question)
    elif question.response== "HH":
        if len(question.options) > 33:
            print(f"You selected {question.options[33]} ")
            question.output = question.options[33]
        else:
            print("Option not supported. Select again.")
            multich(question=question)
    elif question.response== "II":
        if len(question.options) > 34:
            print(f"You selected {question.options[34]} ")
            question.output = question.options[34]
        else:
            print("Option not supported. Select again.")
            multich(question=question)
    elif question.response== "JJ":
        if len(question.options) > 35:
            print(f"You selected {question.options[35]} ")
            question.output = question.options[35]
        else:
            print("Option not supported. Select again.")
            multich(question=question)
    elif question.response== "KK":
        if len(question.options) > 36:
            print(f"You selected {question.options[36]} ")
            question.output = question.options[36]
        else:
            print("Option not supported. Select again.")
            multich(question=question)
    elif question.response== "LL":
        if len(question.options) > 37:
            print(f"You selected {question.options[37]} ")
            question.output = question.options[37]
        else:
            print("Option not supported. Select again.")
            multich(question=question)
    elif question.response== "MM":
        if len(question.options) > 38:
            print(f"You selected {question.options[38]} ")
            question.output = question.options[38]
        else:
            print("Option not supported. Select again.")
            multich(question=question)
    elif question.response== "NN":
        if len(question.options) > 39:
            print(f"You selected {question.options[39]} ")
            question.output=question.options[39]
        else:
            print("Option not supported. Select again.")
            multich(question=question)
    else:
        print("Option not supported. Select again.")
        multich(question= question)
#Confirm choice with user before outputting response.
    def confirm():
        firm= input("Would you like to finalize this selection? [y/n]")
        if firm=='y' or firm=="Y":
            print("Selection confirmed.")
        elif firm=='n' or firm=="N":
            print("Restarting selection.")
            multich(question= question)
        else:
            del firm
            print("Option not supported")
            confirm()
    confirm()
#Output response.
    return question.output



question1= Question(prompt="Select an option.", options=["o1","o2","o3"], response=None, output=None)
response1= multich(question1)
print(response1)