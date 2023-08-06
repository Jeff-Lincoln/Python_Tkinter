import tkinter as tk
from tkinter.ttk import Combobox
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry('500x600')
root.title("STUDENT MANAGEMENT SYSTEM")

bg_color = '#273b7a'

login_stud_icon = tk.PhotoImage(file='images/login_student_img.png')
login_admin_icon = tk.PhotoImage(file='images/admin_img.png')
add_student_icon = tk.PhotoImage(file='images/add_student_img.png')
locked_icon = tk.PhotoImage(file='images/locked.png')
unlocked_icon = tk.PhotoImage(file= 'images/unlocked.png')

add_student_pic_icon = tk.PhotoImage(file='images/add_image.png')

def confirmation_box(message):

    answer = tk.BooleanVar()
    answer.set(False)

    def action(ans):
        answer.set(ans)
        confirmation_box_fm.destroy()

    confirmation_box_fm = tk.Frame(root, highlightbackground=bg_color, 
                                   highlightthickness=3)
    
    message_lb = tk.Label(confirmation_box_fm, text= message, font=('Bold', 15))
    message_lb.pack(pady=20)
    confirmation_box_fm.place(x=100,y=120,width=320, height=220)

    cancel_btn = tk.Button(confirmation_box_fm, text='Cancel', font=('Bold', 15),
                           bd=0, bg=bg_color, fg='white',
                           command= lambda: action(False))
    cancel_btn.place(x=50, y=160)

    yes_btn = tk.Button(confirmation_box_fm, text='Yes', font=('Bold', 15),
                           bd=0, bg=bg_color, fg='white',
                           command= lambda: action(True))
    yes_btn.place(x=190, y=160, width=80)

    confirmation_box_fm.place(x=100, y=120, width=320, height=220)


    root.wait_window(confirmation_box_fm)
    return answer.get()

def  message_box(message):
    message_box_fm = tk.Frame(root, highlightbackground=bg_color, 
                                   highlightthickness=3)
    message_box_fm.place(x=100, y=120, width=320, height=200)

    message_lb = tk.Label(message_box_fm, text=message, font=('Bold', 15),
                          )
    message_lb.pack(pady=50)

    close_btn = tk.Button(message_box_fm, text='X', bd=0, font=('Bold', 13),
                          fg=bg_color, command=lambda: message_box_fm.destroy())
    close_btn.place(x=290, y= 5)


#the welcome page
def welcome_page():
    
    def forward_to_student_Login_age():
        welcome_page_fm.destroy()
        root.update()
        student_login_page()

    def forward_to_admin_Login_age():
        welcome_page_fm.destroy()
        root.update()
        admin_login_page()

    def forward_to_add_account_page():
        welcome_page_fm.destroy()
        root.update()
        add_account_page()


    welcome_page_fm = tk.Frame(root, highlightbackground=bg_color, highlightthickness=3 )

    heading_lb = tk.Label(welcome_page_fm,
                       text='Welcome to Student Registration\n&& Management System ',
                       bg=bg_color, fg='white', font=('bold', 18))
    heading_lb.place(x=0, y=0, width=400)

    student_login_btn = tk.Button(welcome_page_fm, text='Login Student',
                              bg= bg_color, fg='white', font=('Bold', 15), bd=8,
                              command=forward_to_student_Login_age)
    student_login_btn.place(x=120, y=125, width=200)

    student_login_img = tk.Button(welcome_page_fm, image=login_stud_icon, bd=0,
                                  command=forward_to_student_Login_age)
    student_login_img.place(x=60, y=100,)

    admin_login_btn = tk.Button(welcome_page_fm, text='Login Admin',
                              bg= bg_color, fg='white', font=('Bold', 15), bd=8,
                              command=forward_to_admin_Login_age)
    admin_login_btn.place(x=120, y=225, width=200)

    admin_login_img = tk.Button(welcome_page_fm, image=login_admin_icon, bd=0,
                                command=forward_to_admin_Login_age)
    admin_login_img.place(x=60, y=200,)

    add_student_btn = tk.Button(welcome_page_fm, text='Create Account',
                              bg= bg_color, fg='white', font=('Bold', 15), bd=0,
                              command=forward_to_add_account_page)
    add_student_btn.place(x=120, y=325, width=200)

    add_student_img = tk.Button(welcome_page_fm, image=add_student_icon, bd=0,
                                command=forward_to_add_account_page)
    add_student_img.place(x=60, y=300,)

    welcome_page_fm.pack(pady=30)
    welcome_page_fm.pack_propagate(False)
    welcome_page_fm.configure(width=400, height=420)

