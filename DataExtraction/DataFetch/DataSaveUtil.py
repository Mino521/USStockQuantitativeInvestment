import logging


def save_to_db(cik, year, income, conn):
    try:
        sql = 'insert or ignore into archive_content (ID, CIK, Year, EarningsPerShare) VALUES (?,?,?,?);'
        project = [int(str(cik) + str(year)), cik, year, income]
        conn.execute(sql, project)
        conn.commit()
    except Exception as e:
        logging.warning(e)


def insert_comp_infor_table(conn, sic, cik, ticker, comp_name, state, office):
    sql = 'insert or ignore into comp_meta (sic, cik, ticker, company,' \
          ' state_country,office) values (?,?,?,?,?,?);'
    try:
        project = [sic, cik, ticker, comp_name, state, office]
        conn.execute(sql, project)
        conn.commit()
    except Exception as e:
        print(e)