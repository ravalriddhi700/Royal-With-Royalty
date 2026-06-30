from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
import datetime
import mysql.connector
from django.core.files.storage import FileSystemStorage



def getdb():
    mydb = mysql.connector.connect(host="localhost",user="root", passwd="",database="jewellery_db")
    return mydb

def uindex(request):
    try:
        selpro = "SELECT product_tb.*, category_tb.*, staff_tb.*, subcategory_tb.*, CONCAT(ROUND(((product_tb.p_price - product_tb.p_offerprice) / product_tb.p_price) * 100, 0), '% OFF') AS discount_percentage FROM product_tb, category_tb, staff_tb, subcategory_tb WHERE product_tb.cat_id = category_tb.cat_id AND product_tb.s_id = staff_tb.s_id AND product_tb.sub_id = subcategory_tb.sub_id AND product_tb.p_status = 'Active' ORDER BY RAND() LIMIT 8"
        # connection create object
        mydb = getdb()
        mycursor = mydb.cursor()
        #query execute
        mycursor.execute(selpro)
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

        selfeedback = "select * from feedback_tb where f_status = 'Show' " 
        # connection create object
        mydb = getdb()
        mycursor = mydb.cursor()
        #query execute
        mycursor.execute(selfeedback)
        f_data = mycursor.fetchall()

        alldata = {
            'p_data' : p_data,
            'cat_data' : cat_data,
            'sub_data' : sub_data,
            'f_data' : f_data
        }

        return render(request,'uindex.html',alldata)
    
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def uabout(request):
    try:
        
        return render(request,'uabout.html',{})
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def uterms(request):
    try:
        
        return render(request,'uterms.html',{})
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def ucontact(request):
    try:
        if request.POST:
            f_name = request.POST.get("con_name")
            f_contact = request.POST.get("con_contact")
            f_message = request.POST.get("con_message")
            f_status = 'Hide'
            cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

             #insert query
              
            ins = "INSERT INTO `feedback_tb`(`f_name`, `f_contact`, `f_message`, `f_status`, `f_cdate`, `f_udate`) VALUES  ('"+str(f_name)+"','"+str(f_contact)+"','"+str(f_message)+"','"+str(f_status)+"','"+cdate+"','"+cdate+"')"
            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(ins)
            mydb.commit()
            return redirect("ucontact")
        
        else:

            return render(request,'ucontact.html',{})
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def usignup(request):
    try:
        msg = ""
        if request.POST:
            u_name = request.POST.get("u_name")
            u_contact = request.POST.get("u_contact")
            u_address = request.POST.get("u_address")
           
            u_img = request.FILES["u_img"]
            img = FileSystemStorage()
            u_img = img.save(u_img.name,u_img)

            u_password = request.POST.get("u_password")
            
            u_status = "Active"

            cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            #insert query
            sel = "select * from user_tb where `u_contact` = '"+str(u_contact)+"'"
            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(sel)
            udata = mycursor.fetchall()

            if len(udata) > 0:
                msg = "Sorry This Contact Is Already Exists...!"
                alldata = {
                    'msg':msg,

                }
                return render(request,'usignup.html',alldata)
            else:
                ins = "INSERT INTO `user_tb`(`u_name`, `u_contact`, `u_address`, `u_image`, `u_password`, `u_status`, `u_cdate`, `u_udate`) VALUES ('"+str(u_name)+"','"+str(u_contact)+"','"+str(u_address)+"','"+str(u_img)+"','"+str(u_password)+"','"+str(u_status)+"','"+cdate+"','"+cdate+"')"
                #query exe - run
                mydb = getdb()
                mycursor = mydb.cursor()
                mycursor.execute(ins)
                mydb.commit()
                return redirect("usignin")

        else:
           

            alldata = {
                'msg':msg,
                
            }
            
            return render(request,'usignup.html',alldata)
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def usignin(request):
    try:
        msg = ""
        if request.POST:
            u_username = request.POST.get("u_username")
            u_password = request.POST.get("u_password")
           
            #insert query
            sel = "select * from user_tb where `u_contact` = '"+str(u_username)+"' and u_password = '"+str(u_password)+"' and u_status = 'Active'"
            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(sel)
            udata = mycursor.fetchall()

            if len(udata) > 0:
                request.session["uname"] = u_username
                request.session["uimg"] = udata[0][4]
                request.session["userid"] = udata[0][0]
                request.session["utime"] = str(udata[0][8])
        
                return redirect("/")           
            else:
               

                msg = " Invalid Username or Password.!" 
                

                alldata = {
                    'msg':msg
                }

                return render(request,'usignin.html',{'msg':msg})
        else:
            
            alldata = {
                'msg':msg
            }
            return render(request,'usignin.html',alldata)
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def usignout(request):
    try:
    
            #variable decleration
            username = request.session["userid"]
            cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            #insert query

            ins = "UPDATE `user_tb` set `u_udate` = '"+cdate+"' where u_id = '"+str(username)+"'"

            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(ins)
            mydb.commit()

            request.session["uname"] = None
            request.session["uimg"] = None
            request.session["userid"] = None
            request.session["utime"] = None
            
            return redirect("usignin")
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def uprofile(request):
    try:
       if request.POST:
           #variable decleration
           userid = request.session["userid"] 
           u_name = request.POST.get("u_name")
           u_contact = request.POST.get("u_contact")
           u_address = request.POST.get("u_address")
           
           if request.POST.get("u_img") !="":
               u_img = request.FILES["u_img"]
               img = FileSystemStorage()
               old_img = img.save(u_img.name,u_img)

           else:
               old_img = request.POST.get("old_img")

           u_password = request.POST.get("u_password")
          
           
           #insert query
           ins = "UPDATE user_tb SET `u_name` = '"+str(u_name)+"',`u_contact` = '"+str(u_contact)+"',`u_address` = '"+str(u_address)+"', `u_image` = '"+str(old_img)+"',`u_password` = '"+str(u_password)+"' where u_id = '"+str(userid)+"'"
           #query exe - run
           mydb = getdb()
           mycursor = mydb.cursor()
           mycursor.execute(ins)
           mydb.commit()
           return redirect("uprofile")

       else:
            
            userid = request.session["userid"] 
            selu = "select * from user_tb where u_id = '"+str(userid)+"'" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selu)
            u_data = mycursor.fetchall() 
            return render(request,'uprofile.html',{'u_data': u_data})

    except NameError:
        print("internal error")
    except:
        print('Error returned')

