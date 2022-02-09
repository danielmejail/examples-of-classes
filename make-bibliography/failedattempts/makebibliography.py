
class BibItem(object):
    entryTypes = ["article", "book", "booklet", "conference", "inbook", \
            "incollection", "inproceedings", "manual", "masterthesis", \
            "misc", "phdthesis", "proceedings", "techreport", "unpublished"]
    def __init__(self, entrytype, citationkey):
        if ( not(entrytype in BibItem.entryTypes) ):
            raise AttributeError("There is no entry type named " + \
                    entrytype)
        self.entrytype = entrytype
        self.citationkey = citationkey
    def getEntryType(self):
        return self.entrytype
    def getCitationKey(self):
        return self.citationkey

class HasAttrItem(object):
    """
    This class groups the Has* objects
    """

class HasAuthorItem(HasAttrItem):
    def __init__(self, author = ''):
        self.author = author
    def getAuthor(self):
        return self.author
    def setAuthor(self, author):
        self.author = author

class HasTitleItem(HasAttrItem):
    def __init__(self, title = ''):
        self.title = title
    def getTitle(self):
        return self.title
    def setTitle(self, title):
        self.title = title

class HasYearItem(HasAttrItem):
    def __init__(self, year = None):
        self.year = year
    def getYear(self):
        return self.year
    def setYear(self, year):
        self.year = year

class HasJournalItem(HasAttrItem):
    def __init__(self, journal = ''):
        self.journal = journal
    def getJournal(self):
        return self.journal
    def setJournal(self, journal):
        self.journal = journal

class HasVolumeItem(HasAttrItem):
    def __init__(self, volume = ''):
        self.volume = volume
    def getVolume(self):
        return self.volume
    def setVolume(self, volume):
        self.volume = volume

class HasNumberItem(HasAttrItem):
    def __init__(self, number = ''):
        self.number = number
    def getNumber(self):
        return self.number
    def setNumber(self, number):
        self.number = number

class HasPagesItem(HasAttrItem):
    def __init__(self, pages = ''):
        self.pages = pages
    def getPages(self):
        return self.pages
    def setPages(self, pages):
        self.pages = pages

class HasPublisherItem(HasAttrItem):
    def __init__(self, publisher = ''):
        self.publisher = publisher
    def getPublisher(self):
        return self.publisher
    def setPublisher(self, publisher):
        self.publisher = publisher

class HasAddressItem(HasAttrItem):
    def __init__(self, address = ''):
        self.address = address
    def getAddress(self):
        return self.address
    def setAddress(self, address):
        self.address = address

class HasHowpublishedItem(HasAttrItem):
    def __init__(self, howpublished = ''):
        self.howpublished = howpublished
    def getHowpublished(self):
        return self.howpublished
    def setHowpublished(self, howpublished):
        self.howpublished = howpublished

class HasMonthItem(HasAttrItem):
    def __init__(self, month = None):
        self.month = month
    def getMonth(self):
        return self.month
    def setMonth(self, month):
        self.month = month

class HasBooktitleItem(HasAttrItem):
    def __init__(self, booktitle = ''):
        self.booktitle = booktitle
    def getBooktitle(self):
        return self.booktitle
    def setBooktitle(self, booktitle):
        self.booktitle = booktitle

class HasEditorItem(HasAttrItem):
    def __init__(self, editor = ''):
        self.editor = editor
    def getEditor(self):
        return self.editor
    def setEditor(self, editor):
        self.editor = editor

class HasSeriesItem(HasAttrItem):
    def __init__(self, series = ''):
        self.series = series
    def getSeries(self):
        return self.series
    def setSeries(self, series):
        self.series = series

class HasOrganisationItem(HasAttrItem):
    def __init__(self, organisation = ''):
        self.organisation = organisation
    def getOrganisation(self):
        return self.organisation
    def setOrganisation(self, organisation):
        self.organisation = organisation

class HasSchoolItem(HasAttrItem):
    def __init__(self, school = ''):
        self.school = school
    def getSchool(self):
        return self.school
    def setSchool(self, school):
        self.school = school

