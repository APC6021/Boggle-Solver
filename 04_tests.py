# Header Files
import time
from sys import argv

# Global Variables
totalMoves = 0
PREFIX_SIZE = 2

# Checks if path equals to word
def examineState( myBoard, position, path ):
    # Combine position with the path
    fullPath = path + [ position ]

    # Loop through path and get letter at every position in path to form a 
    # lowercase word
    wordFound = "".join( 
               [ getLetter( myBoard, coordinate ) for coordinate in fullPath ] )

    # Return a tuple of the word found and the result of the flag
    return wordFound

# Recursively calls itself to check all words possible in given coordinate
def findWords( position, board, takenPath, myDict, wordList ):
    # Create global variable for total moves
    global totalMoves

    # Increment total moves for every recursion call
    totalMoves += 1
    
    # Get all possible moves at the given coordinate
    possibleMovesList = possibleMoves( position, board )

    # Remove all previously visited coords
    legalMovesList = legalMoves( possibleMovesList, takenPath + [ position ] )

    # Loop through every legal coordinate
    for move in legalMovesList:
        # Get the state of the current word
        strFound = examineState( board, move, takenPath + [ position ] )

        # Get suffix of string found
        wordPrefix = strFound[ 0:PREFIX_SIZE ]

        # Check if the prefix exists in made dictionary
        if wordPrefix in myDict.keys():
            # Check if the current combination of letters is in the dictionary
            if strFound in myDict[ wordPrefix ] and strFound not in wordList:
                # Add current combination of letters to word list
                wordList.append( strFound )

            # Otherwise, keep looking for words
            if any( word.startswith( strFound ) for word in 
                                                         myDict[ wordPrefix ] ):
                # If so, recursively search for the next coordinate
                findWords( move, board, takenPath + [ position ], myDict, 
                                                                      wordList )

# Gets letter at given position in board
def getLetter( board, position ):
    # Unpack position into separate variables
    rowIndex, colIndex = position

    # Return letter at the given position in board
    return board[ rowIndex ][ colIndex ]

# Shows available moves at given path
def legalMoves( moves, path ):
    # Create a list with moves that are not in the given path
    legalMoves = [ currentMove for currentMove in moves 
                                                    if currentMove not in path ]

    # Return legal moves
    return legalMoves

# Convert file contents to list of lists of characters
def loadBoard( fileToOpen ):
    # Open given file in reading mode
    openedFile = open( fileToOpen, 'r' )

    # Read all lines in file and place them all in a variable
    fileContents = [ fileLine.split() for fileLine in openedFile ]

    # Return file contents transformed into list of lists
    return fileContents

# Show the possible moves at the given X,Y coordinates 
def possibleMoves( positionInBoard, boardToCheck ):
    # Get board length
    boardSize = len( boardToCheck )
    
    # Create offset variable
    offsets = [ 0, 1, -1 ]

    # Find all surrounding element coordinates (avoid adding same position
    # by not adding the (0,0) coordinate)
    surroundingCoords = [ ( xOffset, yOffset ) for xOffset in offsets 
                        for yOffset in offsets if xOffset != 0 or yOffset != 0 ]
    
    # Add the current position to the surrounding coordinates only if they are
    # within range of 0 and board size
    updatedCoords = [ tuple( offset + position for offset, position in 
    zip( xyOffset, positionInBoard ) if position >= 0 and position < boardSize ) 
                                             for xyOffset in surroundingCoords ]

    # Eliminate all invalid tuples (negative, greater than board and/or less
    # than one value per tuple)
    possibleCoords = [ coordinate for coordinate in updatedCoords 
                     if all( tupleValue >= 0 and tupleValue < boardSize 
                      for tupleValue in coordinate ) and len( coordinate ) > 1 ]

    # Return all possible coordinates where moves are valid
    return possibleCoords

