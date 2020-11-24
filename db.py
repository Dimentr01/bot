import pymysql


conn = pymysql.connect(host='localhost',
                       database='onepunchman',
                       user='root', #dimentrx
                       password='aH$2ucutROA1',
                       )
cursor = conn.cursor()


def part_of_search_similar_photo(it_end):
    minn = f"""SELECT MIN(BIT_COUNT(phash ^ '{it_end}')) FROM picturehashes;"""
    cursor.execute(minn)
    resultpp = cursor.fetchall()

    req = f"""SELECT picturehashes.id FROM picturehashes WHERE BIT_COUNT(phash ^ '{it_end}')='{resultpp[0][0]}' 
    LIMIT 1;"""
    cursor.execute(req)
    resultp = cursor.fetchall()

    sql = f"""SELECT picturehashes.picturename, series.seriesname, series.fileid, BIT_COUNT(phash ^ '{it_end}'), 
                    picturehashes.times
                    FROM picturehashes,series
                    WHERE picturehashes.sid=series.id and
                    picturehashes.id='{resultp[0][0]}';"""

    cursor.execute(sql)
    result = cursor.fetchall()
    return result


def count():
    sql = """SELECT COUNT(*) FROM users; """
    cursor.execute(sql)
    result = cursor.fetchall()
    return result
