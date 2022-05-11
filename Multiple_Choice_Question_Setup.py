###
### A multiple choice question setup intended to:
### 1) accept a question prompt and print the prompt to the user
### 2) accept a dictionary of options for the user to choose from and print available options to user
### 3) accept an input from the user of a or A, b, B, ...
### 4) return the item from the provided list that was selected by the user
### 5) print this response
### 6) query user to finalize the choice
###
class Question:
    def __init__(self, prompt: str, options: dict, response: str, output: str):
        self.prompt = prompt
        self.options = options
        self.response = response
        self.output = output

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


def multi_choice(question):
    # Print the question's prompt
    print(question.prompt)

    # Print the options in the question's options by looping
    # over the dictionary's key
    for option in question.options.keys():
        print(question.options[option])

    # Prompt the user for an input selection
    question.response = input("Selection:")
    question.response = question.response.upper()

    # Checks to see if the response is appropriate, gives the output value based on the provided list.
    if question.response in question.options.keys():
        print(f"You selected {question.options[question.response]} ")
        question.output = question.options[question.response]
    # Administers question again if inappropriate response given.
    else:
        print("Option not supported. Select again.")
        multi_choice(question=question)

    # Confirm the user's selection
    confirm()
    # Output response.
    return question.output


# Confirm choice with user before outputting response.
def confirm(question):
    firm = input("Would you like to finalize this selection? [y/n]").to_upper()
    if firm == "Y":
        print("Selection confirmed.")
    elif firm == "N":
        print("Restarting selection.")
        multi_choice(question=question,)
    else:
        del firm
        print("Option not supported")
        confirm()


question1 = Question(prompt="Select an option.", options={"A": "o1", "B": "o2", "C": "o3"}, response=None, output=None)
response1 = multi_choice(question1)
print(response1)
