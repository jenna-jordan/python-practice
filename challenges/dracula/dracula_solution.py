# import dracula by line
infile = open("dracula.txt", "r", encoding='utf-8')
fullText = infile.readlines()
infile.close()

# find where actual book starts and ends
bookStart = "DRACULA\n"
bookEnd = "                                THE END\n"
start = fullText.index(bookStart)
end = fullText.index(bookEnd)

# make list containing only desired lines
bookText = fullText[start:end+1]

# join book text into one string
bookTextString = "".join(bookText)

# split into list by Chapter
textChapterList = bookTextString.split("CHAPTER")
removeDracula = textChapterList.pop(0)

chapters = []

# add chapter back in
for cutchapter in textChapterList:
    chapter = "CHAPTER" + cutchapter
    chapters.append(chapter)

# create files for each chapter
for chapter in range(len(chapters)):
  thischapter = chapters[chapter]
  filename = "Dracula-Chapter-" + str(chapter + 1) + ".txt"
  outfile = open(filename, "w")
  print(thischapter, file=outfile)
  outfile.close()

# Bonus section

outfile = open("DraculaStats.csv", "w")
print("chapter, characters, words, lines", file=outfile)

chapCount = 0

for chapter in chapters:
    chapCount = chapCount + 1
    stripChap = chapter.strip()
    countLines = len(stripChap.split("\n"))
    countWords = len(stripChap.split(" "))
    countChars = len(stripChap)
    print(str(chapCount) + ", " + str(countChars) + ", " + str(countWords) + ", " + str(countLines), file=outfile)

outfile.close()