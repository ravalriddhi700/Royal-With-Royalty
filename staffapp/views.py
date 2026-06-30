from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
import datetime
import mysql.connector
from django.core.files.storage import FileSystemStorage

def getdb():
    mydb = mysql.connector.connect(host="localhost",user="root", passwd="",database="jewellery_db")
    return mydb



def sindex(request):
    try:
        feedback = "select count(f_id) from feedback_tb" 
        mydb = getdb()
        mycursor = mydb.cursor()
        #query execute
        mycursor.execute(feedback)
        feedbackcount = mycursor.fetchall()

        sid = request.session["sid"]      
        pendingorder = "select count(o_id) from order_tb,user_tb where order_tb.u_id = user_tb.u_id and order_tb.o_status='Pending' and order_tb.s_id = '"+str(sid)+"'" 
        mydb = getdb()
        mycursor = mydb.cursor()
        #query execute
        mycursor.execute(pendingorder)
        pendingordercount = mycursor.fetchall()

        confirmorder = "select count(o_id) from order_tb,user_tb where order_tb.u_id = user_tb.u_id and order_tb.o_status='Confirm' and order_tb.s_id = '"+str(sid)+"'" 
        mydb = getdb()
        mycursor = mydb.cursor()
        #query execute
        mycursor.execute(confirmorder)
        confirmordercount = mycursor.fetchall()

        completeorder = "select count(o_id) from order_tb,user_tb where order_tb.u_id = user_tb.u_id and order_tb.o_status='Complete' and order_tb.s_id = '"+str(sid)+"'" 
        mydb = getdb()
        mycursor = mydb.cursor()
        #query execute
        mycursor.execute(completeorder)
        completeordercount = mycursor.fetchall()

        
        cancelorder = "select count(o_id) from order_tb,user_tb where order_tb.u_id = user_tb.u_id and order_tb.o_status='Cancel' and order_tb.s_id = '"+str(sid)+"'" 
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

        product = "select count(p_id) from product_tb,category_tb,staff_tb,subcategory_tb where product_tb.cat_id=category_tb.cat_id and product_tb.s_id=staff_tb.s_id and product_tb.sub_id=subcategory_tb.sub_id and product_tb.s_id = '"+str(sid)+"'" 
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

        payment = "select count(payment_tb.p_id) from  payment_tb,order_tb where payment_tb.o_id=order_tb.o_id and order_tb.s_id = '"+str(sid)+"'" 
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
       
    

        return render(request,'sindex.html',alldata)
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def scategory(request):
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
            return redirect("scategory")
        

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
            return redirect("scategory")
        
        else:
            selcat = "select * from category_tb order by cat_id desc" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selcat)
            cat_data = mycursor.fetchall()

            return render(request,'scategory.html',{'cat_data': cat_data})
    except NameError:
        print("internaal error")
    except:
        print('Error returned')

def scategoryedit(request):
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
           return redirect("scategory")

       else:
            
            cat_edt = request.GET.get("cat_edt")
            selcat = "select * from category_tb where cat_id = '"+str(cat_edt)+"'" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selcat)
            cat_data = mycursor.fetchall() 
            return render(request,'scategoryedit.html',{'cat_data': cat_data})

    except NameError:
        print("internal error")
    except:
        print('Error returned')
   
def sfeedback(request):
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
            return redirect("sfeedback")
        else:
            selfed = "select * from feedback_tb order by f_id desc"
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selfed)
            f_data = mycursor.fetchall()

            return render(request,'sfeedback.html',{'f_data': f_data})
        
       
    except NameError:
        print("internal error")
    except:
        print('Error returned')
    
