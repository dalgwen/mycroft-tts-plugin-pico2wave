# Copyright 2017 Mycroft AI Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from mycroft.tts import TTS, TTSValidator
from mycroft.util.log import LOG
from mycroft.configuration import Configuration

import subprocess
from datetime import datetime, timedelta
import requests
from xml.etree import ElementTree


class Pico2WaveTTSPlugin(TTS):

    """TTS module for generating speech using ESpeak."""
    def __init__(self, lang, config):
        super(Pico2WaveTTSPlugin, self)\
            .__init__(lang, config, Pico2WaveTTSValidator(self), 'wav')
        self.config = config
        self.lang = self.config.get("lang", "en-US")

    def get_tts(self, sentence, wav_file):
        """Generate WAV from sentence, phonemes aren't supported.

        Arguments:
            sentence (str): sentence to generate audio for
            wav_file (str): output file

        Returns:
            tuple ((str) file location, None)
        """
        subprocess.call(['pico2wave', '-l', self.lang,
                         '-w', wav_file, sentence])
        return wav_file, None


class Pico2WaveTTSValidator(TTSValidator):
    def __init__(self, tts):
        super(Pico2WaveTTSValidator, self).__init__(tts)

    def validate_lang(self):
        pass

    def validate_connection(self):
        self.tts.renew_token()

    def get_tts_class(self):
        return Pico2WaveTTSPlugin
