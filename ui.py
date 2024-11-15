import tkinter as tk
import time
import ast

class KubbFieldUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Kubb veld")
        
        self.canvas = tk.Canvas(root, width=450, height=550, bg='green')
        self.canvas.pack()
        
        self.canvas.create_rectangle(50, 50, 400, 500, outline='white', width=2)
        
        self.blocks = []
        self.texts = []

        self.root.after(5000, self.plaats_blokken)
        
    def plaats_blokken(self):
        print('blokken updaten')
        for block in self.blocks:
            self.canvas.delete(block)
        for text in self.texts:
            self.canvas.delete(text)
        
        # Clear the lists
        self.blocks = []
        self.texts = []
        
        with open('YOLO_coords.txt', 'r') as file:
            blokken = file.readline()
            blokken_lijst = ast.literal_eval(blokken)
            for blok in blokken_lijst:
                x, y, soort = blok[0], blok[1], blok[2]
                block = self.canvas.create_rectangle(x, y, x + 20, y + 20, fill='brown')
                text = self.canvas.create_text(x + 10, y + 10, text=str(soort), fill='white')
                self.blocks.append(block)
                self.texts.append(text)
                
root = tk.Tk()
app = KubbFieldUI(root)
root.mainloop()
