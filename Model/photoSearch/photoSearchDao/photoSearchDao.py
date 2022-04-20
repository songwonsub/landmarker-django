import common.oracle_db as oradb
from Model.photoSearch.photoSearchVo import photoSearchVo


def selectLandmark():

    conn = oradb.connect()
    cursor = None
    query = 'select * from ~'

    landmark_list = []

    try:
        cursor = conn.cursor()
        result = cursor.execute(query)

        for row in result:

            row_dict = {'no': row[0], 'name': row[1]}
            ai_value = photoSearchVo.photoSearchVo(row_dict)
            landmark_list.append(ai_value)

    except Exception as msg:
        print('select_all() 에러 발생 : ', msg)
    finally:
        cursor.close()
        oradb.close(conn)

    return landmark_list