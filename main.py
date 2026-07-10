import gui
import tkinter as tk

def weight_choice():
    def weight_converter():
        units= ["kg", "g", "mg"]
        
        input_number= weight_obj.weight_number_var.get()
        input_unit_t_convert = weight_obj.weight_unit_t_convert_var.get()
        input_unit_after= weight_obj.weight_unit_after_var.get()

        if (input_unit_t_convert.lower() not in units or input_unit_after.lower() not in units) and (not input_number.isdigit()):
            weight_obj.weight_error("number", "unit")

        elif input_unit_t_convert.lower() not in units or input_unit_after.lower() not in units:
            weight_obj.weight_error("unit")

        elif not input_number.isdigit():
            weight_obj.weight_error('0', "number")

        else:
            input_number= int(input_number)
            if input_unit_t_convert == "kg" and input_unit_after == "g":
                result= input_number*1000

            elif input_unit_t_convert == "kg" and input_unit_after == "mg":
                result= input_number*1000000

            elif input_unit_t_convert == "g" and input_unit_after == "kg":
                result= input_number/1000

            elif input_unit_t_convert == "g" and input_unit_after == "mg":
                result= input_number*1000

            elif input_unit_t_convert == "mg" and input_unit_after == "kg":
                result= input_number/1000000

            else:
                result= input_number/1000

            weight_obj.weight_convert_display(input_number, input_unit_t_convert, input_unit_after, result)

    weight_obj= gui.Unit_converter_weight(weight_converter)

def distance_choice():
    def distance_converter():
        units= ["km", "m", "cm"]

        input_number= distance_obj.distance_number_var.get()
        input_unit_t_convert = distance_obj.distance_unit_t_convert_var.get()
        input_unit_after= distance_obj.distance_unit_after_var.get()

        if (input_unit_t_convert.lower() not in units or input_unit_after.lower() not in units) and (not input_number.isdigit()):
            distance_obj.distance_error("number", "unit")

        elif input_unit_t_convert.lower() not in units or input_unit_after.lower() not in units:
            distance_obj.distance_error("unit")

        elif not input_number.isdigit():
            distance_obj.distance_error('0', "number")

        else:
            input_number= int(input_number)
            if input_unit_t_convert == "km" and input_unit_after == "m":
                result= input_number*1000

            elif input_unit_t_convert == "km" and input_unit_after == "cm":
                result= input_number*100000

            elif input_unit_t_convert == "m" and input_unit_after == "km":
                result= input_number/1000

            elif input_unit_t_convert == "m" and input_unit_after == "cm":
                result= input_number*100

            elif input_unit_t_convert == "cm" and input_unit_after == "km":
                result= input_number/100000

            else:
                result= input_number/100

            distance_obj.distance_convert_display(input_number, input_unit_t_convert, input_unit_after, result)

    distance_obj= gui.Unit_converter_distance(distance_converter)

def time_choice():
    def time_converter():
        units= ["hr", "min", "sec"]

        input_number= time_obj.time_number_var.get()
        input_unit_t_convert = time_obj.time_unit_t_convert_var.get()
        input_unit_after= time_obj.time_unit_after_var.get()

        if (input_unit_t_convert.lower() not in units or input_unit_after.lower() not in units) and (not input_number.isdigit()):
            time_obj.time_error("number", "unit")

        elif input_unit_t_convert.lower() not in units or input_unit_after.lower() not in units:
            time_obj.time_error("unit")

        elif not input_number.isdigit():
            time_obj.time_error('0', "number")

        else:
            input_number= int(input_number)
            if input_unit_t_convert == "hr" and input_unit_after == "min":
                result= input_number*60

            elif input_unit_t_convert == "hr" and input_unit_after == "sec":
                result= input_number*3600

            elif input_unit_t_convert == "min" and input_unit_after == "hr":
                result= input_number/60 

            elif input_unit_t_convert == "min" and input_unit_after == "sec":
                result= input_number*60

            elif input_unit_t_convert == "sec" and input_unit_after == "hr":
                result= input_number/3600

            else:
                result= input_number/60


            time_obj.time_convert_display(input_number, input_unit_t_convert, input_unit_after, result)

    time_obj= gui.Unit_converter_time(time_converter)

unit_obj= gui.Unit_converter_intro(weight_choice, distance_choice, time_choice)

unit_obj.run()