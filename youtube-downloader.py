from pytube import YouTube
from tkinter import *


window = Tk()
window.geometry("600x700")
window.config(bg='red')
window.title("Youtube Downloader")

# youtube_logo = PhotoImage(file="youtube.png")
# window.iconphoto(False,youtube_logo)

Label(window, text="Video Downloader", font="Arial 30 bold", bg="lightgreen").pack(padx=5, pady=50)
video_link = StringVar()

Label(window, text="Enter the link: ", font="Arial 25 bold").place(x=170, y=150)

Entry_link = Entry(window, width=50, font=35, textvariable=video_link, bd=4 ).place(x=35, y=200)

def video_download():
    video_url = YouTube(str(video_link.get()))
    videos = video_url.streams.first()
    videos.download()

    Label(window, text="Download Completed !!", font=("Arial", 45, "bold"), bg="lightpink", fg="black").place(x=120,y=350)
    Label(window, text="Check out your project folder", font="Arial 30 bold", bg="yellow").place(x=20, y=400)

Button(window, text="DOWNLOAD", font="Arial 25 bold", bg="lightblue", command= video_download).place(x=180, y=300)

window.mainloop()
#
# # link = input("Please enter the video url: ")
# link = "https://www.youtube.com/watch?v=FVq6TYw9WjE"
#
# video = YouTube(link)
#
# print(f"the video title is :\n{video.title} \n ----------------")
# print(f"the video description is :\n{video.description} \n ----------------")
# print(f"the video views are :\n{video.views} \n ----------------")
# print(f"the video rating is :\n{video.rating} \n ----------------")
# print(f"the video duration is :\n{video.length} seconds \n ----------------")
#
