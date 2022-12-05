from cProfile import label
from curses.panel import bottom_panel
from re import X
from tkinter import BOTTOM
from turtle import left
import matplotlib.pyplot as plt
import base64
from io import BytesIO
import numpy as np

#プロットしたグラフを画像データとして出力するための関数
def Output_Graph():
	buffer = BytesIO()                   #バイナリI/O(画像や音声データを取り扱う際に利用)
	plt.savefig(buffer, format="png")    #png形式の画像データを取り扱う
	buffer.seek(0)                       #ストリーム先頭のoffset byteに変更
	img   = buffer.getvalue()            #バッファの全内容を含むbytes
	graph = base64.b64encode(img)        #画像ファイルをbase64でエンコード
	graph = graph.decode("utf-8")        #デコードして文字列から画像に変換
	buffer.close()
	return graph

#グラフをプロットするための関数
def Plot_Graph(a,b,c,d,name):
    plt.switch_backend("AGG")
    plt.figure(figsize=(4,3))
    plt.plot(a,b, label="AVG")
    plt.plot(a,c, label="OBP")
    plt.plot(a,d, label="SLG")
    plt.hlines(0.3,0,len(a),linestyles="dotted")
    plt.hlines(0.4,0,len(a),linestyles="dotted")
    plt.hlines(0.5,0,len(a),linestyles="dotted")
    plt.legend()
    plt.gca().set_ylim(bottom=0)
    plt.gca().set_xlim(left=1)
    plt.xlabel(name)
    plt.tight_layout()
    graph = Output_Graph()
    return graph

result = ["single","double","homerun","strikeout"]

#打率生成
def batting_average_and_on_base_percentage(lst):
    bat_avg = []
    hit = 0
    obp = []
    ob = 0
    total_appearance = 0
    at_bat = 0
    f = None
    for i in lst:
        if i == "single" or i == "double" or i == "triple" or i == "homerun":
            hit += 1
            ob += 1
            total_appearance += 1
            at_bat += 1
            bat_avg.append(hit/at_bat)
            obp.append(ob/total_appearance)
        elif i == "strikeout" or i == "groundout" or i == "flyout":
            at_bat += 1
            total_appearance += 1
            bat_avg.append(hit/at_bat)
            obp.append(ob/total_appearance)
        else:
            total_appearance += 1
            ob += 1
            if len(bat_avg) == 0:
                bat_avg.append(None)###初打席で四球or死球だとエラーになってしまう###
            else:
                bat_avg.append(hit/at_bat)
            obp.append(ob/total_appearance)
    return bat_avg, obp

def slugging_percentage(lst):
    slg_per = []
    slg = 0
    total_appearance = 0
    for i in lst:
        total_appearance += 1
        if i == "single" or i == "four-ball" or i == "dead-ball":
            slg += 1
        elif i == "double":
            slg += 2
        elif i == "triple":
            slg += 3
        elif i == "homerun":
            slg += 4
        slg_per.append(slg/total_appearance)
    return slg_per


