## Content
1. Fundamental concepts
2. Creating snapshots
3. Browsing project history
4. Branching & merging
5. Collabrationing use GitHub
6. Rewriting history

## Version control system
Watch every lession in order.
git: a version control system. Track history and work together.
Version control system 2 categories:
1. centralized: Subversion/ Team foundation server.
2. Distributed: e.g. git/mercurial

## Why Git
1. Free
2. Open Source
3. Super Fast
4. Scalable
5. Cheap Branching/Merging

## Using Git
1. The command line
2. Code editors & IDEs
3. Graphical user interfaces

## Installation Git
``` shell
git --version
```
[Download the latest git version](https://www.git-scm.com/downloads)

## Configuring Git
Setting
1. Name
2. Email
3. Default Editor
4. Line ending

Different levels of setting
1. System: all users
2. Global: all reporsitories of the current user
3. Local: the current repository

``` shell
git config --global user.name "Jin Lexuan"
git config --global user.email jinlexuan111@gmail.com
git config --global core.editor "code --wait"
git config --global -e      // open default editor to edit all the global settings
```

line return type
1. windows: /r carriage return, /n line feed
2. macOS/Linux: /n line feed

``` shell
git config --global core.autocrlf true    // for windows
git config --global core.autocrlf input   // for macOS and Linux
```

## Getting Help
1. google: git config
2. enter commend in terminal: git config --help (full image)  git config --help (short summary)
