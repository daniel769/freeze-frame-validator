## freeze-frame-validator
Generate report about freeze frames from input videos

### Overview
Freezing frames, arriving that way from the encoder, are a major artefact in users' perceived QoE. Detecting these
periods in the video is a prerequisite prior to processing them.

### Description
on from a set of given input videos
This program generates a JSON report on some freezing frames characteristics
The characteristics:
* longest period of valid video within each stream
* percentage of all aggregated valid video periods over the entire duration of the stream
* whether the entire videos set is synced freeze-frame wise, iff all videos have the same amount of valid periods, and
* each period's corresponding 'start' or 'end' cross all videos are no more than 500 ms apart.


### Getting Started
* In order to run a toy example, run ffmpeg with freezedetect filter, to generate freezedetect outputs use the following CLI:
```shell
ffmpeg -i ./my_input_video.mp4 -vf "freezedetect=n=0.003,metadata=mode=print:file=freeze_my_input_video.txt" -map 0:v:0 -f null -
```
* Run `freeze_validator.py`  and inspect your outputs in `./output` generated directory



### Assumptions
* The program and Class _FreezeValidator_ runs on already valid generated ffmpeg freezedecets reports
* input files contains pairs of `lavfi.freezedetect.freeze_start` and `lavfi.freezedetect.freeze_end` although a valid 
  input can contain a `lavfi.freezedetect.freeze_start` without its matching `lavfi.freezedetect.freeze_end`
* The program should be run only from the repo parent directory, and the generated files should reside there also,   
and match `*_freeze*.txt` wildcard (and not any other file in this location)
### Output
A typical output will look like:
```json
{
   "all_videos_freeze_frame_synced": false,
   "videos": [
      {
         "longest_valid_period": 7.25,
         "valid_video_percentage": 56.77,
         "valid_periods": "[[4.5, 8.31], [9.98, 12.13], [16.02, 23.27]]"
      },
      {
         "longest_valid_period": 7.37,
         "valid_video_percentage": 61.21,
         "valid_periods": "[[4.5, 10.43], [12.01, 14.25], [18.02, 25.39]]"
      },
      {
         "longest_valid_period": 7.56,
         "valid_video_percentage": 62.63,
         "valid_periods": "[[4.5, 10.61], [12.08, 14.43], [18.02, 25.58]]"
      }
   ]
}
```

### Issues and Future Work
* Add input path option to the executable (freeze_validator.py)
* The current output format needs will need to change to something like:
```json
{
   "all_videos_freeze_frame_synced":true,
   "videos":[
      {
         "longest_valid_period":7.35,
         "valid_video_percentage":56.00,
         "valid_periods":[
            [
               0.00,
               3.50
            ],
            [
               6.65,
               14
            ],
            [
               19.71,
               20.14
            ]
         ]
      },
      {
         "longest_valid_period":7.33,
         "valid_video_percentage":55.10,
         "valid_periods":[
            [
               0.00,
               3.40
            ],
            [
               6.65,
               13.98
            ],
            [
               19.71,
               20.00
            ]
         ]
      }
   ]
} 
```

