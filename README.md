### mycroft-tts-plugin-pico2wave

This TTS service for Mycroft use pico2wave to generate speech. pico2wave must be installed and in the path.
Configuration parameters :

```json
"tts": {
    "module": "pico2wave",
    "pico2wave": {
        "lang": "en-EN"
    }
}
```

##### Installation

`mycroft-pip install git+https://github.com/dalgwen/mycroft-tts-plugin-pico2wave.git`

##### LICENSE :

Apache-2.0