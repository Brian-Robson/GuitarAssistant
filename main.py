class GuitarFretboard:
    def __init__(self, strings, frets, tuning):
        fretboard = [["" for fret in range(frets)] for string in range(strings)]
        self.tunemapping = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
        for note in range(len(tuning)):
            for index in range(len(self.tunemapping)):
                if tuning[note] == self.tunemapping[index]:
                    fretboard[note][0] = index
                    break
            for fret in range(frets - 1):
                if fretboard[note][fret] == 11:
                    fretboard[note][fret + 1] = 0
                else:
                    fretboard[note][fret + 1] = fretboard[note][fret] + 1
        self.fretboard = fretboard

    def TranslateNote(self, note):
        return self.tunemapping[(note)]

    def PrintFretboard(self):
        for string in range(len(self.fretboard)):
            for fret in range(len(self.fretboard[string])):
                print(self.TranslateNote(self.fretboard[string][fret]), end='  ')
            print()
        
strings = int(input("How many strings?: "))
frets = int(input("How many frets?: "))
tuning = []
print("For inputting the tuning of strings, use a '#' for a sharp, ie: 'C#'.")
for string in range(strings):
    printstring = "Input tuning of string " + str(string + 1)
    if string == 0:
        printstring = printstring + "(highest string)"
    if string == range(strings):
        printstring = printstring + "(lowest string)"
    tuning.append(input(printstring + ": "))

test = GuitarFretboard(strings, frets, tuning)
test.PrintFretboard()