txt_data = "I hate these people"
file_path = "output.txt"
with open(file_path,'a') as file:
    file.write("\n" +txt_data)
    print(f"txt file '{file_path}' was created")

