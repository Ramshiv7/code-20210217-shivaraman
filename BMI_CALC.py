import os, json, http

class Person:

    def __init__(self):
        print("BMI Index Calculator")

    def cal_bmi():

        with open("D:\\BMI CALC - PY\\Patient_APIDATA.json", "r") as f:
            content = f.read()
            json_data = json.loads(content)
            print(json_data[1]["Gender"])
            print(type(json_data))
            print("Calculating BMI of the Person from JSON FILE")
            over_weight_count=0
            
            for i in range(len(json_data)):

                bmi_formula = json_data[i]["WeightKg"] / ((json_data[i]["HeightCm"]/ 100) * (json_data[i]["HeightCm"]/ 100) )
                bmi_result = round(bmi_formula,2)
                #print(bmi_formula)


                if bmi_result <= 18.4 :
                    x = {"bmi_category":"Underweight", "bmi_range": bmi_result, "Health risk": "Malnutrition risk"}
                    print(f"Gender:{json_data[i]['Gender']} | Weight: {json_data[i]['WeightKg']} | Height: {json_data[i]['HeightCm']} | bmi_category: {x['bmi_category']} | bmi_range: {x['bmi_range']} | Health Risk: {x['Health risk']} ")
                elif bmi_result >= 18.5 and bmi_result <= 24.9 :
                    x = {"bmi_category":"Normal weight", "bmi_range": bmi_result, "Health risk": "Low risk"}
                    print(f"Gender:{json_data[i]['Gender']} | Weight: {json_data[i]['WeightKg']} | Height: {json_data[i]['HeightCm']} | bmi_category: {x['bmi_category']} | bmi_range: {x['bmi_range']} | Health Risk: {x['Health risk']} ")
                elif bmi_result >= 25 and bmi_result <= 29.9 :
                    x = {"bmi_category":"Overweight", "bmi_range": bmi_result, "Health risk": "Enhanced risk"}
                    over_weight_count+= 1
                    print(f"Gender:{json_data[i]['Gender']} | Weight: {json_data[i]['WeightKg']} | Height: {json_data[i]['HeightCm']} | bmi_category: {x['bmi_category']} | bmi_range: {x['bmi_range']} | Health Risk: {x['Health risk']} ")
                elif bmi_result >= 30 and bmi_result <= 34.9 :
                    x = {"bmi_category":"Moderately obese", "bmi_range": bmi_result, "Health risk": "Medium risk"}
                    print(f"Gender:{json_data[i]['Gender']} | Weight: {json_data[i]['WeightKg']} | Height: {json_data[i]['HeightCm']} | bmi_category: {x['bmi_category']} | bmi_range: {x['bmi_range']} | Health Risk: {x['Health risk']} ")
                elif bmi_result >= 35 and bmi_result <= 39.9 :
                    x = {"bmi_category":"Severely obese", "bmi_range": bmi_result, "Health risk": "High risk"}
                    print(f"Gender:{json_data[i]['Gender']} | Weight: {json_data[i]['WeightKg']} | Height: {json_data[i]['HeightCm']} | bmi_category: {x['bmi_category']} | bmi_range: {x['bmi_range']} | Health Risk: {x['Health risk']} ")
                elif bmi_result >= 40 :
                    x = {"bmi_category":"Very severely obese", "bmi_range": bmi_result, "Health risk": "Very high risk"}
                    print(f"Gender:{json_data[i]['Gender']} | Weight: {json_data[i]['WeightKg']} | Height: {json_data[i]['HeightCm']} | bmi_category: {x['bmi_category']} | bmi_range: {x['bmi_range']} | Health Risk: {x['Health risk']} ")

                else:
                    print("Not Defined")


            print(f'Number of overweight people is {over_weight_count}')





x = Person
x.cal_bmi()
