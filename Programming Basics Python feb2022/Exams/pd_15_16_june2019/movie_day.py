time = int(input())
number_of_scenes = int(input())
time_per_scene = int(input())
location_preparation = time * 0.15
total_scene_time = number_of_scenes * time_per_scene
time_needed = location_preparation + total_scene_time
diff = round(abs(time - time_needed))
if time_needed <= time:
    print(f'You managed to finish the movie on time! You have {diff} minutes left!')
else:
    print(f'Time is up! To complete the movie you need {diff} minutes.')