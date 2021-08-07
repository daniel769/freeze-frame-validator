import FreezeValidator

import json


def test_get_valid_video_periods():
    periods = FreezeValidator.FreezeValidator.get_valid_video_periods("./")
    target = [[[4.5045, 8.3083], [9.97663, 12.1288], [16.016, 23.2733]],
              [[4.5045, 10.4271], [12.012, 14.2476], [18.018, 25.392]],
              [[4.5045, 10.6106], [12.0787, 14.4311], [18.018, 25.5755]]]
    assert periods == target


def test_get_longest_period():
    source = [0.00, 3.50], [6.65, 14], [19.71, 20.14]
    longest = FreezeValidator.FreezeValidator.get_longest_period(source)
    assert longest == 7.35


def test_aggregate_valid_video_periods():
    source = [0.00, 3.40], [6.65, 13.98], [19.71, 20.00]
    aggregated_percentage = FreezeValidator.FreezeValidator.aggregate_valid_video_periods(source)
    assert aggregated_percentage == 55.10


def test_are_all_synced():
    source_1 = [[[4.5045, 8.3083], [9.97663, 12.1288], [16.016, 23.2733]],
                [[4.5045, 10.4271], [12.012, 14.2476], [18.018, 25.392]]]
    is_synced_1 = FreezeValidator.FreezeValidator.are_all_synced(source_1)
    target_1 = False
    assert is_synced_1 == target_1

    source_2 = [[[4.5045, 10.4271], [12.012, 14.2476], [18.018, 25.392]],
                [[4.5045, 10.6106], [12.0787, 14.4311], [18.018, 25.5755]]]
    is_synced_2 = FreezeValidator.FreezeValidator.are_all_synced(source_2)
    target_2 = True
    assert is_synced_2 == target_2


def test_freeze_validator():
    target = """{
   "all_videos_freeze_frame_synced": true,
   "videos": [
      {
         "longest_valid_period": 7.26,
         "valid_video_percentage": 56.77,
         "valid_periods": "[[4.5045, 8.3083], [9.97663, 12.1288], [16.016, 23.2733]]"
      },
      {
         "longest_valid_period": 7.37,
         "valid_video_percentage": 61.17,
         "valid_periods": "[[4.5045, 10.4271], [12.012, 14.2476], [18.018, 25.392]]"
      },
      {
         "longest_valid_period": 7.56,
         "valid_video_percentage": 62.62,
         "valid_periods": "[[4.5045, 10.6106], [12.0787, 14.4311], [18.018, 25.5755]]"
      }
   ]
}"""
    fv = FreezeValidator.FreezeValidator()
    fv.freeze_validator("./")
    assert json.dumps(fv.data, indent=3) == target
