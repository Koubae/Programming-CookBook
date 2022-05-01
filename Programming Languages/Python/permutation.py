def permute(seq):
    if not seq:
        yield seq
    else:
        for i in range(len(seq)):
            rest = seq[:i] + seq[i+1:]
            for x in permute(rest):
                yield seq[i:i+1] + x

print(list(permute('abc')))

