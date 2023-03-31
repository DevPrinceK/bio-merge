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
        sample_url = "https://data.rcsb.org/rest/v1/core/entry/1a0a"
        response = requests.get(sample_url)
        # print(response)
        return response.json()
        # if response.status_code == 200:
        #     data = response.json()
        #     return data

        #     # Extract the metadata
        #     # structure_id = data["id"]
        #     # structure_title = data["rcsb_entry_info"]["title"]
        #     # structure_resolution = data["rcsb_entry_info"]["resolution_combined"]
        #     # num_atoms = data["rcsb_entry_info"]["polymer_entity_count"]["atom"]
        # else:
        #     print(f"Request failed with status code {response.status_code}")
        #     return None

    def from_refseq(self):
        
        pass


    def from_ncbi(query, organism="Homo sapiens", rettype="fasta", retmax=10):
        base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
        db = "nucleotide"
        term = organism + "[organism] AND RefSeq[filter] AND " + query

        # construct the search URL
        search_url = base_url + "esearch.fcgi?db=" + \
            db + "&term=" + term + "&retmax=" + str(retmax)

        # send the request and get the response
        response = requests.get(search_url)

        # extract the list of IDs from the response
        id_list = response.json()["esearchresult"]["idlist"]

        # convert the ID list to a comma-separated string
        id_string = ",".join(id_list)

        # construct the retrieval URL
        retrieve_url = base_url + "efetch.fcgi?db=" + \
            db + "&id=" + id_string + "&rettype=" + rettype

        # send the request and get the response
        response = requests.get(retrieve_url)

        # split the response into individual FASTA sequences
        fasta_list = response.text.split(">")[1:]

        # format the FASTA sequences and return as a list
        return [">" + fasta.strip() for fasta in fasta_list]

    