def suser(request):
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
            return redirect("suser")

        else:    
            selus = "select * from user_tb order by u_id desc"
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selus)
            u_data = mycursor.fetchall()

            return render(request,'suser.html',{'u_data': u_data})
        
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def spayment(request):
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
            return redirect("spayment")
        else:
            sid = request.session["sid"] 
            selpy = "select * from payment_tb,order_tb where payment_tb.o_id=order_tb.o_id and order_tb.s_id = '"+str(sid)+"'  order by payment_tb.p_id desc"
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selpy)
            p_data = mycursor.fetchall()

            return render(request,'spayment.html',{'p_data': p_data})
 
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def ssubcategory(request):
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
            return redirect("ssubcategory")
        
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
            return redirect("ssubcategory")

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

            return render(request,'ssubcategory.html',alldata)
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def ssubcategoryedit(request):
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
           return redirect("ssubcategory")

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

            return render(request,'ssubcategoryedit.html',alldata)
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def sstaff(request):
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
            return redirect("sstaff")
        
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
            return redirect("sstaff")
        
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
            return redirect("sstaff")
        else:
            
            selstaff = "select * from staff_tb"
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selstaff)
            s_data = mycursor.fetchall()

            return render(request,'sstaff.html',{'s_data': s_data})
    
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def sproduct(request):
    try:
        if request.POST:
           
            cat_id = request.POST.get("cat_id")
            sub_id = request.POST.get("sub_id")
            s_id = request.session["sid"]
            p_name = request.POST.get("p_name") 
            p_img = request.FILES["p_image"]
            img = FileSystemStorage()
            p_image = img.save(p_img.name,p_img)
            p_price = request.POST.get("p_price")
            p_offerprice = request.POST.get("p_offerprice")
            p_details = request.POST.get("p_details")
            p_disclamier = request.POST.get("p_disclamier")
            p_size = request.POST.get("p_size")
            p_color = request.POST.get("p_color")
            p_material = request.POST.get("p_material")
            p_status = request.POST.get("p_status")
            cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

             #insert query
              
            ins = "INSERT INTO `product_tb`(`cat_id`,`sub_id`,`s_id`, `p_name`,`p_image`,`p_price`,`p_offerprice`,`p_details`,`p_disclamier`,`p_size`,`p_color`, `p_material`, `p_status`,`p_cdate`,`p_udate`) VALUES ('"+str(cat_id)+"','"+str(sub_id)+"','"+str(s_id)+"','"+str(p_name)+"','"+str(p_image)+"','"+str(p_price)+"','"+str(p_offerprice)+"','"+str(p_details)+"','"+str(p_disclamier)+"','"+str(p_size)+"','"+str(p_color)+"','"+str(p_material)+"','"+str(p_status)+"','"+str(cdate)+"','"+str(cdate)+"')"
            
            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(ins)
            mydb.commit()
            return redirect("sproduct")
        
        elif request.GET.get("p_id") !=None:
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
            return redirect("sproduct")
        
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
            return redirect("sproduct")
        else:
            s_id = request.session["sid"] 
            selpro = "select * from product_tb,category_tb,staff_tb,subcategory_tb where product_tb.cat_id=category_tb.cat_id and product_tb.s_id=staff_tb.s_id and product_tb.sub_id=subcategory_tb.sub_id and product_tb.s_id = '"+str(s_id)+"' order by p_id desc"
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selpro)
            p_data = mycursor.fetchall()

            selsubcategory = "select * from subcategory_tb where sub_status = 'Active'"  
            
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
                'cat_data' : cat_data,
                'p_data': p_data
            }

            return render(request,'sproduct.html',alldata)
        
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def scart(request):
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
            return redirect(f"/staffapp/s{lowercase_string}")
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

            return render(request,'scart.html',alldata)
        
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def slogin(request):
    try:
        msg = ""
        if request.POST:
           #variable decleration
           s_contact = request.POST.get("s_contact")
           s_password = request.POST.get("s_password")
           
           #insert query
           sel = "select * from staff_tb where `s_contact` = '"+str(s_contact)+"' and s_password = '"+str(s_password)+"'"
           #query exe - run
           mydb = getdb()
           mycursor = mydb.cursor()
           mycursor.execute(sel)
           udata = mycursor.fetchall()

           if len(udata) > 0:
               request.session["scontact"] = s_contact
               request.session["simg"] = udata[0][4]
               request.session["sname"] = udata[0][1]
               request.session["sid"] = udata[0][0]
               request.session["stime"] = str(udata[0][8])
        
               return redirect("sindex")           
           else:
               msg = " Invalid Username or Password.!" 
               return render(request,'slogin.html',{'msg':msg})          
        else:
            return render(request,'slogin.html',{'msg':msg})
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def slogout(request):
    try:
        
        #variable decleration
        sid = request.session["sid"]
        cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        #insert query

        ins = "UPDATE `staff_tb` set `s_udate` = '"+cdate+"' where s_id = '"+str(sid)+"'"

        #query exe - run
        mydb = getdb()
        mycursor = mydb.cursor()
        mycursor.execute(ins)
        mydb.commit()

        request.session["sname"] = None
        request.session["sid"] = None
        request.session["scontact"] = None
        request.session["simg"] = None
        request.session["stime"] = None

        return redirect("slogin")
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def sorderreport(request):
    try:
        if request.POST:

            s_date = request.POST.get("s_date")
            e_date = request.POST.get("e_date")            
            o_status = request.POST.get("o_status")
            s_id = request.session["sid"] 

            selorder = "SELECT order_tb.*, user_tb.u_name,user_tb.u_contact,  CASE WHEN order_tb.s_id = 0 THEN '-' ELSE staff_tb.s_name END AS s_name, CASE WHEN order_tb.s_id = 0 THEN '-' ELSE staff_tb.s_contact END AS s_contact FROM order_tb JOIN user_tb ON order_tb.u_id = user_tb.u_id LEFT JOIN staff_tb ON order_tb.s_id = staff_tb.s_id WHERE order_tb.o_status = '"+str(o_status)+"'  and DATE(order_tb.o_cdate) between '"+str(s_date)+"' and '"+str(e_date)+"' and order_tb.s_id = '"+str(s_id)+"' order by o_id desc" 
            #print(selorder)# connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selorder)
            o_data = mycursor.fetchall()
            return render(request,'sorderreport.html',{'order_data': o_data})
        else:
            return render(request,'sorderreport.html',{})

    except NameError:
        print("internal error")
    except:
        print('Error returned')

