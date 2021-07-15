#!/usr/bin/env python

from brain_games.games.game_gcd import gcd_logic
from brain_games.scripts.common_logic import engine


def main():
    engine(gcd_logic)


if __name__ == "__main__":
    main()
