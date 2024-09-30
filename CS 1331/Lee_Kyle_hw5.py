import tkinter as tk
from tkinter import messagebox

#Class for the circular linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#Circular Linked List implementation
class CircularLinkedList:
    def __init__(self):
        self.head = None

    #Appends a new node to the end of the list
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    #Removes a specific node from the list
    def remove(self, node):
        current = self.head
        prev = None
        while True:
            if current.data == node.data:
                if prev:
                    prev.next = current.next
                else:
                    while current.next != self.head:
                        current = current.next
                    current.next = self.head.next
                    self.head = self.head.next
                break
            prev = current
            current = current.next

    #Gets the size of the list
    def get_size(self):
        size = 0
        if self.head:
            current = self.head
            while True:
                size += 1
                current = current.next
                if current == self.head:
                    break
        return size

#Class for the counting-out game
class CountingOutGameGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Counting-Out Game")
        
        self.N = None
        self.K = None
        self.players = CircularLinkedList()

        #Creates the GUI elements
        self.info_text = tk.Text(master, height=10, width=50)
        self.info_text.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        self.N_label = tk.Label(master, text="Enter N (1<N<12):")
        self.N_label.grid(row=1, column=0, padx=5, pady=5)
        self.N_entry = tk.Entry(master)
        self.N_entry.grid(row=1, column=1, padx=5, pady=5)

        self.K_label = tk.Label(master, text="Enter K (K>=1):")
        self.K_label.grid(row=2, column=0, padx=5, pady=5)
        self.K_entry = tk.Entry(master)
        self.K_entry.grid(row=2, column=1, padx=5, pady=5)

        self.start_button = tk.Button(master, text="Start", command=self.start_game)
        self.start_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        self.eliminate_button = tk.Button(master, text="Eliminate", command=self.eliminate_player, state=tk.DISABLED)
        self.eliminate_button.grid(row=3, column=2, padx=5, pady=5)

    #Function to start the game
    def start_game(self):
        try:
            self.N = int(self.N_entry.get())
            self.K = int(self.K_entry.get())
            # Check if N and K are within the specified range
            if not (1 < self.N < 12) or self.K < 1:
                messagebox.showinfo("Invalid Input", "Invalid values for N or K. Please enter valid values.")
                return
        except ValueError:
            messagebox.showinfo("Invalid Input", "Please enter valid values for N and K.")
            return

        #Initializes players in the circular linked list
        self.players = CircularLinkedList()
        for i in range(self.N):
            self.players.append(i)

        #Displays game start message and updates GUI
        self.update_info_text(f"Game started. N={self.N} K={self.K}")
        self.update_players_display()
        self.eliminate_button.config(state=tk.NORMAL)

    #Function to eliminate a player
    def eliminate_player(self):
        if self.players.get_size() == 2:
            # If only 2 players left, declare the winner
            winner = self.players.head.data
            messagebox.showinfo("Game Over", f"Winner: Player {winner}")
            self.info_text.delete(1.0, tk.END)
            self.clear_players_display()
            self.eliminate_button.config(state=tk.DISABLED)
            return

        #Eliminates player based on the counting rule
        for _ in range(self.K - 1):
            self.players.head = self.players.head.next
        eliminated_player = self.players.head.data
        self.players.remove(self.players.head)
        self.update_info_text(f"Player {eliminated_player} eliminated.")
        self.update_players_display()

    #Function to update the informational text
    def update_info_text(self, message):
        self.info_text.insert(tk.END, message + "\n")
        self.info_text.see(tk.END)

    #Function to update the display of players
    def update_players_display(self):
        players_str = "Players: "
        current = self.players.head
        while True:
            players_str += str(current.data) + " "
            current = current.next
            if current == self.players.head:
                break
        self.update_info_text(players_str)

    #Function to clear the display of players
    def clear_players_display(self):
        self.info_text.delete(1.0, tk.END)

#Function to create the GUI
def main():
    root = tk.Tk()
    app = CountingOutGameGUI(root)
    root.mainloop()

#This is the entry point of the program
if __name__ == "__main__":
    main()
