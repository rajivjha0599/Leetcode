class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        neg=False
        if denominator==0:
            return False
        elif numerator==0:
            return "0"
        elif(numerator<0 or denominator<0):
            if(numerator<0 and denominator<0): 
                pass
            else:
                neg=True
        numerator=abs(numerator)
        denominator=abs(denominator)
        if((numerator%denominator)==0):
            if(neg):
                return "-"+str(numerator//denominator)
            else:
                return str(numerator//denominator)
        beforeDecimal=numerator//denominator
        remainderAndQuotientList=[]
        afterdec=""
        while True:
            rem=numerator%denominator
            numerator=rem*10
            if(rem==0):
                afterdec+=str(numerator//denominator)[0:-1]
                break
            for data in remainderAndQuotientList:        
                if [numerator//denominator,numerator%denominator] in remainderAndQuotientList:
                    index_of_pair = remainderAndQuotientList.index([numerator//denominator,numerator%denominator])
                    after_dec_list=list(afterdec)
                    after_dec_list.insert(index_of_pair,"(")
                    afterdec="".join([str(e) for e in after_dec_list])
                    if(neg):
                        return "-"+str(beforeDecimal)+"."+afterdec +")"
                    else:
                        return str(beforeDecimal)+"."+afterdec +")"
            afterdec+=str(numerator//denominator)        
            remainderAndQuotientList.append([numerator//denominator,numerator%denominator])

        if(neg):    
            return "-"+str(beforeDecimal)+"."+afterdec    
        else:
            return str(beforeDecimal)+"."+afterdec
        