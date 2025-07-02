FLAT_SYMBOL = "♭"
SHARP_SYMBOL = "#"

class Pitch:

    PITCH_LIST = [
        "A",
        "A#/B♭",
        "B",
        "C",
        "C#/D♭",
        "D",
        "D#/E♭",
        "E",
        "F",
        "F#/G♭",
        "G",
        "G#/A♭"
    ]

    def __init__(self, pitch: str, sharpen: bool = False, flatten: bool = False):
        """
        Usage examples:
            b_natural = Pitch("B")
            f_sharp = Pitch("F", sharpen=True)
            d_flat = Pitch("D", flatten=True)
            e_flat = Pitch("D#/E♭")
        """
        index_of_pitch = self.PITCH_LIST.index(pitch)
        if sharpen:
            self.pitch_index = self._get_next_higher_pitch_index(index_of_pitch)
        if flatten:
            self.pitch_index = self._get_next_lower_pitch_index(index_of_pitch)
        else:
            self.pitch_index = index_of_pitch

    def _get_next_higher_pitch_index(self, pitch_index: int):
        pitch_index += 1
        if pitch_index >= 12:
            pitch_index -= 12
        return pitch_index
    
    def _get_next_lower_pitch_index(self, pitch_index: int):
        pitch_index -= 1
        if pitch_index < 0:
            pitch_index += 12
        return pitch_index
    
    def get_next_higher_pitch(self):
        higher_pitch = self.PITCH_LIST[self._get_next_higher_pitch_index(self.pitch_index)]
        return Pitch(higher_pitch)
    
    def get_next_lower_pitch(self):
        lower_pitch = self.PITCH_LIST[self._get_next_lower_pitch_index(self.pitch_index)]
        return Pitch(lower_pitch)

    def get_pitch(self):
        return self.PITCH_LIST[self.pitch_index]

    def __str__(self):
        return self.get_pitch()
    
    def __eq__(self, other):
        if self.pitch_index == other.pitch_index:
            return True
        else:
            return False
