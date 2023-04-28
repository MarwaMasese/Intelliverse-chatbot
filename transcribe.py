import openai
openai.api_key = "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"

def Transcribe(audio):
    audio_file= open(f"{audio}.wav", "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    text_output = transcript['text']
    print(text_output)
    return transcript

Transcribe("recording0")