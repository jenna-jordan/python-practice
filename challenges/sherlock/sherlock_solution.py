import string

story = """
To Sherlock Holmes she is always the woman. I have seldom heard him mention her under any other name. In his eyes she eclipses and predominates the whole of her sex. It was not that he felt any emotion akin to love for Irene Adler. All emotions, and that one particularly, were abhorrent to his cold, precise but admirably balanced mind. He was, I take it, the most perfect reasoning and observing machine that the world has seen, but as a lover he would have placed himself in a false position. He never spoke of the softer passions, save with a gibe and a sneer. They were admirable things for the observer - excellent for drawing the veil from men's motives and actions. But for the trained reasoner to admit such intrusions into his own delicate and finely adjusted temperament was to introduce a distracting factor which might throw a doubt upon all his mental results. Grit in a sensitive instrument, or a crack in one of his own high-power lenses, would not be more disturbing than a strong emotion in a nature such as his. And yet there was but one woman to him, and that woman was the late Irene Adler, of dubious and questionable memory.
"""

# split the text on spaces (the default), resulting in a list with each word as an element
story_split = story.split()

# remove punctuation and lowercase everything for each word in the list
story_clean = []
for word in story_split:
    word_clean = word.lower().strip(string.punctuation)
    story_clean.append(word_clean)

# set up dictionary with the words I want to count, initializing at 0
count_words = {'sherlock': 0, 'irene': 0, 'woman': 0, 'man': 0, 'the': 0}

# loop through the words in the story list, then loop through the dictionary keys, and if they match, add one to that word's count
for word in story_clean:
    for find_word in count_words.keys():
        if word == find_word:
            count_words[find_word] += 1

# print resulting dictionary
print(count_words)