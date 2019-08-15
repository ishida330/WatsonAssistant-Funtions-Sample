#
#
# main() このアクションを呼び出すときに実行されます
#
# @param Cloud Functions アクションは 1 つのパラメーターを受け入れます。このパラメーターは JSON オブジェクトでなければなりません。
#
# @return このアクションの出力。この出力は、JSON オブジェクトでなければなりません。
#
#
import sys
import ibm_db

def main(dict):
    print(dict)
    rows = []
    conn = ibm_db.connect("DATABASE=BLUDB;HOSTNAME=dashdb-txn-sbox-yp-dal09-04.services.dal.bluemix.net;PORT=50000;PROTOCOL=TCPIP;UID=xxxxxxxx;PWD=xxxxxxxx;","","")
    sql = "SELECT TITLE,URL FROM xxxxxxxx.ACTION_MOVIE WHERE ACTOR='{}'".format(dict["ACTOR"])
    stmt = ibm_db.exec_immediate(conn, sql)
    row = ibm_db.fetch_assoc(stmt)
    while (row):
        rows.append(row)
        row = ibm_db.fetch_assoc(stmt)
    result = {'result': rows}
    return result
