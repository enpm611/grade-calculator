This simple program calculates the final grade for ENPM 611. It also acts as a demonstration project to show what a simple Python program looks like.

# Setup

The following lays out how to run this program. First, make sure to have set up all the pre-requisites. Then, clone the repository, update the code as you see fit and run it.

## Install Python

This is a Python program that was developed with Python `3.x`. Install the latest version of Python from here:

https://www.python.org/downloads

Once Python is installed, run the following command (from the command line) to check that is was installed correctly:

```bash
python3 --version
```

It should print something like

```
Python 3.10.10
```

## Clone repository

To download the code to your computer, you should have Git installed. If you have not done so, go to 

https://git-scm.com/downloads

and install Git. Once the installation is complete, go to this repository's GitHub page:

https://github.com/enpm611/grade-calculator

and click on the green button on the top right. It will show the repository URL to copy. Copy that URL and go to the command line on your computer. Type:

```bash
git clone https://github.com/enpm611/grade-calculator
```

That should download the repository to your local drive and create a folder called `grade-calculator`. Navigate into that folder:

```bash
cd grade-calculator
```

# Run program

Once in the repository folder, issue the following command to run the program:

```bash
python app/run.py
```

The program should output something like:

```
GRADES --- Quiz 1: 0.78
Can't calculate final grade without all assignments graded
Can't calculate overall course grade without all individual grades.
If all other assignments are 100%, the overall course would be 98.9%, which is a A
```

Now feel free to modify the source code and see how it affect the output. Also, try installing Visual Studio Code (https://www.python.org/downloads) to make it easier to view, modify, and run Python programs.

# Check Commit and Push

Test changes