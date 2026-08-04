import os
def find_music_files(folder):
    music_files = []
    for root,directories, files in os.walk(folder):
        for file in files:
            if file.lower().endswith(
                (".mp3", "flac", ".wav", ".m4a")
            ):
                full_path = os.path.join(root, file)
                music_files.append(full_path)
    return music_files

music_folder = r"C:\Users\wjhar\Music\iTunes"

songs = find_music_files(music_folder)

for song in songs:
    print(song)