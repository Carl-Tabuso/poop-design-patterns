from LocalizerFactory import LocalizerFactory

if __name__ == "__main__":
    french = LocalizerFactory.create("fr")
    english = LocalizerFactory.create("en")
    spanish = LocalizerFactory.create("es")

    message = ["car", "bike", "cycle"]

    word = input(f"Pick a word to translate in three languages: {', '.join(message)}: ")

    print(f"French translation of {word}: {french.translate(word)}")
    print(f"English translation of {word}: {english.translate(word)}")
    print(f"Spanish translation of {word}: {spanish.translate(word)}")
