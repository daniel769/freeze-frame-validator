#!/usr/bin/env python3

import FreezeValidator


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    input_path = './'
    fv = FreezeValidator.FreezeValidator()
    fv.freeze_validator(input_path)
    fv.write_to_file('freeze-summary-2')

# example
# used ffmpeg -i ./freeze_frame_input_a.mp4 -vf "freezedetect=n=-0.003dB:d=2,metadata=mode=print:file=freeze.txt" -map 0:v:0 -f null -

# we could have used ffmpeg lib e.g  ffmpeg.input(url)