#another page(student_login_page)
def student_login_page():
    def show_hide_password():
        if password_ent['show'] == '*':
            password_ent.config(show='')
            show_hide_btn.config(image=unlocked_icon) 
        else:
            password_ent.config(show='*')
            show_hide_btn.config(image=locked_icon) 
    
    def forward_to_welcome_page():
       student_login_page_fm.destroy()
       root.update()
       welcome_page()


    student_login_page_fm = tk.Frame(root, highlightbackground=bg_color,
                                    highlightthickness=3)

    head_lb= tk.Label(student_login_page_fm, text= "Student Login Page", bg=bg_color,
                    fg='white', font=('bold', 18))
    head_lb.place(x=0, y=0,width=400)

    back_btn = tk.Button(student_login_page_fm, text='⏮', font=('Bold', 20),
                         fg=bg_color, bd=0, command=forward_to_welcome_page)
    back_btn.place(x=5, y=40)

    stud_icon_lb= tk.Label(student_login_page_fm, image=login_stud_icon)
    stud_icon_lb.place(x=150, y=40)

    id_number_lb= tk.Label(student_login_page_fm, text='Enter Student ID Number.',
                        font=('Bold', 15),fg=bg_color)
    id_number_lb.place(x=80, y=140)

    id_number_ent = tk.Entry(student_login_page_fm, font=('Bold', 15),
                            justify=tk.CENTER, highlightcolor=bg_color,
                            highlightbackground='gray', highlightthickness=2)
    id_number_ent.place(x=80, y= 190)

    password_lb= tk.Label(student_login_page_fm, text='Enter Student Password.',
                        font=('Bold', 15),fg=bg_color)
    password_lb.place(x=80, y=240)

    password_ent = tk.Entry(student_login_page_fm, font=('Bold', 15),
                            justify=tk.CENTER, highlightcolor=bg_color,
                            highlightbackground='gray', highlightthickness=2,
                            show='*')
    password_ent.place(x=80, y= 290)

    show_hide_btn = tk.Button(student_login_page_fm, image=locked_icon, bd=0,
                            command=show_hide_password)
    show_hide_btn.place(x=310, y=280)



    login_btn = tk.Button(student_login_page_fm, text='Login',
                        font=('Bold', 15), bg=bg_color, fg='white')
    login_btn.place(x=95, y=340, width=200, height=40)

    forgot_password_btn = tk.Button(student_login_page_fm, text ='⚠\nForgot Password',
                                    fg=bg_color, bd=0)
    forgot_password_btn.place(x=150, y=390)


    student_login_page_fm.pack(pady=30)
    student_login_page_fm.pack_propagate(False)
    student_login_page_fm.configure(width=400, height=450)

#another page(Admin_login_page)
def admin_login_page():
    def show_hide_password():
            if password_ent['show'] == '*':
                password_ent.config(show='')
                show_hide_btn.config(image=unlocked_icon) 
            else:
                password_ent.config(show='*')
                show_hide_btn.config(image=locked_icon)

    def forward_to_welcome_page():
        admin_login_page_fm.destroy()
        root.update()
        welcome_page()
        

    admin_login_page_fm = tk.Frame(root, highlightbackground=bg_color,
                                highlightthickness=3)

    heading_lb = tk.Label(admin_login_page_fm, text='Admin Login Page',
                        font=('Bold', 18), bg=bg_color, fg='white')
    heading_lb.place(x=0,y=0, width=400)

    back_btn = tk.Button(admin_login_page_fm, text='⏮', font=('Bold', 20),
                         fg=bg_color, bd=0, command=forward_to_welcome_page)
    back_btn.place(x=5, y=40)


    admin_icon_lb = tk.Label(admin_login_page_fm, image=login_admin_icon)
    admin_icon_lb.place(x=150, y=40)



    username_lb= tk.Label(admin_login_page_fm, text='Enter Admin User Name.',
                            font=('Bold', 15),fg=bg_color)
    username_lb.place(x=80, y=140)

    username_ent = tk.Entry(admin_login_page_fm, font=('Bold', 15),
                                justify=tk.CENTER, highlightcolor=bg_color,
                                highlightbackground='gray', highlightthickness=2)
    username_ent.place(x=80, y= 190)

    password_lb= tk.Label(admin_login_page_fm, text='Enter Admin Password.',
                            font=('Bold', 15),fg=bg_color)
    password_lb.place(x=80, y=240)

    password_ent = tk.Entry(admin_login_page_fm, font=('Bold', 15),
                                justify=tk.CENTER, highlightcolor=bg_color,
                                highlightbackground='gray', highlightthickness=2,
                                show='*')
    password_ent.place(x=80, y= 290)

    show_hide_btn = tk.Button(admin_login_page_fm, image=locked_icon, bd=0,
                                command=show_hide_password)
    show_hide_btn.place(x=310, y=280)



    login_btn = tk.Button(admin_login_page_fm, text='Login',
                            font=('Bold', 15), bg=bg_color, fg='white')
    login_btn.place(x=95, y=340, width=200, height=40)



    admin_login_page_fm.pack(pady=30)
    admin_login_page_fm.pack_propagate(False)
    admin_login_page_fm.configure(width=400, height=430)