class HasInstitutionItem(HasAttrItem):
    def __init__(self, institution = ''):
        self.institution = institution
    def getInstitution(self):
        return self.institution
    def setInstitution(self, institution):
        self.institution = institution

class HasNoteItem(HasAttrItem):
    def __init__(self, note = ''):
        self.note = note
    def getNote(self):
        return self.note
    def setNote(self, note):
        self.note = note

class BindedItem(BibItem, HasTitleItem, HasYearItem, HasPublisherItem, \
        HasAddressItem):
    """ superclass for book and proceedings """
    def __init__(self, entrytype, citationkey, title = '', year = None, \
            publisher = '', address = ''):
        BibItem.__init__(self, entrytype, citationkey)
        HasTitleItem.__init__(self, title)
        HasYearItem.__init__(self, year)
        HasPublisherItem.__init__(self, publisher)
        HasAddressItem.__init__(self, address)

class InBindedItem(BibItem, HasAuthorItem, HasTitleItem, HasYearItem, \
        HasPublisherItem, HasAddressItem, HasPagesItem, HasBooktitleItem):
    def __init__(self, entrytype, citationkey, author = '', title = '', \
            year = None, publisher = '', address = '', pages = '', \
            booktitle = ''):
        BibItem.__init(self, entrytype, citationkey)
        HasAuthorItem.__init(self, author)
        HasTitleItem.__init(self, title)
        HasYearItem.__init(self, year)
        HasPublisherItem.__init(self, publisher)
        HasAddressItem.__init(self, address)
        HasPagesItem.__init(self, pages)
        HasBooktitleItem.__init(self, booktitle)

class ThesisItem(BibItem, HasAuthorItem, HasTitleItem, HasSchoolItem, \
        HasYearItem, HasAddressItem, HasMonthItem):
    def __init__(self, entrytype, citationkey, author = '', title = '', \
            school = '', year = None, address = '', month = None):
        BibItem.__init(self, entrtype, citationkey)
        HasAuthorItem.__init(self, author)
        HasTitleItem.__init(self, title)
        HasSchoolItem.__init(self, school)
        HasYearItem.__init(self, year)
        HasAddressItem.__init(self, address)
        HasMonthItem.__init(self, month)

class ArticleItem(BibItem, HasAuthorItem, HasTitleItem, HasYearItem, \
        HasJournalItem, HasVolumeItem, HasNumberItem, HasPagesItem):
    def __init__(self, citationkey, author = '', title = '', journal = '', \
            year = None, volume = '', number = '', pages = ''):
        BibItem.__init__(self, "article", citationkey)
        HasAuthorItem.__init__(self, author)
        HasTitleItem.__init__(self, title)
        HasYearItem.__init__(self, year)
        HasJournalItem.__init__(self, journal)
        HasVolumeItem.__init__(self, volume)
        HasNumberItem.__init__(self, number)
        HasPagesItem.__init__(self, pages)

class BookItem(BindedItem, HasAuthorItem):
    def __init__(self, citationkey, author = '', title = '', publisher = '', \
            address = '', year = None):
        BindedItem.__init__(self, "book", citationkey, title, year, \
                publisher, address)
        HasAuthorItem.__init__(self, author)

class BookletItem(BibItem, HasAuthorItem, HasTitleItem, HasYearItem, \
        HasHowpublishedItem, HasMonthItem):
    def __init__(self, citationkey, title = '', author = '', \
            howpublished = '', month = None, year = None):
        BibItem.__init__(self, "booklet", citationkey)
        HasAuthorItem.__init__(self, author)
        HasTitleItem.__init__(self, title)
        HasYearItem.__init__(self, year)
        HasHowpublishedItem.__init__(self, howpublished)
        HasMonthItem.__init__(self, month)

class ConferenceItem(InBindedItem, HasSeriesItem):
    def __init__(self, citationkey, author = '', title = '', booktitle = '', \
            series = '', year = None, pages = '', publisher = '', \
            address = ''):
        InBindedItem.__init__(self, "conference", citationkey, author, title, \
                year, publisher, address, pages, booktitle)
        HasSeriesItem.__init__(self, series)

