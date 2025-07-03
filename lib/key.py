#! /opt/homebrew/bin/python3

from pitch import Pitch
from scale import Scale
from chord import Chord, DIMINISHED_SYMBOL

class Key:

    KEY_CHORD_SEQUENCES = { # Valid types of keys must be recorded here in order for the class to work
        "MAJOR": ["MAJOR", "MINOR", "MINOR", "MAJOR", "MAJOR", "MINOR", "DIMINISHED"],
        "MINOR": ["MINOR", "DIMINISHED", "MAJOR", "MINOR", "MINOR", "MAJOR", "MAJOR"]
    }

    def __init__(self, root_pitch: Pitch, key_type: str, scale_type):
        if key_type not in self.KEY_CHORD_SEQUENCES.keys():
            raise Exception("`key_type` is not supported as a valid type of key with a sequence recorded in `Key.KEY_CHORD_SEQUENCES`")
        self.root_pitch = root_pitch
        self.key_type = key_type
        self.scale_type = scale_type

        # Setup the key
        self.scale = Scale(self.root_pitch, scale_type)

        scale_notes = self.scale.get_scale_notes()
        ## Setup its chords
        self.chords = []
        for position in range(len(scale_notes)):
            current_chord = Chord(scale_notes[position], self.KEY_CHORD_SEQUENCES[key_type][position])
            roman_numeral_chord_tuple = (self._get_roman_numeral_chord_notation(current_chord, position + 1), current_chord) # Tuple contains the chord, along with it's roman numeral label

            self.chords.append(roman_numeral_chord_tuple)

    def _get_roman_numeral_chord_notation(self, chord: Chord, chord_degree: int) -> str:
        ROMAN_NUMERALS_ONE_TO_SEVEN= [
            "I",
            "II",
            "III",
            "IV",
            "V",
            "VI",
            "VII"
        ]

        if chord_degree =< 0 or position > 7:
            raise Exception("`position` is not supported as a valid value for 7-note/7-chord keys.")

        chords_roman_numeral = ROMAN_NUMERALS_ONE_TO_SEVEN[chord_degree - 1]
        if chord.get_chord_type() == "MAJOR":
            chords_roman_numeral = chords_roman_numeral.upper()
        elif chord.get_chord_type() == "MINOR":
            chords_roman_numeral = chords_roman_numeral.lower()
        elif chord.get_chord_type() == "DIMINISHED":
            chords_roman_numeral = chords_roman_numeral.lower() + DIMINISHED_SYMBOL
        else:
            raise Exception("``chord` has an unsupported chord type for generating its roman numeral notation.")

        return chords_roman_numeral

    def get_key_chords(self):
        return self.chords
