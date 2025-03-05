# **Video Subtitle Generator with Language Detection and Translation**  

This project is a **Python-based** application that automates the process of generating subtitles for videos in any spoken language. It uses OpenAI's Whisper model for accurate transcription and automatically translates the generated subtitles into *Brazilian Portuguese*. The result is exported as a `.srt` file, which can be easily added to videos using media players or video editing software.  

The application is designed to handle *large video files* (up to 10GB) and is ideal for filmmakers, educators, or anyone working with multilingual content.  

---

### **The Fina Look**  

Below are some visuals to help you understand how the subs are supposed to look

#### **1. Exported Subtitle File**  
*Generated `.srt` files are accurate and can be used directly with most media players. In this example I used VLC*
![vlcsnap-2024-12-11-10h07m48s985](https://github.com/user-attachments/assets/500c5044-6248-4f1a-bf55-4f570f375223)
![vlcsnap-2024-12-11-12h19m52s493](https://github.com/user-attachments/assets/a31f4f6f-5ca5-4a33-8231-4a81efd93362)
![vlcsnap-2024-12-11-12h19m42s374](https://github.com/user-attachments/assets/2491b20e-1e35-4916-8edb-9c64d16642cf)


---

## **Features**  
- Automatic language detection using Whisper.  
- High-accuracy subtitle generation.  
- Subtitle translation to Brazilian Portuguese (or any specified language).  
- Handles large video files (up to 10GB).  
- Easy-to-use and extensible for API or GUI integration.  

---

## **Technologies Used**  
- **Python**  
- [Whisper](https://github.com/openai/whisper): For speech-to-text processing.  
- [FFmpeg](https://ffmpeg.org/): For audio extraction from video files.  
- [mTranslate](https://pypi.org/project/mtranslate/): For subtitle translation.  
- [MoviePy](https://zulko.github.io/moviepy/): For video processing and management.  

---

## **Installation**  

### **Prerequisites**  
- Python 3.8+  
- FFmpeg installed on your system ([Installation Guide](https://ffmpeg.org/download.html)).  
- GPU support (optional) for faster processing.  


## ** Support the Project
If you find this project useful, consider supporting its development:

- USDT (TRC20):

`TLpSee85pWMz9uTCSG3UyPdyWBuzNdKmYA`

- Pix (Brazil):

`f1d8f782-5046-4306-825b-27faa53bc7d4`

## ** License ** 

*This project is licensed under the MIT License.*

*Feel free to contribute to this project by submitting pull requests or opening issues. Feedback and suggestions are always welcome! 😊*

