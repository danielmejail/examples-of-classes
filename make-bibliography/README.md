# make-bibliography

A utility to process '.bib' files.

The goal was to create a programme which would take in a list of objects, each
containing the information on a single bibliographic reference (paths to
various '.bib' files, or, alternatively, other objects containing the same
information), in other words, a 'reference card', and output a single file
containing the information in all of those files (or objects). Alternatively,
information can be appended to an existing bibliography.

In order for this programme to be useful, one would have to be able to
construct such a list. This is accomplished by a search utility. This auxiliary
programme asks for input in order to create a pattern with which it could then
filter an existing index of '.bib' (or other) files and return a list of
objects with information matching the one provided by the user. A manual
selection, with the aid of an interface, is then performed among these
provisional results. Once an item has been chosen, the item is added to the
list of references which would end up in the final bibliography. After this is
done, either another search is performed or the search process ends. 
