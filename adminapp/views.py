from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
import datetime
import mysql.connector
from django.core.files.storage import FileSystemStorage

def getdb():
    mydb = mysql.connector.connect(host="localhost",user="root", passwd="",database="jewellery_db")
    return mydb

def index(request):
    try:
        feedback = "select count(f_id) from feedback_tb" 
        mydb = getdb()
        mycursor = mydb.cursor()
        #query execute
        mycursor.execute(feedback)
        feedbackcount = mycursor.fetchall()

        pendingorder = "select count(o_id) from order_tb,user_tb where order_tb.u_id = user_tb.u_id and order_tb.o_status='Pending'" 
        mydb = getdb()
        mycursor = mydb.cursor()
        #query execute
        mycursor.execute(pendingorder)
        pendingordercount = mycursor.fetchall()

        confirmorder = "select count(o_id) from order_tb,user_tb where order_tb.u_id = user_tb.u_id and order_tb.o_status='Confirm'" 
        mydb = getdb()
        mycursor = mydb.cursor()
        #query execute
        mycursor.execute(confirmorder)
        confirmordercount = mycursor.fetchall()

        completeorder = "select count(o_id) from order_tb,user_tb where order_tb.u_id = user_tb.u_id  and order_tb.o_status='Complete'" 
        mydb = getdb()
        mycursor = mydb.cursor()
        #query execute
        mycursor.execute(completeorder)
        completeordercount = mycursor.fetchall()

        
        cancelorder = "select count(o_id) from order_tb,user_tb where order_tb.u_id = user_tb.u_id and order_tb.o_status='Cancel'" 
        mydb = getdb()
        mycursor = mydb.cursor()
        #query execute
        mycursor.execute(cancelorder)
        cancelordercount = mycursor.fetchall()

        staff = "select count(s_id) from staff_tb" 
        mydb = getdb()
        mycursor = mydb.cursor()
        #query execute
        mycursor.execute(staff)
        staffcount = mycursor.fetchall()

        category = "select count(cat_id) from category_tb" 
        mydb = getdb()
        mycursor = mydb.cursor()
        #query execute
        mycursor.execute(category)
        categorycount = mycursor.fetchall()

        product = "select count(p_id) from product_tb,category_tb,staff_tb,subcategory_tb where product_tb.cat_id=category_tb.cat_id and product_tb.s_id=staff_tb.s_id and product_tb.sub_id=subcategory_tb.sub_id" 
        mydb = getdb()
        mycursor = mydb.cursor()
        #query execute
        mycursor.execute(product)
        productcount = mycursor.fetchall()

        subcategory = "select count(sub_id) from subcategory_tb,category_tb where subcategory_tb.cat_id = category_tb.cat_id" 
        mydb = getdb()
        mycursor = mydb.cursor()
        #query execute
        mycursor.execute(subcategory)
        subcategorycount = mycursor.fetchall()

        user = "select count(u_id) from user_tb" 
        mydb = getdb()
        mycursor = mydb.cursor()
        #query execute
        mycursor.execute(user)
        usercount = mycursor.fetchall()

        payment = "select count(payment_tb.p_id) from  payment_tb,order_tb where payment_tb.o_id=order_tb.o_id" 
        mydb = getdb()
        mycursor = mydb.cursor()
        #query execute
        mycursor.execute(payment)
        paymentcount = mycursor.fetchall()

        alldata = {
            'feedbackcount' :feedbackcount,
            'pendingordercount' : pendingordercount,
            'confirmordercount' : confirmordercount,
            'completeordercount' : completeordercount,
            'cancelordercount' : cancelordercount,
            'staffcount' : staffcount,
            'categorycount' : categorycount,
            'productcount' : productcount,
            'subcategorycount' : subcategorycount,
            'usercount' : usercount,
            'paymentcount' : paymentcount,

        }
       
    

        return render(request,'index.html',alldata)
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def category(request):
    try:
         
        if request.GET.get("cat_id") !=None:
            #variable decleration
            cat_id = request.GET.get("cat_id")
            cat_status = request.GET.get("cat_status")

            if cat_status=="Active":
                cat_status="Deactive"
            else:
                cat_status="Active"
            
            #update:

            cid="UPDATE category_tb SET cat_status='"+str(cat_status)+"' where cat_id='"+str(cat_id)+"'"

            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(cid)
            mydb.commit()
            return redirect("category")
        

        elif request.POST:
            cat_name = request.POST.get("cat_name")
           
            cat_img = request.FILES["cat_image"]
            img = FileSystemStorage()
            cat_image = img.save(cat_img.name,cat_img)
            cat_status = request.POST.get("cat_status")
            cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

             #insert query
              
            ins = "INSERT INTO category_tb(cat_name, cat_image, cat_status, cat_cdate, cat_udate) VALUES ('"+str(cat_name)+"','"+str(cat_image)+"','"+str(cat_status)+"','"+cdate+"','"+cdate+"')"
            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(ins)
            mydb.commit()
            return redirect("category")

        elif request.GET.get("cat_del") !=None:
            #variable decleration
            cat_del = request.GET.get("cat_del")

            #insert query

            cdel = "DELETE from category_tb where cat_id = '"+str(cat_del)+"'"

            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(cdel)
            mydb.commit()
            return redirect("category")
        
        else:
            selcat = "select * from category_tb order by cat_id desc" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selcat)
            cat_data = mycursor.fetchall()

            return render(request,'category.html',{'cat_data': cat_data})
    except NameError:
        print("internaal error")
    except:
        print('Error returned')

