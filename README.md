# Collaborative Python challenges

Hello.

This repo will allow us to solve Python challenges collaboratively. We will catch up in the occasional remote meeting, usually on Saturdays @ 10AM PST. The next meeting will be on **Saturday, March 13 @ 10AM PST**. Closer to the meeting time, check back here for [links to remote collaboration]. In the meantime, you can start to progress through the [first-time setup] section below if you like. Use the new [Discussions] feature in the banner of [this repo on GitHub] if you have any questions, troubles, or if you just want to share your progress on challenges!

[links to remote collaboration]: #links-for-the-meeting-on-saturday-march-13--10am-pst
[first-time setup]: #first-time-setup
[Discussions]: https://github.com/blakeNaccarato/python-challenges/discussions
[this repo on GitHub]: https://github.com/blakeNaccarato/python-challenges

## Links for the meeting on Saturday, March 13 @ 10AM PST

*Check back later for links*.

## Anatomy of this repo

If you've already done the [first-time setup], then you're ready to explore the repo. We will discuss the anatomy of the repo in more detail in our meeting. By the way, "repo" is short for "repository". For now, here is a brief overview of the anatomy of this repo:

- `.lint_config` – Configuration files for our "linters". Linters make sure we're writing clean code.
- `.template` – Blank template challenges, code tests (to check if you did it correctly), and shared code goes here.
- `.vscode` – The settings in here will automatically apply when viewing in VSCode. Also has extension recommendations.
- `user` – Find the subfolder with your name on it and you can start solving challenges.
- `.gitignore` – Lists patterns/files/folders that we don't want to push to GitHub, for example the `.venv` folder.
- `copy_challenges.py` – This script creates `user` subfolders and propagates new challenges, tests, and shared code.
- `LICENSE` – Every repo needs a `LICENSE` file. It tells others the conditions for using your code. MIT is a good one.
- `README.md` – GitHub automatically renders this file if it exists. You're reading it now.
- `requirements.txt` – In a `.venv`, run `pip install -r requirements.txt` to prepare a Python environment.
- `setup.ps1` – PowerShell script that creates a `.venv` and sets it up.

## Challenge sources to be implemented in the future

Here are some sources to free, open-source coding challenges. Once you are familiar with solving the existing Python challenges, and you get accustomed to Git and GitHub functionality, try to implement some interesting challenges from the following links! You will be adding challenges to the `user\.template` folder, and optionally updating `copy_challenges.py` to copy the new type of challenge to other user folders. You can make these changes through a standard `git push` directly to branch `main`, or you can try doing so through "Pull Requests".

- <https://github.com/hurricanemark/DailyCodingChallenge>
- <https://github.com/ledwindra/codewars>
- <https://github.com/donnemartin/interactive-coding-challenges>
- <https://github.com/nyghtowl/Interview_Problems>
- <https://github.com/pybites/challenges>
- <https://github.com/freeCodeCamp/python-coding-challenges>

## First-time setup

We will go over the following setup in our meeting. But if you want to get a head-start, go ahead! It will help speed things along if you get some of this done ahead of time.

- [Collaborative Python challenges](#collaborative-python-challenges)
  - [Links for the meeting on Saturday, March 13 @ 10AM PST](#links-for-the-meeting-on-saturday-march-13--10am-pst)
  - [Anatomy of this repo](#anatomy-of-this-repo)
  - [Challenge sources to be implemented in the future](#challenge-sources-to-be-implemented-in-the-future)
  - [First-time setup](#first-time-setup)
    - [Install Python 3.8.8](#install-python-388)
    - [Install PowerShell 7.1.3](#install-powershell-713)
    - [Install Git](#install-git)
    - [Install VSCode and clone this repo](#install-vscode-and-clone-this-repo)
    - [Install recommended extensions and set up environment](#install-recommended-extensions-and-set-up-environment)
    - [(Optional) GitHub Privacy: Your personal email is exposed by default](#optional-github-privacy-your-personal-email-is-exposed-by-default)

### Install Python 3.8.8

Install Python using the [Python 3.8.8 64-bit installer]. Make sure **not to add Python 3.8 to PATH** as seen below. If you need to see the image below in greater detail, try right-clicking on it and opening it in a new tab.

[Python 3.8.8 64-bit installer]: https://www.python.org/ftp/python/3.8.8/python-3.8.8-amd64.exe

![Python installation screenshots](https://i.imgur.com/5mUiTTU.png)

### Install PowerShell 7.1.3

Download [PowerShell v7.1.3] and install it. The link is an `*.msi` file. Double-click it to install.

[PowerShell v7.1.3]: https://github.com/PowerShell/PowerShell/releases/download/v7.1.3/PowerShell-7.1.3-win-x64.msi

![PowerShell installation screenshot](https://i.imgur.com/TgLRSNr.png)

### Install Git

Install [Git]. Use the following screenshots to guide your installation. Some options may appear slightly different than in these screenshots. That's okay. Just use your best judgement and don't worry about it too much. If you need to see the image below in greater detail, try right-clicking on it and opening it in a new tab.

[Git]: https://git-scm.com/downloads

![Git installation screenshots](https://i.imgur.com/pztSaet.png)

### Install VSCode and clone this repo

Install [VSCode]. I don't have screenshots for this installation process, but it should be pretty straight-forward.

Select the following text with your mouse and **Ctrl+C** to copy it: <https://github.com/blakeNaccarato/python-challenges.git>. You can also get this link on your clipboard by clicking the green "Code" button at [this repo on GitHub], and clicking the clipboard icon for the "HTTPS" option.

![GitHub dialog screenshot](https://i.imgur.com/vjr9P0L.png)

Open VSCode. Press **Ctrl+Shift+P** to bring up the *Command Palette*, and begin typing "Clone" until "Git: Clone" surfaces in the dialog box. Select that option (with the arrow keys, if needed) and press **Enter**. Press **Ctrl+V** to paste the link in the dialog box with the greyed-out text saying "Provide repository URL or pick a repository source." Press **Enter** to confirm the action. Choose anywhere on your local drive (*not in cloud storage like OneDrive or Google Drive*) to put the project. It will go into a subfolder named `python-challenges`. When prompted, click "Open" in the dialog box to open the folder in VSCode, as seen below.

If you are not automatically prompted to log in to GitHub on VSCode when you attempt this action, then follow [this guide] to log in.

![VSCode clone screenshot](https://i.imgur.com/v6cD3sW.png)

[VSCode]: https://code.visualstudio.com/
[this guide]: https://code.visualstudio.com/docs/editor/github

### Install recommended extensions and set up environment

The `.vscode/extensions.json` file recommends certain extensions for this workspace. To install them, click the "Extensions" sidebar button (step 1 below), type `@recommended` in the search bar (2), and then click the cloud icon (3) to install all recommended extensions. After all extensions are installed, you will probably need to reload the VSCode window by pressing **Ctrl+Shift+P** and typing "Developer: Reload window". You may also click the "Reload required" button that pops up on relevant extensions.

![test](https://i.imgur.com/BcLnV2v.png)

Finally, press **CTRL+\`** (that's a "backtick", near the top-left of your keyboard) to pull up the "Integrated Terminal". This gives you a PowerShell terminal in which to execute commands in the current environment. Enter `.\setup.ps1` to set up your Python environment. VSCode may prompt you to "activate" the environment. Click "Yes" if prompted.

### (Optional) GitHub Privacy: Your personal email is exposed by default

This one is optional. Any contributions you make to repositories on GitHub will expose your personal email address. If you want to use a GitHub-specific email address instead, configure the options below.

![GitHub Emails dialog](https://i.imgur.com/HHgykW5.png)
