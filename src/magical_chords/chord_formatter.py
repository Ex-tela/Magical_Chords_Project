formatted_song = []

# def details_formatter(line):
#     for line_ in line.split('\n'):
#         if '{' in line_:
#             split_line = line_.replace('}', '').split()
#             for categories in split_line:
#                 categories_lower = categories.lower()
#                 if 'artist' in categories_lower:
#                     formatted_song.append('<h5 style="color: rgb(73, 73, 73)"><em>' + (' '.join(split_line[1:])) + '<em><h5>')
#                 elif 'title' in categories_lower:
#                     formatted_song.append('<h3 style="color: rgb(50, 10, 87)"><b>' + (' '.join(split_line[1:])) + '</b></h3>')
#                 elif 'key' in categories_lower:
#                     formatted_song.append('<h5>Key of ' + (' '.join(split_line[1:])) + '<h5>')
# 
    # return '\n'.join(formatted_song)

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

    return "".join(result).replace('[', '').replace(']', '')

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
        # result.append(f"<p>{details_formatter(line)}</p>")
        result.append(f"<p>{chord_line(line)}</p>")
        result.append(f"<p>{non_chord_line(line)}</p>")
    print(result)
    return " ".join(result)