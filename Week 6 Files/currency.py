### currency.py
### converts between US dollars and Euros

import tkinter

class DollarsAndEuros:
    def __init__(self):
        self.main_win = tkinter.Tk()

        ## make four frames
        self.frame1 = tkinter.Frame()
        self.frame2 = tkinter.Frame()
        self.frame3 = tkinter.Frame()
        self.frame4 = tkinter.Frame()

        #frame1
        self.factor_lab = tkinter.Label(self.frame1,text='Conversion Factor')
        self.factor_box = tkinter.Entry(self.frame1,width=10)
        self.factor_lab.pack(side='left')
        self.factor_box.pack(side='left')

        #frame2
        self.amt_lab = tkinter.Label(self.frame2,text='Amount to Convert')
        self.amt_box = tkinter.Entry(self.frame2,width=10)
        self.amt_lab.pack(side='left')
        self.amt_box.pack(side='left')        

        #frame3
        self.converted_lab = tkinter.Label(self.frame3,text='Converted Amount')
        # we create a StringVar object to associate with the output label
        self.result = tkinter.StringVar()
        self.result_lab = tkinter.Label(self.frame3,textvariable = self.result)
        self.converted_lab.pack(side='left')
        self.result_lab.pack(side='left') 

        #frame4
        self.us2euros_butt = tkinter.Button(self.frame4,text='US to Euros',command=self.us2euros)
        self.euros2us_butt = tkinter.Button(self.frame4,text='Euros to US',command=self.euros2us)
        self.quit_butt = tkinter.Button(self.frame4,text='Quit',command=self.main_win.destroy)
        self.us2euros_butt.pack(side='left')
        self.euros2us_butt.pack(side='left')
        self.quit_butt.pack(side='left')        
        
        ## pack frames into main window
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
        
        tkinter.mainloop()

    def us2euros(self):
        fact = float(self.factor_box.get())
        us = float(self.amt_box.get())
        ## do the math
        euros = fact * us
        self.result.set(euros)

    def euros2us(self):
        fact = float(self.factor_box.get())
        euros = float(self.amt_box.get())
        ## do the math
        us = euros / fact
        self.result.set(us)
        
gui = DollarsAndEuros()  ## makes a GUI instance
        
