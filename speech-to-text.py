import tkinter as tk
import speech_recognition as sr

def unique_speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  
        audio_data = recognizer.listen(source)
        try:
            recognized_text = recognizer.recognize_google(audio_data)
            text_output.config(text=f"Recognized Text: {recognized_text}")
        except sr.UnknownValueError:
            text_output.config(text="Sorry, I couldn't understand the audio.")
        except sr.RequestError as e:
            text_output.config(text=f"Error occurred: {e}")

root = tk.Tk()
root.title("Speech to Text Converter")

frame = tk.Frame(root, bg="lightgrey")
frame.pack(padx=20, pady=20)

text_output = tk.Label(frame, text="", font=("Arial", 14), bg="lightgrey")
text_output.pack(pady=20)

convert_button = tk.Button(frame, text="Start", font=("Arial", 10), command=unique_speech_to_text)
convert_button.pack(pady=10)

root.mainloop()
