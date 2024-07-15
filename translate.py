import keys

from azure.ai.translation.text import TextTranslationClient, TranslatorCredential
from azure.ai.translation.text.models import InputTextItem
from azure.core.exceptions import HttpResponseError

cred = TranslatorCredential(keys.TRANSLATE_ACCESS, keys.TRANSLATE_REGION)
client = TextTranslationClient(endpoint=keys.TRANSLATE_ENDPOINT, credential=cred)

# documents courtesy of ChatGPT
documents = [
    "I am ecstatic about the promotion I received at work; it's a dream come true!",
    "The concert was absolutely fantastic, and I had an amazing time.",
    "I enjoyed the meal at the new restaurant; it was quite good overall.",
    "The new software update is decent and has some useful features.",
    "I was completely dissatisfied with the customer service I received.",
    "The flight was delayed for hours, and the experience was terrible.",
    "The book was not as interesting as I had hoped; it was a bit dull.",
    "The hotel room was okay, but the cleanliness could have been better.",
    "I'm indifferent about the new policy changes at work; they don't affect me much.",
    "The weather today is average, with nothing remarkable about it."
]

result = client.translate(
    content=[ InputTextItem(text=document) for document in documents ], 
    to=["es", "it"], 
    from_parameter="en"
)

for idx, translation in enumerate(result):
    print(f"{idx+1:>2}. {documents[idx]}")
    for language in translation.translations:
        print(f"{language.to} - {language.text}")
    print("----------")