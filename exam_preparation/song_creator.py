def add_songs(*args):
    songs_dict = {}
    result = []
    final_result = []
    for element in args:
        title, text = element
        if title not in songs_dict:
            songs_dict[title] = [text]
        elif title in songs_dict.keys():
            songs_dict[title].append(text)

    for titles, texts in songs_dict.items():
        final_result.append(f"- {titles}")
        for txt in texts:
            for text in txt:
                final_result.append(f"{text}")

    return "\n".join(final_result)


print(add_songs(
    ("Love of my life",
     ["Love of my life, you've hurt me",
      "You've broken my heart, and now you leave me",
      "Love of my life, can't you see?",
      "Bring it back, bring it back"]),
    ("Beat It", []),
    ("Love of my life",
     ["Don't take it away from me",
      "Because you don't know",
      "What it means to me"]),
    ("Dream On",
     ["Every time that I look in the mirror"]),
))

print(add_songs(
    ("Beat It", []),
    ("Beat It",
     ["Just beat it (beat it), beat it (beat it)",
      "No one wants to be defeated"]),
    ("Beat It", []),
    ("Beat It",
     ["Showin' how funky and strong is your fight",
      "It doesn't matter who's wrong or right"]),
))
