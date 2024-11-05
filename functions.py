import uuid
import whisper # type: ignore
from translate import Translator # type: ignore
from gtts import gTTS # type: ignore
import os
import gradio # type: ignore

# Función para traducir voz a voz
def translateVoice(input_lang, output_lang, audio):
    if not input_lang or not output_lang:
        raise gradio.Error('Los campos de idioma de entrada y salida no pueden estar vacíos')
    if input_lang == output_lang:
        raise gradio.Error('El idioma de entrada y salida deben ser diferentes')

    try:
        model = whisper.load_model('base')
        res = model.transcribe(audio, language='spanish', fp16=False)
        firstTranscription = res['text']
    except Exception as e:
        raise gradio.Error('Error al transcribir a texto: ', str(e))

    try:
        secondTranscription = Translator(from_lang=input_lang, to_lang=output_lang).translate(firstTranscription)
    except Exception as e:
        raise gradio.Error('Error al traducir a inglés: ', str(e))

    try:
        tts = gTTS(secondTranscription, lang=output_lang)
        output_dir = 'data'
        audioId = str(uuid.uuid4())
        output_path = os.path.join(output_dir, f'output_audio_{audioId}_.mp3')

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        tts.save(output_path)
        return output_path
    except Exception as e:
        raise gradio.Error('Error al devolver el audio: ', str(e))

# Función para convertir voz a texto
def voiceToText(audio, input_lang):
    try:
        model = whisper.load_model('base')
        res = model.transcribe(audio, language=input_lang, fp16=False)
        return res['text']
    except Exception as e:
        raise gradio.Error('Error al transcribir a texto: ', str(e))

# Función para convertir texto a voz
def textToVoice(text, lang):
    try:
        tts = gTTS(text, lang=lang)
        output_dir = 'data'
        audioId = str(uuid.uuid4())
        output_path = os.path.join(output_dir, f'output_audio_{audioId}_.mp3')

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        tts.save(output_path)
        return output_path
    except Exception as e:
        raise gradio.Error('Error al devolver el audio: ', str(e))

# Función para borrar carpetas
def deleteFolder():
    try:
        os.system('rm -rf data')
        os.system('rm -rf flagged')
    except Exception as e:
        print('Error al borrar la carpeta data: ', str(e))