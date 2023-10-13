from pytube import YouTube
from datetime import datetime
try:
    # Ask the user to input the YouTube URL
    while True:
        ask = input('Hey Do you want to download youtube video :\n')
        if ask.lower() == 'no':
            print('Thanks for visit')
            break
        elif ask.lower() == 'yes':

            start=datetime.now()
            url = input("Enter the YouTube URL: ")

            yt = YouTube(url)

            print("Title:", yt.title)
            print("Views:", yt.views)
            print('Wait its on the way...')

            # Get the highest resolution stream
            yd = yt.streams.get_highest_resolution()

            # Download the video to the current directory
            yd.download()
            end = datetime.now()
            difference = end - start
            seconds = difference.total_seconds()
            print(f"Download completed.it takes {round(seconds)} seconds.")

        else:
            print('invalid input')


except Exception as e:
    print("An error occurred:", str(e))
