#!/usr/bin/env python
# coding: utf-8

# In[4]:





# In[5]:


import tkinter as tk

# Define the questions, options, and correct answers
questions = [
    "What is the capital of France?",
    "Who painted the Mona Lisa?",
    "What is the largest planet in our solar system?"
]

options = [
    ["Paris", "London", "Rome", "Berlin"],
    ["Leonardo da Vinci", "Pablo Picasso", "Vincent van Gogh", "Michelangelo"],
    ["Jupiter", "Saturn", "Mars", "Earth"]
]

answers = [0, 0, 0]  # Index of the correct answer for each question

# Initialize variables
current_question = 0
score = 0

# Function to check the answer
def check_answer(answer):
    global score, current_question
    
    if answer == answers[current_question]:
        score += 1
    
    current_question += 1
    
    if current_question < len(questions):
        display_question()
    else:
        display_result()

# Function to display the question and options
def display_question():
    question_label.config(text=questions[current_question])
    
    for i in range(4):
        option_buttons[i].config(text=options[current_question][i])

# Function to display the final score
def display_result():
    question_label.config(text="Quiz completed! Your score is: " + str(score) + "/" + str(len(questions)))

# Create the main window
window = tk.Tk()

# Create the question label
question_label = tk.Label(window, text="")
question_label.pack()

# Create the option buttons
option_buttons = []
for i in range(4):
    button = tk.Button(window, text="", command=lambda i=i: check_answer(i))
    button.pack()
    option_buttons.append(button)

# Start the quiz
display_question()

# Run the main window
window.mainloop()




# In[ ]:




