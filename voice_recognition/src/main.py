import speech_recognition as sr

# Initialize the recognizer
r = sr.Recognizer()

# Function to recognize speech
def recognize_speech():
    with sr.Microphone() as source:
        print('Listening...')
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print('You said:', text)
        except sr.UnknownValueError:
            print('Sorry, I could not understand what you said.')
        except sr.RequestError as e:
            print('Sorry, there was an error with the request. Please try again later.')

# Call the function to recognize speech
recognize_speech()