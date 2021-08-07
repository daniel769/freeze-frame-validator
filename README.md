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
In order to run a toy example, first run prerun.sh. This will download a given set of videos, and run ffmpeg with 
freezedetect filter, to generate freezedetect output

### Assumptions made
* The program and Class _FreezeValidator_ runs on already valid generated ffmpeg freezedecets reports
* input files contains pair only of lavfi.freezedetect.freeze_start and lavfi.freezedetect.freeze_end although a valid 
  input can contain a lavfi.freezedetect.freeze_start without its matching lavfi.freezedetect.freeze_end


