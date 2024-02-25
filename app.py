from tkinter import *
from tkinter import messagebox
from pytube import YouTube
import validators


# Download Audio From YouTube
def download_audio():
    """
    Function to download audio from a YouTube video.
    """
    # Get the URL from the entry field
    url = url_download_entry.get()

    # Check if the URL is valid
    if validators.url(url):
        try:
            # Create a YouTube object
            yt = YouTube(url)

            # Filter for audio-only streams and get the first one
            audio_stream = yt.streams.filter(only_audio=True).first()

            # Download the audio stream
            audio_stream.download()

            # Show success message
            messagebox.showinfo("Download Complete", "The Audio Downloaded Successfully")
        except Exception as e:
            # Show error message if download fails
            messagebox.showerror("Error", f"An Error Occurred {e}")
    else:
        # Show error message for invalid URL
        messagebox.showerror("Error", "Please Enter a valid URL")


# Setup GUI
app = Tk()
app.title("Youtube Audio Downloader GUI")
app.geometry("500x300")

# Label for the downloader
downloader_label = Label(app, text="Youtube Audio Downloader", font=("arial", 14, "bold",))
downloader_label.pack(pady=10)

# Label for URL entry
url_label = Label(app, text="Please Enter URL: ", font=("arial", 12))
url_label.pack(pady=10)

# Entry field for URL
url_download_entry = Entry(app, width=40, borderwidth=2, relief=GROOVE)
url_download_entry.pack()

# Button to trigger download
download_button = Button(app, text="Download", font=("arial", 12), width=15, borderwidth=2, relief=GROOVE,
                         command=download_audio)
download_button.pack(pady=50)

# Label for developer info
developer_label = Label(app, text="Made by Ilia keshavarz", font=("arial", 10, "bold"), fg="#212121")
developer_label.pack(pady=15)

# Run the GUI application
app.mainloop()
