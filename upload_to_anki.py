import requests
import socket
import settings

URL = "http://localhost:8766/"

def upload_anki(word,definition,card_type,mp3=None):

    """
        upload a single note to Anki via AnkiConnect.
        Default deck name is : vocabular
    """

    payload = {
        "action": "addNotes",
        "version": 5,
        "params": {
            "notes": [
                {
                    "deckName": "vocabular",
                    "modelName": card_type,
                    "fields": {
                        "Front": word,
                        "Back": definition
                    },
                    "tags": [
                        "automate"
                    ]
                }
            ]
        }
    }

    requests.post(URL,json=payload)

# check if AnkiConnect is running and listening
def is_anki_listening(host="127.0.0.1", port = 8766,timeout= 1):
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock:
        sock.settimeout(timeout)
        try:
            sock.connect((host,port))
            return True
        except (ConnectionRefusedError,socket.timeout):
            return False

# Create a deck if not existed
def ensure_deck_exists():
    payload = {
        "action": "createDeck",
        "version": 6,
        "params": {"deck": "vocabular"}
    }
    requests.post(URL, json=payload)
    settings.deckExists = True

