from datasets import load_dataset
from huggingface_hub import login

login("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")

dataset = load_dataset("audiofolder", data_dir="/Users/PC/OneDrive/Desktop/dataset/audio", drop_labels=True)

dataset.push_to_hub("bacmen/tts_dataset_BAC0092")