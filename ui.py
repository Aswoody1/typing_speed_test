from tkinter import *
from typing_test_brain import Brain
from data import words_cleaner
import random

THEME_COlOR = 'beige'
FONT = 'courier'


class TestInterface:
    def __init__(self, typing_test_brain: Brain):
        self.test = Brain()
        self.window = Tk()
        self.window.title("Typing Speed Test")
        self.window.config(bg=THEME_COlOR, padx=50, pady=50)
        self.title = Label(text='Typing Speed Test', bg=THEME_COlOR, fg='black', font=(FONT, 40, 'bold'))
        self.title.grid(columnspan=3, row=0, column=0)
        self.score = Label(text=f'Score: 0', bg=THEME_COlOR, fg='black', font=(FONT, 15, 'italic'),
                           pady=10)
        self.score.grid(column=0, row=1)
        self.count = 15


        self.mistakes = Label(text=f'Errors: {self.test.mistakes}', bg=THEME_COlOR, fg='black',
                              font=(FONT, 15, 'italic'),
                              pady=10)
        self.mistakes.grid(column=1, row=1)
        self.timer = Label(text=f"Timer: {self.count} secs", bg=THEME_COlOR, fg='black',
                           font=(FONT, 15, 'italic'))
        self.timer.grid(row=1, column=2)
        self.canvas = Canvas(bg='white', height=400, width=600)
        self.canvas.config(borderwidth=0, highlightthickness=0)
        self.canvas.grid(columnspan=3, column=0, row=2)
        self.inputted_word = Entry(bg='beige', fg='beige', borderwidth=0, highlightthickness=0, )
        self.inputted_word.grid(column=0, row=3)
        self.inputted_word.focus()
        self.current_word = None
        self.instructions = Label(text="Press Shift and Up together to start", bg=THEME_COlOR, fg='black',
                                  font=(FONT, 15, 'italic'),
                                  pady=10)
        self.instructions.grid(columnspan=4, row=3)
        self.window.bind("<Shift-Up>", self.timer_starts)
        self.window.bind("<Return>", self.next_word)
        self.window.mainloop()

    def next_word(self, event):
        if self.inputted_word.get() == "":
            pass
        else:
            typed_word = self.inputted_word.get()
            random_word = self.canvas.itemcget(self.current_word, 'text')
            self.inputted_word.delete(0, 300)
            if random_word == typed_word:
                self.correct()
            else:
                self.incorrect()
            self.canvas.itemconfig(self.current_word, text=random.choice(words_cleaner))

    def refresh(self):
        self.window.config(bg='beige')
        self.score.config(bg='beige')
        self.title.config(bg='beige')
        self.mistakes.config(bg='beige')
        self.timer.config(bg='beige')
        self.inputted_word.config(bg='beige')
        self.instructions.config(bg='beige')

    def correct(self):
        self.test.score += 1
        self.score.config(text=f'Score: {self.test.score}', bg='green')
        self.window.config(bg='green')
        self.title.config(bg='green')
        self.mistakes.config(bg='green')
        self.timer.config(bg='green')
        self.instructions.config(bg='green')
        self.inputted_word.config(bg='green')
        self.window.after(500, self.refresh)

    def incorrect(self):
        self.test.mistakes += 1
        self.mistakes.config(text=f'Errors: {self.test.mistakes}', bg='red')
        self.window.config(bg='red')
        self.score.config(bg='red')
        self.title.config(bg='red')
        self.timer.config(bg='red')
        self.instructions.config(bg='red')
        self.inputted_word.config(bg='red')
        self.window.after(500, self.refresh)

    def timer_starts(self, event):
        self.window.unbind("<Shift-Up>")
        self.current_word = self.canvas.create_text(300, 200, text=random.choice(words_cleaner), fill='black',                                             font=(FONT, 30))
        self.inputted_word.delete(0, 300)
        self.instructions.config(text='')
        if self.count > 0:
            self.countdown()

    def countdown(self):
        self.window.after(1000, self.countdown)
        if self.count > 0:
            self.count -= 1
            self.timer.config(text=f'Timer: {self.count} secs')
        elif self.count == 0:
            self.test_is_over()

    def test_is_over(self):

        self.window.unbind("<Return>")
        self.timer.config(text='Timer: 0 secs')
        self.canvas.itemconfig(self.current_word,
                               text=f'You managed to type at a rate of {self.test.score * 4} words per minute with an '
                                    f'overall '
                                    f'\naccuracy of {"{:.2f}".format((self.test.score/(self.test.score + self.test.mistakes)) * 100)}%. Congrats.',
                               font=(FONT, 14))
