from pytube import YouTube

link = input("Please enter the video url: ")

video = YouTube(link)

print(f"the video title is :\n{video.title} \n ----------------")
print(f"the video description is :\n{video.description} \n ----------------")
print(f"the video views are :\n{video.views} \n ----------------")
print(f"the video rating is :\n{video.rating} \n ----------------")
print(f"the video duration is :\n{video.length} seconds \n ----------------")