class InBookItem(InBindedItem):
    def __init__(self, citationkey, author = '', title = '', booktitle = '', \
            year = None, publisher = '', address = '', pages = ''):
        InBindedItem.__init__(self, "inbook", citationkey, author, title, \
                year, publisher, address, pages, booktitle)

class InCollectionItem(InBindedItem, HasEditorItem):
    def __init__(self, citationkey, author = '', editor = '', title = '', \
            booktitle = '', year = None, publisher = '', address = '', \
            pages = ''):
        InBindedItem.__init__(self, "incollection", citationkey, author, \
                title, year, publisher, address, pages, booktitle)
        HasEditorItem.__init__(self, editor)

class InProceedingsItem(InBindedItem, HasSeriesItem):
    def __init__(self, citationkey, author = '', title = '', booktitle = '', \
            series = '', year = None, pages = '', publisher = '', \
            address = ''):
        InBindedItem.__init__(self, "inproceedings", citationkey, author, \
                title, year, publisher, address, pages, booktitle)
        HasSeriesItem.__init__(self, series)

class ManualItem(BibItem, HasTitleItem, HasAuthorItem, HasOrganisationItem, \
        HasAddressItem, HasYearItem):
    def __init__(self, citationkey, title = '', author = '', \
            organisation = '', address = '', year = None):
        BibItem.__init__(self, "manual", citationkey)
        HasTitleItem.__init__(self, title)
        HasAuthorItem.__init__(self, author)
        HasOrganisationItem.__init__(self, organisation)
        HasAddressItem.__init__(self, address)
        HasYearItem.__init__(self, year)

class MasterThesisItem(ThesisItem):
    def __init__(self, citationkey, author = '', title = '', school = '', \
            year = None, address = '', month = None):
        ThesisItem.__init__(self, "masterthesis", citationkey, author, title, \
                school, year, address, month)

class PhDThesisItem(ThesisItem):
    def __init__(self, citationkey, author = '', title = '', school = '', \
            address = '', year = None, month = None):
        ThesisItem.__init__(self, "phdthesis", citationkey, author, title, \
                school, year, address, month)

class MiscItem(BibItem, HasTitleItem, HasAuthorItem, HasHowpublishedItem, \
        HasYearItem, HasNoteItem):
    def __init__(self, citationkey, title = '', author = '', \
            howpublished = '', year = None, note = ''):
        BibItem.__init__(self, "misc", citationkey)
        HasTitleItem.__init__(self, title)
        HasAuthorItem.__init__(self, author)
        HasHowpublishedItem.__init__(self, howpublished)
        HasYearItem.__init__(self, year)
        HasNoteItem.__init__(self, note)

class ProceedingsItem(BindedItem, HasEditorItem, HasSeriesItem, \
        HasVolumeItem):
    def __init__(self, citationkey, editor = '', title = '', series = '', \
            volume = '', publisher = '', address = '', year = None):
        BindedItem.__init__(self, "proceedings", citationkey, title, year, \
                publisher, address)
        HasEditorItem.__init__(self, editor)
        HasSeriesItem.__init__(self, series)
        HasVolumeItem.__init__(self, volume)

class TechReportItem(BibItem, HasTitleItem, HasAuthorItem, \
        HasInstitutionItem, HasAddressItem, HasNumberItem, HasYearItem, \
        HasMonthItem):
    """ this could be grouped together with manual """
    def __init__(self, citationkey, title = '', author = '', \
            institution = '', address = '', number = '', year = None, \
            month = None):
        BibItem.__init__(self, "techreport", citationkey)
        HasTitleItem.__init__(self, title)
        HasAuthorItem.__init__(self, author)
        HasInstitutionItem.__init__(self, institution)
        HasAddressItem.__init__(self, address)
        HasNumberItem.__init__(self, number)
        HasYearItem.__init__(self, year)
        HasMonthItem.__init__(self, month)

class UnpublishedItem(BibItem, HasAuthorItem, HasTitleItem, HasYearItem):
    def __init__(self, citationkey, author = '', title = '', year = None):
        BibItem.__init__(self, "unpublished", citationkey)
        HasAuthorItem.__init__(self, author)
        HasTitleItem.__init__(self, title)
        HasYearItem.__init__(self, year)

