from chemical.models import ChemicalItem

with open('./chemical/chem_invent.tsv', 'r') as f:
    for line in f.readlines():
        if line[0] == '\t':
            # empty line
            continue
        fields = line.split('\t')
        if fields[0] == 'Chemical Name':
            # header line
            continue
        if len(fields) < 9:
            # This line doesn't have enough fields
            print('Not enough fields')
            continue
        # actual reading data
        chemical_name = fields[0]
        storage_location = fields[1]
        quantity = fields[2].replace(',', '')
        unit = fields[3]
        company_name = fields[4]
        catalog_number = fields[5]
        # currently use manual input date time
        # because it's hard to parse and deal with N/A
        order_date = ""
        expiration_date = ""
        comment = fields[8]

        # p
        try:
            q = ChemicalItem(chemical_name=chemical_name, storage_location=storage_location,
                             quantity=quantity, unit=unit, company_name=company_name,
                             catalog_number=catalog_number, comment=comment)
            q.save()
        except:
            print(chemical_name)
