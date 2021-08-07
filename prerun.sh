wget https://storage.googleapis.com/hiring_process_data/freeze_frame_input_a.mp4
wget https://storage.googleapis.com/hiring_process_data/freeze_frame_input_b.mp4
wget https://storage.googleapis.com/hiring_process_data/freeze_frame_input_c.mp4


ffmpeg -i ./freeze_frame_input_a.mp4 -vf "freezedetect=n=0.003,metadata=mode=print:file=freeze_a.txt" -map 0:v:0 -f null -
ffmpeg -i ./freeze_frame_input_b.mp4 -vf "freezedetect=n=0.003,metadata=mode=print:file=freeze_b.txt" -map 0:v:0 -f null -
ffmpeg -i ./freeze_frame_input_c.mp4 -vf "freezedetect=n=0.003,metadata=mode=print:file=freeze_c.txt" -map 0:v:0 -f null -

