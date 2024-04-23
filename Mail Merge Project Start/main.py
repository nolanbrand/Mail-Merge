with open('./Input/Names/invited_names.txt') as names_file:
    name_list = names_file.readlines()

with open('./Input/Letters/starting_letter.txt') as starting_file:
    starting_text = starting_file.read()

for name in name_list:
    letter_text = starting_text.replace('[name]', name.strip())
    with open(f'./Output/ReadyToSend/letter_for_{name.strip()}.txt', 'w') as final_letter:
        final_letter.write(letter_text)

