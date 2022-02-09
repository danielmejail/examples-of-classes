import string

EOF_SIGNAL = ''
WHITESPACE = string.whitespace
LETTERS = string.ascii_letters

class BibItem(object):
    entryTypes = ["article", "book", "booklet", "conference", "inbook", \
            "incollection", "inproceedings", "manual", "masterthesis", \
            "misc", "phdthesis", "proceedings", "techreport", "unpublished"]
    commonFields = ["author", "year", "title", "editor", "journal", "volume", \
            "number", "pages", "publisher", "address", "howpubished", \
            "month", "series", "booktitle", "school", "organisation", \
            "institution", "note"]
    otherFields = ["doi", "isbn", "issn", "url"]

    def __init__(self, entrytype, citationkey):
        """
        each bibliography item is given an entry type among the valid entry
        types and a citation key; without these, it would not be possible to
        classify nor reference the bibitem; the bibitem contents proper are
        saved in a dictionary (str -> str) with keys the field names, such as
        author, year, etc.
        """
        if ( not(entrytype in BibItem.entryTypes) ):
            if ( entrytype != '' ):
                raise AttributeError("There is no entry type named " + \
                        entrytype)
            else:
                # empty entrytype should not be used, except when searching
                pass
        self.entrytype = entrytype
        self.citationkey = citationkey
        self.contents = {}

    def getEntryType(self):
        return self.entrytype
    def getCitationKey(self):
        return self.citationkey
    def getContents(self):
        return self.contents
    def getFields(self):
        return self.contents.keys()

    def setField(self, field, value, heed = True):
        if ( heed ):
            if ( not (field in BibItem.commonFields) ):
                warnmsg = "The field you are about to create is not one " + \
                        "of the common fields."
                print("Warning: " + warnmsg)
                print("Entered: " + str(field) + ".", end = ' ')
                while (True):
                    try:
                        decision = input("Proceed? (y/N) ").lower()
                        if ( not (decision in ["y", "n"]) ):
                            msg = "Please input 'y' if, you'd like to " + \
                                    "proceed, or 'n', if you'd rather not."
                            raise ValueError(msg)
                        elif ( decision == "y" ):
                            print("Proceeding...")
                            break
                        else:
                            print("Backing up")
                            return None
                    except ValueError as e:
                        print("An error occured while processing your choice.")
                        print(e, end = ' ')
        self.contents[field] = value

    def setAuthor(self, author):
        self.setField("author", author, False)
    def setYear(self, year):
        self.setField("year", year, False)
    def setTitle(self, title):
        self.setField("title", title, False)
    def setJournal(self, journal):
        self.setField("journal", journal, False)
    def setVolume(self, volume):
        self.setField("volume", volume, False)
    def setNumber(self, number):
        self.setField("number", number, False)
    def setPages(self, pages):
        self.setField("pages", pages, False)
    def setPublisher(self, publisher):
        self.setField("publisher", publisher, False)
    def setAddress(self, address):
        self.setField("address", address, False)
    def setHowpublished(self, howpublished):
        self.setField("howpublished", howpublished, False)
    def setMonth(self, month):
        self.setField("month", month, False)
    def setSeries(self, series):
        self.setField("series", series, False)
    def setBooktitle(self, booktitle):
        self.setField("booktitle", booktitle, False)
    def setEditor(self, editor):
        self.setField("editor", editor, False)
    def setSchool(self, school):
        self.setField("school", school, False)
    def setOrganisation(self, organisation):
        self.setField("organisation", organisation, False)
    def setInstitution(self, institution):
        self.setField("institution", institution, False)
    def setNote(self, note):
        self.setField("note", note, False)
    def setDOI(self, doi):
        self.setField("doi", doi, False)
    def setURL(self, url):
        self.setField("url", url, False)
    def setISBN(self, isbn):
        self.setField("isbn", isbn, False)
    def setISSN(self, issn):
        self.setField("issn", issn, False)

    def entryTypeFitsPattern(self, other):
        return (self.entrytype == other.entrytype)
    def fieldFitsPattern(self, other, field, loosely = False):
        """
        field : a field in other.getFields()
        if loosely == True, the comparison is loosened; basically *all* the
        words must be there (possibly as substrings), but not necessarily in
        the same order
        """
        if ( loosely ):
            # take out possible braces '{' or '}' inside field value
            otherFieldValue = deleteChars(other.contents[field],'{}')
            selfFieldValue = deleteChars(self.contents.get(field, ''), '{}')
            # convert to lower case
            otherFieldValue = otherFieldValue.lower()
            selfFieldValue = selfFieldValue.lower()
            # loosen (split) pattern
            otherFieldValueSplit = otherFieldValue.split(' ')
            for word in otherFieldValueSplit:
                if ( not (word in selfFieldValue) ):
                    return False
        else:
            if ( not (other.contents[field] in self.contents.get(field, '')) ):
                return False
        return True

    def fitsPattern(self, other, matchEntryType = True, loosely = False, \
            atLeastOne = False):
        """
        a kind of comparison;
        other : a BibItem object with incomplete information;
        returns True, if self fits the pattern of other;
        if loosely == True, the comparison is loosened field-wise;
        however, every field must pass the test fieldFitsPattern;
        atLeastOne chages this : if it is set to True, the result is True, if
        at least one field passes the test
        """
        if ( matchEntryType and (not self.entryTypeFitsPattern(other)) ):
            return False
        if ( atLeastOne ):
            for field in other.getFields():
                if ( self.fieldFitsPattern(other, field, loosely) ):
                    return True
            return False
        else:
            for field in other.getFields():
                if ( not self.fieldFitsPattern(other, field, loosely) ):
                    return False
            return True

    def __str__(self):
        # return str(self.contents)
        bibstring = ''
        bibstring += '@' + self.getEntryType()
        bibstring += '{' + self.getCitationKey() + ',\n'
        for field in self.getFields():
            bibstring += '\t' + field + ' = ' + self.getContents()[field] + \
                    ',\n'
        bibstring += '}\n'
        return bibstring

