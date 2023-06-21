import tkinter as tk
from random import choice

class ShuffleApp:
    def __init__(self, master):
        self.master = master
        master.title("Mythical Generator")
        
        self.options = [
            [True, False],
            ['brass', 'woodwind', 'percussion', 'string'],
            ['trying their best', 'novice', 'master'],
            ['one', 'two', 'three or more'],
            ['fur', 'feathers', 'scales', 'smooth', 'other'],
            ['one', 'two', 'three', 'four', 'five or more'],
            ['cool', 'warm', 'neutral'],
            ['wings', 'symb partner', 'horns', 'bioluminescence', 'multiple heads', 'robotic parts', 'different eyes'],
            ['blend in', 'stand out'],
            ['symmetrical', 'asymmetrical'],
            ['playing instrument', 'anatomy'],
            [True, False],
            "island.txt" #download this if you dont have it
        ]
        
        self.questions = [
            "Instrumental:",
            "If 1 is true, what type?:",
            "How good?:",
            "How many eyes?:",
            "What type of skin?:",
            "How many limbs?:",
            "Colors?:",
            "Special features?:",
            "Does it..?:",
            "Is it..?:",
            "How does it make its sound?:",
            "Is it in a family?:",
            "Island:"
        ]

        self.result_labels = [tk.Label(master, text=question) for question in self.questions]
        self.result_values = [tk.Label(master, text="") for _ in self.questions]
        self.shuffle_buttons = [tk.Button(master, text="Shuffle", command=lambda i=i: self.shuffle_single(i)) for i in range(len(self.questions))]

        for i in range(len(self.questions)):
            self.result_labels[i].grid(row=i, column=0)
            self.result_values[i].grid(row=i, column=1)
            self.shuffle_buttons[i].grid(row=i, column=2)

        self.shuffle_all_button = tk.Button(master, text="Shuffle All", command=self.shuffle_all)
        self.shuffle_all_button.grid(row=len(self.questions), column=0, columnspan=3)

    def shuffle_single(self, index):
        options = self.options[index]
        if isinstance(options, str):
            with open(options, 'r') as file:
                options = [line.strip() for line in file.readlines()]
        result = str(choice(options))
        if index == len(self.options) - 2 and result == 'True':  # this line is probably broken wtfffffff
            with open('all.txt', 'r') as file:
                options = [line.strip() for line in file.readlines()]
                result += ', ' + str(choice(options))
        self.result_values[index]['text'] = result

    def shuffle_all(self):
        for i in range(len(self.questions)):
            self.shuffle_single(i)
#im pretty sure if you were to remake this you could probably do it in 1 line of code sos

if __name__ == "__main__":
    root = tk.Tk()
    my_app = ShuffleApp(root)
    root.mainloop()
