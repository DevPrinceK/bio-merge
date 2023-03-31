from django.shortcuts import render
from django.views import View
from backend.ativ.aquisition import GetData, ReadData
from backend.models import GenBankRecord


class IndexView(View):
    template_name = 'biomerge/index.html'

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)


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

        records = read_data.from_fasta(fasta_file)
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
