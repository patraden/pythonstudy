import io
import csv


def main():
    buffer = io.StringIO()
    print(buffer.readable())
    print(buffer.writable())
    csv_writer = csv.writer(buffer, dialect=csv.excel_tab)
    print(dir(buffer))
    with open("/Users/d.patrakhin//Downloads/mlb_teams_2012.csv", mode='w+') as csv_file:
        # TextIOWrapper
        print(type(csv_file))
        print(dir(csv_file))
        print(csv_file.readable())
        print(csv_file.writable())
        print(csv_file.tell())

    # with open("/Users/d.patrakhin//Downloads/mlb_teams_2012.csv", mode='r', newline='') as csv_file:
    #     csv_reader = csv.reader(csv_file, delimiter=',', dialect=csv.excel, quotechar="\"")
    #     header = next(csv_reader)
    #     s = 0
    #     for row in csv_reader:
    #         row = list(map(lambda e: e.strip(), row))
    #         s += csv_writer.writerow(row)
    #
    # s += buffer.write("something else\r\n")
    # s += buffer.write("something else2\r\n")
    #
    # print(s)
    # print(buffer.tell())
    # buffer.seek(io.SEEK_SET)
    # print(buffer.readlines())
    # buffer.close()

    # line = buffer.readline().rstrip()
    # while line:
    #     print(line)
    #     line = buffer.readline().rstrip()


if __name__ == "__main__":
    main()
