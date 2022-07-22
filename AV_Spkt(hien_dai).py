from tkinter import *
import random
from tkinter import filedialog
from PIL import ImageGrab
from tkinter import messagebox

class My_GUI:
	def __init__(self, w, w1, w2, w3, A, x1, Font_size, M, no_change): # w, w1, w2, w3: 4 cửa sổ giao diện
		self.master = w                                                # A, x1, Font_size, M, no_change: các đối tượng nằm trong lớp các cửa sổ giao diện
		self.window_1 = w1
		self.window_2 = w2
		self.window_3 = w3
		self.Font_size = Font_size
		self.A = A
		self.no_change = no_change

		# master
		self.master.config(bg='purple')
		
		self.L0_1 = Label(w, text='APP QUY ĐỔI ĐIỂM AV_Spkt '+'\u270D', fg='yellow', bg='purple', font=('Times New Roman', 25, 'bold'))
		self.L0_1.place(relx=0.5, rely=0.25, anchor='center')
		self.L0_2 = Label(w, text='\u261E'+' Welcome to my app\nDEVELOPER\nNGO VAN MON', bg='purple', font=('Arial', 25, 'bold'))
		self.L0_2.place(relx=0.5, rely=0.5, anchor='center')
		self.B0 = Button(w, text='App information', font=('arial, 15'), fg='white', bg='green', bd=10, command=self.button_infor_app)
		self.B0.place(relx=0.5, rely=0.75, anchor='center')
		self.L0_3 = Label(w, text='Mời bạn xem thông tin về app hoặc nhấn "Enter" để tiếp tục', font=('Times New Roman', 15, 'italic', 'bold'), fg='black', bg='purple')
		self.L0_3.place(relx=0.5, rely=0.9, anchor='center')
		
		self.color_changer()
		self.master.bind('<Return>', self.enter_quy_doi)
        
        # window_1
		self.window_1.config(bg='purple')

		self.f1_1 = Frame(w1, bg='blue', width=800, height=500)
		self.f1_1.pack(side=TOP)
		self.L1_1 = Label(self.f1_1, text='     Chào mừng bạn đến với app "Quy đổi AV_Spkt". App giúp các bạn SV hệ đại trà và chất lượng cao Tiếng Việt trường ĐH SPKT Tp.HCM có thể dễ dàng dùng các chứng chỉ Quốc tế hoặc chương trình Tiếng Anh quy đổi sang điểm các học phần Anh Văn trong chương trình học của trường.\n', \
			font=('Times New Roman', 15), bg='blue', fg='White', wraplengt=800, justify='left')
		self.L1_1.grid(row=0, column=0, sticky=W)

		self.L1_2 = Label(self.f1_1, text='     Sau khi đọc xong thông tin ở mục "App information" này, mời bạn click "OK đã hiểu" để về trang chủ và nhấn "Enter" trên bàn phím để bắt đầu trải nghiệm dịch vụ mà app đem lại.\n\n     Mở đầu với trang chọn, nhập và quy đổi, mời bạn chọn một chứng chỉ quốc tế hoặc chương trình, sau đó nhập điểm (trừ trường hợp quy đổi chương trình CELL chỉ cần chọn thể hiện đã đỗ nên không cần nhập điểm).Bước cuối cùng là nhấn "Enter" hoặc click vào "Quy đổi" và bạn đến trang kết quả. Lưu ý, khi bạn thao tác lỗi, chương trình sẽ đưa ra những cảnh báo lỗi buộc bạn phải thực hiện lại. Ngoài ra, việc nhấn "Backspace" để xóa kí tự bạn muốn xóa ở thanh nhập điểm sẽ không làm cho cửa sổ giao diện trở về trang chủ.\n\n     Kết thúc với trang kết quả, bạn sẽ thấy một bảng kết quả và bạn hoàn toàn có thể gõ thêm nội dung trên bảng này tùy ý bạn. Trên thanh menu của trang có các công cụ gồm "Edit" giúp bạn điều chỉnh kích cỡ nội dung bảng kết quả, "Save" giúp bạn lưu bảng kết quả dưới dạng tệp text *.txt hoặc tệp hình ảnh *.jpg và cuối cùng là "Exit" giúp bạn trở về trang chủ hoặc thực hiện quy đổi tiếp ở trang chọn, nhập và quy đổi.', \
			font=('Times New Roman', 15), bg='blue', fg='White', wraplengt=800, justify='left')
		self.L1_2.grid(row=1, column=0, sticky=W)

		self.L1_3 = Label(self.f1_1, text='CHÚC BẠN CÓ TRẢI NGHIỆM TỐT TRÊN APP, MÌNH SẴN SÀNG ĐÓN NHẬN GÓP Ý VỀ NHỮNG HẠN CHẾ CỦA APP ĐỂ UPDATE APP OK HƠN.', \
			font=('Times New Roman', 15, 'bold'), bg='blue', fg='black', wraplengt=800, justify='left')
		self.L1_3.grid(row=2, column=0, sticky=W)

		self.f1_2 = Frame(w1, bg='purple')
		self.f1_2.pack(side=BOTTOM)
		self.L1_4 = Label(self.f1_2, text='DEVELOPER\nNGO VAN MON', font=('Times New Roman', 20, 'bold'), fg='yellow', bg='purple')
		self.L1_4.grid(row=0, column=0, padx=120)
		self.B1 = Button(self.f1_2, text='OK đã hiểu', font=('Times New Roman', 20, 'bold'), fg='red', bg='yellow', bd=5, relief=RAISED, command=self.return_trang_chu_1)
		self.B1.grid(row=0, column=1, padx=120)

		# window_2
		self.window_2.config(bg='blue')
		
		self.f2_1 = Frame(w2, bg='purple', width=800, height=50)
		self.f2_1.pack(side=TOP)
		self.L2_1 = Label(self.f2_1, text='Have a nice day !!!', font=('Times New Roman', 20, 'bold'), fg='red', bg='purple')
		self.L2_1.place(relx=0.5, rely=0.5, anchor=CENTER)
		
		self.L2_3 = Label(w2, text='CHỨNG CHỈ QUỐC TẾ & CHƯƠNG TRÌNH', font=('Times New Roman', 15), fg='white', bg='blue')
		self.L2_3.place(relx=0.25, rely=0.2, anchor=CENTER)
		self.LB2 = Listbox(w2, listvariable=x1, font=('Arial', 15), fg='yellow', bg='black', width=35, selectmode=SINGLE)
		self.LB2.place(relx=0.25, rely=0.6, anchor=CENTER)
		
		self.L2_4 = Label(w2, text='NHẬP ĐIỂM', font=('Times New Roman', 15), fg='white', bg='blue')
		self.L2_4.place(relx=0.75, rely=0.2, anchor=CENTER)
		self.E2 = Entry(w2, width=29, bd=10, font=('Times New Roman',15,'bold'))
		self.E2.place(relx=0.75, rely=0.4, anchor=CENTER)
		self.B2_1 = Button(w2, text='Quy đổi (Enter)', font=('Times New Roman', 15, 'bold'), fg='black', bg='green', width=25, bd=5, command=self.enter_ket_qua_1)
		self.B2_1.place(relx=0.75, rely=0.6, anchor=CENTER)
		self.B2_2 = Button(w2, text='Trở lại trang chủ (Backspace)', font=('Times New Roman', 15, 'bold'), fg='black', bg='green', width=25, bd=5, command=self.return_trang_chu_1)
		self.B2_2.place(relx=0.75, rely=0.8, anchor=CENTER)

		self.f2_2 = Frame(w2, bg='purple', width=800, height=50)
		self.f2_2.pack(side=BOTTOM)
		self.L2_2 = Label(self.f2_2, text='Welcome to my app :))', font=('Times New Roman', 20, 'bold'), fg='red', bg='purple')
		self.L2_2.place(relx=0.5, rely=0.5, anchor=CENTER)
        
		self.window_2.bind('<BackSpace>', self.return_trang_chu_2)
		self.window_2.bind('<Return>', self.enter_ket_qua_2)
		self.E2.bind('<BackSpace>', self.nothing)         

        # window_3 
		self.f3_1 = Frame(w3, bg='purple', width=800, height=50)
		self.f3_1.pack(side=TOP)
		self.L3_1 = Label(self.f3_1, text='Exchanged successfully !!!', font=('Times New Roman', 20), fg='red', bg='purple')
		self.L3_1.place(relx=0.5, rely=0.5, anchor=CENTER)

		self.f3_2 = Frame(w3, bg='purple', width=800, height=50)
		self.f3_2.pack(side=BOTTOM)
		self.L3_2 = Label(self.f3_2, text='Thanks for using my app :))', font=('Times New Roman', 20, 'bold'), fg='red', bg='purple')
		self.L3_2.place(relx=0.5, rely=0.5, anchor=CENTER)

		self.T3 = Text(w3, font=('Times New Roman', 20, 'bold'), bg='blue', fg='White', width=800, height=500)
		self.T3.pack()

		self.edit_menu = Menu(M, tearoff=0)
		M.add_cascade(label='Edit', menu=self.edit_menu)
		self.edit_menu.add_radiobutton(label='50%', value=1, variable=Font_size, command=self.scale_change)
		self.edit_menu.add_radiobutton(label='100%', value=2, variable=Font_size, command=self.scale_change)
		self.edit_menu.add_radiobutton(label='150%', value=3, variable=Font_size, command=self.scale_change)
		self.edit_menu.add_radiobutton(label='200%', value=4, variable=Font_size, command=self.scale_change)

		self.save_menu = Menu(M, tearoff=0)
		M.add_cascade(label='Save', menu=self.save_menu)
		self.save_menu.add_command(labe='Type *.txt', command=self.Save_txt)
		self.save_menu.add_command(labe='Type *.jpg', command=self.Save_jpg)

		self.exit_menu = Menu(M, tearoff=0)
		M.add_cascade(label='Exit', menu=self.exit_menu)
		self.exit_menu.add_command(labe='Tới trang chủ', command=self.return_trang_chu_1)
		self.exit_menu.add_command(labe='Quy đổi tiếp', command=self.tiep_tuc_quy_doi)

	def scale_change(self): # thay đổi kích thước text
	   a = self.Font_size.get()
	   if a == 1:
	      self.T3.config(font=('Times New Roman', 10, 'bold'))
	   elif a == 2:
	      self.T3.config(font=('Times New Roman', 20, 'bold'))
	   elif a == 3:
	      self.T3.config(font=('Times New Roman', 30, 'bold'))
	   else:
	      self.T3.config(font=('Times New Roman', 40))
	
	def Save_txt(self): # lưu Text dạng txt
	   X = filedialog.asksaveasfilename(title='SAVE AS', filetype=(('text document','*.txt'),('All type','*.*')), defaultextension='.txt')
	   if X != '':
	      with open(X,'w',encoding='utf-8') as f:
	         A = self.T3.get('1.0', END)
	         f.write(A)
	         f.close()
	      messagebox.showinfo('App Notification', 'Text document has been saved as '+str(X))
	
	def Save_jpg(self): # lưu Text dạng jpg
	   X = filedialog.asksaveasfilename(title='SAVE AS', filetype=(('Image','*.jpg'),('All type','*.*')), defaultextension='.jpg')
	   if X != '':
	      x = self.window_3.winfo_rootx()+self.T3.winfo_x()
	      y = self.window_3.winfo_rooty()+self.T3.winfo_y()

	      x1 = x+self.T3.winfo_width()
	      y1 = y+self.T3.winfo_height()

	      ImageGrab.grab().crop((x, y, x1, y1)).save(X)
	      messagebox.showinfo('App Notification', 'Image document has been saved as '+str(X))
	
	def color_changer(self): # Tạo hiệu ứng màu sắc cho Lable trang chủ
		colors = ["black", "red", "green", "blue", "white"]
		fg = random.choice(colors)
		self.L0_2.config(fg=fg)
		self.L0_2.after(300, self.color_changer)
    
	def refresh(self): # Làm mới trang chọn, nhập và quy đổi
		self.E2.delete(0, END)
		self.LB2.selection_clear(0, END)
	
	def nothing(self, no_change): # Setup value no_change bằng 1 khi nhấn "Backspace" để xóa kí tự ở Entry E2
		self.no_change.set(1)
	
	# Ẩn & hiện cửa sổ (chỉ hiện cửa sổ người dùng cần tương tác)
	def active(self, a, b, c, d):
		s = [self.master, self.window_1, self.window_2, self.window_3]
		for i in s:
			if i == a:
				i.deiconify()
			else: i.withdraw()
	
	def button_infor_app(self): # Hiện window_1
		self.active(self.window_1, self.master, self.window_2, self.window_3)
	
	def tiep_tuc_quy_doi(self): # Hiện window_2
		self.refresh()
		self.active(self.window_2, self.master, self.window_1, self.window_3)
	
	def enter_quy_doi(self, enter_quy_doi): # Hiện window_2
		self.tiep_tuc_quy_doi()

	def return_trang_chu_1(self): # Hiện trang chủ
		self.refresh()
		self.active(self.master, self.window_1, self.window_2, self.window_3)
	
	def return_trang_chu_2(self, return_trang_chu_2): # Hiện trang chủ
		if self.no_change.get() == 1:
			self.no_change.set(0)
			return
		X = messagebox.askquestion('Rời trang?', 'Bạn có muốn trở lại trang chủ không?')
		if X =='yes':
			self.refresh()
			self.active(self.master, self.window_1, self.window_2, self.window_3)

	def enter_ket_qua_1(self): # Hiện trang kết quả
		if self.chon_nhap() == True:
			self.active(self.window_3, self.master, self.window_1, self.window_2)
			self.quy_doi()
			self.T3.config(font=('Times New Roman', 20, 'bold'))
			self.Font_size.set(2)
	
	def enter_ket_qua_2(self, enter_ket_qua_2): # Hiện trang kết quả
		self.enter_ket_qua_1()		
	
	def isfloat(self,num): # Check số thực
		try:
			float(num)
			return True
		except ValueError:
			return False

	def chon_nhap(self): # Đưa ra cảnh báo cho người dùng khi thao tác lỗi 
		y = self.LB2.curselection()
		nhap = self.E2.get()
		if len(y) == 0:
			return messagebox.showerror('Error', 'Vui lòng chọn một chứng chỉ quốc tế hoặc chương trình')
		elif y[0]<4 and nhap == '':
			return messagebox.showerror('Error', 'Chưa nhập điểm')
		elif nhap != '' and y[0]>=4 :
			return messagebox.showerror('Error', 'Yêu cầu không nhập điểm khi quy đổi chương trình CELL') 
		elif self.isfloat(nhap) == False and nhap != '':
			return messagebox.showerror('Error', 'Yêu cầu nhập điểm bằng số')
		return True
	
	# Hàm quy đổi (s: chuỗi chứa các điểm AV quy đổi được ở mốc điểm đầu tiên, T: chuỗi chứa các mốc điểm có thế quy đổi được)
	def diem(self,s,T,nhap):
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
			
			# Trường hợp giá trị nhap trùng với một mốc điểm quy đổi được
			if nhap in T:
				return p[T.index(nhap)]	# Trả về chuỗi điểm AV tương ứng
			
			# Trường hợp giá trị nhap không trùng với một mốc điểm quy đổi được
			T.append(nhap)
			T.sort()
			return p[T.index(nhap)-1] # Trả về chuỗi điểm AV tương ứng

	# Quy đổi và điền kết vào trang kết quả
	def quy_doi(self): 
		self.T3.delete('1.0', END)
		y = self.LB2.curselection()
		nhap = self.E2.get()
		
		# Điểm quy đổi AV1-AV5 khi đỗ các chương trình CELL (COMM3-COMM7)
		CELL = [[7.5, 5.0, 0, 0, 0], [10.0, 7.5, 5.0, 0, 0], [10.0, 10.0, 7.5, 5.0, 0], [10.0, 10.0, 10.0, 7.5, 5.0], [10.0, 10.0, 10.0, 10.0, 7.5]]
		S = [] # chuỗi chứa các điểm AV1-AV5 được quy đổi ra
		
		# Thực hiện quy đổi
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
					S = self.diem([7.5, 5.0, 0, 0, 0], T, nhap)
			
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
					S = self.diem([10.0, 10.0, 10.0, 8.0, 5.5], IBT, nhap)
			
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
					S = self.diem([10.0, 8, 5.5, 0, 0], ITP, nhap)
		
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

		# Ghi kết quả vào T3 
		if nhap != '': # quy đổi chứng chỉ quốc tế cần nhập điểm
			self.T3.insert(INSERT,'<*Quy đổi {} điểm {}*>\n'.format(nhap, self.A[y[0]]))
		else:          # quy đổi chương trình CELL
			self.T3.insert(INSERT,'<*Quy đổi khi đỗ {}*>\n'.format(self.A[y[0]]))
		for i in range(5):
			if S[i] == 0:
				S[i] = 'không quy đổi được'
		for i in range(5):
			self.T3.insert(INSERT,'AV{}: '.format(i+1)+str(S[i])+' điểm\n')

