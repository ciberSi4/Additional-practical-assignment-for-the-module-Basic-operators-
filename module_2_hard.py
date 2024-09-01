# Задание "Слишком древний шифр"

def CheckingTheMultiplicity (given_numbers :int):
    dictionary_up_to_20 : tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
    calculated_password : list = []
    intermediate_variable : list = []
    our_password : str = ""

    for i in range(given_numbers):
        for j in range(i+1, given_numbers):
            intermediate_variable.append(str(dictionary_up_to_20[i]) + " " + str(dictionary_up_to_20[j]))

    for i in range (len(intermediate_variable)):
        string_representation_of_the_i_list_item = str(intermediate_variable[i])
        the_index_of_the_space_in_the_line = string_representation_of_the_i_list_item.find(" ")
        if given_numbers % (int(string_representation_of_the_i_list_item[:the_index_of_the_space_in_the_line])
                            + int(string_representation_of_the_i_list_item[the_index_of_the_space_in_the_line:])) == 0:
            calculated_password.append(intermediate_variable[i])
    # print("Для контроля:", calculated_password)
    for i in range(len(calculated_password)):
            our_password = our_password + " " + str(calculated_password[i])

    return our_password


given_numbers : int = int (input ("Введите число (от 3 до 20) для расшифровывания пароля: "))
our_password = CheckingTheMultiplicity (given_numbers)
print(f"Ваш пароль для введённого числа {given_numbers}: - {our_password}")