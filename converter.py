#! /usr/bin/python
import sys
import csv

def parse_csv(filename):
    ret = []
    with open(sys.argv[1], 'rb') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            if len(row) != 7 or row[0] == '':
                continue
            ret.append({
                'date': row[0],
                'description': row[1],
                'amount': float(row[2]) * -1,
            })
    return ret

def generate_qif(parsed, filename):
    with open(filename, 'w') as f:
        f.write('!Type:CCard\n')
        for elem in parsed:
            amount = str(elem['amount'])
            if elem['amount'] > 0:
                amount = '+' + amount

            f.write('D' + elem['date'] + '\n')
            f.write('T' + amount + '\n')
            f.write('P' + unicode(elem['description'], 'ShiftJIS').encode('utf-8') + '\n')
            f.write('^\n')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'Invalid argument'
        sys.exit(1)

    parsed = parse_csv(sys.argv[1])
    generate_qif(parsed, 'output.qif')
