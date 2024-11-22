import tkinter as tk
import ast

class KubbFieldUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Kubb veld")
        
        self.canvas = tk.Canvas(root, width=450, height=550, bg='green')
        self.canvas.pack()
        
        self.canvas.create_rectangle(25, 25, 425, 525, outline='white', width=2)
        
        self.blocks = []
        self.texts = []

        # Schedule block placement every second
        self.plaats_blokken()
        
    def plaats_blokken(self):
        # Clear all existing blocks and texts from the canvas
        print('plaats blokken')
        print('blokken verplaatsen')
        for block in self.blocks:
            self.canvas.delete(block)
        for text in self.texts:
            self.canvas.delete(text)
        
        # Clear the lists
        self.blocks = []
        self.texts = []
        
        # Read the new block positions from the file and place them on the canvas
        with open('YOLO_coords.txt', 'r') as file:
            blokken = file.readline()
            blokken_lijst = ast.literal_eval(blokken)
            for blok in blokken_lijst:
                x, y, soort = blok[0], blok[1], blok[2]
                x, y = x + 25, y + 25
                block = self.canvas.create_rectangle(x, y, x + 20, y + 20, fill='brown')
                text = self.canvas.create_text(x + 10, y + 10, text=str(soort), fill='white')
                self.blocks.append(block)
                self.texts.append(text)
        
        # Schedule the method to run again after 1000 milliseconds (1 second)
        self.root.after(1000, self.plaats_blokken)

root = tk.Tk()
app = KubbFieldUI(root)
root.mainloop()
