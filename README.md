# Mouse-Disambiguation
HackerRank Real Data Contest 2015 "Mouse vs. Mouse" Problem submission. My model scored ~20 points meaning I was correct 70% of the time, even against challenging inputs. Ranked 147th / 800 or so. 50% of submissions scored at least 1 point (50% correct) which is fairly low. Given that the contest has concluded and all code is publicly available, there should be no issue sharing this here.

# The Challenge:
Given a sentence containing the word "mouse", determine if it represents a computer mouse or an animal. You must define your own corpus (you may not download one (à la nltk) and your final code must be smaller than 10 kb.

# My Solution
I solved this by creating three lists of words, one representing computer mice, one representing animal mice, and one for the program to ignore. The program reads a sentence using nltk and scores it. If the score is higher for one type of mouse, it returns that one. If a sentence is perfectly ambiguous ("The mouse is colored white" scores 50/50, for example) it will make a guess.

# Thoughts
This challenge was my first attempt at NLP and any machine learning task, really. Prior to this, I didn't even know what nltk was. It's still astonishing to me how few words you need to have in your corpus to successfully complete a challenging task like this. I also wasn't aware that it was possible to have a persistent model (that's what the "pickled" string is) that can be input into nltk and used so you don't have to input your entire corpus and go over the 10 kb limit.
