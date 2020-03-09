from tkinter import *
import random

class Application(Frame):
    """A GUI application with three buttons. """
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.master = master
        self.grid()
        self.bttn_clicks = 0
        self.create_widgets()

    def create_widgets(self):
        self.lbl = Label(self, text = "You have clicked the button "+str(self.bttn_clicks)+ " times.")
        self.lbl.grid()

        self.bttn1 = Button(self, text = "Add to count")
        self.bttn1.grid()
        self.bttn1["command"] = self.add_to_count

        Label(self, text = "This is button 2").grid()
        self.bttn2 = Button(self)
        self.bttn2.grid()
        self.bttn2.config(text = "Subtract to count")
        self.bttn2["command"] = self.sub_to_count

        Label(self, text = "This is button 3").grid()
        self.bttn3 = Button(self)
        self.bttn3.grid()
        self.bttn3["text"] = "Reset the times clicked."
        self.bttn3["command"] = self.reset


        self.lbl1 = Label(self, text = "The background color is blue.")
        self.lbl1.grid()
        self.bttn4 = Button(self)
        self.bttn4.grid()
        self.bttn4["text"] = "Change background color."
        self.bttn4["command"] = self.backgrond


    def backgrond(self):
        colors = ["blue", "red", "black", "cornflowerblue", "pink", "purple", "green"]
        color = random.choice(colors)
        self.master.config(bg = color)
        self.lbl1.config(text="Background color is "+color+".")



    def add_to_count(self):
        """ Increase click count and display new total. """
        self.bttn_clicks +=1
        self.lbl.config(text = "You have clicked the button "+str(self.bttn_clicks)+ " times.")
        if self.bttn_clicks > 0 :
            self.lbl.config(bg = "cornflowerblue")
        elif self.bttn_clicks ==0:
            self.lbl.config(bg = "blue")
        else:
            self.lbl.config(bg = "lightblue")

    def sub_to_count(self):
        self.bttn_clicks -=1
        self.lbl.config(text="You have clicked the button " + str(self.bttn_clicks) + " times.")
        if self.bttn_clicks > 0:
            self.lbl.config(bg = "lightblue")
        elif self.bttn_clicks ==0:
            self.lbl.config(bg = "blue")
        else:
            self.lbl.config(bg = "cornflowerblue")

    def reset(self):
        self.bttn_clicks = 0
        self.lbl.config(text="You have clicked the button " + str(self.bttn_clicks) + " times.")
        if self.bttn_clicks > 0:
            self.lbl.config(bg="lightblue")
        elif self.bttn_clicks == 0:
            self.lbl.config(bg="blue")
        else:
            self.lbl.config(bg="cornflowerblue")

def main():
    root = Tk()
    root.title("Buttons 2.0")
    root.geometry("720x1080")
    app = Application(root)
    root.config(bg = "blue")
    root.mainloop()

main()