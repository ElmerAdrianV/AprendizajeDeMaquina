def simple_pred(df,theta):
    vector = df.reshape(1,-1)
    pred = (vector>theta)
    return pred

def simple_acc(ftr, outcome, theta):
    ### BEGIN SOLUTION
    pred = simple_pred
    lbl = outcome.reshape(1,-1)
    cmp = (pred==lbl)
    acc = cmp.mean(axis=1) #mean within each row
    # END SOLUTION
    print('outcome: ',lbl)
    print('------------')
    print('comparasion: ',cmp)
    print('------------')
    print('accuracy: ',acc)
    print('------------')
    return acc