def categoryedit(request):
    try:
       if request.POST:
           #variable decleration
           cat_edt = request.GET.get("cat_edt")
           cat_name = request.POST.get("cat_name")
           
           if request.POST.get("cat_image") !="":
               cat_img = request.FILES["cat_image"]
               img = FileSystemStorage()
               old_img = img.save(cat_img.name,cat_img)

           else:
               old_img = request.POST.get("old_img")

           cat_status = request.POST.get("cat_status")
           cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
           
           #insert query
           ins = "UPDATE `category_tb` set `cat_name` = '"+str(cat_name)+"', `cat_image` = '"+str(old_img)+"', `cat_status` = '"+str(cat_status)+"', `cat_udate` = '"+cdate+"' where cat_id = '"+str(cat_edt)+"'"
           #query exe - run
           mydb = getdb()
           mycursor = mydb.cursor()
           mycursor.execute(ins)
           mydb.commit()
           return redirect("category")

       else:
            
            cat_edt = request.GET.get("cat_edt")
            selcat = "select * from category_tb where cat_id = '"+str(cat_edt)+"'" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selcat)
            cat_data = mycursor.fetchall() 
            return render(request,'categoryedit.html',{'cat_data': cat_data})

    except NameError:
        print("internal error")
    except:
        print('Error returned')
   
def feedback(request):
    try:
        if request.GET.get("f_id") !=None:
            #variable decleration
            f_id = request.GET.get("f_id")
            f_status = request.GET.get("f_status")

            if f_status=="Show":
                f_status="Hide"
            else:
                f_status="Show"

            #update:

            fid="UPDATE feedback_tb SET f_status='"+str(f_status)+"' where f_id='"+str(f_id)+"'"

            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(fid)
            mydb.commit()
            return redirect("feedback")

        elif request.GET.get("f_del") !=None:
            #variable decleration
            f_del = request.GET.get("f_del")

            #insert query

            fdel = "DELETE from feedback_tb where f_id = '"+str(f_del)+"'"

            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(fdel)
            mydb.commit()
            return redirect("feedback")
        else:
            selfed = "select * from feedback_tb order by f_id desc"
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selfed)
            f_data = mycursor.fetchall()

            return render(request,'feedback.html',{'f_data': f_data})
        
       
    except NameError:
        print("internal error")
    except:
        print('Error returned')
    
