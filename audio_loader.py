import librosa


def load_audio(file_path, sr=22050):
y, sr = librosa.load(file_path, sr=sr, mono=True)
return y, sr