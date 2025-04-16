import tkinter as tk
from tkinter import messagebox
import time

class TriviaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Trivia Quiz")
        self.root.geometry("700x600")
        
        # Initialize variables
        self.questions = [
            {"question": "What is the capital of France?", "choices": ["Paris", "London", "Berlin", "Madrid"], "answer": 0},
            {"question": "What is 5 + 3?", "choices": ["5", "8", "7", "9"], "answer": 1},
            {"question": "Which planet is known as the Red Planet?", "choices": ["Earth", "Venus", "Mars", "Jupiter"], "answer": 2},
            {"question": "Who wrote 'Hamlet'?", "choices": ["Shakespeare", "Hemingway", "Dickens", "Austen"], "answer": 0}
        ]
        self.current_question_index = -1
        self.score = 0
        self.start_time = None
        self.timer_seconds = 200
        self.timer_running = False
        
        # Create UI elements
        self.start_button = tk.Button(root, text="Start", command=self.start_quiz, font=("Arial", 14))
        self.start_button.pack(pady=20)

        self.timer_label = tk.Label(root, text=f"Time Remaining: {self.timer_seconds} seconds", font=("Arial", 14))
        self.timer_label.pack()

        self.question_label = tk.Label(root, text="", font=("Arial", 16), wraplength=500)
        self.question_label.pack(pady=20)

        self.choices_frame = tk.Frame(root)
        self.choices_frame.pack()

        self.choices_buttons = []
        for i in range(4):
            btn = tk.Button(self.choices_frame, text="", font=("Arial", 12), state="disabled", command=lambda i=i: self.submit_answer(i))
            btn.pack(side=tk.TOP, pady=5)
            self.choices_buttons.append(btn)

        self.exit_button = tk.Button(root, text="Exit", command=self.exit_quiz, font=("Arial", 14))
        self.exit_button.pack(pady=10)

    def start_quiz(self):
        self.start_button.pack_forget()
        self.score = 0
        self.current_question_index = -1
        self.timer_seconds = 200
        self.timer_running = True
        self.start_time = time.time()
        self.update_timer()
        
        # Enable and display the choice buttons
        for btn in self.choices_buttons:
            btn.config(state="normal")
        self.next_question()

    def update_timer(self):
        if self.timer_running:
            elapsed_time = int(time.time() - self.start_time)
            self.timer_seconds = max(0, 200 - elapsed_time)
            self.timer_label.config(text=f"Time Remaining: {self.timer_seconds} seconds")
            if self.timer_seconds > 0:
                self.root.after(1000, self.update_timer)
            else:
                self.end_quiz()

    def next_question(self):
        self.current_question_index += 1
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            self.question_label.config(text=question["question"])
            for i, choice in enumerate(question["choices"]):
                self.choices_buttons[i].config(text=choice, state="normal")
        else:
            self.end_quiz()

    def submit_answer(self, choice_index):
        question = self.questions[self.current_question_index]
        if choice_index == question["answer"]:
            self.score += 1
        self.next_question()

    def end_quiz(self):
        self.timer_running = False
        end_time = time.time()
        time_taken = int(end_time - self.start_time)
        messagebox.showinfo("Quiz Completed", f"Your Score: {self.score}/{len(self.questions)}\nTime Taken: {time_taken} seconds")
        self.reset_quiz()

    def reset_quiz(self):
        self.start_button.pack(pady=20)
        self.timer_label.config(text=f"Time Remaining: 200 seconds")
        self.question_label.config(text="")
        for btn in self.choices_buttons:
            btn.config(text="", state="disabled")

    def exit_quiz(self):
        self.root.destroy()

# Create the Tkinter application
if __name__ == "__main__":
    root = tk.Tk()
    app = TriviaApp(root)
    root.mainloop()