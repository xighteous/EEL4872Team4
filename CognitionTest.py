import tkinter as tk
from tkinter import messagebox
import time
import random  # Add this import at the top of the file

class TriviaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Trivia Quiz")
        self.root.geometry("700x600")

        # Initialize variables
        self.questionslvl1 = [
            {"question": "Which word best completes the sentence? \"The cat sat on the ____.\"", "choices": ["mat", "hat", "bat", "rat"], "answer": 0, "difficulty": 1, "completed": False},
            {"question": "What is 10 minus 4?", "choices": ["4", "5", "6", "7"], "answer": 2, "difficulty": 1, "completed": False},
            {"question": "Which of the following is a noun?", "choices": ["run", "blue", "dog", "quickly"], "answer": 2, "difficulty": 1, "completed": False},
            {"question": "How many days are in a week?", "choices": ["5", "6", "7", "8"], "answer": 2, "difficulty": 1, "completed": False},
            {"question": "Which planet do we live on?", "choices": ["Mars", "Earth", "Venus", "Jupiter"], "answer": 1, "difficulty": 1, "completed": False},
            {"question": "What color are bananas when ripe?", "choices": ["Red", "Green", "Blue", "Yellow"], "answer": 3, "difficulty": 1, "completed": False},
            {"question": "Which number comes after 9?", "choices": ["8", "10", "11", "12"], "answer": 1, "difficulty": 1, "completed": False},
            {"question": "What is the opposite of \"hot\"?", "choices": ["cold", "warm", "dry", "wet"], "answer": 0, "difficulty": 1, "completed": False},
            {"question": "Which animal barks?", "choices": ["cat", "fish", "dog", "bird"], "answer": 2, "difficulty": 1, "completed": False},
            {"question": "What does the sun provide?", "choices": ["water", "light", "sound", "wind"], "answer": 1, "difficulty": 1, "completed": False},
            {"question": "Which sentence is correct?", "choices": ["He go to school every day.", "He goes to school every day.", "He going to school every day.", "He gone to school every day."], "answer": 1, "difficulty": 1, "completed": False},
            {"question": "What is 12 divided by 3?", "choices": ["2", "3", "4", "5"], "answer": 2, "difficulty": 1, "completed": False}
        ]

        self.questionslvl2 = [
            {"question": "Which continent is the United States on?", "choices": ["Europe", "Asia", "Africa", "North America"], "answer": 3, "difficulty": 2, "completed": False},
            {"question": "What is 5 x 3?", "choices": ["8", "10", "15", "20"], "answer": 2, "difficulty": 2, "completed": False},
            {"question": "Which season comes after spring?", "choices": ["Winter", "Fall", "Autumn", "Summer"], "answer": 3, "difficulty": 2, "completed": False},
            {"question": "What is the capital of France?", "choices": ["Berlin", "London", "Paris", "Rome"], "answer": 2, "difficulty": 2, "completed": False},
            {"question": "What is H2O commonly known as?", "choices": ["Oxygen", "Water", "Hydrogen", "Air"], "answer": 1, "difficulty": 2, "completed": False},
            {"question": "How many legs does a spider have?", "choices": ["6", "8", "10", "12"], "answer": 1, "difficulty": 2, "completed": False},
            {"question": "Which shape has three sides?", "choices": ["Circle", "Square", "Triangle", "Rectangle"], "answer": 2, "difficulty": 2, "completed": False},
            {"question": "Which planet is closest to the sun?", "choices": ["Mars", "Earth", "Venus", "Mercury"], "answer": 3, "difficulty": 2, "completed": False},
            {"question": "What does a thermometer measure?", "choices": ["Length", "Weight", "Temperature", "Speed"], "answer": 2, "difficulty": 2, "completed": False},
            {"question": "Which of the following is a verb?", "choices": ["quickly", "run", "blue", "apple"], "answer": 1, "difficulty": 2, "completed": False},
            {"question": "Which of the following is a simile?", "choices": ["She was a lion in the fight.", "The leaves danced in the wind.", "He is as brave as a lion.", "Time flew by."], "answer": 2, "difficulty": 2, "completed": False},
            {"question": "Solve for x: 2x + 3 = 11", "choices": ["3", "4", "5", "6"], "answer": 1, "difficulty": 2, "completed": False}
        ]

        self.questionslvl3 = [
            {"question": "What is the main idea of a paragraph?", "choices": ["The longest sentence", "The most exciting part", "The central thought", "The last word"], "answer": 2, "difficulty": 3, "completed": False},
            {"question": "What gas do humans need to breathe?", "choices": ["Carbon dioxide", "Nitrogen", "Oxygen", "Helium"], "answer": 2, "difficulty": 3, "completed": False},
            {"question": "Which is a synonym for \"angry\"?", "choices": ["Happy", "Upset", "Kind", "Funny"], "answer": 1, "difficulty": 3, "completed": False},
            {"question": "What is 36 divided by 6?", "choices": ["5", "6", "7", "8"], "answer": 1, "difficulty": 3, "completed": False},
            {"question": "What does it mean to \"predict\"?", "choices": ["Look back", "Guess ahead", "Explain something", "Draw something"], "answer": 1, "difficulty": 3, "completed": False},
            {"question": "What is a fact?", "choices": ["An opinion", "A belief", "A true statement", "A feeling"], "answer": 2, "difficulty": 3, "completed": False},
            {"question": "Which number is a multiple of 4?", "choices": ["9", "11", "12", "13"], "answer": 2, "difficulty": 3, "completed": False},
            {"question": "Who wrote *Romeo and Juliet*?", "choices": ["Charles Dickens", "Mark Twain", "William Shakespeare", "Jane Austen"], "answer": 2, "difficulty": 3, "completed": False},
            {"question": "How many inches are in a foot?", "choices": ["10", "12", "14", "16"], "answer": 1, "difficulty": 3, "completed": False},
            {"question": "Which country is in South America?", "choices": ["Mexico", "Canada", "Brazil", "Spain"], "answer": 2, "difficulty": 3, "completed": False},
            {"question": "What does “bilingual” mean?", "choices": ["Two children", "Two words", "Two languages", "Two schools"], "answer": 2, "difficulty": 3, "completed": False},
            {"question": "If the temperature drops from 75°F to 60°F what is the percent decrease?", "choices": ["10%", "15%", "20%", "25%"], "answer": 2, "difficulty": 3, "completed": False},
            {"question": "What is the author’s tone in the sentence: “The park was eerily silent - as though time had frozen.”?", "choices": ["Joyful", "Angry", "Mysterious", "Hopeful"], "answer": 2, "difficulty": 3, "completed": False}
        ]

        self.questionslvl4 = [
            {"question": "Which ocean is the largest?", "choices": ["Atlantic", "Pacific", "Indian", "Arctic"], "answer": 1, "difficulty": 4, "completed": False},
            {"question": "What is the boiling point of water in Celsius?", "choices": ["90", "100", "110", "120"], "answer": 1, "difficulty": 4, "completed": False},
            {"question": "What does “photosynthesis” help plants do?", "choices": ["Eat bugs", "Absorb water", "Make food", "Breathe air"], "answer": 2, "difficulty": 4, "completed": False},
            {"question": "What is the square root of 49?", "choices": ["5", "6", "7", "8"], "answer": 2, "difficulty": 4, "completed": False},
            {"question": "Which branch of government makes laws?", "choices": ["Executive", "Legislative", "Judicial", "Federal"], "answer": 1, "difficulty": 4, "completed": False},
            {"question": "How many continents are there?", "choices": ["5", "6", "7", "8"], "answer": 2, "difficulty": 4, "completed": False},
            {"question": "What is 25%% of 80?", "choices": ["10", "15", "20", "25"], "answer": 2, "difficulty": 4, "completed": False},
            {"question": "Which word is an antonym of “include”?", "choices": ["Add", "Involve", "Exclude", "Accept"], "answer": 2, "difficulty": 4, "completed": False},
            {"question": "How many sides does a hexagon have?", "choices": ["5", "6", "7", "8"], "answer": 1, "difficulty": 4, "completed": False},
            {"question": "What is an adjective?", "choices": ["A person", "A place", "A describing word", "An action"], "answer": 2, "difficulty": 4, "completed": False},
            {"question": "A triangle has angles measuring 45° and 55°. What is the measure of the third angle?", "choices": ["75°", "80°", "90°", "60°"], "answer": 1, "difficulty": 4, "completed": False}
        ]

        self.questionslvl5 = [
            {"question": "Who invented the telephone?", "choices": ["Albert Einstein", "Isaac Newton", "Alexander Graham Bell", "Nikola Tesla"], "answer": 2, "difficulty": 5, "completed": False},
            {"question": "Which element is represented by the symbol “O”?", "choices": ["Gold", "Hydrogen", "Oxygen", "Silver"], "answer": 2, "difficulty": 5, "completed": False},
            {"question": "Which word best describes someone who is “timid”?", "choices": ["Brave", "Shy", "Funny", "Loud"], "answer": 1, "difficulty": 5, "completed": False},
            {"question": "What’s the capital of Japan?", "choices": ["Beijing", "Seoul", "Hong Kong", "Tokyo"], "answer": 3, "difficulty": 5, "completed": False},
            {"question": "Which of these is not a renewable resource?", "choices": ["Sunlight", "Wind", "Coal", "Water"], "answer": 2, "difficulty": 5, "completed": False},
            {"question": "What is the formula for area of a rectangle?", "choices": ["length + width", "length × width", "2 × length", "width ÷ length"], "answer": 1, "difficulty": 5, "completed": False},
            {"question": "How many degrees are in a right angle?", "choices": ["30", "60", "90", "120"], "answer": 2, "difficulty": 5, "completed": False},
            {"question": "Which planet has the most moons?", "choices": ["Earth", "Mars", "Jupiter", "Saturn"], "answer": 2, "difficulty": 5, "completed": False},
            {"question": "What part of the cell contains DNA?", "choices": ["Ribosome", "Nucleus", "Cytoplasm", "Membrane"], "answer": 1, "difficulty": 5, "completed": False},
            {"question": "Which president issued the Emancipation Proclamation?", "choices": ["George Washington", "Thomas Jefferson", "Abraham Lincoln", "Theodore Roosevelt"], "answer": 2, "difficulty": 5, "completed": False},
            {"question": "What does the word “mitigate” most nearly mean?", "choices": ["Complicate", "Strengthen", "Relieve", "Ignore"], "answer": 2, "difficulty": 5, "completed": False},
            {"question": "In an experiment the scientist controls for humidity and light. What kind of variables are these?", "choices": ["Independent", "Dependent", "Controlled", "Confounding"], "answer": 2, "difficulty": 5, "completed": False}
        ]

        self.questionslvl6 = [
            {"question": "What is the longest river in the world?", "choices": ["Amazon", "Nile", "Mississippi", "Yangtze"], "answer": 1, "difficulty": 6, "completed": False},
            {"question": "Which gas is most abundant in Earth’s atmosphere?", "choices": ["Oxygen", "Carbon dioxide", "Nitrogen", "Hydrogen"], "answer": 2, "difficulty": 6, "completed": False},
            {"question": "How many bones are in the adult human body?", "choices": ["198", "206", "210", "212"], "answer": 1, "difficulty": 6, "completed": False},
            {"question": "Who painted the Mona Lisa?", "choices": ["Van Gogh", "Da Vinci", "Picasso", "Michelangelo"], "answer": 1, "difficulty": 6, "completed": False},
            {"question": "Which country has the most official languages?", "choices": ["Canada", "India", "South Africa", "Switzerland"], "answer": 2, "difficulty": 6, "completed": False},
            {"question": "Which element is liquid at room temperature?", "choices": ["Iron", "Chlorine", "Bromine", "Sodium"], "answer": 2, "difficulty": 6, "completed": False},
            {"question": "What’s the term for animals that eat both plants and meat?", "choices": ["Herbivores", "Carnivores", "Omnivores", "Detritivores"], "answer": 2, "difficulty": 6, "completed": False},
            {"question": "How long does it take Earth to orbit the Sun?", "choices": ["180 days", "240 days", "365 days", "400 days"], "answer": 2, "difficulty": 6, "completed": False},
            {"question": "What’s the main language spoken in Brazil?", "choices": ["Spanish", "Portuguese", "French", "Italian"], "answer": 1, "difficulty": 6, "completed": False},
            {"question": "What’s the powerhouse of the cell?", "choices": ["Nucleus", "Ribosome", "Mitochondria", "Lysosome"], "answer": 2, "difficulty": 6, "completed": False},
            {"question": "What is the solution to the equation: 3(x – 4) = 2x + 1?", "choices": ["x = -11", "x = 11", "x = 13", "x = 5"], "answer": 2, "difficulty": 6, "completed": False},
            {"question": "What is the main effect of dramatic irony in a narrative?", "choices": ["It creates suspense for the reader.", "It reveals the theme.", "It develops the character.", "It adds humor."], "answer": 0, "difficulty": 6, "completed": False}
        ]

        self.questionslvl7 = [
            {"question": "What’s the hardest natural substance on Earth?", "choices": ["Steel", "Quartz", "Diamond", "Granite"], "answer": 2, "difficulty": 7, "completed": False},
            {"question": "Which U.S. state has the most coastline?", "choices": ["Florida", "Alaska", "California", "Hawaii"], "answer": 1, "difficulty": 7, "completed": False},
            {"question": "What’s the smallest prime number greater than 100?", "choices": ["101", "103", "107", "109"], "answer": 0, "difficulty": 7, "completed": False},
            {"question": "What does the term “nocturnal” mean?", "choices": ["Eats plants", "Is awake at night", "Sleeps standing up", "Lives in water"], "answer": 1, "difficulty": 7, "completed": False},
            {"question": "Which country has the highest population?", "choices": ["USA", "India", "China", "Indonesia"], "answer": 1, "difficulty": 7, "completed": False},
            {"question": "Which scientist developed the three laws of motion?", "choices": ["Galileo", "Newton", "Einstein", "Bohr"], "answer": 1, "difficulty": 7, "completed": False},
            {"question": "Which metal is liquid at room temperature?", "choices": ["Iron", "Lead", "Gold", "Mercury"], "answer": 3, "difficulty": 7, "completed": False},
            {"question": "Which blood type is known as the universal donor?", "choices": ["A", "B", "AB", "O"], "answer": 3, "difficulty": 7, "completed": False},
            {"question": "What is the largest desert in the world?", "choices": ["Sahara", "Antarctic", "Arctic", "Gobi"], "answer": 1, "difficulty": 7, "completed": False},
            {"question": "What language has the most native speakers?", "choices": ["English", "Spanish", "Hindi", "Mandarin"], "answer": 3, "difficulty": 7, "completed": False},
            {"question": "A rocket travels 1200 miles in 2 hours then 800 miles in the next hour. What is its average speed?", "choices": ["600 mph", "650 mph", "700 mph", "750 mph"], "answer": 1, "difficulty": 7, "completed": False}
        ]

        self.levels = {
            1: self.questionslvl1,
            2: self.questionslvl2,
            3: self.questionslvl3,
            4: self.questionslvl4,
            5: self.questionslvl5,
            6: self.questionslvl6,
            7: self.questionslvl7,
        }
        
        self.current_level = 4  # Start at level 4
        self.current_question_index = 0  # Track the current question number
        self.total_questions = 10  # Limit to 10 questions
        self.score = 0
        self.start_time = None
        self.timer_seconds = 200
        self.timer_running = False
        self.consecutive_wrong = 0  # Track consecutive wrong answers
        self.correct_answers = 0  # Track correct answers

        # Create the starting screen
        self.start_frame = tk.Frame(root)
        self.start_frame.pack(fill="both", expand=True)
        self.start_frame.config(bg="lightblue")

        self.start_label = tk.Label(
            self.start_frame,
            text="Cognitive Ability Quiz!\n\n"
                 f"You will have {self.timer_seconds} seconds to answer a mix of math, language, science, and trivia questions to assess your cognitive ability.\n\n"
                 "Try to answer as many questions as you can correctly.\n"
                 "Your score will depend on the difficulty of the questions you answer and the amount of time you take.",
            font=("Arial", 14),
            wraplength=600,
            justify="center"
        )
        self.start_label.pack(pady=50)        
        self.start_label.config(bg="lightblue")

        self.start_button = tk.Button(
            self.start_frame,
            text="Start Quiz",
            command=self.start_quiz,
            font=("Arial", 14)
        )
        self.start_button.pack(pady=20)        
        self.start_button.config(bg="lightblue")

        # Create the quiz screen (hidden initially)
        self.quiz_frame = tk.Frame(root)
        self.quiz_frame.config(bg="lightgreen")        

        self.timer_label = tk.Label(self.quiz_frame, text=f"Time Remaining: {self.timer_seconds} seconds", font=("Arial", 14))
        self.timer_label.config(bg="lightgreen")
        self.timer_label.pack()

        self.question_info_label = tk.Label(self.quiz_frame, text="", font=("Arial", 14))  # Show question number and difficulty
        self.question_info_label.config(bg="lightgreen")
        self.question_info_label.pack()

        self.question_label = tk.Label(self.quiz_frame, text="", font=("Arial", 16), wraplength=500)        
        self.question_label.config(bg="lightgreen")
        self.question_label.pack(pady=20)

        self.choices_frame = tk.Frame(self.quiz_frame)
        self.choices_frame.pack()

        self.choices_buttons = []
        for i in range(4):
            btn = tk.Button(self.choices_frame, text="", font=("Arial", 12), state="disabled", bg="lightgreen", command=lambda i=i: self.submit_answer(i))
            btn.pack(side=tk.TOP, pady=5)            
            self.choices_buttons.append(btn)

        self.exit_button = tk.Button(self.quiz_frame, text="Exit", command=self.exit_quiz, font=("Arial", 14))
        self.exit_button.pack(pady=10)

    def start_quiz(self):
        # Hide the starting screen and show the quiz screen
        self.start_frame.pack_forget()
        self.quiz_frame.pack(fill="both", expand=True)

        self.score = 0
        self.current_level = 4  # Start at level 4
        self.current_question_index = 0  # Reset question index
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
        # Check if the total number of questions has been reached
        if self.current_question_index >= self.total_questions:
            self.end_quiz()
            return

        # Get the question bank for the current level
        question_bank = self.levels.get(self.current_level, [])
        if not question_bank:
            self.end_quiz()
            return

        # Shuffle the question bank to randomize question selection
        random.shuffle(question_bank)

        # Find the next unanswered question in the current level
        for question in question_bank:
            if not question["completed"]:
                self.current_question = question
                self.current_question_index += 1  # Increment the question index
                self.question_info_label.config(
                    text=f"Question {self.current_question_index}/{self.total_questions} - Difficulty: {self.current_level}/7"
                )
                self.question_label.config(text=question["question"])
                for i, choice in enumerate(question["choices"]):
                    self.choices_buttons[i].config(text=choice, state="normal")
                question["completed"] = True
                return

        # If no questions are left in the current level, end the quiz
        self.end_quiz()

    def submit_answer(self, choice_index):
        if choice_index == self.current_question["answer"]:
            # Award points based on the difficulty of the current question
            self.score += self.current_question["difficulty"]
            self.correct_answers += 1
            self.consecutive_wrong = 0  # Reset consecutive wrong answers
            self.current_level = min(self.current_level + 1, 7)  # Move up a level
        else:
            self.consecutive_wrong += 1
            if self.consecutive_wrong >= 2:  # Drop difficulty after 2 wrong answers
                self.current_level = max(self.current_level - 1, 1)
                self.consecutive_wrong = 0  # Reset consecutive wrong answers
        self.next_question()

    def end_quiz(self):
        self.timer_running = False
        end_time = time.time()
        time_taken = int(end_time - self.start_time)

        final_score = (self.total_questions / time_taken) * self.score if time_taken > 0 else 0

        messagebox.showinfo("Quiz Completed",
                    f"Your Score: {final_score:.2f}\n"
                    f"Correct Answers: {self.correct_answers}/{self.total_questions}\n"
                    f"Time Taken: {time_taken} seconds")
        self.reset_quiz()

    def reset_quiz(self):
        # Show the start frame again
        self.quiz_frame.pack_forget()
        self.start_frame.pack(fill="both", expand=True)

        # Reset timer and labels
        self.timer_label.config(text=f"Time Remaining: 200 seconds")
        self.question_info_label.config(text="")
        self.question_label.config(text="")
        for btn in self.choices_buttons:
            btn.config(text="", state="disabled")

        # Reset all questions to not completed
        for level in self.levels.values():
            for question in level:
                question["completed"] = False

        # Reset other variables
        self.consecutive_wrong = 0
        self.correct_answers = 0

    def exit_quiz(self):
        self.root.destroy()

# Create the Tkinter application
if __name__ == "__main__":
    root = tk.Tk()
    app = TriviaApp(root)
    root.mainloop()