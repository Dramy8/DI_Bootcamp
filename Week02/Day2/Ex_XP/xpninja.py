#%%
#EX1
# Instructions
# Write a function called get_full_name() that takes three arguments: 
# 1: first_name, 2: middle_name 3: last_name.
# middle_name should be optional, if it’s omitted by the user,
#  the name returned should only contain the first and the last name.
# For example, get_full_name(first_name="john", middle_name="hooker", last_name="lee") 
# will return John Hooker Lee.
# But get_full_name(first_name="bruce", last_name="lee") will return Bruce Lee.

def get_full_name(first_name, last_name, middle_name=''):
    return f"{first_name} {middle_name} {last_name}"


print(get_full_name("Auriane", "Bouaziz", "Sarah"))


# %%
#EX2
# Instructions
# Write a function that converts English text to morse code and another one that does the opposite.
# Hint: Check the internet for a translation table, 
# every letter is separated with a space and every word is separated with a slash /.


# Dictionnaire Morse
morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..'
}

# Dictionnaire inversé (morse → texte)
reverse_dict = {value: key for key, value in morse_dict.items()}


# 🔹 Texte → Morse
def text_to_morse(text):
    result = []

    for letter in text.upper():
        if letter == " ":
            result.append("/")  # séparateur de mots
        else:
            result.append(morse_dict[letter])

    return " ".join(result)


# 🔹 Morse → Texte
def morse_to_text(morse):
    result = []

    words = morse.split(" / ")

    for word in words:
        letters = word.split()

        for letter in letters:
            result.append(reverse_dict[letter])

        result.append(" ")

    return "".join(result).strip()


# 🔹 Programme principal
def main():
    mode = input("Choose mode: text_to_morse (t) or morse_to_text (m): ").lower()

    if mode == "t":
        text = input("Enter text: ")
        print(text_to_morse(text))

    elif mode == "m":
        morse = input("Enter morse code: ")
        print(morse_to_text(morse))

    else:
        print("Invalid choice")


# 🔹 Lancement
main()

#%%
#EX3
# Write a function named box_printer that takes any amount of strings (not in a list) and prints them, 
# one per line, in a rectangular frame.
# For example calling box_printer("Hello", "World", "in", "reallylongword", "a", "frame") will result as:

# ******************
# * Hello          *
# * World          *
# * in             *
# * reallylongword *
# * a              *
# * frame          *
# ******************

def box_printer():
    text = input("Enter your text: ").split()  # mots
    
    max_length = max(len(word) for word in text)
    
    print("*" * (max_length + 4))
    
    for word in text:
        spaces = " " * (max_length - len(word))
        print(f"* {word}{spaces} *")
    
    print("*" * (max_length + 4))


box_printer()
# %%
#EX4
#it orders numbers sorted. , the mechanism behind the sort function for example. 