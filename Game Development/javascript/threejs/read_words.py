import os 
import string


file_path = os.path.join(os.path.abspath(os.getcwd()), "threejs/words.txt" )
# file_path = "/Users/federicobau/Documents/programming/threejs/words.txt"
print(file_path)
with open(file_path, "r") as file_words:
    content = file_words.read()

words = [w.strip() for w in content.split(" ") if w and not w.isspace() and
all(not c.isdigit() and c not in string.punctuation for c in w)

]
print(words)
print(len(words))
total_words = len(words)
cost = 0.16 
total_price = (total_words * cost ) 
print(total_price)
