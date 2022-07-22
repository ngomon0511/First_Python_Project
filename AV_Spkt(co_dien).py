from tkinter import *
import random

w = Tk()
w.title('Programming: Quy đổi điểm AV Spkt cho hệ đại trà và chất lượng cao Tiếng Việt')
w.geometry('800x500+300+100')
w.resizable(False,False)

# Tạo listvariable cho listbox
A = ['TOEIC', 'IELTS', 'TOEFL IBT', 'TOEFL ITP', 'CELL-COMM3', 'CELL-COMM4', 'CELL-COMM5', 'CELL-COMM6', 'CELL-COMM7']
x1 = StringVar(value=A)
B = ['AV1: ', 'AV2: ', 'AV3: ', 'AV4: ', 'AV5: ', ]
x2 = StringVar(value=B)

def click():
	LB2.delete(0,5)
	y = LB1.curselection()
	nhap = E.get()
	S = [] # chuỗi chứa các điểm AV1-AV5
	# Điểm quy đổi AV1-AV5 khi đỗ các chương trình CELL (COMM3-COMM7)
	CELL = [[7.5, 5.0, 0, 0, 0], [10.0, 7.5, 5.0, 0, 0], [10.0, 10.0, 7.5, 5.0, 0], [10.0, 10.0, 10.0, 7.5, 5.0], [10.0, 10.0, 10.0, 10.0, 7.5]]

	# Hàm quy đổi (s: chuỗi chứa các điểm AV quy đổi được ở mốc điểm đầu tiên, T: chuỗi chứa các mốc điểm có thế quy đổi được)
	def diem(s,T,nhap):
			# Tạo chuỗi p gồm các phần tử ( mà mỗi phần tử đó là 1 chuỗi chứa 5 phần tử là 5 điểm AV1-AV5) 
			q = []
			for i in s:
				q.append(i)
			p = []
			p.append(q)
			while sum(s)<50:
				q = []
				for i in range(len(s)):
					if s[i] != 10 and s[i] != 0:
						s[i]+=0.5
				for i in range(2,len(s)):
					if s[i-1] == 7.5:
						s[i] = 5
						break
				for i in s:
					q.append(i)
				p.append(q)
			# kiểm tra phần tử có trong chuỗi
			def kt(a,b):
				for i in a:
					if b == i:
						return True
				return False
			# Trường hợp giá trị nhap trùng với một mốc điểm quy đổi được
			if kt(T,nhap):
				return p[T.index(nhap)]	# Trả về chuỗi điểm AV tương ứng
			# Trường hợp giá trị nhap không trùng với một mốc điểm quy đổi được
			T.append(nhap)
			T.sort()
			return p[T.index(nhap)-1] # Trả về chuỗi điểm AV tương ứng
    
    # Check số thực
	def isfloat(num):
		try:
			float(num)
			return True
		except ValueError:
			return False
    
    # Các trường hợp thao tác lỗi, chương trình sẽ đưa ra cảnh báo
	if len(y) == 0:
		L3.configure(text='Chưa chọn một chứng chỉ quốc tế hoặc chương trình !!!')
	elif y[0]<4 and nhap == '':
		L3.configure(text='Chưa nhập điểm')
	elif nhap != '' and y[0]>=4 :
		L3.configure(text='Yêu cầu không nhập điểm khi quy đổi chương trình CELL')
		return 
	elif isfloat(nhap) == False and nhap != '':
		L3.configure(text='Yêu cầu nhập điểm bằng số')	 
	# Các trường hợp thao tác thỏa mãn yêu cầu chương trình
	else:
		# Các chứng chỉ quốc tế yêu cầu nhập điểm
		if nhap != '':
			nhap = float(nhap)
			if nhap == int(nhap):
				nhap = int(nhap)
			# Chứng chỉ TOEIC
			if y[0] == 0:
				if nhap<325 or nhap>990 or nhap != int(nhap):
					for i in range(5): 
						S.append(0)
				else:
					# Tạo chuỗi chứa các mốc điểm quy đổi được
					T = [325]
					t = 325
					while t<650:
						if t>=500:
							t+=10
						elif t>=425:
							t+=15
						else:
							t+=20
						T.append(t)
					# Quy đổi điểm chứng chỉ quốc tế thành điểm AV1-AV5
					S = diem([7.5, 5.0, 0, 0, 0], T, nhap)
			# Chứng chỉ IELTS
			elif y[0] == 1:
				if nhap<4 or nhap>9:
					for i in range(5): 
						S.append(0)
				elif nhap<4.5:
					for i in range(4):
						S.append(10)
					S.append(7.5)
				elif nhap>=4.5:
					for i in range(5):
						S.append(10)
			# Chứng chỉ TOEFL IBT 
			elif y[0] == 2:
				if nhap<32 or nhap>120 or nhap != int(nhap):
					for i in range(5): 
						S.append(0)
				else:
					# Tạo chuỗi chứa các mốc điểm quy đổi được
					IBT = []
					for ibt in range(32,42):
						IBT.append(ibt)
					# Quy đổi điểm chứng chỉ quốc tế thành điểm AV1-AV5
					S = diem([10.0, 10.0, 10.0, 8.0, 5.5], IBT, nhap)
			# Chứng chỉ TOEFL ITP 
			elif y[0] == 3:
				if nhap<406 or nhap>677 or nhap != int(nhap):
					for i in range(5): 
						S.append(0)
				else:
					# Tạo chuỗi chứa các mốc điểm quy đổi được
					ITP = [406]
					itp = 406
					while itp<500:
						if itp>=460:
							itp+=4
						else:
							itp+=6
						ITP.append(itp)
					# Quy đổi điểm chứng chỉ quốc tế thành điểm AV1-AV5
					S = diem([10.0, 8, 5.5, 0, 0], ITP, nhap)
		# Các chương trình CELL không được phép nhập điểm
		else:
			if y[0] == 4:
				S = CELL[0]
			elif y[0] == 5:
				S = CELL[1]
			elif y[0] == 6:
				S = CELL[2]
			elif y[0] == 7:
				S = CELL[3]
			elif y[0] == 8:
				S = CELL[4]
	    
	    # Thêm listvariable mới vào listbox kết quả LB2 
		if nhap != '': # quy đổi chứng chỉ quốc tế cần nhập điểm
			LB2.insert(0,'<*Quy đổi {} điểm {}*>'.format(nhap, A[y[0]]))
		else:          # quy đổi chương trình CELL
			LB2.insert(0,'<*Quy đổi khi đỗ {}*>'.format(A[y[0]]))
		for i in range(5):
			if S[i] == 0:
				S[i] = 'không quy đổi được'
		for i in range(1,6):
			LB2.insert(i,'AV{}: '.format(i)+str(S[i-1])+' điểm')
		L3.configure(text='Quy đổi thành công')

