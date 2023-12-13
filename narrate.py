# narrate.py
import time
from mine import *
from sys import argv
import http.client
import json

mc = Minecraft()
# Define the server and the endpoint
server = "127.0.0.1:5000"
endpoint = "/narrate"

mc.postToChat("activating narration...")
while True:
    time.sleep(1)
    # Create a connection
    conn = http.client.HTTPConnection(server)

    pos = mc.player.getTilePos()
    mc.postToChat("Position: ")
    mc.postToChat(pos)
    block = mc.getBlock(pos.x, pos.y - 1, pos.z)
    print(block)
    block_types = {
        0: "AR",
        1: "PEDRA",
        2: "GRAMA",
        3: "TERRA",
        4: "PEDRA_BRUTA",
        5: "TABUAS_DE_MADEIRA",
        6: "MUDA",
        7: "ROCHA_MATRIZ",
        8: "AGUA_CORRENTE",
        9: "AGUA_PARADA",
        10: "LAVA_CORRENTE",
        11: "LAVA_PARADA",
        12: "AREIA",
        13: "GRAVILHA",
        14: "MINERIO_DE_OURO",
        15: "MINERIO_DE_FERRO",
        16: "MINERIO_DE_CARVAO",
        17: "MADEIRA",
        18: "FOLHAS",
        20: "VIDRO",
        21: "MINERIO_DE_LAPIS_LAZULI",
        22: "BLOCO_DE_LAPIS_LAZULI",
        24: "ARENITO",
        26: "CAMAS",
        30: "TEIA_DE_ARANHA",
        31: "GRAMA_ALTA",
        35: "LA",
        37: "FLOR_AMARELA",
        38: "FLOR_CIANO",
        39: "COGUMELO_MARRON",
        40: "COGUMELO_VERMELHO",
        41: "BLOCO_DE_OURO",
        42: "BLOCO_DE_FERRO",
        43: "LAJE_DUPLA_DE_PEDRA",
        44: "LAJE_DE_PEDRA",
        45: "BLOCO_DE_TIJOLO",
        46: "TNT",
        47: "ESTANTE_DE_LIVROS",
        48: "PEDRA_MUSGOSA",
        49: "OBSIDIANA",
        50: "TOCHA",
        51: "FOGO",
        53: "ESCADA_DE_MADEIRA",
        54: "BAU",
        56: "MINERIO_DE_DIAMANTE",
        57: "BLOCO_DE_DIAMANTE",
        58: "MESA_DE_TRABALHO",
        60: "TERRA_ARADA",
        61: "FORNALHA_INATIVA",
        62: "FORNALHA_ATIVA",
        64: "PORTA_DE_MADEIRA",
        65: "ESCALA",
        67: "ESCADA_DE_PEDRA",
        71: "PORTA_DE_FERRO",
        73: "MINERIO_DE_REDSTONE",
        78: "NEVE",
        79: "GELO",
        80: "BLOCO_DE_NEVE",
        81: "CACO_DE_CACTO",
        82: "ARGILA",
        83: "CANA_DE_ACUCAR",
        85: "CERCA",
        89: "BLOCO_DE_LUZ_DE_GLOWSTONE",
        95: "ROCHA_MATRIZ_INVISIVEL",
        98: "TIJOLO_DE_PEDRA",
        102: "PAINEL_DE_VIDRO",
        103: "MELANCIA",
        107: "PORTAO_DE_CERCA",
        246: "OBSIDIANA_BRILHANTE",
        247: "NUCLEO_DO_REATOR_DO_NETHER",
    }

    mc.postToChat(block)
    payload = {"event": "Eu piso em {}".format(block_types.get(block))}
    payload_json = json.dumps(payload)
    headers = {"Content-Type": "application/json"}
    conn.request("POST", endpoint, body=payload_json, headers=headers)
    res = conn.getresponse()
    data = res.read()
    conn.close()

    mc.postToChat(data.decode("utf-8"))
    time.sleep(30)
