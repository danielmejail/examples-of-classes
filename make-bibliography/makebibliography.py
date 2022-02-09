from bibitem import *

### copy from strings containing a path to a '.bib' (or some other) file

def copyCardFileContents(cardfile, bibfile):
    """
    appends the contents in cardfile to bibfile
    cardfile : file object open in read mode
    bibfile : file object open in append mode
    """
    for line in cardfile:
        bibfile.write(line)
    # print("Contents copied")

def copyCardFileContentsWrapper(pathToCard, bibfile):
    """
    opens file pathToCard in read mode, calls copyCardFileContents and
    closes file
    """
    try:
        if ( not isinstance(pathToCard, str) ):
            errmsg = 'Expected str object, ' + str(type(pathToCard)) + \
                    ' given instead.'
            raise TypeError(errmsg)
        cardfile = open(pathToCard, 'r')
        copyCardFileContents(cardfile, bibfile)
        cardfile.close()
        assert cardfile.closed
    except TypeError as e:
        print(e)
        raise TypeError(e)
    except AssertionError as e:
        print(e)
        raise AssertionError(e)

def copySelectedFiles(cardList, bibfile):
    """
    cardList : a list of valid file names
    bibfile : file object open in append mode
    """
    for pathToCard in cardList:
        copyCardFileContentsWrapper(pathToCard, bibfile)

### copy from BibItem objects directly to file

def copyBibItemContents(bibitem, bibfile, safe = True):
    """
    appends the information contained in bibitem to bibfile
    bibitem : a BibItem object
    bibfile : a file object open in mode append
    safe : bool, if True last field entry ends with a comma: ',\n', if False,
    trailing comma is omitted
    """
    # bibfile.write('\n')
    bibfile.write('@' + bibitem.getEntryType())
    bibfile.write('{' + bibitem.getCitationKey() + ',\n')
    if ( safe ):
        for field in bibitem.getFields():
            bibfile.write('\t' + field + ' = ' + \
                    bibitem.getContents()[field] + ',\n')
    else:
        fieldsAsList = list(bibitem.getFields())
        for field in fieldsAsList[:-1]:
            bibfile.write('\t' + field + ' = ' + \
                    bibitem.getContents()[field] + ',\n')
        field = fieldsAsList[-1]
        bibfile.write('\t' + field + ' = ' + bibitem.getContents()[field] + \
                '\n')
    bibfile.write('}\n')

def copyBibItemContentsWrapper(bibitem, bibfile):
    """
    wrapper, catches possible errors before calling copyBibItemContents
    """
    try:
        if ( not isinstance(bibitem, BibItem) ):
            errmsg = 'Expected BibItem object, ' + str(type(bibitem)) + \
                    ' given, instead.'
            raise TypeError(errmsg)
        copyBibItemContents(bibitem, bibfile)
    except TypeError as e:
        print(e)
        raise TypeError

def copySelectedBibItems(bibitemList, bibfile):
    """
    bibitemList : a list of BibItem objects
    bibfile : file object open in append mode
    """
    for bibitem in bibitemList:
        copyBibItemContentsWrapper(bibitem, bibfile)

### wrapper function to deal with both previous cases and a the case of mixed
### types

def copySelected(itemList, bibfile, itemsType = None):
    """
    itemList : a list, either [string] or [BibItem]
    bibfile : file object open in append mode
    """
    if ( itemsType == None ):
        for item in itemList:
            if ( isinstance(item, str) ):
                copyCardFileContentsWrapper(item, bibfile)
            elif ( isinstance(item, BibItem) ):
                copyBibItemContentsWrapper(item, bibfile)
            else:
                errmsg = 'Unrecognised reference format: ' + \
                        'neither string (path to file) nor BibItem'
                raise TypeError(errmsg)
    if ( itemsType == 'path' ):
        copySelectedFiles(itemList, bibfile)
    if ( itemsType == 'bibitem' ):
        copySelectedBibItems(itemList, bibfile)

def makeBibliography(itemList, pathToBib, mode = 'a'):
    if ( len(itemList) > 0 ):
        if ( isinstance(itemList[0], str) ):
            itemsType = 'path'
        elif ( isinstance(itemList[0], BibItem) ):
            itemsType = 'bibitem'
        else:
            itemsType = None
    i = 1
    while ( (i < len(itemList)) and (itemsType != None) ):
        if ( not isinstance(itemList[i], type(itemList[0])) ):
            itemsType = None
        i += 1
    bibfile = open(pathToBib, mode)
    copySelected(itemList, bibfile, itemsType)
    bibfile.close()
    assert bibfile.closed

### functions dealing with searching and indexing reference items either
### path strings or BibItems

def searchForCard():
    # ask for input
    # until finished
    #   insert field : value
    # search files for item with similar characteristics
    # make a list of candidates
    # display results
    #   index (some, first N, next N, all, remaining, ...)
    #       for each card to display
    #           display card info in one line, summary
    #       (choose phase)
    #       if found something, indicate index number
    #           show complete info or directly append file_name to cardList
    #           if complete info
    #               is this it ?
    #               append file_name, show next, back to index
    #       else, display some, first N, next N, all, remaining, ...
    #   one by one
    #       display complete info
    #       is this it ?
    #       append file_name, show next
    # choose another ? continue looping until finished
    # once finished, call copySelected
    ## This programme appends to an existing file or creates a new one if there
    ## is no file with the given file name. It does not check whether the file
    ## exists nor whether the file contains certain info, so one might end up
    ## with duplicate content.
    ## It might be better to be able to choose to either create a new file or
    ## overwrite any existing one (open in 'w' mode), or to append to an
    ## existing one or create a new one (open in 'a' mode).
    ## Anyway, the hability to check whether certain information is already in
    ## the file might be useful, as well.
    pass
