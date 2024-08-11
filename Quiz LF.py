import tkinter as tk
from tkinter import messagebox
import tkinter.font as font

# Sample questions for different difficulty levels
QUIZ_DATA = {
    'EASY': [
        {'question': 'Which of the following is a valid \n "variable name" in Python?', 'options': ['2variable', 'variable_name', 'variable-name', 'variable name'], 'answer': 'variable_name'},
        {'question': 'Which of the following is used to define \n a block of code in Python language?', 'options': ['Indentation', 'Key', 'Brackets', 'All of the above'], 'answer': 'Indentation'},
        {'question': 'Which of the following is a \n Python keyword?', 'options': ['function', 'define', 'if', 'while'], 'answer': 'if'}
    ],
    'MEDIUM': [
        {'question': 'Which of the following is the \n correct way to create a list in Python?', 'options': ['my_list = (1, 2, 3)', 'my_list = {1, 2, 3}', 'my_list = [1, 2, 3]', 'None of the above'], 'answer': 'my_list = [1, 2, 3]'},
        {'question': 'Which of the following data types is\n immutable in Python?', 'options': ['List', 'Dictionary', 'Set', 'Tuple'], 'answer': 'Tuple'},
        {'question': 'What is the output of the following code? \n\n print(3 + 2 * 2)', 'options': ['10', '7', '12', '8'], 'answer': '7'}
    ],
    'HARD': [
        {'question': 'Which of the following is correctly \n evaluated for this function? \n\n pow(x,y,z)', 'options': ['(x**y) / z', '(x / y) * z', '(x**y) % z', '(x / y) / z'], 'answer': '(x**y) % z'},
        {'question': 'What will be the output of the \n following code snippet? \n\n s = {1, 2, 3, 3, 2, 4, 5, 5}\n print(s)', 'options': ['{1,2,3,3,2,4,5,5}', '{1,2,3,4,5}', 'Error', 'None of the above'], 'answer': '{1,2,3,4,5}'},
        {'question': 'What will be the result of the \n following expression in Python? \n\n “2 ** 3 + 5 ** 2”', 'options': ['65536', '33', '169', 'None of the above'], 'answer': '33'}
    ]
}

class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.root.geometry("350x550")
        self.root.configure(bg='lightblue')  # Set background color
        
        # Game variables
        self.score = 0
        self.current_question = 0
        self.difficulty = tk.StringVar(value="EASY")

        # Widgets
        self.create_widgets()
        self.load_question()
        

    def create_widgets(self):
        tk.Label(self.root, text="QUIZ GAME", font=("Jokerman", 23), bg='lightblue').pack(pady=10)
        # Bold font for the label
        bold_font = font.Font(weight="bold")

        # Custom font for question text
        question_font = font.Font(family="Century Gothic", size=13, weight="bold")
        option_font = font.Font(family="Century Gothic", size=10)

        # Highlighted Label
        option_menu = tk.OptionMenu(self.root, self.difficulty, "EASY", "MEDIUM", "HARD")
        option_menu.config(font=("Tw Cen MT Condensed Extra Bold", 12), bg='lightgrey')
        option_menu.pack(pady=10)

        self.start_button = tk.Button(self.root, text="Let's Start ", command=self.start_quiz, font=("Showcard Gothic", 11), bg='lightgrey')
        self.start_button.pack(pady=10)


        self.question_label = tk.Label(self.root, text="", font=question_font,  bg="lightblue")
        self.question_label.pack(pady=20)

        self.options = []
        for _ in range(4):
            option = tk.Button(self.root, text="", width=20, command=lambda i=_: self.check_answer(i))
            option.config(font=option_font)
            option.pack(pady=5)
            self.options.append(option)

        self.score_label = tk.Label(self.root, text="Score: 0", font=("Eras Bold ITC", 12, "bold"), bg='lightblue')
        self.score_label.pack(pady=20)

    def start_quiz(self):
        self.score = 0
        self.current_question = 0
        self.update_score()
        self.load_question()

    def load_question(self):
        questions = QUIZ_DATA[self.difficulty.get()]
        question_data = questions[self.current_question]

        self.question_label.config(text=question_data['question'])
        for i, option in enumerate(self.options):
            option.config(text=question_data['options'][i])

    def check_answer(self, selected_option):
        questions = QUIZ_DATA[self.difficulty.get()]
        correct_answer = questions[self.current_question]['answer']

        if self.options[selected_option].cget("text") == correct_answer:
            self.score += 1
            messagebox.showinfo("Correct!", "Well done!")
        else:
            messagebox.showerror("Incorrect!", f"The correct answer was: {correct_answer}")

        self.update_score()
        self.current_question += 1

        if self.current_question < len(questions):
            self.load_question()
        else:
            messagebox.showinfo("Quiz Over", f"Your final score is: {self.score}")
            self.start_button.config(state=tk.NORMAL)

    def update_score(self):
        self.score_label.config(text=f"Score: {self.score}")


if __name__ == "__main__":
    root = tk.Tk()
    game = QuizGame(root)
    root.mainloop()
