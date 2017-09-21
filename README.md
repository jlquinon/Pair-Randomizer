# Pair-Randomizer
Project randomizes pairs of people from a text file ran from a Windows command line. As a coach for my university's dragon boat team, this script automates choosing pairs of people to occasionally lead a land practice from a text file.

## Usage
The version of Python used is 2.7.13.

If it is not already, you must add ```C:\Python27``` to your system PATH variable - the number may vary depending on your version of Python. Instructions on how to do so can be [here](https://stackoverflow.com/questions/4621255/how-do-i-run-a-python-program-in-the-command-prompt-in-windows-7).

This python script uses two libraries, sys and random. The sys library is used to accept a text file as a parameter via the interpreter, and the latter is used to randomize the selection and order of pairs.

For the arguments, the project accepts a text file with a list of people that are to be paired. The format of the .txt file is
```
Person 1
Person 2
Person 3
...
```

To run the project, navigate to the project directory via the command line. Then run the command as follows
```
python choose.py leaders.txt
```
