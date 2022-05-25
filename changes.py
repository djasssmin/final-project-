from my_exceptions import ChoiceError

def changes(files, text1, text2):
    if files == []:
        raise ChoiceError()
    for file in files:
        with open(file, 'r') as f:
            text = f.read()
        with open(file, 'w') as f:
            text = text.replace(text1, text2)
            f.write(text)    
            