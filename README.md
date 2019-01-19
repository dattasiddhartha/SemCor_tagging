# SemCor Tagging

Adj, n, v, r_senses are the input files

For reference, the logic of the codebase is as follows:

dictionary_parser_fixed.py runs a script to generate a dictionary (and exports into a json file) with each word labelled with a corresponding sentence from SemCor - we go through every sentence in SemCor, generate a set of words, and assign indices for each sentence. 

SemCoring-fixed.ipynb generates all the senses that exist in WordNet, then searches for each word in the json file from above, then checks each sentence for that word based on the index; if the sense of the word in the sentence matches the WordNET sense required, then we assign that sentence to the WordNET sense, and generate a dataframe of all the senses with their corresponding SemCor example sentence. The csv output is cdi_semcored_v3.csv .
