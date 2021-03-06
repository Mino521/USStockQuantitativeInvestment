class Tables:
    TABLES = {'OVERVIEW': (
        "CREATE TABLE IF NOT EXISTS `OVERVIEW` ("
        "`Symbol` varchar(20),"
        "`AssetType` varchar(20),"
        "`Name` varchar(100),"
        "`Description` TEXT,"
        "`CIK` int,"
        "`Exchange` char(8),"
        "`Currency` char(8),"
        "`Country`char(8),"
        "`Sector` varchar(20),"
        "`Industry` varchar(100),"
        "`Address` varchar(100),"
        "`FiscalYearEnd` char(10),"
        "`LatestQuarter` DATE,"
        "`MarketCapitalization` bigint(20),"
        "`EBITDA` bigint(20),"
        "`PERatio` double,"
        "`PEGRatio` double, "
        "`BookValue` double,"
        "`DividendPerShare` double,"
        "`DividendYield`double,"
        "`EPS` double,"
        "`RevenuePerShareTTM` double,"
        "`ProfitMargin` double,"
        "`OperatingMarginTTM` double,"
        "`ReturnOnAssetsTTM` double,"
        "`ReturnOnEquityTTM` double,"
        "`RevenueTTM` bigint(20),"
        "`GrossProfitTTM` bigint(20),"
        "`DilutedEPSTTM` double,"
        "`QuarterlyEarningsGrowthYOY` double,"
        "`QuarterlyRevenueGrowthYOY` double,"
        "`AnalystTargetPrice` int,"
        "`TrailingPE` double,"
        "`ForwardPE` double,"
        "`PriceToSalesRatioTTM` double,"
        "`PriceToBookRatio`double, "
        "`EVToRevenue` double, "
        "`EVToEBITDA` double, "
        "`Beta` double, "
        "`52WeekHigh` double, "
        "`52WeekLow` double, "
        "`50DayMovingAverage` double,"
        "`200DayMovingAverage` double, "
        "`SharesOutstanding` bigint(20),"
        "`SharesFloat` bigint(20),"
        "`SharesShort` bigint(20),"
        "`SharesShortPriorMonth` bigint(20),"
        "`ShortRatio` double,"
        "`ShortPercentOutstanding` double, "
        "`ShortPercentFloat` double, "
        "`PercentInsiders` double, "
        "`PercentInstitutions` double, "
        "`ForwardAnnualDividendRate` double, "
        "`ForwardAnnualDividendYield` double, "
        "`PayoutRatio` double, "
        "`DividendDate` DATE, "
        "`ExDividendDate` DATE, "
        "`LastSplitFactor` varchar(20),"
        "`LastSplitDate` DATE,"
        "  PRIMARY KEY (`Symbol`)"
        ") ENGINE=InnoDB"),
        'EARNINGS': (
            "CREATE TABLE IF NOT EXISTS `EARNINGS` ("
            "  `Symbol` varchar(20),"
            "  `fiscalDateEnding` DATE,"
            "  `reportedDate` DATE,"
            "  `reportedEPS` double ,"
            "  `estimatedEPS` double,"
            "  `surprise` double,"
            "  `surprisePercentage` double,"
            "  PRIMARY KEY (`Symbol`, `fiscalDateEnding`)"
            ") ENGINE=InnoDB"),
        'INCOME_STATEMENT': (
            "CREATE TABLE IF NOT EXISTS `INCOME_STATEMENT` ("
            "  `Symbol` varchar(20),"
            "  `fiscalDateEnding` DATE,"
            "  `reportedCurrency` char(8),"
            "  `grossProfit` bigint,"
            "  `totalRevenue` bigint,"
            "  `costOfRevenue` bigint,"
            "  `costofGoodsAndServicesSold` bigint,"
            "  `operatingIncome` bigint,"
            "  `sellingGeneralAndAdministrative` bigint,"
            "  `researchAndDevelopment` bigint,"
            "  `operatingExpenses` bigint,"
            "  `investmentIncomeNet` bigint,"
            "  `netInterestIncome` bigint,"
            "  `interestIncome` bigint,"
            "  `interestExpense` bigint,"
            "  `nonInterestIncome` bigint,"
            "  `otherNonOperatingIncome` bigint,"
            "  `depreciation` bigint,"
            "  `depreciationAndAmortization` bigint,"
            "  `incomeBeforeTax` bigint,"
            "  `incomeTaxExpense` bigint,"
            "  `interestAndDebtExpense` bigint,"
            "  `netIncomeFromContinuingOperations` bigint,"
            "  `comprehensiveIncomeNetOfTax` bigint,"
            "  `ebit` bigint,"
            "  `ebitda` bigint,"
            "  `netIncome` bigint,"
            "  PRIMARY KEY (`Symbol`, `fiscalDateEnding`)"
            ") ENGINE=InnoDB"),
        'BALANCE_SHEET': (
            "CREATE TABLE IF NOT EXISTS `BALANCE_SHEET` ("
            "  `Symbol` varchar(20),"
            "  `fiscalDateEnding` DATE,"
            "  `reportedCurrency` char(8),"
            "  `totalAssets` bigint,"
            "  `totalCurrentAssets` bigint,"
            "  `cashAndCashEquivalentsAtCarryingValue` bigint,"
            "  `cashAndShortTermInvestments` bigint,"
            "  `inventory` bigint,"
            "  `currentNetReceivables` bigint,"
            "  `totalNonCurrentAssets` bigint,"
            "  `propertyPlantEquipment` bigint,"
            "  `accumulatedDepreciationAmortizationPPE` bigint,"
            "  `intangibleAssets` bigint,"
            "  `intangibleAssetsExcludingGoodwill` bigint,"
            "  `goodwill` bigint,"
            "  `investments` bigint,"
            "  `longTermInvestments` bigint,"
            "  `shortTermInvestments` bigint,"
            "  `otherCurrentAssets` bigint,"
            "  `otherNonCurrrentAssets` bigint,"
            "  `totalLiabilities` bigint,"
            "  `totalCurrentLiabilities` bigint,"
            "  `currentAccountsPayable` bigint,"
            "  `deferredRevenue` bigint,"
            "  `currentDebt` bigint,"
            "  `shortTermDebt` bigint,"
            "  `totalNonCurrentLiabilities` bigint,"
            "  `capitalLeaseObligations` bigint,"
            "  `longTermDebt` bigint,"
            "  `currentLongTermDebt` bigint,"
            "  `longTermDebtNoncurrent` bigint,"
            "  `shortLongTermDebtTotal` bigint,"
            "  `otherCurrentLiabilities` bigint,"
            "  `otherNonCurrentLiabilities` bigint,"
            "  `totalShareholderEquity` bigint,"
            "  `treasuryStock` bigint,"
            "  `retainedEarnings` bigint,"
            "  `commonStock` bigint,"
            "  `commonStockSharesOutstanding` bigint,"
            "  PRIMARY KEY (`Symbol`, `fiscalDateEnding`)"
            ") ENGINE=InnoDB"),
        'CASH_FLOW': (
            "CREATE TABLE IF NOT EXISTS `CASH_FLOW` ("
            "  `Symbol` varchar(20),"
            "  `fiscalDateEnding` DATE,"
            "  `reportedCurrency` char(8),"
            "  `operatingCashflow` bigint,"
            "  `paymentsForOperatingActivities` bigint,"
            "  `proceedsFromOperatingActivities` bigint,"
            "  `changeInOperatingLiabilities` bigint,"
            "  `changeInOperatingAssets` bigint,"
            "  `depreciationDepletionAndAmortization` bigint,"
            "  `capitalExpenditures` bigint,"
            "  `changeInReceivables` bigint,"
            "  `changeInInventory` bigint,"
            "  `profitLoss` bigint,"
            "  `cashflowFromInvestment` bigint,"
            "  `cashflowFromFinancing` bigint,"
            "  `proceedsFromRepaymentsOfShortTermDebt` bigint,"
            "  `paymentsForRepurchaseOfCommonStock` bigint,"
            "  `paymentsForRepurchaseOfEquity` bigint,"
            "  `paymentsForRepurchaseOfPreferredStock` bigint,"
            "  `dividendPayout` bigint,"
            "  `dividendPayoutCommonStock` bigint,"
            "  `dividendPayoutPreferredStock` bigint,"
            "  `proceedsFromIssuanceOfCommonStock` bigint,"
            "  `proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet` bigint,"
            "  `proceedsFromIssuanceOfPreferredStock` bigint,"
            "  `proceedsFromRepurchaseOfEquity` bigint,"
            "  `proceedsFromSaleOfTreasuryStock` bigint,"
            "  `changeInCashAndCashEquivalents` bigint,"
            "  `changeInExchangeRate` bigint,"
            "  `netIncome` bigint,"
            "  PRIMARY KEY (`Symbol`, `fiscalDateEnding`)"
            ") ENGINE=InnoDB")

    }
