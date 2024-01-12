from dataclasses import dataclass, field
from typing import List, Union


@dataclass
class Symbol:
    drawing: str
    sound: str = "?"
    translation: str = "?"
    comment: str = ""
    is_translated: bool = False

    def __post_init__(self):
        if self.sound == "?":
            self.sound = "_"
        if self.translation == "?":
            replacement = self.sound if self.sound != "_" else f"({self.drawing})"
            self.translation = "\033[31m" + replacement + "\033[0m"
            self.is_translated = False
        else:
            self.is_translated = True

    def set_translation(self, new_translation):
        self.translation = new_translation
        self.is_translated = True

    def __add__(self, other):
        if isinstance(other, Symbol):
            return Sentence(words=[self, other])
        elif isinstance(other, Sentence):
            return Sentence(words=[self, *other.words])
        return NotImplemented

    def __str__(self):
        return self.sound

    def translate(self):
        return self.translation


@dataclass
class Connector(Symbol):
    pass


@dataclass
class Word(Symbol):
    pass


@dataclass
class ComplexWord(Word):
    sub_symbols: List[Symbol] = field(default_factory=list)


def complex_word_builder(symbols: List[Symbol], translation: str = "", **kwargs):
    if translation == "":
        translation = "-".join([sym.translate() for sym in symbols])
    return ComplexWord(
        sub_symbols=symbols, drawing=", ".join(symbol.drawing for symbol in symbols), translation=translation, **kwargs
    )


@dataclass
class Concept(ComplexWord):
    def __str__(self):
        return "|" + " ".join([str(word) for word in self.sub_symbols]) + "|"


def concept_builder(sub_symbols: List[Union[Symbol, Concept]], translation: str = "?"):
    if translation == "?":
        translation = "-".join(sub_symbol.translate() for sub_symbol in sub_symbols)

    drawings = " ".join([sub_symbol.drawing for sub_symbol in sub_symbols])
    return Concept(sub_symbols=sub_symbols, drawing=drawings, translation="|" + translation + "|")


@dataclass
class Sentence:
    words: List[Union[Symbol, Concept]]

    def __add__(self, other):
        if isinstance(other, (Symbol, Concept)):
            return Sentence(words=[*self.words, other])
        if isinstance(other, Sentence):
            return Sentence(words=[*self.words, *other.words])
        return NotImplemented

    def show_loa(self):
        print(" ".join([str(word) for word in self.words]))

    def show_common(self):
        print(" ".join([word.translate() for word in self.words]))


@dataclass
class Text:
    sentences: List[Sentence]

    def show_loa(self):
        for idx, sentence in enumerate(self.sentences):
            # print(idx)
            sentence.show_loa()

    def show_common(self):
        for idx, sentence in enumerate(self.sentences):
            # print(idx)
            sentence.show_common()
