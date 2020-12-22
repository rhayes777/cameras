def filename_for_time(
        seconds,
        duration
):
    increment = round(seconds / duration)
    return f'videos/{increment}.mp4'
