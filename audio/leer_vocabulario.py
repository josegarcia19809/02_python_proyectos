import pandas as pd
from playsound import playsound

df_vocabulary = pd.read_csv("vocabulary.csv")

buscar = df_vocabulary[df_vocabulary["word"] == "cake"]
audio_buscar=buscar["audio_gb"].iloc[0]
print(audio_buscar)

playsound(f'audios/{audio_buscar}')
