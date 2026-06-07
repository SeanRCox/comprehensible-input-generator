import anthropic
from dotenv import load_dotenv
import json
import os

def gen_text():
    with open('src/anki/data/vocab.json', 'r') as file:
        vocab = json.load(file)

    words = vocab["words"]
    system_prompt = "You are an expert Japanese teacher. Given a list of vocabulary words," \
    " You create simple stories which correlate to about 10-15 seconds of spoken word." \
    " You use primarily the words provided, in addition to N5-N3 level grammar." \
    " You use words not mentioned in the vocab list which are in the context of the prompt." \
    " The stories are intended to be narrated or spoken by a single speaker." \
    " Vocab words will be provided in the base gramatical form, but adjectives and verbs can be conjugated" \
    " You do not include newlines or any punctuation beyond periods. " \
    " You do not include any text before or after the story." \
    f" Here is the vocab list: {words}"

    load_dotenv()
    ANTHROPIC_KEY = os.getenv('ANTHROPIC_KEY')
    client = anthropic.Anthropic(api_key = ANTHROPIC_KEY)

    prompts = [
        "intergalactic baseball game",
        "cute rats drinking boba",
        "dying in elden ring",
        "hitting PRs at the gym",
        "the titan attack on shiganshina",
    ]

    responses = [
        client.messages.create(
            model="claude-haiku-4-5",
            max_tokens=1000,
            system=system_prompt,
            messages=[{"role": "user", "content": p}],
        )
        for p in prompts
    ]

    texts = [r.content[0].text for r in responses]

    return texts

if __name__ == "__main__":
    gen_text()

