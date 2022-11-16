import plot

# bboxの中心下部でプロットする
def centerize(df):
    y_list = df.loc[:,'y'].values
    x_list = df.loc[:,'x'].values
    w_list = df.loc[:,'w'].values
    h_list = df.loc[:,'h'].values

    xc_list = x_list + w_list / 2
    yt_list = y_list + h_list
    print(df)
    return xc_list, yt_list

def kde2d(image, data):
    sns.set()
    fig, ax = plt.subplots(figsize = (10,5))
    sns.kdeplot(x=xc_list, y=yt_list, color='C3', fill=True, alpha=0.8, bw_method=0.1)
    plt.imshow(im, alpha=0.7)
    plt.savefig('2Dkde.png')