def spendingorder(request):
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
            return redirect("spendingorder")
            
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
            return redirect("spendingorder")
        else:
             s_id = request.session["sid"] 
             selor = "SELECT order_tb.*, user_tb.u_name,user_tb.u_contact,  CASE WHEN order_tb.s_id = 0 THEN '-' ELSE staff_tb.s_name END AS s_name, CASE WHEN order_tb.s_id = 0 THEN '-' ELSE staff_tb.s_contact END AS s_contact FROM order_tb JOIN user_tb ON order_tb.u_id = user_tb.u_id LEFT JOIN staff_tb ON order_tb.s_id = staff_tb.s_id WHERE order_tb.o_status = 'Pending' and order_tb.s_id = '"+str(s_id)+"' ORDER BY order_tb.o_id DESC"
             # connection create object
             mydb = getdb()
             mycursor = mydb.cursor()
             #query execute
             mycursor.execute(selor)
             o_data = mycursor.fetchall()

             return render(request,'spendingorder.html',{'o_data': o_data})
        
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def sconfirmorder(request):
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
            return redirect("sconfirmorder")
            
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
            return redirect("sconfirmorder")
        else:
             s_id = request.session["sid"]
             selor = "SELECT order_tb.*, user_tb.u_name,user_tb.u_contact,  CASE WHEN order_tb.s_id = 0 THEN '-' ELSE staff_tb.s_name END AS s_name, CASE WHEN order_tb.s_id = 0 THEN '-' ELSE staff_tb.s_contact END AS s_contact FROM order_tb JOIN user_tb ON order_tb.u_id = user_tb.u_id LEFT JOIN staff_tb ON order_tb.s_id = staff_tb.s_id WHERE order_tb.o_status = 'Confirm' and order_tb.s_id = '"+str(s_id)+"' ORDER BY order_tb.o_id DESC"
             # connection create object
             mydb = getdb()
             mycursor = mydb.cursor()
             #query execute
             mycursor.execute(selor)
             o_data = mycursor.fetchall()

             return render(request,'sconfirmorder.html',{'o_data': o_data})
        
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def scompleteorder(request):
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
            return redirect("scompleteorder")
            
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
            return redirect("scompleteorder")
        else:
             s_id = request.session["sid"]
             selor = "SELECT order_tb.*, user_tb.u_name,user_tb.u_contact,  CASE WHEN order_tb.s_id = 0 THEN '-' ELSE staff_tb.s_name END AS s_name, CASE WHEN order_tb.s_id = 0 THEN '-' ELSE staff_tb.s_contact END AS s_contact FROM order_tb JOIN user_tb ON order_tb.u_id = user_tb.u_id LEFT JOIN staff_tb ON order_tb.s_id = staff_tb.s_id WHERE order_tb.o_status = 'Complete' and order_tb.s_id = '"+str(s_id)+"' ORDER BY order_tb.o_id DESC"
             # connection create object
             mydb = getdb()
             mycursor = mydb.cursor()
             #query execute
             mycursor.execute(selor)
             o_data = mycursor.fetchall()

             return render(request,'scompleteorder.html',{'o_data': o_data})
        
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def scancelorder(request):
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
            return redirect("scancelorder")
            
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
            return redirect("scancelorder")
        else:
             s_id = request.session["sid"]
             selor = "SELECT order_tb.*, user_tb.u_name,user_tb.u_contact,  CASE WHEN order_tb.s_id = 0 THEN '-' ELSE staff_tb.s_name END AS s_name, CASE WHEN order_tb.s_id = 0 THEN '-' ELSE staff_tb.s_contact END AS s_contact FROM order_tb JOIN user_tb ON order_tb.u_id = user_tb.u_id LEFT JOIN staff_tb ON order_tb.s_id = staff_tb.s_id WHERE order_tb.o_status = 'Cancel'and order_tb.s_id = '"+str(s_id)+"' ORDER BY order_tb.o_id DESC"
             # connection create object
             mydb = getdb()
             mycursor = mydb.cursor()
             #query execute
             mycursor.execute(selor)
             o_data = mycursor.fetchall()

             return render(request,'scancelorder.html',{'o_data': o_data})
        
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def spaymentreport(request):
    try:
        if request.POST:

            s_date = request.POST.get("s_date")
            e_date = request.POST.get("e_date")
            s_id = request.session["sid"]             
           

            selpy = "select * from payment_tb,order_tb where payment_tb.o_id=order_tb.o_id and order_tb.s_id = '"+str(s_id)+"' AND DATE(payment_tb.p_cdate) between '"+str(s_date)+"' and '"+str(e_date)+"' order by payment_tb.p_id desc"
            #print(selorder)# connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selpy)
            p_data = mycursor.fetchall()
            return render(request,'spaymentreport.html',{'payment_data': p_data})
        else:
            return render(request,'spaymentreport.html',{})

    except NameError:
        print("internal error")
    except:
        print('Error returned')

