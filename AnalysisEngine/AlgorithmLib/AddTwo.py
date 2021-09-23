def AddOne(args):
    if(isinstance(args,dict)):
        if(isinstance(args["a"],int)):
            return {'result':args["a"]+2}
    return "args error"