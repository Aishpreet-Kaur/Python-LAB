import random
import tkinter as tk
from tkinter import messagebox

# Backend Code 
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 
          'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.all_cards = [Card(suit, rank) for suit in suits for rank in ranks]
                
    def shuffle(self):
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        return self.all_cards.pop()

class Player:
    def __init__(self, name):
        self.name = name
        self.all_cards = [] 
        
    def remove_one(self):
        return self.all_cards.pop(0)
    
    def add_cards(self, new_cards):
        if isinstance(new_cards, list):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

class WarGame:
    def __init__(self, player_one_name, player_two_name, max_rounds=50):
        self.player_one = Player(player_one_name)
        self.player_two = Player(player_two_name)
        self.new_deck = Deck()
        self.new_deck.shuffle()
        for _ in range(26):
            self.player_one.add_cards(self.new_deck.deal_one())
            self.player_two.add_cards(self.new_deck.deal_one())
        self.round_num = 0
        self.max_rounds = max_rounds

    def play_round(self):
        if self.round_num >= self.max_rounds:
            return self.end_game()
        
        self.round_num += 1
        if len(self.player_one.all_cards) == 0:
            return f"{self.player_two.name} wins! {self.player_one.name} is out of cards."
        if len(self.player_two.all_cards) == 0:
            return f"{self.player_one.name} wins! {self.player_two.name} is out of cards."
        
        player_one_card = self.player_one.remove_one()
        player_two_card = self.player_two.remove_one()

        if player_one_card.value > player_two_card.value:
            self.player_one.add_cards([player_one_card, player_two_card])
            winner = self.player_one.name
        elif player_two_card.value > player_one_card.value:
            self.player_two.add_cards([player_one_card, player_two_card])
            winner = self.player_two.name
        else:
            winner = "Tie"

        return (player_one_card, player_two_card, winner)

    def end_game(self):
        player_one_count = len(self.player_one.all_cards)
        player_two_count = len(self.player_two.all_cards)
        if player_one_count > player_two_count:
            return f"Game Over! {self.player_one.name} wins with {player_one_count} cards!"
        elif player_two_count > player_one_count:
            return f"Game Over! {self.player_two.name} wins with {player_two_count} cards!"
        else:
            return "Game Over! It's a tie!"

# UI Code 
class WarGameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Card Game - War")
        self.root.geometry("900x700")
        self.root.configure(bg="#3e4444")

        self.game = None

        # Main Frame
        self.main_frame = tk.Frame(root, bg="#3e4444", padx=20, pady=20)
        self.main_frame.pack()

        self.title_label = tk.Label(self.main_frame, text="WAR CARD GAME", font=("Helvetica", 24, "bold"), bg="#3e4444", fg="white")
        self.title_label.grid(row=0, column=0, columnspan=2, pady=20)

        self.player_one_label = tk.Label(self.main_frame, text="Player 1 Name:", font=("Arial", 14), bg="#3e4444", fg="white")
        self.player_one_label.grid(row=1, column=0, sticky="e")
        self.player_one_entry = tk.Entry(self.main_frame, font=("Arial", 14))
        self.player_one_entry.grid(row=1, column=1)

        self.player_two_label = tk.Label(self.main_frame, text="Player 2 Name:", font=("Arial", 14), bg="#3e4444", fg="white")
        self.player_two_label.grid(row=2, column=0, sticky="e")
        self.player_two_entry = tk.Entry(self.main_frame, font=("Arial", 14))
        self.player_two_entry.grid(row=2, column=1)

        self.start_button = tk.Button(self.main_frame, text="Start Game", font=("Arial", 14), bg="#006400", fg="white", command=self.start_game)
        self.start_button.grid(row=3, column=0, columnspan=2, pady=20)

        # Gameplay Frame
        self.gameplay_frame = tk.Frame(root, bg="#3e4444", padx=20, pady=20)

        self.status_label = tk.Label(self.gameplay_frame, text="Game Status", font=("Arial", 16), bg="#3e4444", fg="white")
        self.status_label.pack(pady=10)

        self.result_label = tk.Label(self.gameplay_frame, text="Result: None", font=("Arial", 14, "bold"), bg="#3e4444", fg="white")
        self.result_label.pack(pady=10)

        # Display the cards for each player
        self.player_one_card_label = tk.Label(self.gameplay_frame, text="Player 1 Card", font=("Arial", 14, "bold"), bg="#3e4444", fg="white")
        self.player_one_card_label.pack(pady=5)
        self.player_one_card_display = tk.Label(self.gameplay_frame, font=("Arial", 18), bg="#ffffff", width=15, height=5, relief="solid")
        self.player_one_card_display.pack(pady=5)

        self.player_two_card_label = tk.Label(self.gameplay_frame, text="Player 2 Card", font=("Arial", 14, "bold"), bg="#3e4444", fg="white")
        self.player_two_card_label.pack(pady=5)
        self.player_two_card_display = tk.Label(self.gameplay_frame, font=("Arial", 18), bg="#ffffff", width=15, height=5, relief="solid")
        self.player_two_card_display.pack(pady=5)

        self.next_round_button = tk.Button(self.gameplay_frame, text="Next Round", font=("Arial", 14), bg="#006400", fg="white", command=self.play_round)
        self.next_round_button.pack(pady=10)


    def start_game(self):
        player_one_name = self.player_one_entry.get()
        player_two_name = self.player_two_entry.get()

        if not player_one_name or not player_two_name:
            messagebox.showerror("Error", "Please enter names for both players!")
            return

        self.game = WarGame(player_one_name, player_two_name)

        self.main_frame.pack_forget()
        self.gameplay_frame.pack()

        self.status_label.config(text=f"{player_one_name} vs {player_two_name}")
        self.result_label.config(text="Result: None")
        self.next_round_button.config(state=tk.NORMAL)

    def play_round(self):
        if not self.game:
            return

        result = self.game.play_round()

        if isinstance(result, str):  # Game Over
            self.result_label.config(text=result)
            messagebox.showinfo("Game Over", result)
            self.next_round_button.config(state=tk.DISABLED)
        else:
            player_one_card, player_two_card, winner = result
            self.result_label.config(text=f"Player 1: {player_one_card} vs Player 2: {player_two_card}. Winner: {winner}")

            # Display the cards as text
            self.player_one_card_display.config(text=str(player_one_card))
            self.player_two_card_display.config(text=str(player_two_card))

# Main loop to run the UI
if __name__ == "__main__":
    root = tk.Tk()
    app = WarGameApp(root)
    root.mainloop()

