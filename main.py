import random
names = ["Andrei", "Angel", "Aleksandar", "Aleksi", "Anastas", "Anton", "Asen", "Asparuh", "Atanas", "Blagun", "Bogdan",
         "Bogomil", "Bojidar", "Boris", "Borislav", "Boyan", "Boiko", "Branimir", "Dafo", "Daniel", "Danail", "Delyan",
         "Desislav", "Dimo", "Dobromir", "Dragan", "Dragomir", "Elian", "Genadi", "Georgi", "Grozdan", "Hristo", "Hristofor",
         "Ilian", "Iordan", "Ivan", "Ivo", "Ivailo", "Kalin"]
places = ["Indianapolis", "Levochevo", "New york", "Draganci", "Ho-chi min", "Stara Zagora", "Dobrinishte"]
verbs = ["plays", "eats", "dresses", "brings", "prays", "snores", "bets"]
nouns = ["bridge", "car", "rocket", "banana", "bike", "house", "river"]
adverbs = ["slowly", "sadly", "awkwardly", "briefly", "cheerfully"]
details = ["in the toilet", "near the bomb", "behind the cat", "inside the fire"]


print("Hey guys lets have some fun!")
user_input = input("Press ENTER and see what happens!")
print()
print()
def random_word_func(words):
    return random.choice(words)


if not user_input:
    full_sentence = f"{random_word_func(names)} {random_word_func(verbs)} {random_word_func(adverbs)} " \
                    f"{random_word_func(details)} in {random_word_func(places)}!!"
    print(full_sentence)


