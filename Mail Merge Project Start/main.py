PLACE_HOLDER = "[name]"

with open('./Input/Names/invited_names.txt', mode= 'r') as names_file:
    names = names_file.readlines()
    
with open('./Input/Letters/starting_letter.txt', mode= 'r') as letter_file:
    letter_content = letter_file.read()
    print(letter_content)
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_content.replace(PLACE_HOLDER, stripped_name)
        new_file = f'./Output/ReadyToSend/{stripped_name}.txt'
        with open(new_file, mode= 'w') as file:
            file.write(new_letter)