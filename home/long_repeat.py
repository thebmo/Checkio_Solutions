def long_repeat(line):
    line = str(line)
    last_char = ""
    last_subset = ""
    last_longest_subset = ""

    for c in line:
        if last_char == c:
            last_subset += c
        else:
            last_subset = c
        if len(last_subset) > len(last_longest_subset):
            last_longest_subset = last_subset

        last_char = c

    return len(last_longest_subset)
