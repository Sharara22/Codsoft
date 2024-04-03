import tkinter as tk
import random

# Function to determine the winner based on user's choice
def determine_winner(user_choice):
    # Generate a random choice for the computer
    computer_choice = random.choice(["rock", "paper", "scissors"])

    # Initialize result variable
    result = ""

    # Determine the winner based on user's choice and computer's choice
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        result = "Congratulations! You won!"
        user_score.set(user_score.get() + 1)  # Increment user's score
    else:
        result = "Sorry, the computer won!"
        computer_score.set(computer_score.get() + 1)  # Increment computer's score

    # Return the result message
    return f"Your choice: {user_choice}\nComputer's choice: {computer_choice}\n{result}"

# Function to reset the game and play again
def play_again():
    result_text.set("")  # Clear the result message

# Create the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

# Set background color
root.configure(bg="#f0f0f0")

# Label for instruction
instruction_label = tk.Label(root, text="Choose rock, paper, or scissors:", bg="#f0f0f0", fg="#333333", font=("Arial", 14))
instruction_label.pack(pady=10)  

# Frame to hold the buttons
buttons_frame = tk.Frame(root, bg="#f0f0f0")
buttons_frame.pack()

# Buttons for rock, paper, and scissors
rock_button = tk.Button(buttons_frame, text="Rock", command=lambda: result_text.set(determine_winner("rock")), bg="#007bff", fg="#ffffff", font=("Arial", 12, "bold"), padx=10, pady=5, bd=0)
rock_button.grid(row=0, column=0, padx=5)

paper_button = tk.Button(buttons_frame, text="Paper", command=lambda: result_text.set(determine_winner("paper")), bg="#28a745", fg="#ffffff", font=("Arial", 12, "bold"), padx=10, pady=5, bd=0)
paper_button.grid(row=0, column=1, padx=5)

scissors_button = tk.Button(buttons_frame, text="Scissors", command=lambda: result_text.set(determine_winner("scissors")), bg="#dc3545", fg="#ffffff", font=("Arial", 12, "bold"), padx=10, pady=5, bd=0)
scissors_button.grid(row=0, column=2, padx=5)

# Label to display game result
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, bg="#f0f0f0", fg="#333333", font=("Arial", 14))
result_label.pack(pady=10)

# Label for scores
score_label = tk.Label(root, text="Scores:", bg="#f0f0f0", fg="#333333", font=("Arial", 14))
score_label.pack()

# Variables to hold user's and computer's scores
user_score = tk.IntVar()
computer_score = tk.IntVar()

# Labels to display user's and computer's scores
user_score_label = tk.Label(root, textvariable=user_score, bg="#f0f0f0", fg="#333333", font=("Arial", 14))
user_score_label.pack()

computer_score_label = tk.Label(root, textvariable=computer_score, bg="#f0f0f0", fg="#333333", font=("Arial", 14))
computer_score_label.pack()

# Button to play again
play_again_button = tk.Button(root, text="Play Again", command=play_again, bg="#ffc107", fg="#333333", font=("Arial", 12, "bold"), padx=10, pady=5, bd=0)
play_again_button.pack(pady=10)

# Run the application
root.mainloop()
