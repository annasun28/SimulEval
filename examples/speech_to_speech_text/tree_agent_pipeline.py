from simuleval.agents import TreeAgentPipeline
from examples.speech_to_speech.english_counter_agent import (
    EnglishSpeechCounter as EnglishSpeechToSpeech,
)
from examples.speech_to_text.english_counter_agent import (
    EnglishSpeechCounter as EnglishSpeechToText,
)


class EnglishWait2SpeechToText(EnglishSpeechToText):
    def __init__(self, args):
        super().__init__(args)
        args.wait_seconds = 2

    @staticmethod
    def add_args(parser):
        pass


class EnglishWait2SpeechToSpeech(EnglishSpeechToSpeech):
    def __init__(self, args):
        super().__init__(args)
        args.wait_seconds = 2

    @staticmethod
    def add_args(parser):
        pass


class DummyTreePipeline(TreeAgentPipeline):
    pipeline = {
        EnglishSpeechToSpeech: [EnglishWait2SpeechToText, EnglishWait2SpeechToSpeech],
        EnglishWait2SpeechToSpeech: [],
        EnglishWait2SpeechToText: [],
    }
