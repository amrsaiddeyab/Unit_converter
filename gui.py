#gui

import tkinter as tk

class Unit_converter_intro():
    def __init__(self, weight_choice, distance_choice, time_choice):
        self.root= tk.Tk()
        self.root.title("Unit Converter")
        self.root.resizable(False, False)
        self.root.geometry("300x450")
        self.root.config(bg="yellow")
        self.screen_width= self.root.winfo_screenwidth()
        self.screen_height= self.root.winfo_screenheight()
        self.x= (self.screen_width // 2) - (300 // 2)
        self.y= (self.screen_height // 2) - (450 // 2)

        self.root.geometry(f"300x420+{self.x}+{self.y}")

        tk.Label(self.root, text="",
                        bg="yellow",
                        font=("Arial", 10, "bold")).grid(row=0, column=0, rowspan=2)
        
        self.text = tk.Label(self.root, text="  Unit Converter!  ",
                        bg="#50C878", fg="blue",
                        font=("Arial", 27, "bold"))
        self.text.grid(row=3, column=0, rowspan=2, columnspan=2, sticky="we")

        tk.Label(self.root, text="",
                        bg="yellow",
                        font=("Arial", 30, "bold")).grid(row=5, column=0, rowspan=1)
        
        self.weight_option= tk.Button(self.root, text="1. Weight   ",
                        bg="yellow", fg="blue",
                        font=("Arial", 18, "bold"), bd=4,
                        command= weight_choice)
        self.weight_option.grid(row=6, column=0, sticky='we')

        tk.Label(self.root, text="",
                        bg="yellow",
                        font=("Arial", 10, "bold")).grid(row=7, column=0, rowspan=1)
        
        self.distance_option= tk.Button(self.root, text="2. Distance",
                        bg="yellow", fg="blue",
                        font=("Arial", 18, "bold"), bd=4,
                        command= distance_choice)
        self.distance_option.grid(row=8, column=0, sticky='we')

        tk.Label(self.root, text="",
                        bg="yellow",
                        font=("Arial", 10, "bold")).grid(row=9, column=0, rowspan=1)
        
        self.time_option= tk.Button(self.root, text="3. Time      ",
                        bg="yellow", fg="blue",
                        font=("Arial", 18, "bold"), bd=4,
                        command= time_choice)
        self.time_option.grid(row=10, column=0, sticky='we')

        tk.Label(self.root, text="",
                        bg="yellow",
                        font=("Arial", 10, "bold")).grid(row=11, column=0, rowspan=1)
        
        self.exit_button= tk.Button(self.root, text="4. Exit      ",
                        bg="#50C878", fg="blue",
                        font=("Arial", 18, "bold"), bd=4,
                        command= self.root.destroy)
        self.exit_button.grid(row=12, column=0, sticky='we')

    def run(self):
        self.root.mainloop()

class Unit_converter_weight():
    def __init__(self, main_window, weight_converter):        
        self.weight_main_root= main_window

        self.root_weight= tk.Toplevel()
        self.root_weight.title("Weight Units")
        self.root_weight.resizable(False, False)
        self.root_weight.geometry("600x350")
        self.root_weight.config(bg="black")
        self.screen_width= self.root_weight.winfo_screenwidth()
        self.screen_height= self.root_weight.winfo_screenheight()
        self.x= (self.screen_width // 2) - (600 // 2)
        self.y= (self.screen_height // 2) - (350 // 2)

        self.root_weight.geometry(f"600x350+{self.x}+{self.y}")

        weight_values= [
            "kg --> g",
            "kg --> mg",
            "g --> kg",
            "g --> mg",
            "mg --> kg",
            "mg --> g",

        ]

        tk.Label(self.root_weight, text="",
                        bg="black",
                        font=("Arial", 10,)).grid(row=0, columnspan=2)

        self.weight_text = tk.Label(self.root_weight, text="                     Weight                     ",
                        bg="blue", fg="white",
                        font=("Arial", 30, "bold"))
        self.weight_text.grid(row=2, column=0, columnspan=3, sticky="ew")

        tk.Label(self.root_weight, text="\n\n",
                        bg="black",
                        font=("Arial", 10, "bold")).grid(row=3, column=0)
        
        self.weight_number_var= tk.StringVar(self.root_weight, value="Enter a number to convert")
        self.weight_options_var= tk.StringVar(self.root_weight, value="Select from the list")

        self.weight_number_convert= tk.Entry(self.root_weight,
                        textvariable= self.weight_number_var,
                        font=("Arial", 15, "bold"), bd=4,
                        bg= "blue", fg="white"
                        )
        self.weight_number_convert.config(width=40)
        self.weight_number_convert.grid(row=4,column=0, sticky='we')

        tk.Label(self.root_weight, text="\n",
                        bg="black",
                        font=("Arial", 10, "bold")).grid(row=5, column=0, sticky="e")
        
        weight_options_list= tk.OptionMenu(self.root_weight, self.weight_options_var, *weight_values)
        weight_options_list.config(font=("Arial", 15, "bold"),  bd=4, width=40, anchor='w', bg= "blue", fg="white")
        weight_options_list["menu"].config(font=("Arial", 20, "bold"))
        weight_options_list.grid(row=6, column=0, sticky="we")

        tk.Label(self.root_weight, text="\n",
                        bg="black",
                        font=("Arial", 10, "bold")).grid(row=7, column=0, sticky="e")

        self.weight_convert= tk.Button(self.root_weight, text="  Convert!",
                        bg="blue", fg="white",
                        font=("Arial", 20, "bold"), bd=4,
                        command= weight_converter)
        self.weight_convert.grid(row=8, column=0, columnspan=3, sticky='we')

        self.root_weight.protocol("WM_DELETE_WINDOW", self.weight_exit)

    def weight_convert_display(self, number, unit_from, unit_to, result):
        self.weight_convert_window= tk.Toplevel()
        self.weight_convert_window.title("Result")
        self.weight_convert_window.resizable(False, False)
        self.weight_convert_window.geometry("600x200")
        self.weight_convert_window.config(bg="black")
        self.screen_width= self.weight_convert_window.winfo_screenwidth()
        self.screen_height= self.weight_convert_window.winfo_screenheight()
        self.x= (self.screen_width // 2) - (600 // 2)
        self.y= (self.screen_height // 2) - (200 // 2)

        self.weight_convert_window.geometry(f"600x200+{self.x}+{self.y}")

        self.weight_result_text = tk.Label(self.weight_convert_window, text="                     Result:                       ",
                        bg="blue", fg="white",
                        font=("Arial", 30, "bold"))
        self.weight_result_text.grid(row=0, column=0, columnspan=2, sticky="ew")

        tk.Label(self.weight_convert_window, text="\n\n",
                        bg="black",
                        font=("Arial", 10, "bold")).grid(row=1, column=0, sticky="ew")

        self.weight_result= tk.Label(self.weight_convert_window, text=f"{number}{unit_from} = {result}{unit_to}",
                        bg="blue", fg="white",
                        font=("Arial", 30, "bold"))
        self.weight_result.grid(row=3, column=0, columnspan=2, sticky="we")

    def weight_error_display(self):
        self.weight_error_window= tk.Toplevel()
        self.weight_error_window.title("Error!")
        self.weight_error_window.resizable(False, False)
        self.weight_error_window.geometry("600x200")
        self.weight_error_window.config(bg="black")
        self.screen_width= self.weight_error_window.winfo_screenwidth()
        self.screen_height= self.weight_error_window.winfo_screenheight()
        self.x= (self.screen_width // 2) - (600 // 2)
        self.y= (self.screen_height // 2) - (200 // 2)

        self.weight_error_window.geometry(f"600x200+{self.x}+{self.y}")

        self.weight_error_text = tk.Label(self.weight_error_window, text="                    ERROR!                       ",
                        bg="blue", fg="white",
                        font=("Arial", 30, "bold"))
        self.weight_error_text.grid(row=0, column=0, columnspan=2, sticky="ew")

    def weight_error_both(self):
        tk.Label(self.weight_error_window, text="\n\n",
                    bg="black",
                    font=("Arial", 10, "bold")).grid(row=1, column=0, sticky="ew")

        self.weight_result= tk.Label(self.weight_error_window,
                    text=f"1. 'Number' must be a number greater than or equal to zero",
                        bg="blue", fg="white",
                        font=("Arial", 15, "bold"))
        self.weight_result.grid(row=3, column=0, columnspan=2, sticky="w")

        self.weight_result= tk.Label(self.weight_error_window,
                    text=f"2. You should select an option from the list",
                        bg="blue", fg="white",
                        font=("Arial", 15, "bold"))
        self.weight_result.grid(row=4, column=0, columnspan=2, sticky="w")

    def weight_error_select(self):
        tk.Label(self.weight_error_window, text="\n\n",
                    bg="black",
                    font=("Arial", 10, "bold")).grid(row=1, column=0, sticky="ew")

        self.weight_result= tk.Label(self.weight_error_window,
                    text=f"1. You should select an option from the list",
                        bg="blue", fg="white",
                        font=("Arial", 18, "bold"))
        self.weight_result.grid(row=3, column=0, columnspan=2, sticky="w")

    def weight_error_number(self):
        tk.Label(self.weight_error_window, text="\n\n",
                    bg="black",
                    font=("Arial", 10, "bold")).grid(row=1, column=0, sticky="w")

        self.weight_result= tk.Label(self.weight_error_window,
                    text=f"1. 'Number' must be a number greater than or equal to zero",
                        bg="blue", fg="white",
                        font=("Arial", 15, "bold"))
        self.weight_result.grid(row=3, column=0, columnspan=2, sticky="w")

    def weight_windows_exit(self):
        self.weight_error_window.destroy()
        self.weight_convert_window.destroy()

    def weight_exit(self):
        self.weight_main_root.deiconify()
        self.root_weight.destroy()
class Unit_converter_distance():
    def __init__(self, main_window, distance_converter):
        self.distance_main_root= main_window

        self.root_distance= tk.Toplevel()
        self.root_distance.title("Distance Units")
        self.root_distance.resizable(False, False)
        self.root_distance.geometry("600x350")
        self.root_distance.config(bg="#728C00")
        self.screen_width= self.root_distance.winfo_screenwidth()
        self.screen_height= self.root_distance.winfo_screenheight()
        self.x= (self.screen_width // 2) - (600 // 2)
        self.y= (self.screen_height // 2) - (350 // 2)

        self.root_distance.geometry(f"600x350+{self.x}+{self.y}")

        distance_values= [
            "km --> m",
            "km --> cm",
            "m --> km",
            "m --> cm",
            "cm --> km",
            "cm --> m",
        ]

        tk.Label(self.root_distance, text="",
                        bg="#728C00",
                        font=("Arial", 10,)).grid(row=0, columnspan=2)

        self.distance_text = tk.Label(self.root_distance, text="                    Distance                   ",
                        bg="#4CC417", fg="white",
                        font=("Arial", 30, "bold"))
        self.distance_text.grid(row=2, column=0, columnspan=3, sticky="ew")

        tk.Label(self.root_distance, text="\n\n",
                        bg="#728C00",
                        font=("Arial", 10, "bold")).grid(row=3, column=0)

        self.distance_number_var= tk.StringVar(self.root_distance, value="Enter a number to convert")
        self.distance_options_var= tk.StringVar(self.root_distance, value="Select from the list")

        self.distance_number_convert= tk.Entry(self.root_distance,
                        textvariable= self.distance_number_var,
                        font=("Arial", 15, "bold"), bd=4,
                        bg="#4CC417", fg="white"
                        )
        self.distance_number_convert.config(width=40)
        self.distance_number_convert.grid(row=4,column=0, sticky='we')

        tk.Label(self.root_distance, text="\n",
                        bg="#728C00",
                        font=("Arial", 10, "bold")).grid(row=5, column=0, sticky="e")
        
        distance_options_list= tk.OptionMenu(self.root_distance, self.distance_options_var, *distance_values)
        distance_options_list.config(font=("Arial", 15, "bold"),
                        bd=4, width=40, anchor='w',
                        bg="#4CC417", fg="white")
        distance_options_list["menu"].config(font=("Arial", 20, "bold"))
        distance_options_list.grid(row=6, column=0, sticky="we")

        tk.Label(self.root_distance, text="\n",
                        bg="#728C00",
                        font=("Arial", 10, "bold")).grid(row=7, column=0, sticky="e")

        self.distance_convert= tk.Button(self.root_distance, text="  Convert!",
                        bg="#08A04B", fg= "white",
                        font=("Arial", 20, "bold"), bd=4,
                        command= distance_converter)
        self.distance_convert.grid(row=8, column=0, columnspan=3, sticky='we')

        self.root_distance.protocol("WM_DELETE_WINDOW", self.distance_exit)
    
    def distance_convert_display(self, number, unit_from, unit_to, result):
        self.distance_convert_window= tk.Toplevel()
        self.distance_convert_window.title("Result")
        self.distance_convert_window.resizable(False, False)
        self.distance_convert_window.geometry("600x200")
        self.distance_convert_window.config(bg="#728C00")
        self.screen_width= self.distance_convert_window.winfo_screenwidth()
        self.screen_height= self.distance_convert_window.winfo_screenheight()
        self.x= (self.screen_width // 2) - (600 // 2)
        self.y= (self.screen_height // 2) - (200 // 2)

        self.distance_convert_window.geometry(f"600x200+{self.x}+{self.y}")

        self.distance_result_text = tk.Label(self.distance_convert_window, text="                     Result:                       ",
                        bg="#4CC417", fg="white",
                        font=("Arial", 30, "bold"))
        self.distance_result_text.grid(row=0, column=0, columnspan=2, sticky="ew")

        tk.Label(self.distance_convert_window, text="\n\n",
                        bg="#728C00",
                        font=("Arial", 10, "bold")).grid(row=1, column=0, sticky="ew")

        self.distance_result= tk.Label(self.distance_convert_window, text=f"{number}{unit_from} = {result}{unit_to}",
                        bg="#4CC417", fg="white",
                        font=("Arial", 30, "bold"))
        self.distance_result.grid(row=3, column=0, columnspan=2, sticky="we")

    def distance_error_display(self, e1= None, e2= None):
        self.distance_error_window= tk.Toplevel()
        self.distance_error_window.title("Error!")
        self.distance_error_window.resizable(False, False)
        self.distance_error_window.geometry("600x200")
        self.distance_error_window.config(bg="#728C00")
        self.screen_width= self.distance_error_window.winfo_screenwidth()
        self.screen_height= self.distance_error_window.winfo_screenheight()
        self.x= (self.screen_width // 2) - (600 // 2)
        self.y= (self.screen_height // 2) - (200 // 2)

        self.distance_error_window.geometry(f"600x200+{self.x}+{self.y}")

        self.distance_error_text = tk.Label(self.distance_error_window, text="                    ERROR!                       ",
                        bg="#4CC417", fg="white",
                        font=("Arial", 30, "bold"))
        self.distance_error_text.grid(row=0, column=0, columnspan=2, sticky="ew")

    def distance_error_both(self):
        tk.Label(self.distance_error_window, text="\n\n",
                    bg="#728C00",
                    font=("Arial", 10, "bold")).grid(row=1, column=0, sticky="ew")

        self.distance_result= tk.Label(self.distance_error_window,
                    text=f"1. 'Number' must be a number greater than or equal to zero",
                        bg="#4CC417", fg="white",
                        font=("Arial", 15, "bold"))
        self.distance_result.grid(row=3, column=0, columnspan=2, sticky="w")

        self.distance_result= tk.Label(self.distance_error_window,
                    text=f"2. You should select an option from the list",
                        bg="#4CC417", fg="white",
                        font=("Arial", 15, "bold"))
        self.distance_result.grid(row=4, column=0, columnspan=2, sticky="w")

    def distance_error_select(self):
        tk.Label(self.distance_error_window, text="\n\n",
                    bg="#728C00",
                    font=("Arial", 10, "bold")).grid(row=1, column=0, sticky="ew")

        self.distance_result= tk.Label(self.distance_error_window,
                    text=f"1. You should select an option from the list",
                        bg="#4CC417", fg="white",
                        font=("Arial", 18, "bold"))
        self.distance_result.grid(row=3, column=0, columnspan=2, sticky="w")

    def distance_error_number(self):
        tk.Label(self.distance_error_window, text="\n\n",
                    bg="#728C00",
                    font=("Arial", 10, "bold")).grid(row=1, column=0, sticky="w")

        self.distance_result= tk.Label(self.distance_error_window,
                    text=f"1. 'Number' must be a number greater than or equal to zero",
                        bg="#4CC417", fg="white",
                        font=("Arial", 15, "bold"))
        self.distance_result.grid(row=3, column=0, columnspan=2, sticky="w")

    def distance_exit(self):
        self.distance_main_root.deiconify()
        self.root_distance.destroy()

class Unit_converter_time():
    def __init__(self, main_window, time_converter):
        self.time_main_root= main_window

        self.root_time= tk.Toplevel()
        self.root_time.title("Time Units")
        self.root_time.resizable(False, False)
        self.root_time.geometry("600x350")
        self.root_time.config(bg="gray")
        self.screen_width= self.root_time.winfo_screenwidth()
        self.screen_height= self.root_time.winfo_screenheight()
        self.x= (self.screen_width // 2) - (600 // 2)
        self.y= (self.screen_height // 2) - (350 // 2)

        self.root_time.geometry(f"600x350+{self.x}+{self.y}")

        time_values= [
            "hr --> min",
            "hr --> sec",
            "min --> hr",
            "min --> sec",
            "sec --> hr",
            "sec --> min",
        ]

        tk.Label(self.root_time, text="",
                        bg="gray",
                        font=("Arial", 10,)).grid(row=0, columnspan=2)

        self.time_text = tk.Label(self.root_time, text="                       Time                       ",
                        bg="#A9A9A9", fg="white",
                        font=("Arial", 30, "bold"))
        self.time_text.grid(row=2, column=0, columnspan=3, sticky="ew")

        tk.Label(self.root_time, text="\n\n",
                        bg="gray", fg="white",
                        font=("Arial", 10, "bold")).grid(row=3, column=0)

        self.time_number_var= tk.StringVar(self.root_time, value="Enter a number to convert")
        self.time_options_var= tk.StringVar(self.root_time, value="Select from the list")

        self.time_number_convert= tk.Entry(self.root_time,
                        textvariable= self.time_number_var,
                        font=("Arial", 15, "bold"), bd=4,
                        bg="gray", fg="white"
                        )
        self.time_number_convert.config(width=40)
        self.time_number_convert.grid(row=4,column=0, sticky='we')

        tk.Label(self.root_time, text="\n",
                        bg="gray",
                        font=("Arial", 10, "bold")).grid(row=5, column=0, sticky="e")
        
        time_options_list= tk.OptionMenu(self.root_time, self.time_options_var, *time_values)
        time_options_list.config(font=("Arial", 15, "bold"),
                        bd=4, width=40, anchor='w',
                        bg="gray", fg="white")
        time_options_list["menu"].config(font=("Arial", 20, "bold"))
        time_options_list.grid(row=6, column=0, sticky="we")

        tk.Label(self.root_time, text="\n",
                        bg="gray",
                        font=("Arial", 10, "bold")).grid(row=7, column=0, sticky="e")

        self.time_convert= tk.Button(self.root_time, text="  Convert!",
                        bg="#A9A9A9", fg="white",
                        font=("Arial", 20, "bold"), bd=4,
                        command= time_converter)
        self.time_convert.grid(row=8, column=0, columnspan=3, sticky='we')

        self.root_time.protocol("WM_DELETE_WINDOW", self.time_exit)

    def time_convert_display(self, number, unit_from, unit_to, result):
        self.time_convert_window= tk.Toplevel()
        self.time_convert_window.title("Result")
        self.time_convert_window.resizable(False, False)
        self.time_convert_window.geometry("600x200")
        self.time_convert_window.config(bg="gray")
        self.screen_width= self.time_convert_window.winfo_screenwidth()
        self.screen_height= self.time_convert_window.winfo_screenheight()
        self.x= (self.screen_width // 2) - (600 // 2)
        self.y= (self.screen_height // 2) - (200 // 2)

        self.time_convert_window.geometry(f"600x200+{self.x}+{self.y}")

        self.time_result_text = tk.Label(self.time_convert_window, text="                     Result:                       ",
                        bg="#A9A9A9", fg="white",
                        font=("Arial", 30, "bold"))
        self.time_result_text.grid(row=0, column=0, columnspan=2, sticky="ew")

        tk.Label(self.time_convert_window, text="\n\n",
                        bg="gray",
                        font=("Arial", 10, "bold")).grid(row=1, column=0, sticky="ew")

        self.time_result= tk.Label(self.time_convert_window, text=f"{number}{unit_from} = {result}{unit_to}",
                        bg="#A9A9A9", fg="white",
                        font=("Arial", 30, "bold"))
        self.time_result.grid(row=3, column=0, columnspan=2, sticky="we")

    def time_error_display(self, e1= None, e2= None):
        self.time_error_window= tk.Toplevel()
        self.time_error_window.title("Error!")
        self.time_error_window.resizable(False, False)
        self.time_error_window.geometry("600x200")
        self.time_error_window.config(bg="gray")
        self.screen_width= self.time_error_window.winfo_screenwidth()
        self.screen_height= self.time_error_window.winfo_screenheight()
        self.x= (self.screen_width // 2) - (600 // 2)
        self.y= (self.screen_height // 2) - (200 // 2)

        self.time_error_window.geometry(f"600x200+{self.x}+{self.y}")

        self.time_error_text = tk.Label(self.time_error_window, text="                    ERROR!                       ",
                        bg="#A9A9A9", fg="white",
                        font=("Arial", 30, "bold"))
        self.time_error_text.grid(row=0, column=0, columnspan=2, sticky="ew")

    def time_error_both(self):
        tk.Label(self.time_error_window, text="\n\n",
                    bg="gray",
                    font=("Arial", 10, "bold")).grid(row=1, column=0, sticky="ew")

        self.time_result= tk.Label(self.time_error_window,
                    text=f"1. 'Number' must be a number greater than or equal to zero",
                        bg="#A9A9A9", fg="white",
                        font=("Arial", 15, "bold"))
        self.time_result.grid(row=3, column=0, columnspan=2, sticky="w")

        self.time_result= tk.Label(self.time_error_window,
                    text=f"2. You should select an option from the list",
                        bg="#A9A9A9", fg="white",
                        font=("Arial", 15, "bold"))
        self.time_result.grid(row=4, column=0, columnspan=2, sticky="w")

    def time_error_select(self):
        tk.Label(self.time_error_window, text="\n\n",
                    bg="gray",
                    font=("Arial", 10, "bold")).grid(row=1, column=0, sticky="ew")

        self.time_result= tk.Label(self.time_error_window,
                    text=f"1. You should select an option from the list",
                        bg="#A9A9A9", fg="white",
                        font=("Arial", 18, "bold"))
        self.time_result.grid(row=3, column=0, columnspan=2, sticky="w")

    def time_error_number(self):
        tk.Label(self.time_error_window, text="\n\n",
                    bg="gray",
                    font=("Arial", 10, "bold")).grid(row=1, column=0, sticky="w")

        self.time_result= tk.Label(self.time_error_window,
                    text=f"1. 'Number' must be a number greater than or equal to zero",
                        bg="#A9A9A9", fg="white",
                        font=("Arial", 15, "bold"))
        self.time_result.grid(row=3, column=0, columnspan=2, sticky="w")

    def time_exit(self):
        self.time_main_root.deiconify()
        self.root_time.destroy()