def sstaffedit(request):
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
           return redirect("sstaff")

       else:
            
            s_edt = request.GET.get("s_edt")
            selcat = "select * from staff_tb where s_id = '"+str(s_edt)+"'" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selcat)
            s_data = mycursor.fetchall() 
            return render(request,'sstaffedit.html',{'s_data': s_data})

    except NameError:
        print("internal error")
    except:
        print('Error returned')
   
def sprofile(request):
    try:
       if request.POST:
           #variable decleration
          
           s_name = request.POST.get("s_name")
           s_edt = request.session["sid"]
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
           return redirect("sindex")

       else:
            
            s_edt = request.session["sid"]
            selcat = "select * from staff_tb where s_id = '"+str(s_edt)+"'" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selcat)
            s_data = mycursor.fetchall() 
            return render(request,'sprofile.html',{'s_data': s_data})

    except NameError:
        print("internal error")
    except:
        print('Error returned')

def sproductedit(request):
    try:
       if request.POST:
           #variable decleration
           p_edt = request.GET.get("p_edt")
           sid=request.session["sid"]
           cat_name = request.POST.get("cat_name")
           sub_name = request.POST.get("sub_name")
           p_name = request.POST.get("p_name")
           
           if request.POST.get("p_image") !="":
               p_image = request.FILES["p_image"]
               img = FileSystemStorage()
               old_img = img.save(p_image.name,p_image)

           else:
               old_img = request.POST.get("old_img")
            
           p_price=request.POST.get("p_price")
           p_offerprice=request.POST.get("p_offerprice") 
           p_details=request.POST.get("p_details")
           p_disclamier=request.POST.get("p_disclamier")
           p_size=request.POST.get("p_size")
           p_color=request.POST.get("p_color")
           p_material=request.POST.get("p_material")
           p_status = request.POST.get("p_status")
           pdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
           
           #insert query
           ins = "UPDATE `product_tb` SET `cat_id`='"+str(cat_name)+"',`sub_id`='"+str(sub_name)+"',`p_name`='"+str(p_name)+"',`p_image`='"+str(old_img)+"',`p_price`='"+str(p_price)+"',`p_offerprice`='"+str(p_offerprice)+"',`p_details`='"+str(p_details)+"',`p_disclamier`='"+str(p_disclamier)+"',`p_size`='"+str(p_size)+"',`p_color`='"+str(p_color)+"',`p_material`='"+str(p_material)+"',`p_status`='"+str(p_status)+"',`p_udate`= '"+pdate+"' WHERE p_id = '"+str(p_edt)+"'"
           #query exe - run
           mydb = getdb()
           mycursor = mydb.cursor()
           mycursor.execute(ins)
           mydb.commit()
           return redirect("sproduct")

       else:  
            
            p_edt = request.GET.get("p_edt")
            sid=request.session["sid"]
            selproduct = "select * from product_tb where p_id = '"+str(p_edt)+"'" 
            print(selproduct)
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selproduct)
            p_data = mycursor.fetchall()

            selcat = "select * from category_tb where cat_status = 'Active'" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selcat)
            cat_data = mycursor.fetchall()

            selsubcategory = "select * from subcategory_tb where sub_status = 'Active' " 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selsubcategory)
            sub_data = mycursor.fetchall()



            alldata = {
                'p_data' : p_data,
                'cat_data' : cat_data,
                'sub_data' : sub_data,
            }

            return render(request,'sproductedit.html',alldata)
    except NameError:
        print("internal error")
    except:
        print('Error returned')
