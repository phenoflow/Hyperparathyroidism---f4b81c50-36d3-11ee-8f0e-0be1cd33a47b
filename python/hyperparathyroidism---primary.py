# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"C120.00","system":"readv2"},{"code":"C120000","system":"readv2"},{"code":"C120100","system":"readv2"},{"code":"C120200","system":"readv2"},{"code":"C1z3100","system":"readv2"},{"code":"Cyu4100","system":"readv2"},{"code":"K08y100","system":"readv2"},{"code":"N332500","system":"readv2"},{"code":"105537.0","system":"med"},{"code":"17339.0","system":"med"},{"code":"18740.0","system":"med"},{"code":"19457.0","system":"med"},{"code":"3559.0","system":"med"},{"code":"4116.0","system":"med"},{"code":"49456.0","system":"med"},{"code":"53819.0","system":"med"},{"code":"56524.0","system":"med"},{"code":"65478.0","system":"med"},{"code":"73923.0","system":"med"},{"code":"73934.0","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('hyperparathyroidism-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["hyperparathyroidism---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["hyperparathyroidism---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["hyperparathyroidism---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