def user(request):
    try:
        if request.GET.get("u_id") !=None:
            #variable decleration
            u_id = request.GET.get("u_id")
            u_status = request.GET.get("u_status")

            if u_status=="Active":
                u_status="Deactive"
            else:
                u_status="Active"

            #update:

            uid="UPDATE user_tb SET u_status='"+str(u_status)+"' where u_id='"+str(u_id)+"'"

            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(uid)
            mydb.commit()
            return redirect("user")

        elif request.GET.get("u_del") !=None:
            #variable decleration
            u_del = request.GET.get("u_del")

            #delete query

            udel = "DELETE from user_tb where u_id = '"+str(u_del)+"'"

            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(udel)
            mydb.commit()
            return redirect("user")

        else:    
            selus = "select * from user_tb order by u_id desc"
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selus)
            u_data = mycursor.fetchall()

            return render(request,'user.html',{'u_data': u_data})
        
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def payment(request):
    try:
        if request.GET.get("p_id") !=None:
            #variable decleration
            p_id = request.GET.get("p_id")
            p_status = request.GET.get("p_status")

            if p_status=="Success":
                p_status="Fail"
            else:
                p_status="Success"

            #update:

            pid="UPDATE payment_tb SET p_status='"+str(p_status)+"' where p_id='"+str(p_id)+"'"

            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(pid)
            mydb.commit()
            return redirect("payment")
        
        elif request.GET.get("p_del") !=None:
            #variable decleration
            p_del = request.GET.get("p_del")

            #insert query

            pdel = "DELETE from payment_tb where p_id = '"+str(p_del)+"'"

            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(pdel)
            mydb.commit()
            return redirect("payment")
        else:
            selpy = "select * from payment_tb,order_tb where payment_tb.o_id=order_tb.o_id order by payment_tb.p_id desc"
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selpy)
            p_data = mycursor.fetchall()

            return render(request,'payment.html',{'p_data': p_data})
 
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def subcategory(request):
    try:
        if request.POST:
            
            cat_id = request.POST.get("cat_id")
            sub_name = request.POST.get("sub_name")
           
            sub_img = request.FILES["sub_image"]
            img = FileSystemStorage()
            sub_image = img.save(sub_img.name,sub_img)
            
            sub_status = request.POST.get("sub_status")
            cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

             #insert query
              
            ins = "INSERT INTO `subcategory_tb`(`cat_id`,`sub_name`, `sub_image`, `sub_status`, `sub_cdate`, `sub_udate`) VALUES ('"+str(cat_id)+"','"+str(sub_name)+"','"+str(sub_image)+"','"+str(sub_status)+"','"+cdate+"','"+cdate+"')"
            
            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(ins)
            mydb.commit()
            return redirect("subcategory")
        
        elif request.GET.get("sub_del") !=None:
            #variable decleration
            sub_del = request.GET.get("sub_del")

            #insert query

            ins = "DELETE from `subcategory_tb` where sub_id = '"+str(sub_del)+"'"

            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(ins)
            mydb.commit()
            return redirect("subcategory")

        else:    
            selsubcategory = "select * from subcategory_tb,category_tb where subcategory_tb.cat_id = category_tb.cat_id order by sub_id desc" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selsubcategory)
            sub_data = mycursor.fetchall()

            selcat = "select * from category_tb where cat_status = 'Active' order by cat_id desc" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selcat)
            cat_data = mycursor.fetchall()

            alldata = {
                'sub_data' : sub_data,
                'cat_data' : cat_data
            }

            return render(request,'subcategory.html',alldata)
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def subcategoryedit(request):
    try:
       if request.POST:
           #variable decleration
           sub_edt = request.GET.get("sub_edt")
           
           cat_id = request.POST.get("cat_id")
           sub_name = request.POST.get("sub_name")
           
           if request.POST.get("sub_image") !="":
               sub_img = request.FILES["sub_image"]
               img = FileSystemStorage()
               old_img = img.save(sub_img.name,sub_img)

           else:
               old_img = request.POST.get("old_img")

           sub_status = request.POST.get("sub_status")
           subdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
           
           #insert query
           ins = "UPDATE `subcategory_tb` SET `cat_id`='"+str(cat_id)+"',`sub_name`='"+str(sub_name)+"',`sub_image`='"+str(old_img)+"',`sub_status`='"+str(sub_status)+"',`sub_udate`= '"+subdate+"' WHERE sub_id = '"+str(sub_edt)+"'"
           #query exe - run
           mydb = getdb()
           mycursor = mydb.cursor()
           mycursor.execute(ins)
           mydb.commit()
           return redirect("subcategory")

       else:  
            
            sub_edt = request.GET.get("sub_edt")

            selsubcategory = "select * from subcategory_tb where sub_id = '"+str(sub_edt)+"'" 
            print(selsubcategory)
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selsubcategory)
            sub_data = mycursor.fetchall()

            selcat = "select * from category_tb where cat_status = 'Active'" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selcat)
            cat_data = mycursor.fetchall()

            alldata = {
                'sub_data' : sub_data,
                'cat_data' : cat_data
            }

            return render(request,'subcategoryedit.html',alldata)
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def staff(request):
    try:
        if request.POST:
            s_name = request.POST.get("s_name")
            s_address = request.POST.get("s_address")
            s_contact = request.POST.get("s_contact")

            s_img = request.FILES["s_image"]
            img = FileSystemStorage()
            s_image = img.save(s_img.name,s_img)

            s_password = request.POST.get("s_password")
            s_status = request.POST.get("s_status")
            cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
           
            

            ins = "INSERT INTO `staff_tb` (`s_name`, `s_address`, `s_contact`, `s_image`, `s_password`, `s_status`, `s_cdate`, `s_udate`) VALUES ('"+str(s_name)+"','"+str(s_address)+"','"+str(s_contact)+"','"+str(s_image)+"','"+str(s_password)+"','"+str(s_status)+"','"+cdate+"','"+cdate+"')"
        
            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(ins)
            mydb.commit()
            return redirect("staff")
        
        elif request.GET.get("s_id") !=None:
            #variable decleration
            s_id = request.GET.get("s_id")
            s_status = request.GET.get("s_status")

            if s_status=="Active":
                s_status="Deactive"
            else:
                s_status="Active"

            #update:

            sid="UPDATE staff_tb SET s_status='"+str(s_status)+"' where s_id='"+str(s_id)+"'"

            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(sid)
            mydb.commit()
            return redirect("staff")
        
        elif request.GET.get("s_del") !=None:
            #variable decleration
            s_del = request.GET.get("s_del")

            #insert query

            sdel = "DELETE from staff_tb where s_id = '"+str(s_del)+"'"

            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(sdel)
            mydb.commit()
            return redirect("staff")
        else:
             selstaff = "select * from staff_tb order by s_id desc"
             # connection create object
             mydb = getdb()
             mycursor = mydb.cursor()
             #query execute
             mycursor.execute(selstaff)
             s_data = mycursor.fetchall()

             return render(request,'staff.html',{'s_data': s_data})
        
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def product(request):
    try:
        if request.GET.get("p_id") !=None:
            #variable decleration
            p_id = request.GET.get("p_id")
            p_status = request.GET.get("p_status")

            if p_status=="Active":
                p_status="Deactive"
            else:
                p_status="Active"

            #update:

            pid="UPDATE product_tb SET p_status='"+str(p_status)+"' where p_id='"+str(p_id)+"'"

            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(pid)
            mydb.commit()
            return redirect("product")
        
        elif request.GET.get("p_del") !=None:
            #variable decleration
            p_del = request.GET.get("p_del")

            #delete query

            pdel = "DELETE from product_tb where p_id = '"+str(p_del)+"'"

            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(pdel)
            mydb.commit()
            return redirect("product")
        else:
             selpro = "select * from product_tb,category_tb,staff_tb,subcategory_tb where product_tb.cat_id=category_tb.cat_id and product_tb.s_id=staff_tb.s_id and product_tb.sub_id=subcategory_tb.sub_id order by p_id desc"
             # connection create object
             mydb = getdb()
             mycursor = mydb.cursor()
             #query execute
             mycursor.execute(selpro)
             p_data = mycursor.fetchall()

             return render(request,'product.html',{'p_data': p_data})
        
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def cart(request):
    try:
        if request.POST:
            s_id = request.POST.get("s_id")
            o_id = request.GET.get("order_id")
            ord_status = request.GET.get("ord_status")+ "order"
            lowercase_string = ord_status.lower()
            staffupd = "UPDATE order_tb SET s_id='"+str(s_id)+"' where o_id='"+str(o_id)+"'"

            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(staffupd)
            mydb.commit()
            return redirect(f"/adminapp/{lowercase_string}")
        else:
            o_id = request.GET.get("order_id")
            selcart = "select * from cart_tb,category_tb,subcategory_tb,product_tb,order_tb where order_tb.o_id  = cart_tb.o_id and cart_tb.cat_id=category_tb.cat_id and cart_tb.sub_id=subcategory_tb.sub_id and cart_tb.p_id=product_tb.p_id and cart_tb.o_id = '"+str(o_id)+"'"
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selcart)
            c_data = mycursor.fetchall()

            selstaff = "select * from staff_tb where s_status = 'Active'"
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selstaff)
            s_data = mycursor.fetchall()

            alldata = {
                's_data' : s_data,
                'c_data': c_data

            }

            return render(request,'cart.html',alldata)
        
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def login(request):
    try:
        msg = ""
        if request.POST:
           #variable decleration
           a_username = request.POST.get("a_username")
           a_password = request.POST.get("a_password")
           
           #insert query
           sel = "select * from admin_tb where `a_username` = '"+str(a_username)+"' and a_password = '"+str(a_password)+"'"
           #query exe - run
           mydb = getdb()
           mycursor = mydb.cursor()
           mycursor.execute(sel)
           udata = mycursor.fetchall()

           if len(udata) > 0:
               request.session["name"] = a_username
               request.session["img"] = udata[0][3]
               request.session["time"] = str(udata[0][4])
        
               return redirect("/adminapp")           
           else:
               msg = " Invalid Username or Password.!" 
               return render(request,'login.html',{'msg':msg})          
        else:
            return render(request,'login.html',{'msg':msg})
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def logout(request):
    try:
        
        #variable decleration
        username = request.session["name"]
        cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        #insert query

        ins = "UPDATE `admin_tb` set `a_lastseen` = '"+cdate+"' where a_username = '"+str(username)+"'"

        #query exe - run
        mydb = getdb()
        mycursor = mydb.cursor()
        mycursor.execute(ins)
        mydb.commit()

        request.session["name"] = None
        request.session["img"] = None
        request.session["time"] = None

        return redirect("login")
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def orderreport(request):
    try:
        if request.POST:

            s_date = request.POST.get("s_date")
            e_date = request.POST.get("e_date")            
            o_status = request.POST.get("o_status")
            
            selorder = "SELECT order_tb.*, user_tb.u_name,user_tb.u_contact,  CASE WHEN order_tb.s_id = 0 THEN '-' ELSE staff_tb.s_name END AS s_name, CASE WHEN order_tb.s_id = 0 THEN '-' ELSE staff_tb.s_contact END AS s_contact FROM order_tb JOIN user_tb ON order_tb.u_id = user_tb.u_id LEFT JOIN staff_tb ON order_tb.s_id = staff_tb.s_id WHERE order_tb.o_status = '"+str(o_status)+"'  and DATE(order_tb.o_cdate) between '"+str(s_date)+"' and '"+str(e_date)+"' order by o_id desc" 
        
            #print(selorder)# connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selorder)
            o_data = mycursor.fetchall()
            return render(request,'orderreport.html',{'order_data': o_data})
        else:
            return render(request,'orderreport.html',{})

    except NameError:
        print("internal error")
    except:
        print('Error returned')

