
import json
import glob
import os

# The data needs to be inverted to show when video was valid and should be stored as a series of points.
# This is based off freeze_start and freeze_end values. The unit of these values are seconds.
# For example, the above would translate to [0, 5.30], [7.36, 16.78]

class FreezeValidator:
    def __init__(self):
        self.data = {}

    @staticmethod
    def get_valid_video_periods(filepath):
        file_wc = 'freeze*.txt'
        file_list = glob.glob(filepath + '/' + file_wc)
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

    # longest period of valid video within each stream.
    @staticmethod
    def get_longest_period(periods_set):

        durations = [per[1] - per[0] for per in periods_set]
        return round(max(durations), 2)

    # percentage of all aggregated valid video periods over the entire duration of the stream.
    @staticmethod
    def aggregate_valid_video_periods(periods_set):
        ratio = sum([ per[1] - per[0] for per in periods_set])/periods_set[-1][1]
        return round(ratio * 100, 2)

    @staticmethod
    def are_all_synced(periods_set):
        return True

    def freeze_validator(self, input_path):
        # Use a breakpoint in the code line below to debug your script.

        intervals_list_all_streams = FreezeValidator.get_valid_video_periods(input_path)

        stream_res = []
        for intervals_list in intervals_list_all_streams:
            longest_period = FreezeValidator.get_longest_period(intervals_list)
            valid_video_percentage = FreezeValidator.aggregate_valid_video_periods(intervals_list)

            current_stream_res = {'longest_valid_period': longest_period,
                                  'valid_video_percentage': valid_video_percentage,
                                  'valid_periods': str(intervals_list)}

            stream_res.append(current_stream_res)

        all_synced = FreezeValidator.are_all_synced(intervals_list_all_streams)

        self.data['all_videos_freeze_frame_synced'] = all_synced
        self.data['videos'] = stream_res

    def write_to_file(self, filename='freeze-summary'):
        output_dir = './output'
        if not os.path.exists(output_dir):
            os.mkdir(output_dir)
        with open(output_dir + "/" + filename + '.json', 'w') as f:
            json.dump(self.data, f, indent=3)
