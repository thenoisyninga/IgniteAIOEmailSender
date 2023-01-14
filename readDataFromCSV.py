def get_data(filename):
    import csv

    sheet_cells = []

    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            sheet_cells.append(row)

    data_dictionary = {}

    num_of_categories = len(sheet_cells[0])
    num_of_delegates = len(sheet_cells) - 1

    for i in range(num_of_categories):
        data_dictionary[sheet_cells[0][i]] = []
        for j in range(num_of_delegates):
            data_dictionary[sheet_cells[0][i]].append(sheet_cells[j + 1][i])

    num_of_delegations = int(num_of_delegates / 4)

    return data_dictionary, num_of_delegates, num_of_delegations

