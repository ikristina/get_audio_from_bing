# get_audio_from_bing
Downloads mp3 sounds from the [Bing Translator](https://www.bing.com/translator) for english words and expressions in csv file.

### How to use

1. Make csv file with required words and expressions. Each word (or expression) has to start from new line.
2. By default, 2 mp3 files will be downloaded: UK accent with male voice and US accent with female voice.

Change gender settings for countries: 21 - 24 lines.
Change download settings: 57 - ... lines. (Pass different country parameter to make_request_for_mp3 function).
