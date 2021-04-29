
def chord_line(line):
    result = []    

    print_on = False
    for c in line:
        if c == '[':
            result.append("<b>")
            print_on = True
        if print_on:
            result.append(c)
        else:        
            result.append("&nbsp;")
        if c == ']':
            result.append("</b>")
            print_on = False

    return "".join(result)


def non_chord_line(line):
    result = []
    print_on = True
    for c in line:
        if c == '[':
            print_on = False
        if print_on:
            result.append(c)        
        if c == ']':
            print_on = True

    return "".join(result)

def format(chord):
    result = []
    lines = chord.split("\n")
    for line in lines:
        result.append(f"<p>{chord_line(line)}</p>")
        result.append(f"<p>{non_chord_line(line)}</p>")
    print(result)
    return " ".join(result)