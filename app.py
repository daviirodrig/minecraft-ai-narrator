import os
from flask import Flask, request
import openai
import pygame

import edge_tts
from elevenlabs import generate, set_api_key, play
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


@app.route("/narrate", methods=["POST"])
async def generate_narration():
    data = request.get_json()

    system_prompt = "Você vai narrar minhas ações no Jogo Minecraft, como o narrador de 'A Stanley Parable'. Narre com bom humor, faça piadas, seja irônico. Todas as mensagens enviadas são eventos que ocorreram no jogo. Narre sempre em português. Responda apenas com o texto da narração. Você é muito bem humorado com várias zoeiras, fala muitas coisas zoeiras e engraçadas. Nunca fale mensagens motivadoras, apenas piadas e coisas engraçadas"

    msgs = [
        {
            "role": "system",
            "content": system_prompt,
        },
        {"role": "user", "content": f"Jogador pisou em {data['event'].split(' ')[-1]}"},
    ]

    c = openai.Client(
        api_key=os.getenv("OPENAI_KEY"), base_url=os.getenv("OPENAI_BASE_URL")
    )
    print(data["event"])
    resp = c.chat.completions.create(
        messages=msgs,
        model="gpt-3.5-turbo",
        stream=False,
        temperature=0.8,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    print(resp)

    # set_api_key(os.getenv("XI_API_KEY"))
    # audio = generate(
    #                 text=resp.choices[0].message.content,
    #                 voice="Bella",
    #                 model='eleven_multilingual_v2'
    #             )
    # play(audio)

    communicate = edge_tts.Communicate(
        resp.choices[0].message.content, "pt-BR-AntonioNeural"
    )
    await communicate.save("some.mp3")
    file = "some.mp3"
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    return resp.choices[0].message.content


@app.route("/")
def hello_world():
    return "Hello, World!"


if __name__ == "__main__":
    app.run(debug=True)
