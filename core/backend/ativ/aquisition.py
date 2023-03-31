import requests
from Bio import SeqIO, Entrez
from Bio.PDB import PDBParser


class ReadData():
    '''Class for reading data from local files'''

    def __init__(self):
        pass

    def from_fasta(self, fasta_file):
        # reads data from fasta file
        records = SeqIO.parse(fasta_file, "fasta")
        return records

    def from_pdb(self, pdb_file):
        # reads data from pdb file
        parser = PDBParser()
        structure = parser.get_structure("structure", pdb_file)
        return structure


class GetData():
    '''
    This class gets data from various online sources
    '''

    def __init__(self):
        pass

    def from_genbank(self, accession_id):
        # gets data from genbank
        # Set the email address to use for accessing NCBI's servers
        Entrez.email = "default@example.com"

        # Use the Entrez.efetch() function again to retrieve the record in GenBank format
        try:
            handle = Entrez.efetch(
                db="nucleotide", id=accession_id, rettype="gb", retmode="text")
        except Exception as e:
            print(e)
            print('Error retrieving record from GenBank')
            return None
        else:
            record = SeqIO.read(handle, "genbank")
            handle.close()
        return record

    def from_pubmed(self, genbank_record):
        # Set the email address to use for accessing NCBI's servers
        Entrez.email = "default@example.com"

        # Extract the PubMed IDs associated with the GenBank record
        pubmed_ids = [
            ref.pubmed_id for ref in genbank_record.annotations['references']]

        # Use the Entrez.efetch() function to retrieve the PubMed records
        handle = Entrez.efetch(db="pubmed", id=pubmed_ids,
                               rettype="medline", retmode="text")
        records = Medline.parse(handle)
        handle.close()

        return list(records)

    def from_uniprot(self, uniprot_id, format='fasta'):
        # gets data from uniprot - default is fasta
        base_url = "https://www.uniprot.org/uniprot/"
        response = requests.get(base_url + uniprot_id + "." + format)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Error downloading data for UniProt ID {uniprot_id}")
            return None

    def from_pdb(self, pdb_id):
        base = "https://data.rcsb.org/rest/v1/core/entry/"
        url = f"{base}/{pdb_id}"

        # get the data
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the response JSON data
            data = response.json()
            return data

            # Extract the metadata
            # structure_id = data["id"]
            # structure_title = data["rcsb_entry_info"]["title"]
            # structure_resolution = data["rcsb_entry_info"]["resolution_combined"]
            # num_atoms = data["rcsb_entry_info"]["polymer_entity_count"]["atom"]
        else:
            print(f"Request failed with status code {response.status_code}")
            return None
