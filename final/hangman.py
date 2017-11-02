# Hangman game


import random
import string

WORDLIST_FILENAME = "words.txt"


def loadWords():
    """返回文件 words.txt 中的单词list

    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print('加载单词文件...')
    with open(WORDLIST_FILENAME, 'r', -1) as inFile:
        line = inFile.readline()
        wordlist = line.split()
    print('    {}个单词加载了'.format(len(wordlist)))
    return wordlist


def chooseWord(wordlist):
    """随机从 wordlist 取出一个单词

    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''

    assert isinstance(secretWord, str)
    assert isinstance(lettersGuessed, list)

    return all(i in lettersGuessed for i in secretWord)


def getGuessedWord(secretWord, lettersGuessed):
    '''类似这种返回 ta_ t，将 secretWord 中的字符填充在 单词 lettersGuessed中

    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''

    assert isinstance(secretWord, str)
    assert isinstance(lettersGuessed, list)

    secretWords = [i for i in secretWord]
    for k in range(len(secretWords)):
        if secretWords[k] not in lettersGuessed:
            secretWords[k] = '_'

    return ''.join(['_ ' if i == '_' else i for i in secretWords])


def getAvailableLetters(lettersGuessed):
    '''返回不在 lettersGuessed 中的小写字母字符list

    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    l = []
    for i in 'abcdefghijklmnopqrstuvwxyz':
        if i not in lettersGuessed:
            l.append(i)
    return l


def checkSingleLetter(singleLetter):
    if not isinstance(singleLetter, str):
        print('不是字符串：{}'.format(singleLetter))
        return

    if len([i for i in singleLetter]) != 1:
        print('是多字母而非单字母：{}'.format(singleLetter))
        return

    if not singleLetter.isalpha():
        print('非字母：{}'.format(singleLetter))
        return

    return singleLetter.lower()


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''

    guesses_left = 8
    lettersGuessed = []

    print(secretWord)
    print('欢迎来到 Hangman 游戏!')
    print('你要猜的单词长度是：{}'.format(len(secretWord)))

    while guesses_left > 0:
        print('-----------')
        print('你还有 {} 次机会'.format(guesses_left))
        print('    可选字母有：{}'.format(''.join(getAvailableLetters(lettersGuessed))))
        singleLetter = checkSingleLetter(input('    请输入一个字母：'))
        if singleLetter is None:
            return

        lettersGuessed.append(singleLetter)

        guessed = getGuessedWord(secretWord, lettersGuessed)
        if isWordGuessed(secretWord, lettersGuessed):
            print('''猜对了: {} !!!'''.format(guessed))
            return

        if singleLetter not in getAvailableLetters(lettersGuessed[:-1]):
            print('傻不傻，你已经猜过这个字母了: {}'.format(guessed))
            lettersGuessed.pop()
            continue

        if singleLetter in secretWord:
            print('这个字母在: {}'.format(guessed))
            continue
        else:
            print('这个字母不在: {}'.format(guessed))
            guesses_left = guesses_left - 1

    print('傻不傻，游戏结束，你没有猜对。')


if __name__ == '__main__':
    secretWord = chooseWord(wordlist).lower()
    hangman(secretWord)
