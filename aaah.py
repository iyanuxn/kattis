while True:
    user_input = input("Enter amount of (aaaah's) Jon Marius can say: ").lower()
    h = user_input.count('h')
    if (h != 1):
        print("Input doesn't fit format")
        continue
    else:
        break
while True:
    doc_rec = input("Enter Doctor's recommendation of (aaaah's): ").lower()
    h = doc_rec.count('h')
    if (h != 1):
        print("Input doesn't fit format")
        continue
    else:
        break
user_length = len(user_input)
doc_length = len(doc_rec)
if user_length >= doc_length:
    print('go')
    exit()
else:
    print('no')
    exit()