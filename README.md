# Boggle Solver

>[!NOTE]
>This project is no longer actively maintained or supported.

Boggle is a word game where players attempt to find as many words as possible from a grid of randomly 
arranged letters within a time limit. Words are formed by connecting adjacent letters horizontally, 
vertically, or diagonally. Each letter can only be used once per word, and words must be at least 
three letters long. For more information, click [here](https://en.wikipedia.org/wiki/Boggle).

I created this Python script to allow the user to find all words in any board regardless of size.

## Key Features
- Custom Board Support: The script can solve any board, regardless of its size and/or letter arrangements.
- Custom Dictionary: The script can be provided with any dictionary of words, which it will use to
  search for valid words on the board.
- Found Word(s) Output: At the end of the script's runtime, the found word(s) in the board will be saved
  inside a new text file. The name of the file will depend on the name of the board text file. For example,
  if the text file is named "board4.txt", the file containing the words will be named "board4_words.txt". 

## Getting Started
1. Download and Install Python
- Go to the [official Python website](https://www.python.org/downloads/).
- Download the latest version of Python for your operating system (Windows, macOS, or Linux).
- Run the installer and make sure to check the box that says "Add Python to PATH" during the installation
  process. This will allow you to run Python from the command line.

2. Verify Installation
- Open a terminal or command prompt.
- Type the following command and press Enter:
  ```sh
  python --version
  ```

3. Download the Script
- Download the [Python script](https://github.com/APC6021/Boggle-Solver/blob/main/04_tests.py).

4. Board and Dictionary
- Board
  - If you would like to use a custom board, create a text file with NxN letters separated by a space.
  - Otherwise, download the [provided board](https://github.com/APC6021/Boggle-Solver/blob/main/board4.txt).

- Dictionary
  - If you would like to use a custom dictionary, create a text file with one word per line.
  - Otherwise, download the [provided dictionary](https://github.com/APC6021/Boggle-Solver/blob/main/twl06.txt).

5. Navigate to the directory where the files were downloaded.
    ```sh
    cd file_location
    ```

6. Run the Script
  >[!NOTE]
  > If running the script on Windows, write the following commands as they are.\
  > If running the script on Mac/Linux. use "python3" instead of "python".

- To run the script, you have two options:
  - Give the script no arguments (which will default to checking the board4.txt file, as well as the twl06.txt dictionary)
    ```sh
    python 04_tests.py
    ```
  - Give the script a board and a dictionary (where <your_board.txt> and <your_dictionary.txt> are replaced with your text files.)
    ```sh
    python 04_tests.py <your_board.txt> <your_dictionary.txt>
    ```
