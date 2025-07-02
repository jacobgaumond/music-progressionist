#! /opt/homebrew/bin/python3

from pitch import Pitch

class Scale:

    SCALE_SEQUENCES = { # Valid types of scales must be recorded here in order for the class to work
        "MAJOR": [2, 2, 1, 2, 2, 2, 1],
        "NATURAL_MINOR": [2, 1, 2, 2, 1, 2, 2],
        "HARMONIC_MINOR": [2, 1, 2, 2, 1, 3, 1]
    }

    def __init__(self, tonic_pitch: Pitch, scale_type: str):
        if scale_type not in self.SCALE_SEQUENCES.keys():
            raise Exception("`scale_type` is not supported as a valid type of scale with a sequence recorded in `Scale.SCALE_SEQUENCES`")
        self.tonic_pitch = tonic_pitch
        self.scale_type = scale_type

        # Build the scale
        self.scale_notes = [self.tonic_pitch]
        for step in self.SCALE_SEQUENCES[scale_type]:
            next_note = self.scale_notes[-1]
            for i in range(step):
                next_note = next_note.get_next_higher_pitch()

            if next_note != self.tonic_pitch:
                self.scale_notes.append(next_note)

    def get_scale_notes(self):
        return self.scale_notes

# Testing
if __name__ == "__main__":
    def test_scales(tonic_pitch: str, scale_type: str, expected_result):
        expected_pitches = []
        for pitch in expected_result:
            expected_pitches.append(Pitch(pitch))

        test_scale = Scale(Pitch(tonic_pitch), scale_type).get_scale_notes()
        if test_scale == expected_pitches:
            return True
        else:
            return False

    num_tests = 0
    failed_tests = []

    scale_testing_list = [
        {"tonic_pitch": "C", "scale_type": "MAJOR", "expected_result": ["C", "D", "E", "F", "G", "A", "B"]},
        {"tonic_pitch": "G", "scale_type": "MAJOR", "expected_result": ["G", "A", "B", "C", "D", "E", "F#/G♭"]},
        {"tonic_pitch": "F#/G♭", "scale_type": "MAJOR", "expected_result": ["F#/G♭", "G#/A♭", "A#/B♭", "B", "C#/D♭", "D#/E♭", "F"]},

        {"tonic_pitch": "A", "scale_type": "NATURAL_MINOR", "expected_result": ["A", "B", "C", "D", "E", "F", "G"]},
        {"tonic_pitch": "D", "scale_type": "NATURAL_MINOR", "expected_result": ["D", "E", "F", "G", "A", "A#/B♭", "C"]},
        {"tonic_pitch": "G#/A♭", "scale_type": "NATURAL_MINOR", "expected_result": ["G#/A♭", "A#/B♭", "B", "C#/D♭", "D#/E♭", "E", "F#/G♭"]},

        {"tonic_pitch": "A", "scale_type": "HARMONIC_MINOR", "expected_result": ["A", "B", "C", "D", "E", "F", "G#/A♭"]},
        {"tonic_pitch": "D", "scale_type": "HARMONIC_MINOR", "expected_result": ["D", "E", "F", "G", "A", "A#/B♭", "C#/D♭"]},
        {"tonic_pitch": "G#/A♭", "scale_type": "HARMONIC_MINOR", "expected_result": ["G#/A♭", "A#/B♭", "B", "C#/D♭", "D#/E♭", "E", "G"]}
    ]

    print("Begin testing scale generation:")
    for scale_test in scale_testing_list:
        num_tests += 1
        if not test_scales(scale_test["tonic_pitch"], scale_test["scale_type"], scale_test["expected_result"]):
            failed_tests += [scale_test]
    print("Finished testing scale generation...")

    num_failed_tests = len(failed_tests)
    print(str(num_tests) + " tests have been completed.\n\t" + str(num_tests - num_failed_tests) + " PASSED\n\t" + str(num_failed_tests) + " FAILED")

    if len(failed_tests) > 0:
        print("The following tests failed:")
        while len(failed_tests) > 0:
            print("\t" + str(failed_tests.pop()))
