# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os

import ffmpeg
import json
import glob
#import re, os

# The data needs to be inverted to show when video was valid and should be stored as a series of points.
# This is based off freeze_start and freeze_end values. The unit of these values are seconds.
# For example, the above would translate to [0, 5.30], [7.36, 16.78]
def get_valid_video_periods(filepath):
    file_wc = 'freeze*.txt'
    file_list = glob.glob(filepath+'/'+file_wc)
    all_periods = []
    for textfile in file_list:
        print("processing: " + textfile)
        read_text = open(textfile).readlines()
        start_lines = [line for line in read_text if '_start' in line]
        end_lines = [line for line in read_text if '_end' in line]

        cur_periods = []

        for idx in range(len(start_lines)):
            start = float(start_lines[idx].split("=")[1].strip())
            end = float(end_lines[idx].split("=")[1].strip())
            cur_periods.append([start, end])

        all_periods.append(cur_periods)

    return all_periods

    #return [ [[0.00, 3.50], [6.65, 14], [19.71, 20.14]], [[0.00, 3.40], [6.65, 13.98], [19.71, 20.00]] ]
    # lavfi.freezedetect.freeze_start = 4.5045
    # lavfi.freezedetect.freeze_end = 10.4271
    #
    # lavfi.freezedetect.freeze_start = 12.012
    # lavfi.freezedetect.freeze_end = 14.2476
    #
    # lavfi.freezedetect.freeze_start = 18.018
    # lavfi.freezedetect.freeze_end = 25.392

# longest period of valid video within each stream.
def get_longest_period(periods_set):

    # duration = [ per[1] - per[0] for per in periods_set]
    durations = []
    for per in periods_set:
        durations.append(per[1]-per[0])
    return max(durations)
    # return 7.35

# percentage of all aggregated valid video periods over the entire duration of the stream.
def aggregate_valid_video_periods(periods_set):
    # percentage = sum([ per[1] - per[0] for per in periods_set])/periods_set[-1][1]
    sum_dur = 0.0
    for per in periods_set:
        sum_dur += per[1]-per[0]

    return sum_dur/periods_set[-1][1]
    # return 56.00

def are_all_synced(periods_set):
    return True


def freeze_validator(input_path):
    # Use a breakpoint in the code line below to debug your script.

    intervals_list_all_streams = get_valid_video_periods(input_path)

    stream_res = []
    for intervals_list in intervals_list_all_streams:
        longest_period = get_longest_period(intervals_list)
        valid_video_percentage = aggregate_valid_video_periods(intervals_list)

        #current_stream_res = []
        # current_stream_res.append({'longest_valid_period', longest_period})
        # current_stream_res.append({'valid_video_percentage', valid_video_percentage})
        # #current_stream_res.append({'valid_periods', intervals_list})
        current_stream_res = {}
        current_stream_res['longest_valid_period'] = longest_period
        current_stream_res['valid_video_percentage'] = valid_video_percentage
        current_stream_res['valid_periods'] = str(intervals_list)

        stream_res.append(current_stream_res)

    all_synced = are_all_synced(intervals_list_all_streams)

    data = {}
    data['all_videos_freeze_frame_synced'] = all_synced
    data['videos'] = stream_res
    json_data = json.dumps(data)
    output_dir = './output'
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    with open(output_dir+'/result.json', 'w') as f:
        json.dump(data, f, indent=3)
    print(json_data)

    print("end")



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # inputs = {
    #     'https://storage.googleapis.com/hiring_process_data/freeze_frame_input_a.mp4',
    #     'https://storage.googleapis.com/hiring_process_data/freeze_frame_input_b.mp4',
    #     'https://storage.googleapis.com/hiring_process_data/freeze_frame_input_c.mp4'
    # }
    #inputs = get_valid_video_periods('./')
    input_path = './'
    freeze_validator(input_path)

# example
# used ffmpeg -i ./freeze_frame_input_a.mp4 -vf "freezedetect=n=-0.003dB:d=2,metadata=mode=print:file=freeze.txt" -map 0:v:0 -f null -

# we could have used ffmpeg lib e.g  ffmpeg.input(url)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

