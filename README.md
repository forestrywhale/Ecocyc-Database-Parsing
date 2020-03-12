# Ecocyc-Database-Parsing
Helpful functions for parsing EcoCyc Database file.

EcoCyc is a heavy curated scientific database for the bacterium Escherichia coli K-12 MG1655. The EcoCyc project performs literature-based curation of its genome, and of transcriptional regulation, transporters, and metabolic pathways.

Database link: https://ecocyc.org/

This repository is aiming at facilitating database analysis with Python. Mainly, the function read database files into a pandas.DataFrame. The database file formats can be found here: http://brg.ai.sri.com/ptools/flatfile-format.html

To install the package:

    pip install Ecocyc-Parse

To import the package:

    import Ecocyc_Parse as ep