def main():
	w = Tk()
	w.title('Programming: Quy đổi điểm AV Spkt cho SV hệ đại trà và chất lượng cao Tiếng Việt')
	w.geometry('800x500+300+100')
	w.resizable(False, False)

	w1 = Toplevel()
	w1.geometry('800x550+300+100')
	w1.title('App information')
	w1.resizable(False, False)

	w2 = Toplevel()
	w2.geometry('800x500+300+100')
	w2.title('Chọn chứng chỉ và nhập điểm')
	w2.resizable(False, False)

	w3 = Toplevel()
	w3.geometry('800x500+300+100')
	w3.title('Kết quả quy đổi')
	w3.resizable(False, False)

	A = ['TOEIC', 'IELTS', 'TOEFL IBT', 'TOEFL ITP', 'CELL-COMM3', 'CELL-COMM4', 'CELL-COMM5', 'CELL-COMM6', 'CELL-COMM7']
	x1 = StringVar(value=A)
	Font_size = IntVar()
	no_change = IntVar()
	M = Menu(w3)
	w3.config(menu=M)

	w1.withdraw()
	w2.withdraw()
	w3.withdraw()	

	My_GUI(w, w1, w2, w3, A, x1, Font_size, M, no_change)

	w.mainloop()

if __name__ == '__main__':
	main()