def pendingorder(request):
    try:
        if request.GET.get("ord_id") !=None:
            #variable decleration
            o_id = request.GET.get("ord_id")
            o_status = request.GET.get("o_status")

            if o_status=="Pending":
                o_status="Confirm"
            elif o_status=="Confirm":
                o_status="Complete"
            elif o_status=="Complete":
                o_status="Cancel"
            else:
                o_status="Pending"

            #update:

            oid="UPDATE order_tb SET o_status='"+str(o_status)+"' where o_id='"+str(o_id)+"'"

            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(oid)
            mydb.commit()
            return redirect("pendingorder")
            
        elif request.GET.get("o_del") !=None:
            #variable decleration
            o_del = request.GET.get("o_del")

            #insert query

            odel = "DELETE from order_tb where o_id = '"+str(o_del)+"'"

            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(odel)
            mydb.commit()
            return redirect("pendingorder")
        else:
             selor = "SELECT order_tb.*, user_tb.u_name,user_tb.u_contact,  CASE WHEN order_tb.s_id = 0 THEN '-' ELSE staff_tb.s_name END AS s_name, CASE WHEN order_tb.s_id = 0 THEN '-' ELSE staff_tb.s_contact END AS s_contact FROM order_tb JOIN user_tb ON order_tb.u_id = user_tb.u_id LEFT JOIN staff_tb ON order_tb.s_id = staff_tb.s_id WHERE order_tb.o_status = 'Pending' ORDER BY order_tb.o_id DESC"
             # connection create object
             mydb = getdb()
             mycursor = mydb.cursor()
             #query execute
             mycursor.execute(selor)
             o_data = mycursor.fetchall()

             return render(request,'pendingorder.html',{'o_data': o_data})
        
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def confirmorder(request):
    try:
        if request.GET.get("ord_id") !=None:
            #variable decleration
            o_id = request.GET.get("ord_id")
            o_status = request.GET.get("o_status")

            if o_status=="Pending":
                o_status="Confirm"
            elif o_status=="Confirm":
                o_status="Complete"
            elif o_status=="Complete":
                o_status="Cancel"
            else:
                o_status="Pending"

            #update:

            oid="UPDATE order_tb SET o_status='"+str(o_status)+"' where o_id='"+str(o_id)+"'"

            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(oid)
            mydb.commit()
            return redirect("confirmorder")
            
        elif request.GET.get("o_del") !=None:
            #variable decleration
            o_del = request.GET.get("o_del")

            #insert query

            odel = "DELETE from order_tb where o_id = '"+str(o_del)+"'"

            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(odel)
            mydb.commit()
            return redirect("confirmorder")
        else:
             selor = "SELECT order_tb.*, user_tb.u_name,user_tb.u_contact,  CASE WHEN order_tb.s_id = 0 THEN '-' ELSE staff_tb.s_name END AS s_name, CASE WHEN order_tb.s_id = 0 THEN '-' ELSE staff_tb.s_contact END AS s_contact FROM order_tb JOIN user_tb ON order_tb.u_id = user_tb.u_id LEFT JOIN staff_tb ON order_tb.s_id = staff_tb.s_id WHERE order_tb.o_status = 'Confirm' ORDER BY order_tb.o_id DESC"
             # connection create object
             mydb = getdb()
             mycursor = mydb.cursor()
             #query execute
             mycursor.execute(selor)
             o_data = mycursor.fetchall()

             return render(request,'confirmorder.html',{'o_data': o_data})
        
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def completeorder(request):
    try:
        if request.GET.get("ord_id") !=None:
            #variable decleration
            o_id = request.GET.get("ord_id")
            o_status = request.GET.get("o_status")

            if o_status=="Pending":
                o_status="Confirm"
            elif o_status=="Confirm":
                o_status="Complete"
            elif o_status=="Complete":
                o_status="Cancel"
            else:
                o_status="Pending"

            #update:

            oid="UPDATE order_tb SET o_status='"+str(o_status)+"' where o_id='"+str(o_id)+"'"

            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(oid)
            mydb.commit()
            return redirect("completeorder")
            
        elif request.GET.get("o_del") !=None:
            #variable decleration
            o_del = request.GET.get("o_del")

            #insert query

            odel = "DELETE from order_tb where o_id = '"+str(o_del)+"'"

            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(odel)
            mydb.commit()
            return redirect("completeorder")
        else:
             selor = "SELECT order_tb.*, user_tb.u_name,user_tb.u_contact,  CASE WHEN order_tb.s_id = 0 THEN '-' ELSE staff_tb.s_name END AS s_name, CASE WHEN order_tb.s_id = 0 THEN '-' ELSE staff_tb.s_contact END AS s_contact FROM order_tb JOIN user_tb ON order_tb.u_id = user_tb.u_id LEFT JOIN staff_tb ON order_tb.s_id = staff_tb.s_id WHERE order_tb.o_status = 'Complete' ORDER BY order_tb.o_id DESC"
             # connection create object
             mydb = getdb()
             mycursor = mydb.cursor()
             #query execute
             mycursor.execute(selor)
             o_data = mycursor.fetchall()

             return render(request,'completeorder.html',{'o_data': o_data})
        
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def cancelorder(request):
    try:
        if request.GET.get("ord_id") !=None:
            #variable decleration
            o_id = request.GET.get("ord_id")
            o_status = request.GET.get("o_status")

            if o_status=="Pending":
                o_status="Confirm"
            elif o_status=="Confirm":
                o_status="Complete"
            elif o_status=="Complete":
                o_status="Cancel"
            else:
                o_status="Pending"

            #update:

            oid="UPDATE order_tb SET o_status='"+str(o_status)+"' where o_id='"+str(o_id)+"'"

            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(oid)
            mydb.commit()
            return redirect("cancelorder")
            
        elif request.GET.get("o_del") !=None:
            #variable decleration
            o_del = request.GET.get("o_del")

            #insert query

            odel = "DELETE from order_tb where o_id = '"+str(o_del)+"'"

            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(odel)
            mydb.commit()
            return redirect("cancelorder")
        else:
             selor = "SELECT order_tb.*, user_tb.u_name,user_tb.u_contact,  CASE WHEN order_tb.s_id = 0 THEN '-' ELSE staff_tb.s_name END AS s_name, CASE WHEN order_tb.s_id = 0 THEN '-' ELSE staff_tb.s_contact END AS s_contact FROM order_tb JOIN user_tb ON order_tb.u_id = user_tb.u_id LEFT JOIN staff_tb ON order_tb.s_id = staff_tb.s_id WHERE order_tb.o_status = 'Cancel' ORDER BY order_tb.o_id DESC"
             # connection create object
             mydb = getdb()
             mycursor = mydb.cursor()
             #query execute
             mycursor.execute(selor)
             o_data = mycursor.fetchall()

             return render(request,'cancelorder.html',{'o_data': o_data})
        
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def userreport(request):
    try:
        if request.POST:

            s_date = request.POST.get("s_date")
            e_date = request.POST.get("e_date")            
           

            selus = "select * from user_tb where DATE(user_tb.u_cdate) between '"+str(s_date)+"' and '"+str(e_date)+"'  order by u_id desc"
            #print(selorder)# connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selus)
            u_data = mycursor.fetchall()
            return render(request,'userreport.html',{'user_data': u_data})
        else:
            return render(request,'userreport.html',{})

    except NameError:
        print("internal error")
    except:
        print('Error returned')

