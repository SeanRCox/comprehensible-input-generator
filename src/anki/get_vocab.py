import json
import requests
import os

# AnkiConnect exposes port 8765
ANKI_URL = f"http://{os.environ.get('ANKI_HOST', 'localhost')}:8765"

def anki_invoke(action, **params):
    payload = {"action": action, "version": 6, "params": params}
    response = requests.post(ANKI_URL, json=payload).json()
    if response.get('error'):
        raise Exception(response['error'])
    return response['result']

def get_vocab():
    # Get all the cards in Young and Mature
    current_vocab_cards = anki_invoke('findCards', query='deck:current (is:review)')
    
    note_ids = anki_invoke('cardsToNotes', cards=current_vocab_cards)
    notes = anki_invoke('notesInfo', notes=note_ids)

    # Strip each card for the Japanese voacb word only
    vocab_words = [note['fields']['Vocabulary-Kanji']['value'] for note in notes]

    return vocab_words

def save_vocab():
    # Store vocab words as a simple JSON object
    data = {
        "words": get_vocab()
    }

    json_str = json.dumps(data, indent=4)
    with open("src/anki/data/vocab.json", "w") as f:
        f.write(json_str)

if __name__ == "__main__":
    save_vocab()