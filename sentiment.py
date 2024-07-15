import keys

from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

cred = AzureKeyCredential(keys.LANG_ACCESS)
client = TextAnalyticsClient(endpoint=keys.LANG_ENDPOINT, credential=cred)

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

results = client.analyze_sentiment(documents)

for idx, result in enumerate(results):
    print(f"{idx + 1:>2}. {''.join([sentence.text for sentence in result.sentences])}")
    print(result.sentiment)
    print(f"- positive: {result.confidence_scores.positive:.2f}")
    print(f"- negative: {result.confidence_scores.negative:.2f}")
    print(f"- neutral: {result.confidence_scores.neutral:.2f}")