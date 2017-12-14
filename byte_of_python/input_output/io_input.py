def reverse(text):
    return text[::-1]

def is_palindrome(text):
    return text == reverse(text)

onething = input('Enter text: ')
something = onething.replace(' ','').replace(',','').replace('.','')\
    .replace('"','').lower()
if is_palindrome(something):
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")

#print(reverse(something))
#a = something[::-1]
#print(a)

