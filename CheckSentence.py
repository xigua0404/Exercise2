import unittest
class sentence:
  def check_sentence(wordslist):
    wordDict={}
    newlist=[]
    for w in wordslist:
      wordDict[w]=len(w) 
    #print wordDict
    longestword=max(wordDict, key=wordDict.get)
    #print wordDict[longestword],longestword
    newlist.append(wordDict[longestword])
    newlist.append(longestword)
    print newlist
    return newlist

  words="The cow jumped over the moon"
#I can change it as a user input: words=input("Input a sentence with double quote:")
  wordslist=words.split(" ")
  #print wordslist
  check_sentence(wordslist)

#unit test
  def test_len(self):
    testsentence="The longest word here is aasdkfldskafhds"
    testlist=testsentence.split(" ")
    self.assertEqual(check_sentence(testlist),['15','aasdkfldskafhds'])

