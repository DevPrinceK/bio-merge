import pandas as pd

class MergeData():
    '''
    Class for merging gene and protein data 
    to avoid duplication of data - anti-redundancy
    '''
    def __init__(self, gene_data, protein_data):
        self.gene_data = gene_data
        self.protein_data = protein_data

    def merge(self):
        gene_df = pd.DataFrame(self.gene_data)
        protein_df = pd.DataFrame(self.protein_data)
        integrated_df = gene_df.merge(protein_df, on="uniprot_id")
        return integrated_df

# Sample data gene data
gene_data = {
    "gene_id": ["gene1", "gene2", "gene3"],
    "uniprot_id": ["P12345", "P23456", "P34567"],
}

# sample protein data
protein_data = {
    "uniprot_id": ["P12345", "P23456", "P34567"],
    "protein_name": ["Protein1", "Protein2", "Protein3"],
}
