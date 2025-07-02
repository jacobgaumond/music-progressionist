#! /opt/homebrew/bin/python3

from pitch import Pitch
from scale import Scale
from chord import Chord

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
        self.chords = []
        for position in range(len(scale_notes)):
            self.chords.append(Chord(scale_notes[position], self.KEY_CHORD_SEQUENCES[key_type][position]))

    def get_key_chords(self):
        return self.chords
