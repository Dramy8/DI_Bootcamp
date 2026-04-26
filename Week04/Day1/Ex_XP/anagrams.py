from anagram_checker import AnagramChecker

checker = AnagramChecker()

while True:
    word = input("Enter one word or 'quit' to exit: ").strip()
    if word == "quit":
        break
    if " " in word:
        print("You can enter only one word")
        continue
    if not word.isalpha():
        print("Only alphabetical letters allowed")
        continue

    is_valid = checker.is_valid_word(word)

    if not is_valid:
        print(f"{word} is not a valid English word.")
        continue
    
    anagrams = checker.get_anagrams(word)

    print(f'YOUR WORD: "{word.upper()}"')
    print("This is a valid English word.")
    print(f"Anagrams for your word: {', '.join(anagrams)}")