## The command-line interface

Interaction with a computer is typically done through a graphical user interface (GUI). With a GUI, instructions are sent to the computer by clicking a mouse and interacting with menus. GUIs are often designed to be used intuitively, and basic interaction with one can be done from the first moment a user sees it. However, this way of delivering instructions to a computer involves a lot of user interaction, which can greatly reduce productivity and is prone to user-error.

Imagine the following task: for a literature search, you have to copy the third line of one thousand text files in one thousand different directories and paste it into a single file. Using a GUI, you would not only be clicking at your desk for several hours, but you could potentially also commit an error in the process of completing this repetitive task.

In such tasks we can take advantage of a Unix shell, which is often referred to as a terminal. A Unix shell is both a command-line interface (CLI) and a scripting language. With the proper commands, the shell enables us to repeat specific tasks with or without modification as many times as we would want. The task we describe above can be completed in seconds using the shell.

### Using the terminal

During the installation of the software we use in our courses you have watched a video on how to use the Mac OS terminal. In the exercises below you will practice the very basics of the terminal. Don't worry; the exercises won't be as intricate as the task described in the example above.

> You don’t have to hand in these practice exercises. They’re here for you to test yourself.

**Exercise 1** Starting from `/Users/amanda/data`, which of the following commands could Amanda use to navigate to her home directory, which is `/Users/amanda`?

    1. cd .
    2. cd /
    3. cd /home/amanda
    4. cd ../..
    5. cd ~
    6. cd home
    7. cd ~/data/..
    8. cd
    9. cd ..

**Exercise 2** Using the filesystem diagram below, if `pwd` displays `/Users/thing`, what will `ls -F ../backup` display?

    1. ../backup: No such file or directory
    2. 2012-12-01 2013-01-08 2013-01-27
    3. 2012-12-01/ 2013-01-08/ 2013-01-27/
    4. original/ pnas_final/ pnas_sub/

![](filesystem-challenge.svg)

**Exercise 3** Using the filesystem diagram below, if `pwd` displays `/Users/backup`, and `-r` tells `ls` to display things in reverse order, what command(s) will result in the following output:

```
pnas_sub/ pnas_final/ original/
```

![](filesystem-challenge2.svg)


    ls pwd
    ls -r -F
    ls -r -F /Users/backup


<details markdown="1"><summary  markdown="span">Answer</summary>

**Exercise 1**

    1. No: . stands for the current directory.
    2. No: / stands for the root directory.
    3. No: Amanda’s home directory is /Users/amanda.
    4. No: this command goes up two levels, i.e. ends in /Users.
    5. Yes: ~ stands for the user’s home directory, in this case /Users/amanda.
    6. No: this command would navigate into a directory home in the current  directory if it exists.
    7. Yes: unnecessarily complicated, but correct.
    8. Yes: shortcut to go back to the user’s home directory.
    9. Yes: goes up one level.

**Exercise 2**

    1. No: there is a directory backup in /Users.
    2. No: this is the content of Users/thing/backup, but with .., we asked for one level further up.
    3. No: see previous explanation.
    4. Yes: ../backup/ refers to /Users/backup/.

**Exercise 3**

    1. No: pwd is not the name of a directory.
    2. Yes: ls without directory argument lists files and directories in the current directory.
    4. Yes: uses the absolute path explicitly.

</details>

## Acknowledgement

The information and exercises on this page have been adapted from [content on Software Carpentry](https://swcarpentry.github.io/shell-novice/) under the [CC BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).

<!--
pwd
open
ls
cd
cd ..
clear
touch
* tab completion + double tab
nano
* history arrow keys
history command
rm
mkdir
touch
rm -r (dir)

This is where we take advantage of the Unix shell. The Unix shell is both a command-line interface (CLI) and a scripting language, allowing such repetitive tasks to be done automatically and fast. With the proper commands, the shell can repeat tasks with or without some modification as many times as we want. Using the shell, the task in the literature example can be accomplished in seconds.

man/help

https://swcarpentry.github.io/shell-novice/02-filedir/index.html#absolute-vs-relative-paths

https://swcarpentry.github.io/shell-novice/02-filedir/index.html#relative-path-resolution

https://swcarpentry.github.io/shell-novice/02-filedir/index.html#ls-reading-comprehension

https://swcarpentry.github.io/shell-novice/02-filedir/index.html#general-syntax-of-a-shell-command <- deze eerst

https://swcarpentry.github.io/shell-novice/03-create/index.html#creating-files-a-different-way

https://swcarpentry.github.io/shell-novice/03-create/index.html#moving-files-and-directories

https://swcarpentry.github.io/shell-novice/03-create/index.html#moving-files-to-a-new-folder

https://swcarpentry.github.io/shell-novice/03-create/index.html#copying-files-and-directories

https://swcarpentry.github.io/shell-novice/03-create/index.html#renaming-files

https://swcarpentry.github.io/shell-novice/03-create/index.html#moving-and-copying

https://swcarpentry.github.io/shell-novice/03-create/index.html#using-rm-safely

https://swcarpentry.github.io/shell-novice/03-create/index.html#organizing-directories-and-files

-->
