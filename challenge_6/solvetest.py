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


def get_search_area(sheet, y0, x0, y1, x1):
    return map(lambda row: row[x0:x1+1], sheet[y0:y1+1])


def get_posible_axis_range(search_area, k):
    rows = len(search_area)
    columns = len(search_area[0])
    return k, k, rows-k-1, columns-k-1


def get_pieces(search_area, y, x, k):
    upper_piece = map(lambda row: row[x-k:x], search_area[y-k:y])
    lower_piece = map(lambda row: row[x+1:x+1+k], search_area[y+1:y+1+k])
    # print upper_piece
    # print lower_piece
    return upper_piece+lower_piece


def get_quality(search_area, y, x, k):
    pieces = get_pieces(search_area, y, x, k)
    return sum(map(sum, pieces))


def get_max_quality(sheet, y0, x0, y1, x1, k):
    search_area = get_search_area(sheet, y0, x0, y1, x1)
    # for row in search_area:
    #     print row
    axis_y0, axis_x0, axis_y1, axis_x1 = get_posible_axis_range(search_area, k)
    qualities = []
    for y in xrange(axis_y0, axis_y1+1):
        for x in xrange(axis_x0, axis_x1+1):
            quality = get_quality(search_area, y, x, k)
            # print y, x, quality
            qualities.append(quality)
    return max(qualities)

if __name__ == "__main__":
    rows, columns, sheet = read_sheet('sheet.data')

    cases = int(input())
    for i in xrange(cases):
        line_range = raw_input()
        y0, x0, y1, x1, k = map(lambda x: int(x), line_range.split())
        print "Case %d: %d" % (i+1, get_max_quality(sheet, y0, x0, y1, x1, k))
