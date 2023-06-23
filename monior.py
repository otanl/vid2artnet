import tkinter as tk
from socket import *

host = '127.0.0.1'  # 送信元IPアドレス
universe = 0  # universe番号

num_rows = 20
num_cols = 1

class UDPRcv:
    def __init__(self):
        # IPアドレスを取得、表示
        SrcIP = gethostbyname(host)
        SrcPort = 6454  # 受信元ポート番号
        self.SrcAddr = (SrcIP, SrcPort)  # アドレスをtupleに格納
        self.BUFSIZE = 1024  # バッファサイズ指定
        self.udpServSock = socket(AF_INET, SOCK_DGRAM)  # ソケット作成
        self.udpServSock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.udpServSock.bind(self.SrcAddr)  # 受信元アドレスでバインド

    def recv(self):
        packet, addr = self.udpServSock.recvfrom(self.BUFSIZE)
        data = [int(b) for b in packet]
        try:
            if data[14] == universe:
                del data[0:18]
                visualize_data(data)  # データを可視化する関数を呼び出す
        except IndexError:
            pass

def visualize_data(data):
    num_rectangles = int(512/3)
    for i in range(num_rectangles):
        red = data[i*3]
        green = data[i*3+1]
        blue = data[i*3+2]
        color = f"#{red:02x}{green:02x}{blue:02x}"
        
        row = i // num_cols
        col = i % num_cols
        x0 = col * (400 / num_cols)
        y0 = row * (400 / num_rows)
        x1 = x0 + (400 / num_cols)
        y1 = y0 + (400 / num_rows)
        
        rectangle_id = f"rectangle_{row}_{col}"
        if canvas.find_withtag(rectangle_id):
            canvas.itemconfig(rectangle_id, fill=color)
        else:
            canvas.create_rectangle(x0, y0, x1, y1, fill=color, tags=rectangle_id)


# ウィンドウの作成
window = tk.Tk()
window.title("Artnet Visualizer")
window.geometry("400x400")

# キャンバスの作成
canvas = tk.Canvas(window, width=400, height=400)
canvas.pack()

# UDPRcvオブジェクトの作成
udp = UDPRcv()

# 受信ループ
def receive_loop():
    udp.recv()
    window.after(1, receive_loop)

# 受信ループの開始
receive_loop()

# アプリケーションの実行
window.mainloop()
