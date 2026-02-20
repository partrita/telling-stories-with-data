
import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.bwriter import BibTexWriter

def deduplicate_bib(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as bibtex_file:
        parser = BibTexParser(common_strings=False)
        bib_database = bibtexparser.load(bibtex_file, parser=parser)

    # Use a dictionary to keep track of seen keys
    seen_keys = set()
    unique_entries = []

    for entry in bib_database.entries:
        if entry['ID'] not in seen_keys:
            unique_entries.append(entry)
            seen_keys.add(entry['ID'])
        else:
            print(f"Skipping duplicate entry: {entry['ID']}")

    bib_database.entries = unique_entries
    
    writer = BibTexWriter()
    with open(output_file, 'w', encoding='utf-8') as bibtex_file:
        bibtexparser.dump(bib_database, bibtex_file)

if __name__ == "__main__":
    deduplicate_bib('mybook/references.bib', 'mybook/references_clean.bib')
