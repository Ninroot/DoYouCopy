from src.Story import Story


def main():
    mainStory = Story('../resources/start.json')
    mainStory.start()

if __name__ == '__main__':
    main()