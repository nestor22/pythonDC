def checkIfNotNumeric(*args):
    """
    This function veryfi is all arguments are numeric
    """
    retValue=True
    for x in args:
        if not(isinstance(x,(int,float))):
            return False
        
    return True
            
