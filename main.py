#main

import gui

def main():
    def validation(number):
        try:
            number = float(number)
            if number < 0:
                number= None

        except ValueError:
            number= None

        return (number)
    
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
            error1= False
            error2= False

            try:
                number= weight_obj.weight_number_var.get()
                unit_from, unit_to= weight_obj.weight_options_var.get().split("-->")
                unit_from= unit_from.strip()
                unit_to= unit_to.strip()

            except (ValueError, AttributeError):
                error1= True

            finally:
                number = validation(number)

                if number:
                    if not error1:
                        units_dict= {
                            "kg": 1,
                            "g": 1000,
                            "mg": 1000000
                        }

                        result, number= calculate(units_dict, number, unit_from, unit_to)
                        weight_obj.weight_convert_display(number, unit_from, unit_to, result)

                else:
                    error2= True

                if error1 and error2:
                    weight_obj.weight_error_display()
                    weight_obj.weight_error_both()

                elif error1:
                    weight_obj.weight_error_display()
                    weight_obj.weight_error_select()

                elif error2:
                    weight_obj.weight_error_display()
                    weight_obj.weight_error_number()

        unit_obj.root.withdraw()

        weight_obj= gui.Unit_converter_weight(unit_obj.root, weight_converter)

    def distance_choice():
        def distance_converter():
            error1= False
            error2= False

            try:
                number= distance_obj.distance_number_var.get()
                unit_from, unit_to= distance_obj.distance_options_var.get().split("-->")
                unit_from= unit_from.strip()
                unit_to= unit_to.strip()

            except (ValueError, AttributeError):
                error1= True

            finally:
                number = validation(number)

                if number:
                    if not error1:
                        units_dict= {
                            "km": 1,
                            "m": 1000,
                            "cm": 100000
                        }

                        result, number= calculate(units_dict, number, unit_from, unit_to)
                        distance_obj.distance_convert_display(number, unit_from, unit_to, result)

                else:
                    error2= True

                if error1 and error2:
                    distance_obj.distance_error_display()
                    distance_obj.distance_error_both()

                elif error1:
                    distance_obj.distance_error_display()
                    distance_obj.distance_error_select()

                elif error2:
                    distance_obj.distance_error_display()
                    distance_obj.distance_error_number()

        unit_obj.root.withdraw()
        
        distance_obj= gui.Unit_converter_distance(unit_obj.root, distance_converter)

    def time_choice():
        def time_converter():
            error1= False
            error2= False

            try:
                number= time_obj.time_number_var.get()
                unit_from, unit_to= time_obj.time_options_var.get().split("-->")
                unit_from= unit_from.strip()
                unit_to= unit_to.strip()

            except (ValueError, AttributeError):
                error1= True

            finally:
                number = validation(number)

                if number:
                    if not error1:
                        units_dict= {
                            "hr": 1,
                            "min": 60,
                            "sec": 3600
                        }

                        result, number= calculate(units_dict, number, unit_from, unit_to)
                        time_obj.time_convert_display(number, unit_from, unit_to, result)

                else:
                    error2= True

                if error1 and error2:
                    time_obj.time_error_display()
                    time_obj.time_error_both()

                elif error1:
                    time_obj.time_error_display()
                    time_obj.time_error_select()

                elif error2:
                    time_obj.time_error_display()
                    time_obj.time_error_number()
        
        unit_obj.root.withdraw()
        
        time_obj= gui.Unit_converter_time(unit_obj.root, time_converter)

    unit_obj= gui.Unit_converter_intro(weight_choice, distance_choice, time_choice)

    unit_obj.run()

if __name__=="__main__":
    main()