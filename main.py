import gradio as gradio # type: ignore
import threading
from functions import translateVoice, voiceToText, textToVoice, deleteFolder

# Crear interfaces de Gradio para cada función
translate_voice_interface = gradio.Interface(
    fn=translateVoice,
    inputs=[
        gradio.Dropdown(choices=['en', 'es', 'fr', 'de'], label='Idioma de entrada', value='es'),
        gradio.Dropdown(choices=['en', 'es', 'fr', 'de'], label='Idioma de salida', value='en'),
        gradio.Audio(sources=['microphone', 'upload'], type='filepath', label='Audio a traducir')
    ],
    outputs=gradio.Audio(),
    title='Traducir Voz a Voz',
    description='Esta es una simple traducción de voz a voz',
)

voice_to_text_interface = gradio.Interface(
    fn=voiceToText,
    inputs=[
        gradio.Audio(sources=['microphone', 'upload'], type='filepath', label='Audio a texto'),
        gradio.Dropdown(choices=['en', 'es', 'fr', 'de'], label='Idioma de entrada', value='es')
    ],
    outputs=gradio.Textbox(),
    title='Voz a Texto',
    description='Esta es una simple conversión de voz a texto',
)

text_to_voice_interface = gradio.Interface(
    fn=textToVoice,
    inputs=[
        gradio.Dropdown(choices=['en', 'es', 'fr', 'de'], label='Idioma', value='en'),
        gradio.Textbox(label='Texto a convertir')
    ],
    outputs=gradio.Audio(),
    title='Texto a Voz',
    description='Esta es una simple conversión de texto a voz',
)

# Crear una interfaz de pestañas de Gradio
tabbed_interface = gradio.TabbedInterface(
    [translate_voice_interface, voice_to_text_interface, text_to_voice_interface],
    tab_names=['Traducir Voz a Voz', 'Voz a Texto', 'Texto a Voz']
)

# Lanzar la interfaz de pestañas
tabbed_interface.launch(server_name="0.0.0.0", server_port=80)

# Temporizador para borrar la carpeta de datos cada hora
timer = threading.Event()
while not timer.wait(3600):
    deleteFolder()