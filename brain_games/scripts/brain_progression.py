#!/usr/bin/env python

from brain_games.games.game_progression import progression_logic
from brain_games.scripts.common_logic import engine


def main():
    engine(progression_logic)


if __name__ == "__main__":
    main()
