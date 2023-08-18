<div align="center" style="margin-bottom: 70px">
	<h1>🔥FireCommit</h1><br>
	<img alt="Static Badge" src="https://img.shields.io/badge/license-GNU%20Public%20v3-critical">
	<img alt="Static Badge" src="https://img.shields.io/badge/version-v6.1%20--%20stable-green">
	<img alt="Static Badge" src="https://img.shields.io/badge/lang-87b5e0?style=flat&logo=Python">
	<img alt="Static Badge" src="https://img.shields.io/badge/Extension-133b61?style=flat&logo=Git">
	<img alt="Static Badge" src="https://img.shields.io/badge/FireCommit-910806?style=flat&logo=Fireship">
</div>

## Features

 > Commandline-Tool

 > Platform-independent

 > Modifications possible

## Description

In large projects it's important to use verbose and structured commit messages. This can be challenging when working in a big team with many
developers. The provided script helps you with that. 

## Requirements

- Python, Vesion >= 3.7 [ [Installation](https://www.python.org/downloads/) ]

## Installation

In your git repository, create a directory named `commitmsg`. Furthermore, add 
the provided files ([See Latest Release](https://github.com/BenSt099/FireCommit/releases)) into the directory you just created. See **Usage** for starting the script.

## Usage

The script was tested on Windows and Linux (MacOS: Not Tested (Works on my machine 😉)). For starting the script, open a terminal / command prompt and type:

```bash
python FireCommit_v6.py
```

or

```bash
python3 FireCommit_v6.py
```

## Documentation

For the full documentation, click [here](https://github.com/BenSt099/FireCommit/blob/main/docs/docs.adoc).

## Known Issues

1. Committing Without Adding

    - The script warns you if some files are unstaged but it doesn't
      include those files into the commit. You have to manually add them to the staging area.

2. Unexpected Result When Running ``git log``

    - When writing a verbose commit message, a compromise must be made regarding the readability of the git log.

    - If you run `git log`, you may see a large amount of text that would fill up pages.

    - Using `git shortlog` will not help: 

<div align="center" style="margin-bottom: 70px">
	<img alt="Picture of a bad git shortlog" src="pictures/BadGitShortLog.png">
</div>

To search for single commits more easily, use

```bash
git log --pretty=format:"%cn committed %h on %cd with Topic: %f"
```

or similar modifications.

## License

This project is licensed under GNU General Public License v3.0. Fore more information, click [here](https://github.com/BenSt099/FireCommit/blob/main/LICENSE).