# # Write letters to new file 
def outputToFile( filename, wordList ):
    # Create new file name according to given board file name
    newFileName = filename.replace( ".txt", "_words.txt" )

    # Open new file name in writing mode
    openedFile = open( newFileName, "w" )

    # Write words to new file
    [ openedFile.write( word.lower() + "\n" ) for word in wordList ]

    # Close opened file
    openedFile.close()

# Print the board to the user
def printBoard( boardToPrint ):
    # Print each board letter one by one (use * to print without list format)
    [ print( *boardLetter ) for boardLetter in boardToPrint ]

# Convert dictionary contents to list
def readDictionary( filename, board ):
    # Get the largest size possible for a word
    maxWordSize = len( board ) * len( board )

    # Create word suffix dictionary
    wordDict = {}

    # Open given file in reading mode
    openedFile = open( filename, 'r' )

    # Loop through dictionary file
    for word in openedFile:
        # Update current word with uppercase and strip \n
        word = word.upper().strip()

        # Get word prefix (get prefix from first two letters)
        wordPrefix = word[ 0:PREFIX_SIZE ]

        # Check if the prefix is not in the dictionary
        if wordPrefix not in wordDict.keys():
            # Add prefix as dictionary key
            wordDict.update( { wordPrefix : [] } )

        # Check if the word is equal or less than the maximum word size
        if len( word ) <= maxWordSize:
            # Add word to the dictionary at the key
            wordDict[ wordPrefix ].append( word )

    # Return dictionary transformed into list
    return wordDict

# Main Boggle Function
def runBoard( board_filename, dictionary_filename ):
    # Initialize Variables
    path = []
    wordList = []
    wordDict = {}
    decimalPlace = 3

    # Load board into variable
    myBoard = loadBoard( board_filename )

    # Read dictionary and place dictionary words into variable
    myDict = readDictionary( dictionary_filename, board_filename )

    # Print board to user
    printBoard( myBoard )

    # Print text to user
    print( "\nAnd we're off!" )    

    # Get starting time   
    startTime = time.time()

    # Loop through every row in the board
    for row in range( len( myBoard ) ):
        # Loop through every column in the board
        for column in range( len( myBoard ) ):
            # Recursively call helper function
            findWords( ( row, column ), myBoard, path, myDict, wordList )

    # Print amount of time it took program to run
    print( "All done\n" )
    
    # Get ending time
    endTime = time.time()

    # Print moves and time the program took to run
    print( "Searched total of", totalMoves, "moves in", endTime - startTime, "seconds" )

    # Create dictionary with word list
    [ wordDict.setdefault( len( word ), [] ).append( word ) 
                                                          for word in wordList ]
    
    # Display the words found
    print("\nWords found:")

    # Loop through each key in the dictionary
    for key, contents in sorted( wordDict.items() ):
        # Print the keys of letters found in the dictionary without making
        # new line
        print( key, "-letter words: ", end="" )

        # Print the words at every key with a comma separator
        print( *contents, sep=", " )

    # Sort word list in alphabetical order
    wordList.sort()

    # Display words in alphabetical order   
    print( "\nFound", len( wordList ), "words in total." )

    # Display words in alphabetical order
    print( "Alpha-sorted list words:" )

    # Display word list with comma separator
    print( ", ".join( wordList ).upper() )

    # Return the word list
    return wordList

# Main Function
def main( board, dictionary ):
    # Check if there are exactly 3 arguments (python file name, board, and
    # dictionary)
    if len( argv ) == 3:
        # Initialize Variables (use _ to ignore python file name)
        _, boardFile, dictFile = argv

        # Print text
        print( "Found the following arguments:", boardFile, dictFile )

        # Run main boggle program with arguments
        wordList = runBoard( boardFile, dictFile )

        # Output words to file
        outputToFile( boardFile, wordList )
    
    # Otherwise, assume there are no arguments
    else:
        # Print text
        print( "No arguments found" )

        # Run main boggle program with no arguments
        wordList = runBoard( board, dictionary )

        # Output words to file
        outputToFile( board, wordList )

# Call main function
main( "board4.txt", "twl06.txt" )

# argv = [ "04_tests.py", "board4.txt", "twl06.txt" ]