# Frame hình nền 
f0 = Frame(w, bg='purple', width=800, height=500)
f0.place(relx=0.5, rely=0.5, anchor='center')

# Frame chọn chứng chỉ quốc tế 
f1 = Frame(w, bg='blue')
f1.place(relx=0.25, rely=0.5, anchor=CENTER)
L1 = Label(f1, text='CHỨNG CHỈ QUỐC TẾ & CHƯƠNG TRÌNH', font=('arial', 15), fg='white', bg='blue')
L1.grid(row=0, column=0, padx=30, pady=30)
LB1 = Listbox(f1, listvariable=x1, font=('arial', 15), width=30, fg='yellow', bg='black', selectmode=SINGLE)
LB1.grid(row=1, column=0, padx=30, pady=30)

# Frame nhập điểm, quy đổi và kết quả
f2 = Frame(w, bg='blue')
f2.place(relx=0.75, rely=0.5, anchor=CENTER)
L2 = Label(f2, text='NHẬP ĐIỂM', font=('arial', 15), fg='white', bg='blue')
L2.grid(row=0, column=0, padx=30, pady=5)
E = Entry(f2, width=25, bd=10, font=('arial,15'))
E.grid(row=1, column=0, padx=30, pady=10)
B = Button(f2, text='QUY ĐỔI', font=('arial, 13'), fg='black', bg='green', width=25, bd=10, command=click)
B.grid(row=2, column=0, padx=30, pady=10)
L3 = Label(f2, text='KẾT QUẢ', font=('arial', 15), fg='white', bg='blue')
L3.grid(row=3, column=0, padx=30, pady=5)
LB2 = Listbox(f2, listvariable=x2, font=('arial', 15), width=30, height=7, fg='yellow', bg='black', selectmode=MULTIPLE)
LB2.grid(row=4, column=0, padx=30, pady=5)

# Cảnh báo ở phía trên chương trình
L3 = Label(w, text='Vui lòng chọn một chứng chỉ quốc tế hoặc chương trình', fg='red', bg='purple', font=('arial', 20, 'bold'))
L3.pack(side=TOP)
def color_changer(): # Tạo hiệu ứng cho cảnh báo 
	colors = ["black", "red" , "green" , "blue"]
	fg = random.choice(colors)
	L3.config(fg = fg)
	L3.after(500, color_changer)
color_changer()

# Lưu ý ở phía dưới chương trình
L4 = Label(w, text='* Lưu ý: Nếu bạn đỗ các chương trình CELL thì chỉ cần chọn, không cần nhập điểm', fg='black', bg='purple', font=('arial', 15, 'bold'))
L4.pack(side=BOTTOM)

w.mainloop()