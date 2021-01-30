import librosa
import speech_recognition as sr
import os

train_audio_path = "C:/Users/Ieshitha Wijetunge/Downloads/Audio/"


def get_file_paths(dirname):
    file_paths = []
    for root, directories, files in os.walk(dirname):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)
            print("loading files")
    return file_paths


def recognize_multiple(file):
    r = sr.Recognizer()
    with sr.WavFile(file) as source:        # use "test.wav" as the audio source
        audio = r.record(source)            # extract audio data from the file
        print("In Recognize_multiple method")
    try:
        print("lol")
        print("Transcription: " + r.recognize_google(audio))  # recognize speech using Google Speech Recognition
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:  # speech is unintelligible
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

def main():
    print("njfeiw")
    files = get_file_paths(train_audio_path)
    for file in files:                              # execute for each file
        (filepath, ext) = os.path.splitext(file)    # get the file extension
        file_name = os.path.basename(file)          # get the basename for writing to output file
        print(file_name)                            # only interested if extension is '.wav'
        recognize_multiple(file)


if __name__ == '__main__':
    main()

# import speech_recognition as sr
# import os
#
# r = sr.Recognizer()
# with sr.AudioFile("C:/Users/Ieshitha Wijetunge/Downloads/Audio/F_0101_14y8m_1.wav") as source:              # use "test.wav" as the audio source
#     audio = r.record(source)                        # extract audio data from the file
#     print("yo")
#     try:
#         print("lol")
#         print("Transcription: " + r.recognize_google(audio))   # recognize speech using Google Speech Recognition
#     except LookupError:                                        # speech is unintelligible
#         print("Could not understand audio")
