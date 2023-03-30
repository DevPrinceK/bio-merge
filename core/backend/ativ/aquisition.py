import requests


class GetData():
    '''
    This class gets data from various sources 
    and returns a dictionary of the data.
    '''

    def __init__(self):
        pass

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
        response = requests.get(url)
        if response.status_code == 200:
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

    def from_refseq(self):
        pass

    def from_ncbi(self):
        pass
