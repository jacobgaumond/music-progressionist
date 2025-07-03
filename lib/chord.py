#! /opt/homebrew/bin/python3

from pitch import Pitch

DIMINISHED_SYMBOL = "°" # "dim" is also applicable in certain contexts

class Chord:

    CHORD_SEQUENCES = { # Valid types of chords must be recorded here in order for the class to work
        "MAJOR": [4, 3],
        "MINOR": [3, 4],
        "DIMINISHED": [3, 3]
    }

    CHORD_SUFFIXES = {
        "MAJOR": "",
        "MINOR": "m",
        "DIMINISHED": DIMINISHED_SYMBOL
    }

    def __init__(self, root_pitch: Pitch, chord_type: str):
        if chord_type not in self.CHORD_SEQUENCES.keys():
            raise Exception("`chord_type` is not supported as a valid type of chord with a sequence recorded in `Chord.CHORD_SEQUENCES`")
        self.root_pitch = root_pitch
        self.chord_type = chord_type

        # Build the chord
        self.chord_notes = [self.root_pitch]
        for step in self.CHORD_SEQUENCES[chord_type]:
            next_note = self.chord_notes[-1]
            for i in range(step):
                next_note = next_note.get_next_higher_pitch()
            self.chord_notes.append(next_note)
    
    def get_chord_notes(self):
        return self.chord_notes
    
    def get_chord_name(self):
        return str(self.root_pitch) + self.CHORD_SUFFIXES[self.chord_type]

    def get_chord_type(self):
        return self.chord_type

    def __eq__(self, other):
        if self.root_pitch != other.root_pitch:
            return False
        elif self.chord_type != other.chord_type:
            return False
        elif self.chord_notes != self.chord_notes:
            return False
        else:
            return True


# Testing
if __name__ == "__main__":
    def test_chord_notes(root_pitch: str, chord_type: str, expected_result):
        expected_pitches = []
        for pitch in expected_result:
            expected_pitches.append(Pitch(pitch))

        test_chord = Chord(Pitch(root_pitch), chord_type).get_chord_notes()
        if test_chord == expected_pitches:
            return True
        else:
            return False

    def test_chord_names(root_pitch: str, chord_type: str, expected_result):
        test_chord = Chord(Pitch(root_pitch), chord_type).get_chord_name()
        if test_chord == expected_result:
            return True
        else:
            return False

    num_tests = 0
    failed_tests = []

    chord_note_testing_list = [
        {"root_pitch": "C", "chord_type": "MAJOR", "expected_result": ["C", "E", "G"]},
        {"root_pitch": "G", "chord_type": "MAJOR", "expected_result": ["G", "B", "D"]},
        {"root_pitch": "F#/G♭", "chord_type": "MAJOR", "expected_result": ["F#/G♭", "A#/B♭","C#/D♭"]},

        {"root_pitch": "A", "chord_type": "MINOR", "expected_result": ["A", "C", "E"]},
        {"root_pitch": "D", "chord_type": "MINOR", "expected_result": ["D", "F", "A"]},
        {"root_pitch": "G#/A♭", "chord_type": "MINOR", "expected_result": ["G#/A♭", "B", "D#/E♭"]},

        {"root_pitch": "B", "chord_type": "DIMINISHED", "expected_result": ["B", "D","F"]},
        {"root_pitch": "E", "chord_type": "DIMINISHED", "expected_result": ["E", "G", "A#/B♭"]},
        {"root_pitch": "G#/A♭", "chord_type": "DIMINISHED", "expected_result": ["G#/A♭", "B", "D"]}
    ]
    chord_name_testing_list = [
        {"root_pitch": "C", "chord_type": "MAJOR", "expected_result": "C"},
        {"root_pitch": "G", "chord_type": "MAJOR", "expected_result": "G"},
        {"root_pitch": "F#/G♭", "chord_type": "MAJOR", "expected_result": "F#/G♭"},

        {"root_pitch": "A", "chord_type": "MINOR", "expected_result": "Am"},
        {"root_pitch": "D", "chord_type": "MINOR", "expected_result": "Dm"},
        {"root_pitch": "G#/A♭", "chord_type": "MINOR", "expected_result": "G#/A♭m"},

        {"root_pitch": "B", "chord_type": "DIMINISHED", "expected_result": "Bdim"},
        {"root_pitch": "E", "chord_type": "DIMINISHED", "expected_result": "Edim"},
        {"root_pitch": "G#/A♭", "chord_type": "DIMINISHED", "expected_result": "G#/A♭dim"}
    ]

    print("Begin testing chord generation:")
    for chord_test in chord_note_testing_list:
        num_tests += 1
        if not test_chord_notes(chord_test["root_pitch"], chord_test["chord_type"], chord_test["expected_result"]):
            failed_tests += [chord_test]
    for chord_test in chord_name_testing_list:
        num_tests += 1
        if not test_chord_names(chord_test["root_pitch"], chord_test["chord_type"], chord_test["expected_result"]):
            failed_tests += [chord_test]
    print("Finished testing chord generation...")

    num_failed_tests = len(failed_tests)
    print(str(num_tests) + " tests have been completed.\n\t" + str(num_tests - num_failed_tests) + " PASSED\n\t" + str(num_failed_tests) + " FAILED")

    if len(failed_tests) > 0:
        print("The following tests failed:")
        while len(failed_tests) > 0:
            print("\t" + str(failed_tests.pop()))
