#main

import gui

def main():
    def validation(number, units, unit1, unit2):
        try:
            number = float(number)
            error2= not (number >= 0)

        except ValueError:
            number= None
            error2= True

        error1 = not ((unit1 in units) and (unit2 in units))
            
        return (error1, error2, number)
    
    def calculate(units_dict, number, unit_from, unit_to):
        if number.is_integer():
            number= int(number)

        result= number * (units_dict[unit_to] / units_dict[unit_from])

        result= round(result, 6)

        if result.is_integer():
            result= int(result)

        return result, number

    def weight_choice():
        def weight_converter():
            units= ("kg", "g", "mg")
            
            number= weight_obj.weight_number_var.get() 
            unit_from = weight_obj.weight_unit_from_var.get()
            unit_to= weight_obj.weight_unit_to_var.get()

            unit_from= unit_from.lower().strip()
            unit_to= unit_to.lower().strip()

            error1, error2, number = validation(number, units, unit_from, unit_to)


            if error1 or error2:
                weight_obj.weight_error_display()

                if (error1) and (error2):
                    weight_obj.weight_error_both()

                elif error1:
                    weight_obj.weight_error_first()

                else:
                    weight_obj.weight_error_second()

            else:
                units_dict= {
                    "kg": 1,
                    "g": 1000,
                    "mg": 1000000
                }

                result, number= calculate(units_dict, number, unit_from, unit_to)

                weight_obj.weight_convert_display(number, unit_from, unit_to, result)
        
        unit_obj.root.withdraw()

        weight_obj= gui.Unit_converter_weight(unit_obj.root, weight_converter)

    def distance_choice():
        def distance_converter():
            units= ("km", "m", "cm")

            number= distance_obj.distance_number_var.get()
            unit_from= distance_obj.distance_unit_from_var.get()
            unit_to= distance_obj.distance_unit_to_var.get()

            unit_from= unit_from.lower().strip()
            unit_to= unit_to.lower().strip()

            error1, error2, number = validation(number, units, unit_from, unit_to)

            if error1 or error2:
                distance_obj.distance_error_display()

                if (error1) and (error2):
                    distance_obj.distance_error_both()

                elif error1:
                    distance_obj.distance_error_first()

                else:
                    distance_obj.distance_error_second()

            else:
                units_dict= {
                    "km": 1,
                    "m": 1000,
                    "cm": 100000
                }

                result, number= calculate(units_dict, number, unit_from, unit_to)

                distance_obj.distance_convert_display(number, unit_from, unit_to, result)

        unit_obj.root.withdraw()
        
        distance_obj= gui.Unit_converter_distance(unit_obj.root, distance_converter)

    def time_choice():
        def time_converter():
            units= ("hr", "min", "sec")

            number= time_obj.time_number_var.get()
            unit_from = time_obj.time_unit_from_var.get()
            unit_to= time_obj.time_unit_to_var.get()

            unit_from= unit_from.lower().strip()
            unit_to= unit_to.lower().strip()

            error1, error2, number = validation(number, units, unit_from, unit_to)

            if error1 or error2:
                time_obj.time_error_display()

                if (error1) and (error2):
                    time_obj.time_error_both()

                elif error1:
                    time_obj.time_error_first()

                else:
                    time_obj.time_error_second()

            else:
                units_dict= {
                    "hr": 1,
                    "min": 60,
                    "sec": 3600
                }

                result, number= calculate(units_dict, number, unit_from, unit_to)

                time_obj.time_convert_display(number, unit_from, unit_to, result)
        
        unit_obj.root.withdraw()
        
        time_obj= gui.Unit_converter_time(unit_obj.root, time_converter)

    unit_obj= gui.Unit_converter_intro(weight_choice, distance_choice, time_choice)

    unit_obj.run()

if __name__=="__main__":
    main()