# Nashville Number System
Given a root note, create a specified chord progression using the Nashville number system.

Major pattern: W W H W W W H

Where:
- W  = Whole step, i.e. 2 frets.
- H = Half step, i.e. 1 fret.

Example:

| Root | 1 | 2(W) | 3(W) | 4(H) | 5(W) | 6(W) | 7(W) | 8(H) |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| **G** | G | A | B | C | D | E | F# | G |
| **E** | E | F# | G# | A | B | C# | D# | E |

After creating this major scale we assign the numbers 1 -> 8 to each note in the major scale, e.g. Using G major scale from above we get: ```G = 1, A = 2, ..., F# = 7, G = 8 = 1```.

To create the chord list we apply the following pattern to the above notes:
1. Major
2. Minor
3. Minor
4. Major
5. Major
6. Minor
7. Diminished


Applying the above pattern to a G major scale gives us the following chords:

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| G | Am | Bm | C | D | Em | F#dim | G |

From these possible chords we can then express the progression using the number system, e.g. 5 4 1 4 = D C G C.