student_gender =tk.StringVar()
class_list = ['1st', '2nd','3rd', '4th']


#the add_account page
def add_account_page():

    pic_path = tk.StringVar()
    pic_path.set('')

    def open_pic():
        path = askopenfilename()

        if path:
           
            img = ImageTk.PhotoImage(Image.open(path).resize((100, 100)))
            pic_path.set(path)

            add_pic_btn.config(image=img)
            add_pic_btn.image = img
           

    def forward_to_welcome_page():
        
        ans = confirmation_box(message='Do You Want to Leave \nRegistration form?')
        if ans:
            add_account_page_fm.destroy()
            root.update()
            welcome_page()
    

    def remove_highlight_warning(entry):
        if entry['highlightbackground'] != 'gray':
            if entry.get() != '':
                entry.config(highlightcolor=bg_color,
                       highlightbackground='gray')




    def check_input_validation():
        if student_name_ent.get() == '':
            student_name_ent.config(highlightcolor='red',
                                    highlightbackground='red')
            student_name_ent.focus()
            message_box(message='Student Full Name is Required')
        elif student_age_ent.get() == '':
            student_age_ent.config(highlightcolor='red',
                                    highlightbackground='red')
            student_age_ent.focus()
            message_box(message='Student Age is Required')
        elif student_contact_ent.get() == '':
            student_contact_ent.config(highlightcolor='red',
                                    highlightbackground='red')
            student_contact_ent.focus()
            message_box(message='Student Contact Num is Required')
        elif select_year_btn.get() == '':
            select_year_btn.focus()
            message_box(message='Select Student year of Study')
        elif student_email_ent.get() == '':
            student_email_ent.config(highlightcolor='red',
                                    highlightbackground='red')
            student_email_ent.focus()
            message_box(message='Student Email Address is Required')
        elif account_password_ent.get() == '':
            account_password_ent.config(highlightcolor='red',
                                    highlightbackground='red')
            account_password_ent.focus()
            message_box(message='Create a Password is Required')





    add_account_page_fm = tk.Frame(root, highlightbackground=bg_color,
                                    highlightthickness=3)

    add_pic_section_fm = tk.Frame(add_account_page_fm, highlightbackground=bg_color,
                                highlightthickness=2)
    add_pic_section_fm.place(x=5, y=5, width=105, height=105)

    add_pic_btn = tk.Button(add_pic_section_fm, image=add_student_pic_icon,
                            bd=0, command=open_pic)
    add_pic_btn.pack()
    
    student_name_lb = tk.Label(add_account_page_fm, text='Enter Student Full Name.',
                            font=('Bold', 12))

    student_name_lb.place(x=5, y=130)

    student_name_ent = tk.Entry(add_account_page_fm, font=('Bold', 15),
                                highlightcolor=bg_color, highlightbackground='gray',
                                highlightthickness=2)
    student_name_ent.place(x=5, y=160, width=180)
    student_name_ent.bind('<KeyRelease>',
                          lambda e: remove_highlight_warning(entry=student_name_ent))

    student_gender_lb = tk.Label(add_account_page_fm, text='Select Student Gender',
                                font=('Bold', 12))
    student_gender_lb.place(x=5, y=210)

    male_gender_btn = tk.Radiobutton(add_account_page_fm, text='Male',
                                    font=('Bold, 12'), variable=student_gender,
                                    value='male')
    male_gender_btn.place(x=5, y=235)

    female_gender_btn = tk.Radiobutton(add_account_page_fm, text='Female',
                                    font=('Bold, 12'), variable=student_gender,
                                    value='female')
    female_gender_btn.place(x=75, y=235)

    student_gender.set('male')

    student_age_lb = tk.Label(add_account_page_fm, text='Enter Student Age.',
                            font=('Bold', 12))
    student_age_lb.place(x=5, y=275)

    student_age_ent = tk.Entry(add_account_page_fm, font=('Bold', 15),
                                highlightcolor=bg_color, highlightbackground='gray',
                                highlightthickness=2)
    student_age_ent.place(x=5, y=305, width=180)
    student_age_ent.bind('<KeyRelease>',
                          lambda e: remove_highlight_warning(entry=student_age_ent))

    student_contact_lb = tk.Label(add_account_page_fm, text='Enter Contact Phone Number.',
                            font=('Bold', 12))
    student_contact_lb.place(x=5, y=360)

    student_contact_ent = tk.Entry(add_account_page_fm, font=('Bold', 15),
                                highlightcolor=bg_color, highlightbackground='gray',
                                highlightthickness=2)
    student_contact_ent.place(x=5, y=390, width=180)
    student_contact_ent.bind('<KeyRelease>',
                          lambda e: remove_highlight_warning(entry=student_contact_ent))


    student_year_lb = tk.Label(add_account_page_fm, text='Select Student Year of Study..',
                            font=('Bold', 12))
    student_year_lb.place(x=5, y=445)

    select_year_btn = Combobox(add_account_page_fm, font=('Bold', 15),
                                state='readonly', values=class_list)
    select_year_btn.place(x=5, y=475, width=180, height=30)

    student_id_lb = tk.Label(add_account_page_fm, text='Student ID Number:',
                            font=('Bold', 12))
    student_id_lb.place(x=240, y=35)

    student_id = tk.Entry(add_account_page_fm, font=('Bold', 18), bd=0)
    student_id.place(x=380, y=35, width=80)

    student_id.insert(tk.END, '123456')
    student_id.config(state='readonly')

    id_info_lb = tk.Label(add_account_page_fm, text='''Automatically generated ID Number
!Remember Using ID Number
Student will login Account, ''', justify=tk.LEFT)
    id_info_lb.place(x=240, y=65)

    student_email_lb = tk.Label(add_account_page_fm, text='Enter Student Email Address.',
                            font=('Bold', 12))
    student_email_lb.place(x=240, y=130)

    student_email_ent = tk.Entry(add_account_page_fm, font=('Bold', 15),
                                highlightcolor=bg_color, highlightbackground='gray',
                                highlightthickness=2)
    student_email_ent.place(x=240, y=160, width=180)
    student_email_ent.bind('<KeyRelease>',
                          lambda e: remove_highlight_warning(entry=student_email_ent))

    email_info_lb = tk.Label(add_account_page_fm, text='''Via Email Address Student
Can Recover Account
! In Case of Forgetting Password and also
Student will get Future Notification''', justify=tk.LEFT)
    email_info_lb.place(x=240, y=200)

    account_password_lb = tk.Label(add_account_page_fm, text='Create Account Password',
                                font=('Bold', 12))
    account_password_lb.place(x=240, y=275)
   
    account_password_ent = tk.Entry(add_account_page_fm, font=('Bold', 15),
                                highlightcolor=bg_color, highlightbackground='gray',
                                highlightthickness=2)
    account_password_ent.place(x=240, y=307, width=180)
    account_password_ent.bind('<KeyRelease>',
                          lambda e: remove_highlight_warning(entry=account_password_ent))

    account_password_info_lb = tk.Label(add_account_page_fm, text='''Via Student Created Password
And Provided Student ID Number
Student can Login Account''', justify=tk.LEFT)
    account_password_info_lb.place(x=240, y=345)

    home_btn = tk.Button(add_account_page_fm, text='Home', font=('Bold', 15),
                        bg='red', fg='white', bd=0,
                        command=forward_to_welcome_page)
    home_btn.place(x=240, y=420)

    submit_btn = tk.Button(add_account_page_fm, text='Submit', font=('Bold', 15),
                        bg=bg_color, fg='white', bd=0,
                        command=check_input_validation)
    submit_btn.place(x=360, y=420)


    add_account_page_fm.pack(pady=5)
    add_account_page_fm.pack_propagate(False)
    add_account_page_fm.configure(width=480, height=580)

welcome_page()
root.mainloop()
