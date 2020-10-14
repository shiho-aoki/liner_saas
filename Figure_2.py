import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import japanize_matplotlib
import numpy as np

#make figur
def least_squares(x:list, y:list, label_name:list, a_:list, b_:list, a_disp:list, b_disp:list,
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
    marker_size = [12,10]

    i = 1
    for x_data, y_data, name, l, a,b , a_d, b_d in zip(x, y, label_name, liner_marker, a_,b_, a_disp, b_disp):
        ##redl_caouse
        n_x = np.array(x_data)

        if(i is 1):
            plt.plot([0, n_x.max()], [b, a*n_x.max() + b], linestyle=l, color="k", label=f"計算値\n{name}\ny=ax+b\n a="+str(a_d)+' b='+str(b_d))
            i +=1
            continue
        plt.plot([0, n_x.max()], [b, a*n_x.max() + b], linestyle=l, color="k", label=f"{name}\ny=ax+b\n a="+str(a_d)+' b='+str(b_d))

    i = 1
    for x_data, y_data, p, name, m_s in zip(x, y, plot_marker, label_name, marker_size):
        ##out side
        if(i is 1):
            plt.plot(x_data,y_data, p, markeredgecolor="k", color="w", markersize = m_s, label=f"実験値\n{name}")
            plt.plot(x_data, y_data, 'o', color="k", markersize='1')
            i +=1
            continue
        plt.plot(x_data,y_data, p, markeredgecolor="k", color="w", markersize = m_s, label=f"{name}")
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
x = [[0.0 ,5267970.0 ,9871312.5 ,14494275.0 ,19620000.0 ,24402375.0 ,29454525.0 ,34114275.0 ,39190950.0 ,43997850.0 ,48853800.0],
     [0.0 ,5267970.0 ,9871312.5 ,14494275.0 ,19620000.0 ,24402375.0 ,29454525.0 ,34114275.0 ,39190950.0 ,43997850.0 ,48853800.0]
    ]

y = [[0.000000, 0.000041 , 0.000068 ,0.000090 ,0.000110 ,0.000132 ,0.000158 ,0.000182 ,0.000211 ,0.000239 , 0.000268 ],
     [0.000000, -0.000003 ,-0.000009 ,-0.000017 ,-0.000028 ,-0.000037 ,-0.000045 ,-0.000054 ,-0.000064 ,-0.000071 ,-0.000077]
]

label_name = ['伸び', '縮み']
a_ = [5.20917E-12,-1.70259E-12]
b_ = [8.76E-06, 4.86E-06]
a_disp = ['$5.21×10^{{-}12}$','$-1.70×10^{{-}12}$']
b_disp = ['$8.76×10^{{-}6}$', '$4.86×10^{{-}6}$']
title='図1.2　応力とひずみの関係'
x_label='応力$\it{ σ }$（Pa）'
y_label="ひずみ$\it{ ε }$"
x_limt=[0.0,6.0E7]
y_limt=[-1.0E-4,3.0E-4]

least_squares(x,y, label_name, a_, b_, a_disp, b_disp,
        title = title,
        x_label=x_label,
        y_label= y_label,
        x_limt = x_limt,
        y_limt = y_limt
)