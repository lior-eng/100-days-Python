import pandas as pd

phonetic_data_frame = pd.read_csv("./NATO-alphabet-start/nato_phonetic_alphabet.csv")
# {"A": "Alfa", "B": "Bravo"}
phonetic_dict = {}
phonetic_dict = {row.letter:row.code for (_, row) in phonetic_data_frame.iterrows()}

def generate_phonetic() -> None:
    user_word = input("Enter a word to see the phonetic code: ").upper()
    try:
        phonetic_list = [phonetic_dict[letter] for letter in user_word]
    except KeyError:
        print("Invalid input. Only letters in the alphabet ")
        generate_phonetic()
    else:
        print(phonetic_list)
        
generate_phonetic()   


#################   explanations of loops   #################

student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

student_data_frame = pd.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass