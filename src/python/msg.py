from grongier.pex import Message

from dataclasses import dataclass

@dataclass
class ScrapRequest(Message):
    url:str = None

@dataclass
class ScrapResponse(Message):
    QuoteList:dict = None

@dataclass
class InspectRequest(Message):
    url:str = None

@dataclass
class InspectResponse(Message):
    html:str = None