from django.shortcuts import render
from django.views import View
from backend.ativ.aquisition import GetData, ReadData
from backend.models import GenBankRecord, DataFile
import os
from django.db.models import Q
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


class IndexView(View):
    template_name = 'biomerge/index.html'

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)


class GeneralSearch(View):
    '''CBV for searching sequences'''

    template = 'biomerge/index.html'

    def get(self, request, *args, **kwargs):
        search_term = request.GET.get('query')
        results = GenBankRecord.objects.filter(
            Q(accession_id__icontains=search_term) |
            Q(organism__icontains=search_term) |
            Q(molecule_type__icontains=search_term) |
            Q(taxonomy__icontains=search_term) |
            Q(references__icontains=search_term) |
            Q(sequence_data__icontains=search_term) |
            Q(source__icontains=search_term)
        ).order_by('-id')
        context = {
            'results': results,
            'query': search_term,
            'total_results': results.count(),
            'search': True,
        }
        return render(request, self.template, context)


class UpdateDBSelectionView(View):
    template_name = 'biomerge/db_update_selection.html'

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)


class LoadDataView(View):
    template_name1 = 'biomerge/load_from_api.html'
    template_name2 = 'biomerge/load_from_file.html'

    def get(self, request, *args, **kwargs):
        load_type = str(request.GET.get('load_type'))
        print(load_type, type(load_type))
        if load_type == 'api':
            template = self.template_name1
        elif load_type == 'file':
            template = self.template_name2
        else:
            template = self.template_name1
        context = {}
        return render(request, template, context)


class APIResultsView(View):
    template_name = 'biomerge/api_results.html'

    def get(self, request, *args, **kwargs):
        query = request.GET.get('query') or 'U12345'
        db_name = request.GET.get('db_name') or 'genbank'
        get_data = GetData()
        record = get_data.from_genbank(query)
        data = GenBankRecord.objects.filter(accession_id=query).first()
        results_message = {}
        if data is not None:
            results_message = f'Record ({record.id}) Already In Database'
            return render(request, self.template_name, {"results_message": results_message})
        if record is not None:
            # record = record.__dict__
            molecule_type = record.annotations.get('molecule_type', '')
            source = record.features[0].qualifiers.get(
                'isolation_source', [''])[0]
            taxonomy = '; '.join(record.annotations['taxonomy'])
            references = '\n'.join([str(ref)
                                   for ref in record.annotations['references']])
            try:
                genbank_record = GenBankRecord(
                    accession_id=record.id,
                    organism=record.annotations['organism'],
                    sequence_length=len(record.seq),
                    molecule_type=molecule_type,
                    source=source,
                    taxonomy=taxonomy,
                    references=references,
                    sequence_data=str(record.seq)
                )
                genbank_record.save()
            except Exception as e:
                print(e)
                print('Error saving record to database')
                results_message = f'Error saving record ({record.id}) to database'
            else:
                print('Record saved to database')
                results_message = f'Record ({record.id}) saved to database'

        context = {
            'results_message': results_message
        }
        return render(request, self.template_name, context)


class FileResultsView(View):
    template_name = 'biomerge/file_results.html'

    def get(self, request, *args, **kwargs):
        read_data = ReadData()
        fasta_file = request.GET.get('fasta_file')
        # file_path = os.path.join(BASE_DIR, 'upload', fasta_file)
        file = DataFile.objects.create(file=fasta_file)

        records = read_data.from_fasta(file.get_file_path())
        for seq_record in records:
            if '|' in seq_record.id:
                accession_id = seq_record.id.split('|')[1]
            else:
                accession_id = seq_record.id

            # get data from genank
            record = get_data.from_genbank(accession_id)
            if record is not None:
                # record = record.__dict__
                molecule_type = record.annotations.get('molecule_type', '')
                source = record.features[0].qualifiers.get(
                    'isolation_source', [''])[0]
                taxonomy = '; '.join(record.annotations['taxonomy'])
                references = '\n'.join([str(ref)
                                        for ref in record.annotations['references']])
                try:
                    genbank_record = GenBankRecord(
                        accession_id=record.id,
                        organism=record.annotations['organism'],
                        sequence_length=len(record.seq),
                        molecule_type=molecule_type,
                        source=source,
                        taxonomy=taxonomy,
                        references=references,
                        sequence_data=str(record.seq)
                    )
                    genbank_record.save()
                except Exception as e:
                    print(e)
                    print('Error saving record to database')
                    results_message = f'Error saving record ({record.id}) to database'
                else:
                    print('Record saved to database')
                    results_message = f'Record ({record.id}) saved to database'

        context = {
            'results_message': results_message,
        }
        return render(request, self.template_name, context)


class DisplaySequenceView(View):
    template_name = 'biomerge/display_results.html'

    def get(self, request, *args, **kwargs):
        accession_id = request.GET.get('accession_id')
        seq = GenBankRecord.objects.filter(accession_id=accession_id).first()
        context = {
            'seq':seq,
        }
        return render(request, self.template_name, context)