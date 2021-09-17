import numpy as np
from sklearn.metrics import r2_score
import math
def GordonGrowModel(args):
    if(isinstance(args,dict)):
        if(isinstance(args["dividends"],list)):
            dividendsList = args["dividends"]
            g=math.pow((dividendsList[-1]/dividendsList[0]),(1/(len(dividendsList)-1)))-1
            result = {"Growth rate": g }
            predict = [dividendsList[0]]
            for i in range(1,len(dividendsList)):
                predict.append(predict[i-1]*(1+g))
            result["r2_score"]=r2_score(dividendsList,predict)
            if(isinstance(args["DiscountRate"],float)):
                sharePrice = dividendsList[-1]/(args["DiscountRate"]/g)
                result["sharePrice"] = sharePrice
                return result
    return "args error"