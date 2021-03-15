"""Copy tests, challenges, and shared code to all user folders."""

from shutil import copy
import pathlib

USER_FOLDER_NAMES = [
    "blake",
    "brad",
    "collab",
    "devin",
    "fatima",
    "kevin",
    "naz",
    "zack",
]

CHALLENGE_FOLDER_NAMES = [
    "devin",
    "20-04",
]

root = pathlib.Path()

users = root / "users"
challenges = root / ".challenges"

user_folders = (users / user_folder_name for user_folder_name in USER_FOLDER_NAMES)
challenge_folders = [challenges / folder_name for folder_name in CHALLENGE_FOLDER_NAMES]

for user_folder in user_folders:

    if not user_folder.exists():
        user_folder.mkdir(parents=True)

    for challenge_folder in challenge_folders:

        user_specific_challenge_folder = user_folder / challenge_folder.stem
        if not user_specific_challenge_folder.exists():
            user_specific_challenge_folder.mkdir(parents=True)

        # e.g. `tests_john.py`
        tests = challenge_folder / "test.py"
        user_specific_tests_filename = f"test_{user_folder.name}.py"
        user_specific_tests = user_folder / user_specific_tests_filename
        copy(tests, user_specific_tests)

        # copy a challenge if it doesn't already exist
        for challenge in challenge_folder.iterdir():
            if not (user_specific_challenge_folder / challenge.name).exists():
                copy(challenge, user_specific_challenge_folder)
