import kagglehub

# Download latest version
path = kagglehub.dataset_download("kadircandrisolu/birdclef25-mel-spectrograms")

print("Path to dataset files:", path)
