import pyttsx3

def initialize_voice_engine():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    print("Available Voices:")
    for i, voice in enumerate(voices):
        print(f"{i + 1}. {voice.name}")
    return engine, voices

def speak_text_with_selected_voice(engine, text, voice_index):
    engine.setProperty('voice', voices[voice_index].id)
    engine.say(text)
    engine.runAndWait()

def main():
    print("Initializing Voice Engine...")
    engine, voices = initialize_voice_engine()
    print("Initialization successful!")
    print("Select a voice (Enter the voice number): ")
    for i, voice in enumerate(voices):
        print(f"{i + 1}. {voice.name}")
    voice_index = int(input()) - 1
    text = input("Enter the text you want to hear: ")
    print("Speaking...")
    speak_text_with_selected_voice(engine, text, voice_index)
    print("Speech completed.")
    
main()
