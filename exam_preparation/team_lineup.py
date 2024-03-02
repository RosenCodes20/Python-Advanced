def team_lineup(*args):
    teams_dict = {}
    result = []
    for name, team in args:
        if team not in teams_dict:
            teams_dict[team] = [name]

        elif team in teams_dict:
            teams_dict[team].append(name)

    for country, name in sorted(teams_dict.items(), key=lambda x:(-len(x[1]), x[0])):
        result.append(f"{country}:")
        for names in name:
            result.append(f"  -{names}")

    return "\n".join(result)


print(team_lineup(
   ("Lionel Messi", "Argentina"),
   ("Neymar", "Brazil"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Harry Kane", "England"),
   ("Kylian Mbappe", "France"),
   ("Raheem Sterling", "England")))

print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany")))

print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany"),
   ("Bruno Fernandes", "Portugal"),
   ("Bernardo Silva", "Portugal"),
   ("Harry Maguire", "England")))
