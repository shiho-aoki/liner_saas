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
x = [ [0 ,6177.285, 8152354.571, 12228531.86, 16304709.14,20380886.43],
      [0 ,6177.285, 8152354.571, 12228531.86, 16304709.14,20380886.43],
      [0 ,6177.285, 8152354.571, 12228531.86, 16304709.14,20380886.43],
      [0 ,6177.285, 8152354.571, 12228531.86, 16304709.14,20380886.43]
    ]

y = [[0, -2.40E-05, -4.60E-05, -7.00E-05, -9.20E-05, -1.13E-04],
     [0, -2.40E-05, -4.70E-05, -7.00E-05, -9.20E-05, -1.15E-04],
     [0, 2.00E-05, 4.20E-05, 6.30E-05, 8.60E-05, 1.07E-04],
     [0, 2.00E-05, 4.20E-05, 6.30E-05, 8.50E-05, 1.07E-04]
    ]

label_name = ['右上面','左上面','右下面','左下面']
a_ = [-5.56E-12, -5.62E-12, 5.29E-12, 5.26E-12]
b_ = [-8.57E-07, -7.14E-07, -8.57E-07, -8.57E-07]
a_disp = ['$-5.56×10^{{-}12}$', '$-5.62×10^{{-}12}$', '$5.29×10^{{-}12}$', '$5.26×10^{{-}12}$']
b_disp = ['$-8.57×10^{{-}7}$', '$-7.14×10^{{-}7}$', '$-8.57×10^{{-}7}$', '$-8.57×10^{{-}7}$']
title='図1.1 曲げ試験における応力とひずみの関係'
x_label='応力$\it{ σ }$（Pa）'
y_label="ひずみ$\it{ ε }$"
x_limt=[0,2.5E7]
y_limt=[-1.5E-4,1.5E-4]

least_squares(x,y, label_name, a_, b_, a_disp, b_disp,
        title = title,
        x_label=x_label,
        y_label= y_label,
        x_limt = x_limt,
        y_limt = y_limt
)