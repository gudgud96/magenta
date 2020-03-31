## Guidelines to use PerformanceEncoder

This is a snapshot of magenta repository that allow functions on encoding / decoding MIDI files into performance event tokens 
(e.g. in Music Transformer project).

We can wrap them up in self-defined functions:

```python
def magenta_encode_midi(midi_filename, is_eos=False):
    mpe = MidiPerformanceEncoder(
            steps_per_second=STEPS_PER_SECOND,
            num_velocity_bins=NUM_VELOCITY_BINS,
            min_pitch=MIN_PITCH,
            max_pitch=MAX_PITCH,
            add_eos=is_eos,
            is_ctrl_changes=True)

    ns = magenta.music.midi_file_to_sequence_proto(midi_filename)
    return mpe.encode_note_sequence(ns)


def magenta_decode_midi(notes, is_eos=False):
    mpe = MidiPerformanceEncoder(
            steps_per_second=STEPS_PER_SECOND,
            num_velocity_bins=NUM_VELOCITY_BINS,
            min_pitch=MIN_PITCH,
            max_pitch=MAX_PITCH,
            add_eos=is_eos,
            is_ctrl_changes=True)

    pm = mpe.decode(notes, return_pm=True)
    return pm
```

The main difference is on the `is_ctrl_changes` argument. In this version, we added **pedal sustain** as a new performance event
, such that MIDI files encoded and decoded maximally preserves the pedal sustain control changes. 
We set the pedal sustain event to have 16 bins, hence 16 extra new tokens are added to the vocabulary. If you wish to also 
encode the pedal sustain event, set `is_ctrl_changes=True`.
