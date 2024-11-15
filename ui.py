import tkinter as tk
import random

class KubbFieldUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Kubb veld")
        
        self.canvas = tk.Canvas(root, width=450, height=550, bg='green')
        self.canvas.pack()
        
        self.canvas.create_rectangle(50, 50, 400, 500, outline='white', width=2)
        
        self.blocks = []
        self.texts = []
        for i in range(5):
            block = self.canvas.create_rectangle(0, 0, 20, 20, fill='brown')
            text = self.canvas.create_text(10, 10, text=f"Block {i+1}", fill='white')
            self.blocks.append(block)
            self.texts.append(text)
        
        button = tk.Button(root, text="Update Positions Internally", command=self.update_positions_internally)
        button.pack(pady=20)
        
    def update_positions_internally(self):
        for i in range(5):
            x = random.randint(50, 330)
            y = random.randint(50, 430)
            self.canvas.coords(self.blocks[i], x, y, x + 20, y + 20)
            self.canvas.coords(self.texts[i], x + 10, y + 10)

root = tk.Tk()
app = KubbFieldUI(root)
root.mainloop()
