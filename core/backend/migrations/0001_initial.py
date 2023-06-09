# Generated by Django 4.1.7 on 2023-03-30 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Disease",
            fields=[
                (
                    "disease_id",
                    models.AutoField(primary_key=True, serialize=False, unique=True),
                ),
                ("disease_name", models.CharField(max_length=300)),
                ("disease_type", models.CharField(max_length=100)),
                ("omim_id", models.CharField(max_length=50)),
            ],
            options={
                "verbose_name_plural": "Diseases",
            },
        ),
        migrations.CreateModel(
            name="Gene",
            fields=[
                (
                    "gene_id",
                    models.AutoField(primary_key=True, serialize=False, unique=True),
                ),
                ("gene_symbol", models.CharField(max_length=100)),
                ("gene_name", models.CharField(max_length=300)),
                ("organism", models.CharField(max_length=150)),
                ("chromosome", models.CharField(max_length=50)),
                ("start_position", models.IntegerField()),
                ("end_position", models.IntegerField()),
                ("strand", models.CharField(max_length=100)),
            ],
            options={
                "verbose_name_plural": "Genes",
            },
        ),
        migrations.CreateModel(
            name="Pathway",
            fields=[
                (
                    "pathway_id",
                    models.AutoField(primary_key=True, serialize=False, unique=True),
                ),
                ("pathway_name", models.CharField(max_length=200)),
                ("pathway_description", models.CharField(max_length=500)),
            ],
            options={
                "verbose_name_plural": "Pathways",
            },
        ),
        migrations.CreateModel(
            name="Protein",
            fields=[
                (
                    "protein_id",
                    models.AutoField(primary_key=True, serialize=False, unique=True),
                ),
                ("uniprot_id", models.CharField(max_length=100)),
                ("protein_name", models.CharField(max_length=200)),
                ("protein_sequence", models.TextField()),
                ("molecular_weight", models.FloatField()),
                ("function", models.TextField()),
                ("cellular_location", models.TextField()),
                ("pdb_id", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "gene_id",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="backend.gene",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Proteins",
            },
        ),
        migrations.CreateModel(
            name="ProteinStructure",
            fields=[
                (
                    "pdb_id",
                    models.AutoField(primary_key=True, serialize=False, unique=True),
                ),
                ("structure_name", models.CharField(max_length=200)),
                ("structure_resolution", models.FloatField()),
                ("structure_method", models.CharField(max_length=100)),
                ("structure_date", models.DateField()),
            ],
            options={
                "verbose_name_plural": "ProteinStructures",
            },
        ),
        migrations.CreateModel(
            name="Publication",
            fields=[
                (
                    "publication_id",
                    models.AutoField(primary_key=True, serialize=False, unique=True),
                ),
                ("title", models.CharField(max_length=400)),
                ("authors", models.CharField(max_length=1024)),
                ("journal", models.TextField()),
                ("publication_date", models.DateField()),
                ("pubmed_id", models.CharField(max_length=100)),
            ],
            options={
                "verbose_name_plural": "Publications",
            },
        ),
        migrations.CreateModel(
            name="Transcript",
            fields=[
                (
                    "transcript_id",
                    models.AutoField(primary_key=True, serialize=False, unique=True),
                ),
                ("transcript_name", models.CharField(max_length=200)),
                ("transcript_type", models.CharField(max_length=100)),
                ("exon_count", models.IntegerField()),
                (
                    "gene_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="backend.gene"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Transcripts",
            },
        ),
        migrations.CreateModel(
            name="ProteinPublication",
            fields=[
                (
                    "protein_publication_id",
                    models.AutoField(primary_key=True, serialize=False, unique=True),
                ),
                (
                    "protein_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="backend.protein",
                    ),
                ),
                (
                    "publication_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="backend.publication",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "GenePublications",
            },
        ),
        migrations.CreateModel(
            name="ProteinPathway",
            fields=[
                (
                    "protein_pathway_id",
                    models.AutoField(primary_key=True, serialize=False, unique=True),
                ),
                (
                    "pathway_id",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="backend.pathway",
                    ),
                ),
                (
                    "protein_id",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="backend.protein",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "ProteinPathways",
            },
        ),
        migrations.CreateModel(
            name="ProteinInteraction",
            fields=[
                (
                    "interaction_id",
                    models.AutoField(primary_key=True, serialize=False, unique=True),
                ),
                (
                    "interaction_type",
                    models.CharField(blank=True, max_length=500, null=True),
                ),
                ("confidence_score", models.FloatField()),
                (
                    "data_source",
                    models.CharField(blank=True, max_length=500, null=True),
                ),
                (
                    "protein_id1",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="first_protein",
                        to="backend.protein",
                    ),
                ),
                (
                    "protein_id2",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="second_protein",
                        to="backend.protein",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "ProteinInteractions",
            },
        ),
        migrations.CreateModel(
            name="GenePublication",
            fields=[
                (
                    "gene_publication_id",
                    models.AutoField(primary_key=True, serialize=False, unique=True),
                ),
                (
                    "gene_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="backend.gene"
                    ),
                ),
                (
                    "publication_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="backend.publication",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "GenePublications",
            },
        ),
        migrations.CreateModel(
            name="GeneDiseaseAssociation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("association_type", models.CharField(max_length=100)),
                ("evidence_source", models.CharField(max_length=500)),
                (
                    "disease_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="backend.disease",
                    ),
                ),
                (
                    "gene_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="backend.gene"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "GeneDiseaseAssociations",
            },
        ),
    ]
