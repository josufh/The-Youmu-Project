# import speech_recognition as sr

# r = sr.Recognizer()

# while(1):
#     try:
#         with sr.Microphone() as source:
#             r.adjust_for_ambient_noise(source, duration=0.2)
#             audio = r.listen(source, phrase_time_limit=2)
#             MyText = r.recognize_google(audio, language='ja')

#     except sr.RequestError as e:
#         print("Could not request the results: {0}".format(e))
#     except sr.WaitTimeoutError:
#         print("Timedout")
#     except sr.UnknownValueError:
#         print("unknown error occurred")

speech = ''

def Listen():
    loop = True
    while(loop):
        cmd_input = input().lower()
        if(cmd_input.__contains__('youmu')):
            loop = False

Listen()

