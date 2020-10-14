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
            plt.plot(x_data,y_data, p, markeredgecolor="k", color="w", markersize = '10')
            plt.plot(x_data, y_data, 'o', color="k", markersize='1')
            i +=1
            continue
        plt.plot(x_data,y_data, p, markeredgecolor="k", color="w", markersize = '10')
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
x = [[0,3,6,9 ,12 ,15 ,18 ,21 ,24 ,27 ,30 ,33 ,36 ,39]]
y = [[14.9250 ,13.7320 ,13.4213 ,13.1047 ,12.9683 ,12.6224 ,12.4116 ,12.4013 ,12.1171 ,11.7184 ,11.7184 ,11.0047 ,11.0047 ,11.0047 ]]
label_name = ['']
a_ = [-0.088054224]
b_ = [14.15665203]
a_disp = ['$-8.81×10^{{-}2}$']
b_disp = ['14.2']
title='図1.3　応力緩和実験'
x_label='時間$\it{ t }$（s）'
y_label="$\it{ ln[σ - γ_0G_e] }$"
x_limt=[0,4.0E1]
y_limt=[0,2.00E1]

least_squares(x,y, label_name, a_, b_, a_disp, b_disp,
        title = title,
        x_label=x_label,
        y_label= y_label,
        x_limt = x_limt,
        y_limt = y_limt
)