def uproduct(request):
    try:
        if request.GET.get("sub_id") !=None:
            #variable decleration
            sub_id = request.GET.get("sub_id")

            #delete query

            selpro = "select * from product_tb,category_tb,staff_tb,subcategory_tb where product_tb.cat_id=category_tb.cat_id and product_tb.s_id=staff_tb.s_id and product_tb.sub_id=subcategory_tb.sub_id and product_tb.p_status='Active' and product_tb.sub_id='"+str(sub_id)+"' order by p_id desc"
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selpro)
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

            return render(request,'uproduct.html',alldata)

        elif request.GET.get("cat_id") !=None:
            #variable decleration
            cat_id = request.GET.get("cat_id")

            #delete query

            selpro = "select * from product_tb,category_tb,staff_tb,subcategory_tb where product_tb.cat_id=category_tb.cat_id and product_tb.s_id=staff_tb.s_id and product_tb.sub_id=subcategory_tb.sub_id and product_tb.p_status='Active' and product_tb.cat_id='"+str(cat_id)+"' order by p_id desc"
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selpro)
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

            return render(request,'uproduct.html',alldata)
        elif request.GET.get("search") !=None:
            #variable decleration
            search = request.GET.get("search")

            #delete query

            selpro = "select * from product_tb,category_tb,staff_tb,subcategory_tb where product_tb.cat_id=category_tb.cat_id and product_tb.s_id=staff_tb.s_id and product_tb.sub_id=subcategory_tb.sub_id and product_tb.p_status='Active' and product_tb.p_name like '%"+str(search)+"%' order by p_id desc"
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selpro)
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

            return render(request,'uproduct.html',alldata)    
        else:
            selpro = "select * from product_tb,category_tb,staff_tb,subcategory_tb where product_tb.cat_id=category_tb.cat_id and product_tb.s_id=staff_tb.s_id and product_tb.sub_id=subcategory_tb.sub_id and product_tb.p_status='Active' order by p_id desc"
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selpro)
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

            return render(request,'uproduct.html',alldata)
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def uforgotpassword(request):
    try:
        msg = ""
        if request.POST:
            u_username = request.POST.get("u_username")
           
            #insert query
            sel = "select * from user_tb where `u_contact` = '"+str(u_username)+"' and u_status = 'Active'"
            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(sel)
            udata = mycursor.fetchall()

            if len(udata) > 0:
         

                
                alldata = {
             
                    'msg':msg,
                    'udata':udata
                }

                return render(request,'uforgotpassword.html',alldata)
                
            else:
       

                msg = " Sorry This Contact Is Not Registered...!" 
                

                alldata = {
               
                    'msg':msg
                }

                return render(request,'uforgotpassword.html',alldata)
        else:


            alldata = {
              
                'msg':msg
            }
            return render(request,'uforgotpassword.html',alldata)
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def uproductdetails(request):
    try:
        msg = ""
        if request.POST:
            userid = request.session["userid"]
            o_total =   request.POST.get("o_total")
            o_status = 'Cart'
            p_id = request.GET.get("pid")
            od_status = 'Active'
            cat_id = request.POST.get("cat_id")
            sub_id = request.POST.get("sub_id")

            cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            #insert query
            chk = "select * from order_tb,cart_tb where order_tb.o_id = cart_tb.o_id and order_tb.u_id = '"+str(userid)+"' and cart_tb.p_id = '"+str(p_id)+"' and cart_tb.cart_status = 'Active'"
            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(chk)
            chkdata = mycursor.fetchall()

            if len(chkdata) > 0:
                msg = "You have Already added this product to the Cart.!"
                p_id = request.GET.get("pid")
                
                selpro = "select * from product_tb,category_tb,staff_tb,subcategory_tb where product_tb.cat_id=category_tb.cat_id and product_tb.s_id=staff_tb.s_id and product_tb.sub_id=subcategory_tb.sub_id and product_tb.p_status='Active' and product_tb.p_id = '"+str(p_id)+"'" 
                print(selpro)
                # connection create object
                mydb = getdb()
                mycursor = mydb.cursor()
                #query execute
                mycursor.execute(selpro)
                p_data = mycursor.fetchall()

                relpro = "select * from product_tb,category_tb,staff_tb,subcategory_tb where product_tb.cat_id=category_tb.cat_id and product_tb.s_id=staff_tb.s_id and product_tb.sub_id=subcategory_tb.sub_id and product_tb.p_status='Active' order by p_id desc"
                # connection create object
                mydb = getdb()
                mycursor = mydb.cursor()
                #query execute
                mycursor.execute(relpro)
                rdata = mycursor.fetchall()

                alldata = {
                    'p_data' : p_data,
                    'rdata' : rdata,
                    'msg' : msg,
                }


                return render(request,'uproductdetails.html',alldata)  
            
            else:
                ordchk = "select * from order_tb where o_status = 'Cart' and  u_id = '"+str(userid)+"'" 
                # connection create object
                mydb = getdb()
                mycursor = mydb.cursor()
                #query execute
                mycursor.execute(ordchk)
                odata = mycursor.fetchall()
                if len(odata) == 0:

                    ins = "INSERT INTO `order_tb`(`u_id`,`o_quantity`,`o_total`, `o_status`, `o_cdate`, `o_udate`) VALUES ('"+str(userid)+"','1','"+str(o_total)+"','"+str(o_status)+"','"+cdate+"','"+cdate+"')"           
                    #query exe - run
                    mydb = getdb()
                    mycursor = mydb.cursor()
                    mycursor.execute(ins)
                    mydb.commit()

                    lastid = mycursor.lastrowid
                
                    ins1 = "INSERT INTO `cart_tb`(`o_id`,`cat_id`,`sub_id`, `p_id`, `cart_price`, `cart_quantity`, `cart_totalprice`, `cart_status`,`cart_cdate`,`cart_udate`) VALUES ('"+str(lastid)+"','"+str(cat_id)+"','"+str(sub_id)+"','"+str(p_id)+"','"+str(o_total)+"','1','"+str(o_total)+"','"+str(od_status)+"','"+cdate+"','"+cdate+"')"           
                    
                    #query exe - run
                    mydb = getdb()
                    mycursor = mydb.cursor()
                    mycursor.execute(ins1)
                    mydb.commit()
                    return redirect("ucart")

                else:
                    lastid = odata[0][0]
                    
                    ins1 = "INSERT INTO `cart_tb`(`o_id`,`cat_id`,`sub_id`, `p_id`, `cart_price`, `cart_quantity`, `cart_totalprice`, `cart_status`,`cart_cdate`,`cart_udate`) VALUES ('"+str(lastid)+"','"+str(cat_id)+"','"+str(sub_id)+"','"+str(p_id)+"','"+str(o_total)+"','1','"+str(o_total)+"','"+str(od_status)+"','"+cdate+"','"+cdate+"')"           
                    
                    #query exe - run
                    mydb = getdb()
                    mycursor = mydb.cursor()
                    mycursor.execute(ins1)
                    mydb.commit()
                    return redirect("ucart")
        

        else:
            pid = request.GET.get("pid")

            selpro = "select * from product_tb,category_tb,staff_tb,subcategory_tb where product_tb.cat_id=category_tb.cat_id and product_tb.s_id=staff_tb.s_id and product_tb.sub_id=subcategory_tb.sub_id and product_tb.p_status='Active' and product_tb.p_id = '"+str(pid)+"'" 
            print(selpro)
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selpro)
            p_data = mycursor.fetchall()

            relpro = "select * from product_tb,category_tb,staff_tb,subcategory_tb where product_tb.cat_id=category_tb.cat_id and product_tb.s_id=staff_tb.s_id and product_tb.sub_id=subcategory_tb.sub_id and product_tb.p_status='Active' order by p_id desc"
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(relpro)
            rdata = mycursor.fetchall()

            alldata = {
                'p_data' : p_data,
                'rdata' : rdata,
                'msg' : msg,
            }


            return render(request,'uproductdetails.html',alldata)
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def ucart(request):
    try:
        if request.POST:
            userid = request.session["userid"]
            o_totalquntity = request.POST.get("o_quantity")
            o_total = request.POST.get("o_total")
            o_shipping = request.POST.get("o_shippingaddress")
            o_status = "Pending"
            od_status = "Deactive"
            o_pincode = request.POST.get("o_pincode")
            
            cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            #insert query
            chk = "select * from order_tb,cart_tb where order_tb.o_id = cart_tb.o_id and order_tb.u_id = '"+str(userid)+"' and order_tb.o_status = 'Cart' and cart_tb.cart_status = 'Active'"
            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(chk)
            chkdata = mycursor.fetchall()

            o_id = chkdata[0][0]

            up1 = "update cart_tb set cart_status = '"+str(od_status)+"',cart_udate = '"+cdate+"' where o_id  = '"+str(o_id)+"'"
            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(up1)
            mydb.commit()
 

            up = "update order_tb set o_quantity = '"+str(o_totalquntity)+"',o_total = '"+str(o_total)+"',o_shippingaddress = '"+str(o_shipping)+"',o_pincode = '"+str(o_pincode)+"' ,o_status = '"+str(o_status)+"',o_udate = '"+cdate+"' where u_id = '"+str(userid)+"' and o_status = 'Cart'"
            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(up)
            mydb.commit()

            ins = "insert into payment_tb(o_id,p_amount,p_status,p_cdate)values('"+str(o_id)+"','"+str(o_total)+"','Success','"+cdate+"')"
            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(ins)
            mydb.commit()
            return redirect(f"/upayment?b_id={o_total}")

        elif request.GET.get("minus") !=None: 
            bdid = request.GET.get("bdid")
            qty = request.GET.get("qty")
            price = request.GET.get("price")

            newqty = int(qty) - 1
            newprice = int(price) * newqty
            cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            up = "update cart_tb  set cart_quantity = '"+str(newqty)+"', cart_totalprice = '"+str(newprice)+"',cart_udate = '"+cdate+"' where cart_id = '"+str(bdid)+"'"
             #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(up)
            mydb.commit()
            return redirect("ucart")

        elif request.GET.get("pluse") !=None: 
            bdid = request.GET.get("bdid")
            qty = request.GET.get("qty")
            price = request.GET.get("price")

            newqty = int(qty) + 1
            newprice = int(price) * newqty
            cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            up = "update cart_tb  set cart_quantity = '"+str(newqty)+"', cart_totalprice = '"+str(newprice)+"',cart_udate = '"+cdate+"' where cart_id = '"+str(bdid)+"'"
             #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(up)
            mydb.commit()
            return redirect("ucart")
        
        elif request.GET.get("delete") !=None: 
              bdid = request.GET.get("bdid")

              ins = "DELETE from `cart_tb` where cart_id = '"+str(bdid)+"'"

              #query exe - run
              mydb = getdb()
              mycursor = mydb.cursor()
              mycursor.execute(ins)
              mydb.commit()
              return redirect("ucart")


        else:    
            userid = request.session["userid"]
            selcart = "SELECT * from cart_tb,order_tb,product_tb,category_tb,subcategory_tb WHERE order_tb.o_id = cart_tb.o_id and cart_tb.p_id = product_tb.p_id and cart_tb.sub_id = subcategory_tb.sub_id and cart_tb.cat_id = category_tb.cat_id and cart_tb.cart_status = 'Active' and order_tb.u_id = '"+str(userid)+"'" 
            
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selcart)
            cart_data = mycursor.fetchall()

            seltotal = "SELECT sum(cart_totalprice) from cart_tb,order_tb,product_tb,category_tb,subcategory_tb WHERE order_tb.o_id = cart_tb.o_id and cart_tb.p_id = product_tb.p_id and cart_tb.sub_id = subcategory_tb.sub_id and cart_tb.cat_id = category_tb.cat_id and cart_tb.cart_status = 'Active' and order_tb.u_id = '"+str(userid)+"'" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(seltotal)
            total_data = mycursor.fetchall()

            seltotalqty = "SELECT sum(cart_quantity) from cart_tb,order_tb,product_tb,category_tb,subcategory_tb WHERE order_tb.o_id = cart_tb.o_id and cart_tb.p_id = product_tb.p_id and cart_tb.sub_id = subcategory_tb.sub_id and cart_tb.cat_id = category_tb.cat_id and cart_tb.cart_status = 'Active' and order_tb.u_id = '"+str(userid)+"'" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(seltotalqty)
            totalqty_data = mycursor.fetchall()

                    
            alldata = {
            'cart_data' : cart_data,
            'total_data' : total_data,
            'totalqty_data' :totalqty_data
            }
            return render(request,'ucart.html',alldata)
        
        
        
    except NameError:
        print("internal error")
    except:
        print('Error returned')



