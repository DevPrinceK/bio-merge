from django.db import models


class GenBankRecord(models.Model):
    accession_id = models.CharField(max_length=100, unique=True)
    organism = models.CharField(max_length=100)
    sequence_length = models.IntegerField()
    molecule_type = models.CharField(max_length=50)
    source = models.TextField()
    taxonomy = models.TextField()
    references = models.TextField()
    sequence_data = models.TextField()

    def __str__(self):
        return self.accession_id


class Gene(models.Model):
    '''schema for genes table'''
    gene_id = models.AutoField(primary_key=True, unique=True)
    gene_symbol = models.CharField(max_length=100)
    gene_name = models.CharField(max_length=300)
    organism = models.CharField(max_length=150)
    chromosome = models.CharField(max_length=50)
    start_position = models.IntegerField()
    end_position = models.IntegerField()
    strand = models.CharField(max_length=100)

    def __str__(self):
        return self.gene_name

    class Meta:
        verbose_name_plural = "Genes"


class Transcript(models.Model):
    '''schema for the transcript table'''
    transcript_id = models.AutoField(primary_key=True, unique=True)
    gene_id = models.ForeignKey(Gene, on_delete=models.CASCADE)
    transcript_name = models.CharField(max_length=200)
    transcript_type = models.CharField(max_length=100)
    exon_count = models.IntegerField()

    def __str__(self):
        return self.transcript_name

    class Meta:
        verbose_name_plural = "Transcripts"


class Protein(models.Model):
    '''Schema for the protein table'''
    protein_id = models.AutoField(primary_key=True, unique=True)
    uniprot_id = models.CharField(max_length=100)
    gene_id = models.ForeignKey(Gene, on_delete=models.CASCADE, null=True, blank=True)  # noqa
    protein_name = models.CharField(max_length=200)
    protein_sequence = models.TextField()
    molecular_weight = models.FloatField()
    function = models.TextField()
    cellular_location = models.TextField()
    pdb_id = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.protein_name

    class Meta:
        verbose_name_plural = "Proteins"


class ProteinStructure(models.Model):
    '''schema for the protein structure table'''
    pdb_id = models.AutoField(primary_key=True, unique=True)
    structure_name = models.CharField(max_length=200)
    structure_resolution = models.FloatField()
    structure_method = models.CharField(max_length=100)
    structure_date = models.DateField()

    def __str__(self):
        return self.structure_name

    class Meta:
        verbose_name_plural = "ProteinStructures"


class ProteinInteraction(models.Model):
    '''schema for the protein interaction table'''
    interaction_id = models.AutoField(primary_key=True, unique=True)
    protein_id1 = models.ForeignKey(Protein, on_delete=models.CASCADE, null=True, related_name='first_protein')  # noqa
    protein_id2 = models.ForeignKey(Protein, on_delete=models.CASCADE, null=True, related_name='second_protein')  # noqa
    interaction_type = models.CharField(max_length=500, null=True, blank=True)
    confidence_score = models.FloatField()
    data_source = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.interaction_id

    class Meta:
        verbose_name_plural = "ProteinInteractions"


class Pathway(models.Model):
    '''schema for the pathway table'''
    pathway_id = models.AutoField(primary_key=True, unique=True)
    pathway_name = models.CharField(max_length=200)
    pathway_description = models.CharField(max_length=500)

    def __str__(self):
        return self.pathway_name

    class Meta:
        verbose_name_plural = "Pathways"


class ProteinPathway(models.Model):
    '''schema for the protein pathway table'''
    protein_pathway_id = models.AutoField(primary_key=True, unique=True)
    pathway_id = models.ForeignKey(Pathway, on_delete=models.CASCADE, null=True)  # noqa
    protein_id = models.ForeignKey(Protein, on_delete=models.CASCADE, null=True)  # noqa

    def __str__(self):
        return self.protein_pathway_id

    class Meta:
        verbose_name_plural = "ProteinPathways"


class Disease(models.Model):
    '''schema for the disease table'''
    disease_id = models.AutoField(primary_key=True, unique=True)
    disease_name = models.CharField(max_length=300)
    disease_type = models.CharField(max_length=100)
    omim_id = models.CharField(max_length=50)

    def __str__(self):
        return self.disease_name

    class Meta:
        verbose_name_plural = "Diseases"


class GeneDiseaseAssociation(models.Model):
    '''schema for the gene disease association table'''
    gene_id = models.ForeignKey(Gene, on_delete=models.CASCADE)
    disease_id = models.ForeignKey(Disease, on_delete=models.CASCADE)
    association_type = models.CharField(max_length=100)
    evidence_source = models.CharField(max_length=500)

    def __str__(self):
        return self.association_type

    class Meta:
        verbose_name_plural = "GeneDiseaseAssociations"


class Publication(models.Model):
    '''schema for the publication table'''
    publication_id = models.AutoField(primary_key=True, unique=True)
    title = models.CharField(max_length=400)
    authors = models.CharField(max_length=1024)
    journal = models.TextField()
    publication_date = models.DateField()
    pubmed_id = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Publications"


class GenePublication(models.Model):
    '''schema for the gene publication table'''
    gene_publication_id = models.AutoField(primary_key=True, unique=True)  # noqa
    gene_id = models.ForeignKey(Gene, on_delete=models.CASCADE)
    publication_id = models.ForeignKey(Publication, on_delete=models.CASCADE)  # noqa

    def __str__(self):
        return self.gene_publication_id

    class Meta:
        verbose_name_plural = "GenePublications"


class ProteinPublication(models.Model):
    '''schema for the protein publication table'''
    protein_publication_id = models.AutoField(primary_key=True, unique=True)  # noqa
    protein_id = models.ForeignKey(Protein, on_delete=models.CASCADE)
    publication_id = models.ForeignKey(Publication, on_delete=models.CASCADE)  # noqa

    def __str__(self):
        return self.gene_publication_id

    class Meta:
        verbose_name_plural = "GenePublications"