### Functions to translate files into bibitems

def findEntryTypeInFile(cardfile):
    """
    cardfile : file object open in read mode;
    returns entry type of bibitem;
    does not check whether the entry type is valid or not according to
    BibItem.entryTypes;
    once the entry type is read, the rest is ignored
    if no 'at' is found at the beginning of a line, return an empty string
    """
    et = ''
    # look for the first 'at' sign at the beginning of a line
    prevchar = ''
    char = cardfile.read(1)
    while ( (char != EOF_SIGNAL) and \
            (char != '@' or ((prevchar != '') and (prevchar != '\n'))) ):
        prevchar = char
        char = cardfile.read(1)
    if ( char != EOF_SIGNAL ):
        # then, char == '@' and (prevchar == '' or prevchar == '\n')
        # start copying
        while ( char != EOF_SIGNAL and char != '{' ):
            et += char
            char = cardfile.read(1)
        et = et[1:] # omit the '@'
    et = et.strip(WHITESPACE)
    return et

def findCitationKeyInFile(cardfile):
    """
    cardfile : file object open in read mode;
    returns citation key for bibitem;
    beginning of a line;
    once this is found, copy characters (even whitespaces) up to the first
    comma ',' following '{';
    strip this substring from whitespaces;
    return remaining string (might be empty)
    """
    ck = ''
    # look for the first 'at' sign at the beginning of a line
    prevchar = ''
    char = cardfile.read(1)
    while ( (char != EOF_SIGNAL) and \
            (char != '@' or ((prevchar != '') and (prevchar != '\n'))) ):
        prevchar = char
        char = cardfile.read(1)
    if ( char != EOF_SIGNAL ):
        # then, char == '@' and (prevchar == '' or prevchar == '\n')
        # look for the openning brace '{'
        while ( char != EOF_SIGNAL and char != '{' ):
            # there is no need to remember prevchar
            char = cardfile.read(1)
        if ( char != EOF_SIGNAL ):
            # then, char == '{'
            # start copying
            while ( (char != EOF_SIGNAL) and (char != ',') ):
                ck += char
                char = cardfile.read(1)
            ck = ck[1:] # omit the '{'
    # while ( ck[0] in WHITESPACE ):
        # ck = ck[1:]
    # while ( ck[-1] in WHITESPACE ):
        # ck = ck[:-1]
    ck = ck.strip(WHITESPACE)
    return ck

def fromCardFileToBibItem(cardfile):
    """
    cardfile : file object open in read mode containing bibliographic
    information;
    returns : BibItem object
    """
    entrytype = findEntryTypeInFile(cardfile)
    cardfile.seek(0,0)
    citationkey = findCitationKeyInFile(cardfile)
    cardfile.seek(0,0)
    bibitem = BibItem(entrytype, citationkey)
    for line in cardfile:
        line = line.strip(WHITESPACE)
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
            bibitem.setField(field, value, False)
    return bibitem

def fromPathToBibItem(pathToCard):
    cardfile = open(pathToCard, 'r')
    bibitem = fromCardFileToBibItem(cardfile)
    cardfile.close()
    assert cardfile.closed
    return bibitem