def uorder(request):
    try:
        if request.GET.get("oid") !=None: 
            bdid = request.GET.get("oid")
            
            ins = "update  order_tb  set o_status = 'Cancel' where o_id = '"+str(bdid)+"'"
            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(ins)
            mydb.commit()
            return redirect("uorder")

        else:    
            userid = request.session["userid"]
            
            selcart = "SELECT * from order_tb WHERE o_status != 'Cart' and u_id = '"+str(userid)+"'" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selcart)
            cart_data = mycursor.fetchall()

            alldata = {
            'cart_data' : cart_data,
            }
        return render(request,'uorder.html',alldata)
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def uorderdetails(request):
    try:
        bdid = request.GET.get("oid")

        sel = "SELECT * FROM cart_tb,product_tb,category_tb,subcategory_tb WHERE cart_tb.p_id = product_tb.p_id and cart_tb.cat_id = category_tb.cat_id and cart_tb.sub_id = subcategory_tb.sub_id and cart_tb.cart_status = 'Deactive' and cart_tb.o_id = '"+str(bdid)+"'" 
        mydb = getdb()
        mycursor = mydb.cursor()
        #query execute
        mycursor.execute(sel)
        od_data = mycursor.fetchall()
        
        alldata = {
            'od_data' : od_data,
        }

        return render(request,'uorderdetails.html',alldata)
    except NameError:
        print("internal error")
    except:
        print('Error returned')


def upayment(request):
    try:
        if request.POST:
            return redirect("uorder")
        else:
            return render(request,'upayment.html',{})
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def uthankyou(request):
    try:
        
        return render(request,'uthankyou.html',{})
    except NameError:
        print("internal error")
    except:
        print('Error returned')