def feedbackreport(request):
    try:
        if request.POST:

            s_date = request.POST.get("s_date")
            e_date = request.POST.get("e_date")            
           

            selfed = "select * from feedback_tb where DATE(feedback_tb.f_cdate) between '"+str(s_date)+"' and '"+str(e_date)+"' order by f_id desc"
            #print(selorder)# connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selfed)
            f_data = mycursor.fetchall()
            return render(request,'feedbackreport.html',{'feedback_data': f_data})
        else:
            return render(request,'feedbackreport.html',{})

    except NameError:
        print("internal error")
    except:
        print('Error returned')

def paymentreport(request):
    try:
        if request.POST:

            s_date = request.POST.get("s_date")
            e_date = request.POST.get("e_date")            
           

            selpy = "select * from payment_tb,order_tb where payment_tb.o_id=order_tb.o_id AND DATE(payment_tb.p_cdate) between '"+str(s_date)+"' and '"+str(e_date)+"' order by payment_tb.p_id desc"
            #print(selorder)# connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selpy)
            p_data = mycursor.fetchall()
            return render(request,'paymentreport.html',{'payment_data': p_data})
        else:
            return render(request,'paymentreport.html',{})

    except NameError:
        print("internal error")
    except:
        print('Error returned')

def productreport(request):
    try:
        if request.POST:

            s_date = request.POST.get("s_date")
            e_date = request.POST.get("e_date")            
           

            selpro = "select * from product_tb,category_tb,staff_tb,subcategory_tb where product_tb.cat_id=category_tb.cat_id and product_tb.s_id=staff_tb.s_id and product_tb.sub_id=subcategory_tb.sub_id AND DATE(product_tb.p_cdate) between '"+str(s_date)+"' and '"+str(e_date)+"' order by product_tb.p_id desc"
            #print(selorder)# connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selpro)
            p_data = mycursor.fetchall()
            return render(request,'productreport.html',{'product_data': p_data})
        else:
            return render(request,'productreport.html',{})

    except NameError:
        print("internal error")
    except:
        print('Error returned')

