from controller import *

# Tạo cửa sổ
root = tk.Tk()
root.title("DỰ ĐOÁN LOÀI CÁ")
root.geometry("600x300")
root.iconbitmap(r"img\Kumo-circle.ico")

# Tạo frame chính
main_frame = tk.Frame(root)
main_frame.pack(fill="both", expand=True)
main_frame.pack_propagate(False)

## Set background
background = Image.open(path + r"\img\background.jpg")
background = background.resize((1000,500))
render = ImageTk.PhotoImage(background)
img = Label(main_frame, image=render)
img.place(x=0, y=0, relwidth=1, relheight=1)

## Tạo frame con để nhập thông số
frame1 = tk.Frame(main_frame, bg="#008BEA", width=300, height=300)
frame1.pack_propagate(False)
frame1.pack(side="left", fill="y")

### Tạo tiêu đề nhập
tittle_input = tk.Frame(frame1,bg='#008BEA', width=300, height=40)
tittle_input.pack_propagate(False)
tittle_input.pack(side="top", fill="x")
label_tittle = tk.Label(tittle_input, text="NHẬP CÁC THÔNG SỐ")
label_tittle.config(font=('Courier',10,'bold'), bg="#008BEA", bd=10)
label_tittle.pack(pady=10, fill='both')

### Tạo frame nhập
frame_input = tk.Frame(frame1, width=300, height=200)
frame_input.pack_propagate(False)
frame_input.pack(fill="x")
### Tạo cột thứ nhất
col1 = tk.Frame(frame_input, bg="#008BEA", width=150, height=200)
col1.pack_propagate(False)
col1.pack(side="left", fill='both')

#### Tạo spinbox lấy weight, height, width
label_weight = tk.Label(col1, text="Nhập khối lượng: ")
label_weight.pack(padx=10, pady=(20,0), fill='x')
sbweight = DoubleVar()
spinbox_weight = Spinbox(col1, from_=0, to=2000, increment=0.1, textvariable=sbweight)
spinbox_weight.pack(side="top", padx=10, pady=(0,10))

label_height = tk.Label(col1, text="Nhập chiều cao: ")
label_height.pack(padx=10, pady=(10,0), fill='x')
sbheight = DoubleVar()
spinbox_height = Spinbox(col1, from_=0, to=50, increment=0.1, textvariable=sbheight)
spinbox_height.pack(side="top", padx=10, pady=(0,10))

label_width = tk.Label(col1, text="Nhập chiều rộng chéo: ")
label_width.pack(padx=10, pady=(10,0), fill='x')
sbwidth = DoubleVar()
spinbox_width = Spinbox(col1, from_=0, to=50, increment=0.1, textvariable=sbwidth)
spinbox_width.pack(side="top", padx=10, pady=(0,10))

### Tạo cột thứ hai
col2 = tk.Frame(frame_input, bg="#008BEA", width=150, height=200)
col2.pack_propagate(False)
col2.pack(side="right", fill='both')

#### Tạo spinbox lấy length
label_ver = tk.Label(col2, text="Nhập chiều dài dọc: ")
label_ver.pack(padx=10, pady=(20,0), fill='x')
sbver = DoubleVar()
spinbox_ver = Spinbox(col2, from_=0, to=2000, increment=0.1, textvariable=sbver)
spinbox_ver.pack(side="top", padx=10, pady=(0,10))

label_dia = tk.Label(col2, text="Nhập chiều dài chéo: ")
label_dia.pack(padx=10, pady=(10,0), fill='x')
sbdia = DoubleVar()
spinbox_dia = Spinbox(col2, from_=0, to=100, increment=0.1, textvariable=sbdia)
spinbox_dia.pack(side="top", padx=10, pady=(0,10))

label_cro = tk.Label(col2, text="Nhập chiều dài ngang: ")
label_cro.pack(padx=10, pady=(10,0), fill='x')
sbcro = DoubleVar()
spinbox_cro = Spinbox(col2, from_=0, to=100, increment=0.1, textvariable=sbcro)
spinbox_cro.pack(side="top", padx=10, pady=(0,10))

### Tạo button submit
submit = tk.Frame(frame1, width=300, height=60, bg="#019CDD")
submit.pack_propagate(False)
submit.pack(side="bottom", fill="y", anchor='n')
button_submit = tk.Button(submit, text='OK', font=('ROBOTO',12), bg='#FFFFFF', fg='#000000')
button_submit.config(command= lambda: predict(Weight= float(spinbox_weight.get()),
                                              LengthVer= float(spinbox_ver.get()),
                                              LengthDia= float(spinbox_dia.get()),
                                              LengthCro= float(spinbox_cro.get()),
                                              Height=float(spinbox_height.get()),
                                              Width=float(spinbox_width.get()),
                                              img=img,
                                              answer=answer))
button_submit.pack()


# Tạo frame để hiển thị kết  quả
frame2 = tk.Frame(main_frame, bg="#0087EB", width=150, height=150)
frame2.pack_propagate(False)
frame2.pack(side="top", anchor='center', fill="y")
# Load hình ảnh
image = Image.open(path + r"\img\image_" + f"{fish}.png")
image = image.resize((150,100))
photo = ImageTk.PhotoImage(image)
# Hiển thị ảnh trong label
img = tk.Label(frame2, image=photo)
img.pack(side='top', pady=(10,0))

# Hiển thị kết quả
answer = tk.Text(frame2, bg="#6A9BD7")
answer.config(font=('Arial',10,'italic'))
answer.pack(anchor='center')
root.mainloop()
