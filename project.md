# Project Outline

- Input a list of vocab words (either manually or automatically from anki if possible)
- Prompt an LLM to create scripts using those words with certain parameters (num sentences, num new words, etc)
- Could ask it to focus on stories/scripts with areas of interest
- Use ElevenLabs API to generate audio files of those scripts 
- Generate new audio files everyday as vocabulary expands

Notes:
- Upload to Github, make sure to hide API keys
- Add a bash command which will re-query anki, update the vocab list, and generate new input
- JSON file to store words, will just be a simple list