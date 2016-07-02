notes = [
    'C', 'C#', 
    'D', 'D#', 
    'E',
    'F', 'F#',
    'G', 'G#',
    'A', 'A#',
    'B'
]

chords = [
    'C', 
    'Dmin', 'D', 
    'Emin', 'E'
    'F',
    'Gmin', 'G',
    'Amin', 'A',
    'Bmin', 'B'
]

def create_major_scale(root):
    W = 2
    H = 1
    pattern = [W, W, H, W, W, W, H]

    major_scale = [root]

    note_index = notes.index(root)
    for next_note in pattern:
        note_index = (note_index + next_note) % len(notes)
        major_scale.append(notes[note_index])

    return major_scale

def create_chord_list(scale):
    pattern = ['', 'm', 'm', '', '', 'm', 'dim', '']

    chord_list = []
    for i in range(0, len(scale)):
        chord_list.append(scale[i] + pattern[i])

    return chord_list

def create_chord_progression(chord_list, progression):
    chord_progression = []

    for i in progression:
        # Need to offset by -1 to take into account difference in counting starts
        chord_progression.append(chord_list[i])

    return chord_progression

def account_for_offset(x):
    return x - 1

if __name__ == '__main__':
    # Get root
    root = 'G'

    # Create major scale
    scale = create_major_scale(root)
    print(scale)

    # Apply pattern (m min min m m min dim)
    chord_list = create_chord_list(scale)
    print(chord_list)

    progression = [5, 4, 1, 4]
    progression = map(account_for_offset, progression)

    chord_progression = create_chord_progression(chord_list, progression)
    print(chord_progression)