    # listS = ['apple', 'banana', 'kathal', 'aam', 'jaam', 'anaar']
    # j = len(listS) - 1
    # # print(len(listS))
    # # print(j)
    # for i in range(0,len(listS)):
    #     if (i == j or i!=j) and (i==j+1 or i==j-1):
    #         print(listS[j])
    #     j=j-1

# ----------------------------------------------------------
# string looping

    # test_string = "abc1234"

    # for char in test_string:
    #     print(chr(ord(char) + 1))

# =============================================
# Looping dictionary
    # database = {
    #     'abc@gmail.com' : 'abc1234', #bcd2345
    #     'gef@gmail.com' : 'bcd4567', #cde5678
    #     'qwert@gmail.com' : 'eworig781'
    # }

    # for key,value in database.items():
    #     encoded_password = ""

    #     for char in value:
            
    #         if(char == 'z'):
    #             encoded_character = 'a'
    #         elif(char == 'Z'):
    #             encoded_character = 'A'
    #         else:
    #             encoded_character = chr(ord(char) + 1)

    #         encoded_password = encoded_password + encoded_character
        
    #     database[key] = encoded_password

    # print(database)

# =========================================================
# PhoneBook

PhoneBook = {
    'Amit' :{
        'NickName' : 'Datto',
        'Age' : 22,
        'City' : 'Dhaka'
    },
    'Mahera': {
        'Name': {
            'First_Name' : 'Mahera',
            'Last_Name' : 'Rezwan'
        },
        'Age': 24,
        'City': 'Rajshahi'
    }
}

print(PhoneBook)