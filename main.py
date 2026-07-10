#main

import gui

def main():
    def validation(number, units, unit1, unit2):
        try:
            number = float(number)
            if number >= 0:
                r2= True
            
            else:
                r2= False

        except ValueError:
            r2= False

        if (unit1 not in units) or (unit2 not in units):
            r1 = False
        
        else:
            r1 = True
            
        return (r1, r2)

    def weight_choice():
        def weight_converter():
            units= ["kg", "g", "mg"]
            
            number= weight_obj.weight_number_var.get() 
            unit_from = weight_obj.weight_unit_from_var.get()
            unit_to= weight_obj.weight_unit_to_var.get()

            unit_from= unit_from.lower().strip()
            unit_to= unit_to.lower().strip()

            r1, r2 = validation(number, units, unit_from, unit_to)

            if (not r1) and (not r2):
                weight_obj.weight_error("number", "unit")

            elif not r1:
                weight_obj.weight_error("unit")

            elif not r2:
                weight_obj.weight_error(None, "number")

            else:
                units_dict= {
                    "kg": 1,
                    "g": 1000,
                    "mg": 1000000
                }

                number= int(number)

                result= number * (units_dict[unit_to] / units_dict[unit_from])

                if len(str(result)) > 5 :
                    result= round(result, 6)

                if int(result) == result:
                    result= int(result)

                weight_obj.weight_convert_display(number, unit_from, unit_to, result)
        
        unit_obj.root.withdraw()

        weight_obj= gui.Unit_converter_weight(unit_obj.root, weight_converter)

    def distance_choice():
        def distance_converter():
            units= ["km", "m", "cm"]

            number= distance_obj.distance_number_var.get()
            unit_from= distance_obj.distance_unit_from_var.get()
            unit_to= distance_obj.distance_unit_to_var.get()

            unit_from= unit_from.lower().strip()
            unit_to= unit_to.lower().strip()

            r1, r2 = validation(number, units, unit_from, unit_to)

            if (not r1) and (not r2):
                distance_obj.distance_error("number", "unit")

            elif not r1:
                distance_obj.distance_error("unit")

            elif not r2:
                distance_obj.distance_error(None, "number")

            else:
                units_dict= {
                    "km": 1,
                    "m": 1000,
                    "cm": 100000
                }

                number= int(number)

                result= number * (units_dict[unit_to] / units_dict[unit_from])

                if len(str(result)) > 5 :
                    result= round(result, 6)

                if int(result) == result:
                    result= int(result)

                distance_obj.distance_convert_display(number, unit_from, unit_to, result)

        unit_obj.root.withdraw()
        
        distance_obj= gui.Unit_converter_distance(unit_obj.root, distance_converter)

    def time_choice():
        def time_converter():
            units= ["hr", "min", "sec"]

            number= time_obj.time_number_var.get()
            unit_from = time_obj.time_unit_from_var.get()
            unit_to= time_obj.time_unit_to_var.get()

            unit_from= unit_from.lower().strip()
            unit_to= unit_to.lower().strip()

            r1, r2 = validation(number, units, unit_from, unit_to)

            if (not r1) and (not r2):
                time_obj.time_error("number", "unit")

            elif not r1:
                time_obj.time_error("unit")

            elif not r2:
                time_obj.time_error(None, "number")

            else:
                units_dict= {
                    "hr": 1,
                    "min": 60,
                    "sec": 3600
                }

                number= int(number)

                result= number * (units_dict[unit_to] / units_dict[unit_from])

                if len(str(result)) > 5 :
                    result= round(result, 6)

                if int(result) == result:
                    result= int(result)

                time_obj.time_convert_display(number, unit_from, unit_to, result)
        
        unit_obj.root.withdraw()
        
        time_obj= gui.Unit_converter_time(unit_obj.root, time_converter)

    unit_obj= gui.Unit_converter_intro(weight_choice, distance_choice, time_choice)

    unit_obj.run()

if __name__=="__main__":
    main()