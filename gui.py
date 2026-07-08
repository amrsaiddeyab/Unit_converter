import tkinter as tk

class Unit_converter_intro():
    def __init__(self, weight_choice, distance_choice, time_choice):
        self.root= tk.Tk()
        self.root.title("Unit Converter")
        self.root.resizable(False, False)
        self.root.geometry("300x350")
        self.root.config(bg="yellow")
        self.screen_width= self.root.winfo_screenwidth()
        self.screen_height= self.root.winfo_screenheight()
        self.x= (self.screen_width // 2) - (300 // 2)
        self.y= (self.screen_height // 2) - (350 // 2)

        self.root.geometry(f"300x350+{self.x}+{self.y}")

        tk.Label(self.root, text="",
                        bg="yellow",
                        font=("Arial", 10, "bold")).grid(row=0, column=0, rowspan=2)
        
        self.text = tk.Label(self.root, text="  Unit Converter!  ",
                        bg="#08A04B", fg="blue",
                        font=("Arial", 27, "bold"))
        self.text.grid(row=3, column=0, rowspan=2, columnspan=2, sticky="we")

        tk.Label(self.root, text="",
                        bg="yellow",
                        font=("Arial", 30, "bold")).grid(row=5, column=0, rowspan=1)
        
        self.weight_option= tk.Button(self.root, text="1. Weight   ",
                        bg="yellow", fg="blue",
                        font=("Arial", 18, "bold"), bd=3,
                        command=weight_choice)
        self.weight_option.grid(row=6, column=0, sticky='we')

        tk.Label(self.root, text="",
                        bg="yellow",
                        font=("Arial", 10, "bold")).grid(row=7, column=0, rowspan=1)
        
        self.distance_option= tk.Button(self.root, text="2. Distance",
                        bg="yellow", fg="blue",
                        font=("Arial", 18, "bold"), bd=3,
                        command=distance_choice)
        self.distance_option.grid(row=8, column=0, sticky='we')

        tk.Label(self.root, text="",
                        bg="yellow",
                        font=("Arial", 10, "bold")).grid(row=9, column=0, rowspan=1)
        
        self.time_option= tk.Button(self.root, text="3. Time      ",
                        bg="yellow", fg="blue",
                        font=("Arial", 18, "bold"), bd=3,
                        command=time_choice)
        self.time_option.grid(row=10, column=0, sticky='we')

    def run(self):
        self.root.mainloop()

class Unit_converter_weight():
    def __init__(self):
        self.root_weight= tk.Tk()
        self.root_weight.title("Weight Units")
        self.root_weight.resizable(False, False)
        self.root_weight.geometry("600x350")
        self.root_weight.config(bg="blue")
        self.screen_width= self.root_weight.winfo_screenwidth()
        self.screen_height= self.root_weight.winfo_screenheight()
        self.x= (self.screen_width // 2) - (600 // 2)
        self.y= (self.screen_height // 2) - (350 // 2)

        self.root_weight.geometry(f"600x350+{self.x}+{self.y}")


class Unit_converter_distance():
    def __init__(self):
        self.root_distance= tk.Tk()
        self.root_distance.title("Distance Units")
        self.root_distance.resizable(False, False)
        self.root_distance.geometry("600x350")
        self.root_distance.config(bg="green")
        self.screen_width= self.root_distance.winfo_screenwidth()
        self.screen_height= self.root_distance.winfo_screenheight()
        self.x= (self.screen_width // 2) - (600 // 2)
        self.y= (self.screen_height // 2) - (350 // 2)

        self.root_distance.geometry(f"600x350+{self.x}+{self.y}")

        tk.Label(self.root_distance, text="",
                        bg="green",
                        font=("Arial", 10, "bold")).grid(row=0, columnspan=2)

        self.distance_text = tk.Label(self.root_distance, text="                 Distance                  ",
                        bg="yellow", fg="blue",
                        font=("Arial", 33, "bold"))
        self.distance_text.grid(row=2, column=0, sticky="we")

        self.distance_units_text = tk.Label(self.root_distance,
                        text="\nType one of these units:('km', 'm','cm'):",
                        bg="green", fg="blue",
                        font=("Arial", 22))
        self.distance_units_text.grid(row=3, column=0, sticky="w")

        self.input_weight= tk.Label(self.root_distance,
                        text="",
                        bg="green", fg="blue",
                        font=("Arial", 22))
        self.input_weight.grid(row=5, column=0, sticky="w")

        self.weight_unit_to_convert= tk.Entry()

class Unit_converter_time():
    def __init__(self):
        self.root_time= tk.Tk()
        self.root_time.title("Time Units")
        self.root_time.resizable(False, False)
        self.root_time.geometry("600x350")
        self.root_time.config(bg="gray")
        self.screen_width= self.root_time.winfo_screenwidth()
        self.screen_height= self.root_time.winfo_screenheight()
        self.x= (self.screen_width // 2) - (600 // 2)
        self.y= (self.screen_height // 2) - (350 // 2)

        self.root_time.geometry(f"600x350+{self.x}+{self.y}")