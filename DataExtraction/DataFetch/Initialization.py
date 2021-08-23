import mysql.connector
from DataFetchUtil import DataFetcher
from DatabaseUtil import *

config = {
    'user': 'user',
    'password': 'password',
    'host': '127.0.0.1',
    'database': 'employees'
}
DB_NAME = 'Data'
TABLES = {}
TABLES['latest_content'] = (
    "CREATE TABLE `latest_content` ("
    "  `CIK` int,"
    "  `Ticker` VARCHAR(20),"
    "  `ReportDate` TEXT,"
    "  `Year` int,"
    "  `totalCurrAssets` REAL,"
    "  `longTermDebt` REAL,"
    "  `Income` REAL,"
    "  `Total_Share` REAL,"
    "  `Quarter` int,"
    "  `dividend` int,"
    "  `bookValue` REAL,"
    "  `sharePrice` REAL,"
    "  PRIMARY KEY (`Ticker`)"
    ") ENGINE=InnoDB")

TABLES['test_result'] = (
    "CREATE TABLE `test_result` ("
    "  `CIK` int,"
    "  `Ticker` VARCHAR(20),"
    "  `Test_1` int,"
    "  `Test_2` int,"
    "  `Test_3` int,"
    "  `Test_4` int,"
    "  `Test_5` int,"
    "  `Test_6` int,"
    "  PRIMARY KEY (`Ticker`)"
    ") ENGINE=InnoDB")

TABLES['archive_content'] = (
    "CREATE TABLE `archive_content` ("
    "  `ID` int,"
    "  `CIK` int,"
    "  `Year` int,"
    "  `EarningsPerShare` REAL,"
    "  PRIMARY KEY (`ID`)"
    ") ENGINE=InnoDB")

TABLES['COMP_META'] = (
    "CREATE TABLE `COMP_META` ("
    "  `SIC` int,"
    "  `CIK` int,"
    "  `Ticker` VARCHAR(20),"
    "  `Company` VARCHAR(100),"
    "  `State_Country` VARCHAR(20),"
    "  `Office` VARCHAR(50),"
    "  PRIMARY KEY (`Ticker`)"
    ") ENGINE=InnoDB")

TABLES['SIC_INFOR'] = (
    "CREATE TABLE `SIC_INFOR` ("
    "  `SIC` int,"
    "  `Office` VARCHAR(50),"
    "  `Industry_Title` VARCHAR(50),"
    "  PRIMARY KEY (`SIC`)"
    ") ENGINE=InnoDB")


def init():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    create_database(cursor, DB_NAME)
    create_table(cursor, TABLES)

    cursor.close()
    conn.close()


if __name__ == '__main__':
    init()
    DataFetcher.download_report()
