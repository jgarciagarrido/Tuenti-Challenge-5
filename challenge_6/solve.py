import itertools


def read_sheet(name):
    f = open(name)
    dimension = f.readline()
    rows, columns = map(lambda x: int(x), dimension.split())
    line = f.readline()
    sheet = []
    while line:
        sheet.append(map(lambda x: int(x), line.split()))
        line = f.readline()
    f.close()
    return rows, columns, sheet


def get_posible_axis_range(search_area, k):
    rows = len(search_area)
    columns = len(search_area[0])
    return itertools.product(xrange(k, rows-k), xrange(k, columns-k))


def get_pieces_quality(search_area, y, x, k):
    upper_piece = itertools.imap(lambda row: sum(row[x-k:x]), search_area[y-k:y])
    lower_piece = itertools.imap(lambda row: sum(row[x+1:x+1+k]), search_area[y+1:y+1+k])
    return sum(upper_piece) + sum(lower_piece)


def get_max_quality(sheet, y0, x0, y1, x1, k):
    search_area = map(lambda row: row[x0:x1+1], sheet[y0:y1+1])
    rows = y1+1-y0
    columns = x1+1-x0
    axis_range = itertools.product(xrange(k, rows-k), xrange(k, columns-k))
    qualities = itertools.imap(lambda axis: get_pieces_quality(search_area, axis[0], axis[1], k), axis_range)
    return max(qualities)

if __name__ == "__main__":
    rows, columns, sheet = read_sheet('sheet.data')
    cases = int(input())
    for i in xrange(cases):
        line_range = raw_input()
        y0, x0, y1, x1, k = map(lambda x: int(x), line_range.split())
        print "Case %d: %d" % (i+1, get_max_quality(sheet, y0, x0, y1, x1, k))
