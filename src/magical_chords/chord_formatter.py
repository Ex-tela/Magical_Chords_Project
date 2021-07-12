def details_formatter(lines):
    formatted_song = []
    for line in lines:
        if '{' in line:
            split_line = line.split(':')
            formatted_song.append(split_line[-1])
        else:
            pass

    return ''' 
    <p>&nbsp;</p>
    '''.join(formatted_song)

def song_preview(song):
    result = []
    lines = song.split('\n')
    for line in lines:
        if '{' in line:
            pass
        elif '---' in line:
            pass
        elif '@' in line:
            pass
        elif '=' in line:
            pass
        else:
            result.append(line)
    result = ' / '.join(result).strip(' / ').replace('''    
    ''', '')
    return result[:250] + '...'


def format(chord):
    result = []
    lines = chord.split("\n")
    result.append("<h5 style=\"color: rgb(73, 73, 73)\"><em>")
    result.append(f"<p>{details_formatter(lines)}</p>")
    result.append("</h5></em>")
    return ''.join(result).replace('}','')

