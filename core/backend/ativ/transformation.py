from Bio import SeqIO
from io import StringIO


class DataParser():
    '''
    Class for parsing data from a string 
    into a list of SeqRecord objects
    '''

    def parse_fasta(self, fasta_data):
        # parse the fasta data into a list of SeqRecord objects
        fasta_io = StringIO(fasta_data)
        records = list(SeqIO.parse(fasta_io, "fasta"))
        return records

    def parse_pdb(self):
        # parse the pdb data into a list of SeqRecord objects
        


# fasta_data = download_uniprot_data(uniprot_id)
# parsed_records = parse_fasta_data(fasta_data)
# for record in parsed_records:
#     print(record.id, record.description, record.seq)
