def simple_mood_classifier(features):
energy = features["energy"]
tempo = features["tempo"]


if energy > 0.05 and tempo > 120:
return "Energetic"
return "Calm"