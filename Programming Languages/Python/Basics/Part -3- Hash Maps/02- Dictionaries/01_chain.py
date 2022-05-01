from itertools import chain


def cat_key(c):
    categories = {' ': None,
            string.ascii_lowercase: 'lower',
            string.ascii_uppercase: 'upper'}
    for key in categories:
        if c in key:
            return categories[key]
    else:
        return 'other'

print(cat_key('a'), cat_key('A'), cat_key('!'), cat_key(' '))

# ('lower', 'upper', 'other', None)



def cat_key(c):
    cat_1 = {' ': None}
    cat_2 = dict.fromkeys(string.ascii_lowercase, 'lower')
    cat_3 = dict.fromkeys(string.ascii_uppercase, 'upper')
    categories = dict(chain(cat_1.items(), cat_2.items(), cat_3.items()))
    # categories = {**cat_1, **cat_2, **cat_3} - I'll explain this later
    return categories.get(c, 'other')


print(cat_key('a'), cat_key('A'), cat_key('!'), cat_key(' '))
# ('lower', 'upper', 'other', None)


categories = {}
for c in text:
    key = cat_key(c)
    if key:
        categories.setdefault(key, set()).add(c)
        
for cat in categories:
    print(f'{cat}:', ''.join(categories[cat]))

# upper: UQNS
# lower: dlsumxihcfbapnroeqtvg
# other: [?-].,