# Coding Challenge #2: Dracula

Credit for creating this challenge goes to Elizabeth Wickes

For this challenge, you will be using the plain text copy of Dracula. It is available online here: http://www.gutenberg.org/cache/epub/345/pg345.txt 

You will need to import this text from the file, parse through the text to find the individual chapters, and then write those chapters to separate files.
The file names should be "Dracula-Chapter-#" (where you fill in the chapter number as a number, e.g. 1, 2, 3..., and not as a roman numeral). For example, "Dracula-Chapter-1.txt", "Dracula-Chapter-2.txt", etc. There is no need to use leading 0s. There is no need to convert the roman numerals - just use a counter starting at 1.
Each chapter file should start with "CHAPTER #" (e.g. "CHAPTER 1") as the first line and contain exactly the text content of that chapter (e.g. CHAPTER 1 will end with "sky"). Don't worry about extra newlines at the beginning or end, but you shouldn't have extra newlines between the text lines. The content of the chapter files should look exactly as it does from the original file.
Do not hard-code any line number, position numbers, or chapter numbers in the script. There are a total of 27 chapters, but you should not be doing anything 27 separate times in the script.

HINT: you should become familiar with many of the core string and list methods in order to parse through the Dracula text. For example, .index(), .join(), .split(), .pop(), .append(). You should also be comfortable with string and list indexing. And finally, you should know how to read in text from a file and how to write text to a file.

## BONUS
Write a script that calculates how many lines, words, and letters there are in each chapter, and write it out to a separate data file with headers and one row per chapter. This code can be in the same file as the one separating the chapters or in a different file. The output file should look like a CSV:

chapter, characters, words, lines
1, 1000000, 10000, 1000
2, 1000000, 10000, 1000
etc