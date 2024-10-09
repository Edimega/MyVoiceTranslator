import uuid
import gradio as gradio # type: ignore
import whisper # type: ignore
from translate import Translator # type: ignore
from gtts import gTTS # type: ignore
import os
import threading


def translateVoice(input_lang, output_lang, audio):
    if not input_lang or not output_lang:
        raise gradio.Error('Los campos de idioma de entrada y salida no pueden estar vacíos')
    if input_lang == output_lang:
        raise gradio.Error('El idioma de entrada y salida deben ser diferentes')


    # Translate voice to text
    try:
        model = whisper.load_model('base')
        res = model.transcribe(audio, language='spanish', fp16=False)
        firstTranscription = res['text']
    except Exception as e:
        raise gradio.Error('Error al transcribir a texto: ', str(e))


    # Translate text to english
    try:
        secondTranscription = Translator(from_lang=input_lang, to_lang=output_lang).translate(firstTranscription)
    except Exception as e:
        raise gradio.Error('Error al traducir a inglés: ', str(e))


    # Translate text to voice in english and save in a folder data
    try:
        tts = gTTS(secondTranscription, lang=output_lang)
        output_dir = 'data'
        # generate a unique id to add to the audio file name
        audioId = str(uuid.uuid4())
        output_path = os.path.join(output_dir, f'output_audio_{audioId}_.mp3')

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        tts.save(output_path)
        return output_path
    except Exception as e:
        raise gradio.Error('Error al devolver el audio: ', str(e))

# Create the user interface
view = gradio.Interface(
    fn=translateVoice,
    inputs=[
        gradio.Dropdown(choices=['en', 'es', 'fr', 'de'], label='Idioma de entrada', value='es'),
        gradio.Dropdown(choices=['en', 'es', 'fr', 'de'], label='Idioma de salida', value='en'),
        gradio.Audio(sources=['microphone', 'upload'], type='filepath', label='Audio a traducir')
    ],
    outputs=[
        gradio.Audio()
        ],
    title='Traslate Voice',
    description='This is a simple voice translator',
)

# Running the user interface
view.launch(server_name="0.0.0.0", server_port=80)

# Function to delete folders
def deleteFolder():
    try:
        os.system('rm -rf data')
        os.system('rm -rf flagged')
    except Exception as e:
        print('Error al borrar la carpeta data: ', str(e))

# timer to delete the data folder every hour
timer = threading.Event()
while not timer.wait(3600):
    deleteFolder()