import requests
import DatabaseUtil


def query_data(function, symbol, conn, cursor, apikey='AOTR8MTUM9ZQ10R4', DB_NAME='company_analysis_data'):
    url = 'https://www.alphavantage.co/query?function={}&symbol={}&apikey={}'.format(function, symbol, apikey)
    r = requests.get(url)
    data = r.json()
    if data is None or len(data) == 0:
        return -1
    if function == "OVERVIEW":
        sql, values = get_sql_and_values(function, symbol, data)
        DatabaseUtil.write_to_database(conn, cursor, sql, tuple(values), DB_NAME)

    else:
        quarterly_data = data['quarterlyEarnings'] if function == 'EARNINGS' else data['quarterlyReports']
        for report in quarterly_data:
            sql, values = get_sql_and_values(function, symbol, report)
            DatabaseUtil.write_to_database(conn, cursor, sql, tuple(values), DB_NAME)
    return 1


def contain_space(s):
    res = ""
    for i in range(len(s)):
        if s[i] != ' ' and s[i] != ',' and s[i] != ':':
            res += s[i]
        else:
            res += '_'
    return res


def get_sql_and_values(function_name, symbol, data):
    sql = "INSERT IGNORE INTO " + function_name + " ("
    temp = "VALUES ("
    values = []
    if function_name != "OVERVIEW":
        sql += "Symbol" + ', '
        temp += '%s, '
        values.append(symbol)
    for key, value in data.items():
        sql += key + ', '
        temp += '%s, '
        if value == 'None':
            values.append(None)
        else:
            values.append(value)
    sql = sql[:-2] + ') ' + temp[:-2] + ') '
    return sql, values



