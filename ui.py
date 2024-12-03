import tkinter as tk
import ast
import cv2
from PIL import Image, ImageTk

class KubbFieldUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Kubb veld")
        
        self.canvas = tk.Canvas(root, width=450, height=550, bg='green')
        self.canvas.pack()
        
        self.canvas.create_rectangle(25, 25, 425, 525, outline='white', width=2)
        
        self.blocks = []
        self.texts = []

        self.plaats_blokken()
        
    def plaats_blokken(self):
        '''        print('plaats blokken')
        print('blokken verplaatsen')'''
        for block in self.blocks:
            self.canvas.delete(block)
        for text in self.texts:
            self.canvas.delete(text)
        
        self.blocks = []
        self.texts = []
        self.images = []
        
        with open('YOLO_coords.txt', 'r') as file:
            blokken = file.readline()
            try:
                blokken_lijst = ast.literal_eval(blokken)
                self.blocks = []
                self.texts = []
                self.images = []
                for blok in blokken_lijst:
                    x, y = int(blok[0]), int(blok[1])-25
                    if 'enkel_recht' in blok[2]:
                        path = r"images/enkel_recht.png"
                        image = Image.open(path)
                        resized_image = image.resize((50, 50))
                        photo = ImageTk.PhotoImage(resized_image)

                        # plaatsen
                        blok = self.canvas.create_image(x, y, image=photo, anchor = tk.NW)
                        self.blocks.append(blok)
                        self.images.append(photo)
                    elif 'dubbel_recht' == blok[2]:
                        path = r"images/dubbel_recht.png"
                        image = Image.open(path)
                        resized_image = image.resize((50, 50))
                        photo = ImageTk.PhotoImage(resized_image)

                        # plaatsen
                        blok = self.canvas.create_image(x, y, image=photo, anchor = tk.NW)
                        self.blocks.append(blok)
                        self.images.append(photo)
                    elif 'driedubbel_recht' == blok[2]:
                        path = r"images/driedubbel_recht.png"
                        image = Image.open(path)
                        resized_image = image.resize((50, 50))
                        photo = ImageTk.PhotoImage(resized_image)

                        # plaatsen
                        blok = self.canvas.create_image(x, y, image=photo, anchor = tk.NW)
                        self.blocks.append(blok)
                        self.images.append(photo)
                    elif 'koning_recht' == blok[2]:
                        path = r"images/koning_recht.png"
                        image = Image.open(path)
                        resized_image = image.resize((50, 50))
                        photo = ImageTk.PhotoImage(resized_image)

                        # plaatsen
                        blok = self.canvas.create_image(x, y, image=photo, anchor = tk.NW)
                        self.blocks.append(blok)
                        self.images.append(photo)
                    elif 'koning_omgevallen' == blok[2]:
                        path = r"images/koning_omgevallen.png"
                        image = Image.open(path)
                        resized_image = image.resize((50, 50))
                        photo = ImageTk.PhotoImage(resized_image)

                        # plaatsen
                        blok = self.canvas.create_image(x, y, image=photo, anchor = tk.NW)
                        self.blocks.append(blok)
                        self.images.append(photo)
                    elif 'omgevallen' == blok[2]:
                        path = r"images/omgevallen.png"
                        image = Image.open(path)
                        resized_image = image.resize((50, 50))
                        photo = ImageTk.PhotoImage(resized_image)

                        # plaatsen
                        blok = self.canvas.create_image(x, y, image=photo, anchor = tk.NW)
                        self.blocks.append(blok)
                        self.images.append(photo)
                    else:
                        path = r"images/stok.png"
                        image = Image.open(path)
                        resized_image = image.resize((108, 75))
                        photo = ImageTk.PhotoImage(resized_image)

                        # plaatsen
                        x, y = x-25, y
                        blok = self.canvas.create_image(x, y, image=photo, anchor = tk.NW)
                        self.blocks.append(blok)
                        self.images.append(photo)
            except:
                pass


            '''            
            for blok in blokken_lijst:
                x, y, soort = blok[0], blok[1], blok[2]
                x, y = x + 25, y + 25
                block = self.canvas.create_rectangle(x, y, x + 20, y + 20, fill='brown')
                text = self.canvas.create_text(x + 10, y + 10, text=str(soort), fill='white')
                self.blocks.append(block)
                self.texts.append(text)'''
        
        # Schedule the method to run again after 1000 milliseconds (1 second)
        self.root.after(100, self.plaats_blokken)


def main():
    open('YOLO_coords.txt', 'w').close()
    root = tk.Tk()
    app = KubbFieldUI(root)
    root.mainloop()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        root.destroy()


if __name__ == '__main__':
    main()
