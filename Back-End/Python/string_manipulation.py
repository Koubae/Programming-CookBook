# ================= < Removing Many Blank space (\n) > ================= #

# Simple

def string_cleaner(str):

    cleaned_string = []
    string_separated = str.split(' ')
    for word in string_separated:
        if word: # Not Blank line
            remove_whitespace_from_side = word.strip().replace('\n', ' ') # NOTE: we do this because there are multiple \n\n in some string
            separate_each_string = remove_whitespace_from_side.split()
            if separate_each_string:  # NOTE: If empty means that is a useless white spece within a string
                rejoined_sub_string = ' '.join(separate_each_string)
                ready_string = rejoined_sub_string.replace(' ', '\n') # Add again \n
                cleaned_string.append(ready_string)
    ready_to_go = ' '.join(cleaned_string)
    return ready_to_go

result = string_cleaner(test_string)

print(result)

# --------------- Using Re


import re


def normalize_text(get_text):
    saved_new_lines = []
    counter = 0
    for each_line in get_text.split("\n"):
        if not each_line == "":
            normalize_each_line = re.sub(r'\s+', ' ', each_line.strip())
            if each_line.startswith(" "):
                saved_new_lines[counter-1] += " " + normalize_each_line
            else:
                saved_new_lines.append(normalize_each_line)
                counter += 1
    return "\n".join(saved_new_lines)



# OTher

print( ' '.join([s for s in S.split(' ') if s.strip()]) )
print(' '.join([s.replace('\n\n', '\n') for s in test_string.split(' ') if s.strip()]))

def normalize_text(get_text):

    saved_new_lines = []
    for each_line in get_text.split("\n"):
        if each_line:  # -> Check if line is empty if is ''  in Python == False! :) 
            normalize_each_line = re.sub(r'\s+', repl=' ', string=each_line)
            normalize_each_line = normalize_each_line.strip()
            saved_new_lines.append(normalize_each_line)

    return "\n".join(saved_new_lines)


result = normalize_text(test_string)
print(result) 


# ------------------- string.whitespace
import string

    def string_cleaner(str):
        cleaned_string = []
        string_separated = str.split(' ')
        for word in string_separated:
            if word:
                if word in string.whitespace:
                    del word
                else:
                    cleaned_string.append(word)

        ready_baby = ' '.join(cleaned_string)
        return ready_baby

result = string_cleaner(test_string)

print(' '.join([s for s in test_string.split(' ') if s and s not in string.whitespace]))



# -------------- Use Function isspace 
def string_cleaner(str):
    cleaned_string = []
    string_separated = str.split(' ')
    for word in string_separated:
        if word:
            if word.isspace():
                del word
            else:
                cleaned_string.append(word)

    ready_baby = ' '.join(cleaned_string)
    return ready_baby


result = string_cleaner(test_string)

print(result)

print(' '.join([string for string in test_string.split(' ') if string and not string.isspace()]))