import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import japanize_matplotlib
import numpy as np

#make liner data
def exp_redl(y, x):
    n = len(x)
    a = ((np.dot(y, x)- x.sum() * y.sum()/n)/((y ** 2).sum() - y.sum()**2 / n))
    b = (x.sum() - a * y.sum())/n
    return a, b

#make figur
def least_squares(x:list, y:list, label_name:list, 
                x_exp = 1, y_exp=1,
                title='title', x_label='x_axis', y_label="y_axis",
                x_limt=[-1,1], y_limt=[-1,1]):
    # fig = plt.figure()
    # ax = fig.add_subplot(111)
    plt.rcParams['font.family'] = 'IPAexGothic'
    plt.rcParams['font.size'] = 12
    ##軸内側に
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    ##メモリ指定する
    plt.rcParams['xtick.major.width'] = 1.0
    plt.rcParams['ytick.major.width'] = 1.0
    ##軸名／タイトル
    plt.title(title, y=-0.15)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.rcParams["font.size"] = 12
    plt.gca().xaxis.get_major_formatter().set_useOffset(False)
    plt.gca().xaxis.set_major_formatter(ScalarFormatter(useMathText=True))
    plt.gca().ticklabel_format(style="sci",  axis="x",scilimits=(0,0)) 
    plt.gca().yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
    plt.gca().ticklabel_format(style="sci",  axis="y",scilimits=(0,0)) 

    #範囲
    plt.xlim(x_limt)
    plt.ylim(y_limt)
    plt.gca().spines['bottom'].set_position(('data', 0))
    plt.gca().spines['left'].set_position(('data', 0))
    #上と右の枠を消す
    plt.gca().spines['right'].set_visible(False)
    plt.gca().yaxis.set_ticks_position('left')
    plt.gca().spines['top'].set_visible(False)
    plt.gca().xaxis.set_ticks_position('bottom')

    #data
    plot_marker = ['o', 's', 'p', '*', '+', 'D']
    liner_marker = ["-", "--", "-.", ":"]
    i = 1
    for x_data, y_data, name, l in zip(x, y, label_name, liner_marker):
        ##redl_caouse
        n_x = np.array(x_data)
        n_y = np.array(y_data)
        a, b = exp_redl(n_x, n_y)
        print(a,b)
        # a_ = a * (x_exp/y_exp)
        # b_ = b * (1/y_exp)
        if(i is 1):
            plt.plot([0, n_x.max()], [b, a*n_x.max() + b], linestyle=l, color="k")
            i +=1
            continue
        plt.plot([0, n_x.max()], [b, a*n_x.max() + b], linestyle=l, color="k")

    i = 1
    for x_data, y_data, p, name in zip(x, y, plot_marker, label_name):
        ##out side
        if(i is 1):
            plt.plot(x_data,y_data, p, markeredgecolor="k", color="w", markersize = '10', label=f"実験値\n{name}")
            plt.plot(x_data, y_data, 'o', color="k", markersize='1')
            i +=1
            continue
        plt.plot(x_data,y_data, p, markeredgecolor="k", color="w", markersize = '10', label=f"{name}")
        ##in side
        plt.plot(x_data, y_data, 'o', color="k", markersize='1')

    plt.legend(title='凡例', borderaxespad=0, loc='upper left', bbox_to_anchor=(1, 1),title_fontsize=12, fontsize=9, ncol=2)

    plt.tight_layout()
    plt.show()

#========================================================
#==========================================================
#===========================================================
#=========Use Spase==========================================

#1 Prepare x and y data
######x,y == 図1.2
x = [ [0.0 ,5267970.0 ,9871312.5 ,14494275.0 ,19620000.0 ,24402375.0 ,29454525.0 ,34114275.0 ,39190950.0 ,43997850.0 ,48853800.0],
        [0.0 ,5267970.0 ,9871312.5 ,14494275.0 ,19620000.0 ,24402375.0 ,29454525.0 ,34114275.0 ,39190950.0 ,43997850.0 ,48853800.0]
    ]

y = [[0,0.000041,0.000068,0.000090 ,0.000110 ,0.000132,0.000158, 0.000182 ,0.000211, 0.000239 ,0.000268],
    [0, -0.000003, -0.000009, -0.000017, -0.000028, -0.000037, -0.000045, -0.000054, -0.000064, -0.000071, -0.000077]
]


#2 prepare format data
name = ['伸び','縮み']

least_squares(x,y,name,
        x_exp = 10**7,
        y_exp = 10**(-5),
        title='図1.2 応力とひずみの関係',
        x_label='応力$\it{ σ }$（Pa）',
        y_label='歪み$\it{ ε }$',
        x_limt= [0,60000000],
        y_limt=[-0.000100,0.000300]
)