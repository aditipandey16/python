letter='''Dear <|name>,
You are selected!
Date:<|DATE|>'''
name=input("enter ur name")
date=input("enter date")
letter=letter.replace("<|name>",name)
letter=letter.replace("<|DATE|>",date)
print(letter)