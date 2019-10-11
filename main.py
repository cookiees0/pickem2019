from pickem_parser import PickEmParser
from pickem_group import PickEmGroup


def main():
    p = PickEmParser()
    p.parse_from_tsv('reddit_ratings_2019.tsv')

    all_groups = {"A": ["Cloud9", "Hong Kong Attitude", "G2 Esports", "Griffin"],
                  "B": ["GAM Esports", "Splyce", "FunPlus Phoenix", "J-Team"],
                  "C": ["SK Telecom T1", "Fnatic", "Royal Never Give Up", "Clutch Gaming"],
                  "D": ["DAMWON Gaming", "ahq e-Sports Club", "Team Liquid", "Invictus Gaming"]}

    for group_no in all_groups:
        group = PickEmGroup([p.get_pickem_team(team) for team in all_groups[group_no]], group_no)
        group.eu_ties()
        group.simulate_group()
        group.print_results()
        print()


if __name__ == "__main__":
    main()
