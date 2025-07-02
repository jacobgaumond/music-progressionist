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
