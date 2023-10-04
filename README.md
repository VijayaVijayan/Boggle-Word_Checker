# Boggle-Word_Checker
  Code Wednesday

# Word Search

This is a Python function to find a word on a 2D board. search for the given word on the board.

## Function Description

The `find_word` function takes two arguments:

- `board`: A 2D list representing the board.
- `word`: The word to search for on the board.

It returns `True` if the word is found on the board, and `False` otherwise.

## How It Works

- The function starts by iterating through the elements of the board and invoking a recursive `search` function for each cell.
- The `search` function recursively explores neighboring cells in eight possible directions to check if they match the characters of the word.
- If a match is found, the character in the board is temporarily replaced with `None` to mark it as visited during the search.
- If the entire word is found, the function returns `True`. Otherwise, it backtracks by restoring the original character and continues the search.
- If no match is found, the function returns `False`.

## Sample Test Case

Here's how you can use the `find_word` function:

```python
testBoard = [
      ["E","A","R","A"],
      ["N","L","E","C"],
      ["I","A","I","S"],
      ["B","Y","O","R"]
    ]
    test.assert_equals( find_word(testBoard, "C"               ), True  , "Test for C")
    test.assert_equals( find_word(testBoard, "EAR"             ), True  , "Test for EAR")
    test.assert_equals( find_word(testBoard, "EARS"            ), False , "Test for EARS")
    test.assert_equals( find_word(testBoard, "BAILER"          ), True  , "Test for BAILER")
    test.assert_equals( find_word(testBoard, "RSCAREIOYBAILNEA"), True  , "Test for RSCAREIOYBAILNEA")
    test.assert_equals( find_word(testBoard, "CEREAL"          ), False , "Test for CEREAL")
    test.assert_equals( find_word(testBoard, "ROBES"           ), False , "Test for ROBES")

# Contributing:-

    > Contributions are welcome! If you find any issues or want to add enhancements to the script, feel free to create a pull request.









