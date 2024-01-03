def validate_data(data_list):
    if not all(isinstance(item,(int, float)) for item in data_list):
           raise TypeError("Invalid data in list")

data = [1, 2, 2.3, four]
try:
    validate_data(data)
    print("Data is valid")
except TypeError as e:
    print(e)