### Functions to write the information contained in a BibItem object into
### a file

def fromBibItemToCardFile(bibitem, cardfile):
    """
    bibitem : BibItem object
    cardfile : file object open in write or append mode
    """
    cardfile.write(str(bibitem))

def fromSelectedItemsToBibFile(bibitemList, bibfile):
    """
    copies the contents of various BibItem objects into bibfile without
    having to close and reopen the file;
    a bibfile contains the contents of many cardfiles
    """
    for bibitem in bibitemList:
        fromBibItemToCardFile(bibitem, bibfile)

def fromBibItemToPath(bibitem, pathToCard, mode = 'a'):
    cardfile = open(pathToCard, mode)
    fromBibItemToCardFile(bibitem, cardfile)
    cardfile.close()
    assert cardfile.closed

def fromSelectedItemsToPath(bibitemList, pathToBib, mode = 'a', \
        allAtOnce = True):
    """
    Copies the contents of the various BibItem objects in bibitemList to the
    file in pathToBib.
    If mode is set to 'a' (append), an existing file is opened in append mode
    or a new one is created.
    If mode is set to 'w' (write), the contents of an existing file are deleted
    or a new file is created.
    If allAtOnce is set to True, the path is opened and closed only once for
    the whole list.
    Otherwise, it is opened and closed for each item in the list
    """
    if ( allAtOnce ):
        bibfile = open(pathToBib, mode)
        fromSelectedItemsToBibFile(bibitemList, bibfile)
        bibfile.close()
        assert bibfile.closed
    else:
        # overwrite any existing content if mode = 'w'
        bibfile = open(pathToBib, mode)
        bibfile.close()
        for bibitem in bibitemList:
            fromBibItemToPath(bibitem, pathToBib, mode = 'a')

class RefCard(object):
    """
    this class turns out to be useless;
    keeping it, just in case
    """
    def __init__(self, filename):
        """
        filename : name of the file containing the information in the newly
        created RefCard object, must be a '.bib' file
        """
        if ( not (filename[-4:] == '.bib') ):
            raise Exception("File does not have the required '.bib' extension")
        self.location = filename
        self.bibitem = fromPathToBibItem(filename)
    def getLocation(self):
        return self.location
    def getItem(self):
        return self.bibitem


def filterPathList(pathList, pattern, matchEntryType = True, loosely = False, \
        atLeastOne = False):
    """
    pathList : list of str objects containing the locations of bib files
    pattern : BibItem object with desired details
    returns : a list containing RefCard objects matching the pattern
    """
    prospective = []
    for path in pathList:
        refcard = RefCard(path)
        item = refcard.getItem()
        # compare
        if ( item.fitsPattern(pattern, matchEntryType, loosely, atLeastOne) ):
            prospective.append(refcard)
    return prospective

def createFilter():
    """
    returns BibItem object with desired details, a pattern to match in a search
    """
    pass

def searchForMatches(pathList):
    """
    ask for input : enter the information that should be contained in the
    card;
    create filter;
    ask for input : ask whether the search should be loose, whether every field
    must be a match;
    apply filter with specified arguments;
    return list of matches
    """
    pattern = createFilter()
    if ( pattern.getEntryType() == '' ):
        matchEntryType = False
    else:
        while ( True ):
            matchEntryType = input("Match entry type to " + \
                    pattern.getEntryType() + "? (Y/n) ").lower()
            if ( matchEntryType == 'y' ):
                matchEntryType = True
                break
            elif ( matchEntryType == 'n' ):
                matchEntryType = False
                break
            else:
                print("Please enter a 'y', if you'd like to look only for " + \
                        "items matching entry type, or a 'n', if you'd " + \
                        "rather look for every possible match regardless " + \
                        "of entry type.")
    while ( True ):
        loosely = input("Should the search be made loose? (y/N) ").lower()
        if ( loosely == 'y' ):
            loosely = True
            break
        elif ( loosely == 'n' ):
            loosely = False
            break
        else:
            print("Please enter a 'y', if you'd like a loose search, " + \
                    "or a 'n', if you'd rather the results match exactly " +\
                    "the data you provided.")
    while ( True ):
        atLeastOne = input("Should every field be a match? (Y/n) ").lower()
        if ( atLeastOne == 'y' ):
            atLeastOne = True
            break
        elif ( atLeastOne == 'n' ):
            atLeastOne = False
            break
        else:
            print("Please enter a 'y', if you'd like each result to be a " + \
                    "match for at least one field, or a 'n', if you'd " + \
                    "rather every field be a match.")
    return filterPathList(pathList, pattern, matchEntryType, loosely, atLeastOne)

