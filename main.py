from scanner import find_music_files

def main():
    music_folder = r"C:\Users\wjhar\Music\iTunes"

    songs = find_music_files(music_folder)

    for song in songs:
        print(song)

    if __name__ == "__main__":
        main()