def staffedit(request):
    try:
       if request.POST:
           #variable decleration
           s_edt = request.GET.get("s_edt")
           s_name = request.POST.get("s_name")
           s_address = request.POST.get("s_address")
           s_contact = request.POST.get("s_contact")
           
           if request.POST.get("s_image") !="":
               s_img = request.FILES["s_image"]
               img = FileSystemStorage()
               old_img = img.save(s_img.name,s_img)

           else:
               old_img = request.POST.get("old_img")
            
           s_password = request.POST.get("s_password")
           s_status = request.POST.get("s_status")
           cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
           
           #insert query
           ins = "UPDATE `staff_tb` set `s_name` = '"+str(s_name)+"',`s_address` = '"+str(s_address)+"',`s_contact` = '"+str(s_contact)+"', `s_image` = '"+str(old_img)+"', `s_password` = '"+str(s_password)+"',`s_status` = '"+str(s_status)+"', `s_udate` = '"+cdate+"' where s_id = '"+str(s_edt)+"'"
           #query exe - run
           mydb = getdb()
           mycursor = mydb.cursor()
           mycursor.execute(ins)
           mydb.commit()
           return redirect("staff")

       else:
            
            s_edt = request.GET.get("s_edt")
            selcat = "select * from staff_tb where s_id = '"+str(s_edt)+"'" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selcat)
            s_data = mycursor.fetchall() 
            return render(request,'staffedit.html',{'s_data': s_data})

    except NameError:
        print("internal error")
    except:
        print('Error returned')
   
