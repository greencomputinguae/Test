
class Coin_calculation:


    def coin_cal_fun(packet_coin, object_price):
        packet_coin.sort()
        result=[]
        residual=object_price
        ind=len(packet_coin)-1
        index_used=[]
        while residual>0 and ind>-1:
            val=packet_coin[ind]
            if residual>=val and ind not in index_used:
                residual-=val
                result.append(val)
                index_used.append(ind)
            else:
                ind-=1

        if sum(result)!=object_price:
            result = []

        return result

