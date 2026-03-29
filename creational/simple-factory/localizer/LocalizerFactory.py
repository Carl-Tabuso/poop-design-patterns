from FrenchLocalizer import FrenchLocalizer
from EnglishLocalizer import EnglishLocalizer
from SpanishLocalizer import SpanishLocalizer

class LocalizerFactory():
    localizers = {
        "en": EnglishLocalizer,
        "es": SpanishLocalizer,
        "fr": FrenchLocalizer,
    }

    @staticmethod
    def create(lang: str = "en") -> any:
        localizers = LocalizerFactory.localizers
        if (lang not in localizers):
            raise ValueError(f"Language \"{lang}\" is not supported.")
        
        return LocalizerFactory.localizers[lang]()
