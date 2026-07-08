import gui

def weight_choice():
    weight_obj= gui.Unit_converter_weight()

def distance_choice():
    distance_obj= gui.Unit_converter_distance()

def time_choice():
    time_obj= gui.Unit_converter_time()

unit_obj= gui.Unit_converter_intro(weight_choice, distance_choice, time_choice)

unit_obj.run()