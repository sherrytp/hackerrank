# https://www.hackerrank.com/challenges/jim-and-the-orders/problem?h_r=next-challenge&h_v=zen

# key is how to sorted dictionary by values/keys

def jimOrders(orders):
    d = {i+1:sum(v) for i,v in enumerate(orders)}
    return dict(sorted(d.items(), key = lambda x:x[1])).keys()