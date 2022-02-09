from makebibliography import *

# bibitem0 = BibItem('article', 'bib0')
# bibitem0.setAuthor('you')
# bibitem0.setField('coauthor', 'me')

# bibDirectory = ''
# workingDirectory = ''
#
# bibitem0 = BibItem('article', 'bib0')
#
# def setBibDirectory():
#     print("Where do you keep your reference cards?")
#     bib_dir = input("Please, enter directory: ")

# file_name = './invalid_file_name.txt'
# file_name = './bibitem.py'
# try:
#     file = open(file_name, 'r')
# except IOError as e:
#     print("An error was encountered opening the file " + file_name)
#     print("Perhaps it is not a valid file name")
#     print("Complete error message: ")
#     print("\t" + str(e))
# else:
#     # N = 110
#     print("File opened successfully")
#     # print("Reading first {} lines:".format(N))
#     # print("")
#     # for i in range(N):
#     #     print("+\t" + file.readline(), end = '')
#     # print("")
#     print("Closing file")
#     file.close()


### COPY TEST

def test_copy_from_paths():
    cardList = ['./testdir/zero.bib', './testdir/one.bib', './testdir/two.bib']
    bib_file_name = './testdir/mergedbibfromfiles.bib'
    # bibfile = open(bib_file_name, 'a')
    # copySelectedFiles(cardList, bibfile)
    # bibfile.close()
    # assert bibfile.closed
    makeBibliography(cardList, bib_file_name, 'a')

def test_copy_from_items():
    cardList = ['./testdir/zero.bib', './testdir/one.bib', './testdir/two.bib']
    bib_file_name = './testdir/mergedbibfromitems.bib'
    # bibfile = open(bib_file_name, 'a')
    bibitemList = []
    for pathToCard in cardList:
        cardfile = open(pathToCard, 'r')
        entrytype = findEntryTypeInFile(cardfile)
        cardfile.seek(0,0)
        citationkey = findCitationKeyInFile(cardfile)
        cardfile.seek(0,0)
        bibitem = BibItem(entrytype, citationkey)
        for line in cardfile:
            line = line.strip(WHITESPACE)
            # if ( '=' in line ):
            if ( (len(line) > 0) and ((line[0] in LETTERS) or ('=' in line)) ):
                field = ''
                value = ''
                i = 0
                while ( i < len(line) ):
                    if ( (line[i] in WHITESPACE) or (line[i] == '=') ):
                        break
                    field += line[i]
                    i += 1
                field = field.strip(WHITESPACE)
                while ( i < len(line) ):
                    if ( line[i] == '=' ):
                        i += 1
                        break
                    i += 1
                while ( (i < len(line)) and (line[i] != ',') ):
                    value += line[i]
                    i += 1
                value = value.strip(WHITESPACE)
                bibitem.setField(field, value)
        bibitemList.append(bibitem)
    # copySelectedBibItems(bibitemList, bibfile)
    # bibfile.close()
    # assert bibfile.closed

    makeBibliography(bibitemList, bib_file_name, 'a')

### TEST FROM PATH TO ITEM AND FROM ITEM TO PATH

def test_from_path_to_item(prnt = True):
    cardList = ['./testdir/zero.bib', './testdir/one.bib', './testdir/two.bib']
    bibitemList = []
    for path in cardList:
        bibitemList.append(fromPathToBibItem(path))
    if ( prnt ):
        for item in bibitemList:
            print(item)
    return bibitemList

def test_from_path_to_refcard(prnt = True):
    cardList = ['./testdir/zero.bib', './testdir/one.bib', './testdir/two.bib']
    refcardList = []
    for path in cardList:
        refcard = RefCard(path)
        refcardList.append(refcard)
    if ( prnt ):
        for refcard in refcardList:
            path = refcard.getLocation()
            item = refcard.getItem()
            print('contents of file : ' + path)
            print(item)
    return refcardList

def test_from_item_to_path(mode):
    """ mode = 'a' or mode = 'w' """
    bib_file_path = './testdir/fromitemstobib.bib'
    bibitemList = test_from_path_to_item(False)
    fromSelectedItemsToPath(bibitemList, bib_file_path, mode)

# test_from_path_to_item()
# test_from_path_to_refcard()
# test_from_item_to_path('w')
# test_from_item_to_path('a')
