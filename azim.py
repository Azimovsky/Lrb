import re

def clean_text(text):
    name_pattern = r'(?<![\.\?]\s)(?<!^)[A-ZА-Я][a-zа-я]+(?: [A-ZА-Я][a-zа-я]+)?\b'
    phone_pattern = r'\d{1,12}'
    location_pattern = r'\b(район|улица|область|ул.)\b'

    cleaned_text = re.sub(name_pattern, '[censored]', text)
    cleaned_text = re.sub(phone_pattern, '[censored]', cleaned_text)
    cleaned_text = re.sub(location_pattern, '[censored]', cleaned_text)
    
    return cleaned_text

with open('letter.txt', 'r', encoding='utf-8') as file:
    text = file.read()

cleaned_text = clean_text(text)

with open('cleaned_letter.txt', 'w', encoding='utf-8') as output_file:
    output_file.write(cleaned_text)
