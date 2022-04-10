from flask import Blueprint, render_template, request, flash, redirect, url_for, Flask
from .models import User, userinterests, interestsimg
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
import random, base64, io, os
from cryptography.fernet import Fernet
import PIL.Image as Image
from werkzeug.utils import secure_filename
from  sqlalchemy.sql.expression import func



auth = Blueprint('auth', __name__)
app = Flask(__name__)
RanObjpath=os.path.join(app.root_path, 'static\objects').replace("\\","/")
intimgpath=os.path.join(app.root_path, 'static\Images').replace("\\","/")
@auth.route('/login', methods=['GET', 'POST'])
def login():
    global email, ranloc, isauth
    key= b'_-IlTXCOOJc5TOzQsJOKHqnDzIdB7uIihDuihL05GfY='
    fernet= Fernet(key)
    if request.form.get('btn')=="next1":
        if request.method == 'POST':   
            email= request.form.get('email')         
            user = db.session.query(User).filter_by(email=email).first()
            if user:
                BGimg=Image.open(intimgpath+"/"+"BGimg.jpeg")
                #open background
                #------------------------------------------------------------------------------------
                #------------------------------------------------------------------------------------
                #display 1st image (user)
                user = db.session.query(User).filter_by(email=email).first()
                usrid= user.id
                #------------------------------------------------------------------------------------
                usr_int1_row= db.session.query(userinterests).filter_by(user_id=usrid).first()
                usr_int1_id=usr_int1_row.id
                usr_int1 = fernet.decrypt(usr_int1_row.interestname).decode('utf-8')
                usr_int2_row= db.session.query(userinterests).filter_by(user_id=usrid,id=usr_int1_id+1).first()
                usr_int2 = fernet.decrypt(usr_int2_row.interestname).decode('utf-8')
                usr_int3_row= db.session.query(userinterests).filter_by(user_id=usrid,id=usr_int1_id+2).first()
                usr_int3 = fernet.decrypt(usr_int3_row.interestname).decode('utf-8')
                usr_int4_row= db.session.query(userinterests).filter_by(user_id=usrid,id=usr_int1_id+3).first()
                usr_int4 = fernet.decrypt(usr_int4_row.interestname).decode('utf-8')
                usr_int5_row= db.session.query(userinterests).filter_by(user_id=usrid,id=usr_int1_id+4).first()
                usr_int5 = fernet.decrypt(usr_int5_row.interestname).decode('utf-8')
                usr_int6_row= db.session.query(userinterests).filter_by(user_id=usrid,id=usr_int1_id+5).first()
                usr_int6 = fernet.decrypt(usr_int6_row.interestname).decode('utf-8')
                usr_int7_row= db.session.query(userinterests).filter_by(user_id=usrid,id=usr_int1_id+6).first()
                usr_int7 = fernet.decrypt(usr_int7_row.interestname).decode('utf-8')
                usr_int8_row= db.session.query(userinterests).filter_by(user_id=usrid,id=usr_int1_id+7).first()
                usr_int8 = fernet.decrypt(usr_int8_row.interestname).decode('utf-8')
                usr_int9_row= db.session.query(userinterests).filter_by(user_id=usrid,id=usr_int1_id+8).first()
                usr_int9 = fernet.decrypt(usr_int9_row.interestname).decode('utf-8')
                usr_int10_row= db.session.query(userinterests).filter_by(user_id=usrid,id=usr_int1_id+9).first()
                usr_int10 = fernet.decrypt(usr_int10_row.interestname).decode('utf-8')
                usr_int11_row= db.session.query(userinterests).filter_by(user_id=usrid,id=usr_int1_id+10).first()
                usr_int11 = fernet.decrypt(usr_int11_row.interestname).decode('utf-8')
                usr_int12_row= db.session.query(userinterests).filter_by(user_id=usrid,id=usr_int1_id+11).first()
                usr_int12 = fernet.decrypt(usr_int12_row.interestname).decode('utf-8')
                usr_int13_row= db.session.query(userinterests).filter_by(user_id=usrid,id=usr_int1_id+12).first()
                usr_int13 = fernet.decrypt(usr_int13_row.interestname).decode('utf-8')
                usr_int14_row= db.session.query(userinterests).filter_by(user_id=usrid,id=usr_int1_id+13).first()
                usr_int14 = fernet.decrypt(usr_int14_row.interestname).decode('utf-8')
                usr_int15_row= db.session.query(userinterests).filter_by(user_id=usrid,id=usr_int1_id+14).first()
                usr_int15 = fernet.decrypt(usr_int15_row.interestname).decode('utf-8')

                #------------------------------------------------------------------------------------
                BGimg1=BGimg
                randintid1_1 = db.session.query(userinterests).filter_by(user_id=usrid).order_by(func.random()).first()
                rand_int_id1_1= randintid1_1.interestname
                dec_rand_int_id1_1= fernet.decrypt(rand_int_id1_1)
                str_rand_int_id1_1= dec_rand_int_id1_1.decode('utf-8')
                get_rand_int_id1_1= db.session.query(interestsimg).filter_by(interestname=str_rand_int_id1_1).first()
                rand_int_picdata1_1= get_rand_int_id1_1.imgnum[:-1]
                rand_gen_int_cat1_1 = get_rand_int_id1_1.imgcategory
                i=str(random.randrange(1,4))
                randpicname1_1= secure_filename(rand_int_picdata1_1+i+".jpg")
                img1_1 = Image.open(intimgpath+"/"+randpicname1_1)
                width, hight = img1_1.size
                new_width= width//2
                new_hight= hight//2
                resized_img1_1=img1_1.resize((new_width,new_hight))
                area1_1=(0,0)
                BGimg1.paste(resized_img1_1,area1_1)
                #----------------------------------------------------------------------------------
                randintid1_2 = db.session.query(userinterests).filter_by(user_id=usrid).order_by(func.random()).first()
                while True:
                    randintid1_2 = db.session.query(userinterests).filter_by(user_id=usrid).order_by(func.random()).first()
                    if randintid1_2 != randintid1_1:
                        rand_int_id1_2= randintid1_2.interestname
                        dec_rand_int_id1_2= fernet.decrypt(rand_int_id1_2)
                        str_rand_int_id1_2= dec_rand_int_id1_2.decode('utf-8')
                        get_rand_int_id1_2= db.session.query(interestsimg).filter_by(interestname=str_rand_int_id1_2).first()
                        rand_int_picdata1_2= get_rand_int_id1_2.imgnum[:-1]
                        rand_gen_int_cat1_2 = get_rand_int_id1_2.imgcategory
                        i=str(random.randrange(1,4))
                        if rand_gen_int_cat1_2 != rand_gen_int_cat1_1:
                            randpicname1_2= secure_filename(rand_int_picdata1_2+i+".jpg")
                            img1_2 = Image.open(intimgpath+"/"+randpicname1_2)
                            width, hight = img1_2.size
                            new_width= width//2
                            new_hight= hight//2
                            resized_img1_2=img1_2.resize((new_width,new_hight))
                            area1_2=(960,0)
                            BGimg1.paste(resized_img1_2,area1_2)
                            break
                        else:
                            randintid1_2 = db.session.query(userinterests).filter_by(user_id=usrid).order_by(func.random()).first()
                    else:
                        randintid1_2 = db.session.query(userinterests).filter_by(user_id=usrid).order_by(func.random()).first()
                #----------------------------------------------------------------------------------
                randintid1_3 = db.session.query(userinterests).filter_by(user_id=usrid).order_by(func.random()).first()
                while True:
                    if randintid1_3 != randintid1_1 and randintid1_3 != randintid1_2:
                        rand_int_id1_3= randintid1_3.interestname
                        dec_rand_int_id1_3= fernet.decrypt(rand_int_id1_3)
                        str_rand_int_id1_3= dec_rand_int_id1_3.decode('utf-8')
                        get_rand_int_id1_3= db.session.query(interestsimg).filter_by(interestname=str_rand_int_id1_3).first()
                        rand_int_picdata1_3= get_rand_int_id1_3.imgnum[:-1]
                        rand_gen_int_cat1_3 = get_rand_int_id1_3.imgcategory
                        i=str(random.randrange(1,4))
                        if rand_gen_int_cat1_3 != rand_gen_int_cat1_1 and rand_gen_int_cat1_3 != rand_gen_int_cat1_2:
                            randpicname1_3= secure_filename(rand_int_picdata1_3+i+".jpg")
                            img1_3 = Image.open(intimgpath+"/"+randpicname1_3)
                            width, hight = img1_3.size
                            new_width= width//2
                            new_hight= hight//2
                            resized_img1_3=img1_3.resize((new_width,new_hight))
                            area1_3=(0,540)
                            BGimg1.paste(resized_img1_3,area1_3)
                            break
                        else:
                            randintid1_3 = db.session.query(userinterests).filter_by(user_id=usrid).order_by(func.random()).first()
                    else:
                        randintid1_3 = db.session.query(userinterests).filter_by(user_id=usrid).order_by(func.random()).first()
                #----------------------------------------------------------------------------------
                randintid1_4 = db.session.query(userinterests).filter_by(user_id=usrid).order_by(func.random()).first()
                while True:
                    if randintid1_4 != randintid1_1 and randintid1_4 != randintid1_2 and randintid1_4 != randintid1_3:
                        rand_int_id1_4= randintid1_4.interestname
                        dec_rand_int_id1_4= fernet.decrypt(rand_int_id1_4)
                        str_rand_int_id1_4= dec_rand_int_id1_4.decode('utf-8')
                        get_rand_int_id1_4= db.session.query(interestsimg).filter_by(interestname=str_rand_int_id1_4).first()
                        rand_int_picdata1_4= get_rand_int_id1_4.imgnum[:-1]
                        rand_gen_int_cat1_4 = get_rand_int_id1_4.imgcategory
                        i=str(random.randrange(1,4))
                        if rand_gen_int_cat1_4 != rand_gen_int_cat1_1 and rand_gen_int_cat1_4 != rand_gen_int_cat1_2 and rand_gen_int_cat1_4 != rand_gen_int_cat1_3:
                            randpicname1_4= secure_filename(rand_int_picdata1_4+i+".jpg")
                            img1_4 = Image.open(intimgpath+"/"+randpicname1_4)
                            width, hight = img1_4.size
                            new_width= width//2
                            new_hight= hight//2
                            resized_img1_4=img1_4.resize((new_width,new_hight))
                            area1_4=(960,540)
                            BGimg1.paste(resized_img1_4,area1_4)
                            break
                        else:
                          randintid1_4 = db.session.query(userinterests).filter_by(user_id=usrid).order_by(func.random()).first()  
                    else:
                        randintid1_4 = db.session.query(userinterests).filter_by(user_id=usrid).order_by(func.random()).first()
                data1 = io.BytesIO()
                BGimg1.save(data1,"JPEG")
                encode_img_data1 = base64.b64encode(data1.getvalue())
                #----------------------------------------------------------------------------------
                #----------------------------------------------------------------------------------
                #display 2nd image
                BGimg2=BGimg           
                randintid2_1 = random.randrange(1, db.session.query(interestsimg).count())
                while True:
                    rand_gen_int_id2_1 = db.session.query(interestsimg).filter_by(id=randintid2_1).first()
                    rand_gen_int_num2_1 = rand_gen_int_id2_1.imgnum[:-1]
                    rand_gen_int_cat2_1 = rand_gen_int_id2_1.imgcategory
                    rand_gen_int_name2_1 = rand_gen_int_id2_1.interestname
                    i=str(random.randrange(1,4))
                    if rand_gen_int_name2_1 != usr_int1 and rand_gen_int_name2_1 != usr_int2 and rand_gen_int_name2_1 != usr_int3 and rand_gen_int_name2_1 != usr_int4 and rand_gen_int_name2_1 != usr_int5 and rand_gen_int_name2_1 != usr_int6 and rand_gen_int_name2_1 != usr_int7 and rand_gen_int_name2_1 != usr_int8 and rand_gen_int_name2_1 != usr_int9 and rand_gen_int_name2_1 != usr_int10 and rand_gen_int_name2_1 != usr_int11 and rand_gen_int_name2_1 != usr_int12 and rand_gen_int_name2_1 != usr_int13 and rand_gen_int_name2_1 != usr_int14 and rand_gen_int_name2_1 != usr_int15:
                        randpicname2_1= secure_filename(rand_gen_int_num2_1+i+".jpg")
                        img2_1 = Image.open(intimgpath+"/"+randpicname2_1)
                        width, hight = img2_1.size
                        new_width= width//2
                        new_hight= hight//2
                        resized_img2_1=img2_1.resize((new_width,new_hight))
                        area2_1=(0,0)
                        BGimg2.paste(resized_img2_1,area2_1)
                        break
                    else:
                       randintid2_1 = random.randrange(1, db.session.query(interestsimg).count()) 
                #----------------------------------------------------------------------------------
                randintid2_2 = random.randrange(1, db.session.query(interestsimg).count())
                while True:
                    if randintid2_2 != randintid2_1:
                        rand_gen_int_id2_2 = db.session.query(interestsimg).filter_by(id=randintid2_2).first()
                        rand_gen_int_num2_2 = rand_gen_int_id2_2.imgnum[:-1]
                        rand_gen_int_cat2_2 = rand_gen_int_id2_2.imgcategory
                        rand_gen_int_name2_2 = rand_gen_int_id2_2.interestname
                        i=str(random.randrange(1,4))
                        if rand_gen_int_name2_2 != usr_int1 and rand_gen_int_name2_2 != usr_int2 and rand_gen_int_name2_2 != usr_int3 and rand_gen_int_name2_2 != usr_int4 and rand_gen_int_name2_2 != usr_int5 and rand_gen_int_name2_2 != usr_int6 and rand_gen_int_name2_2 != usr_int7 and rand_gen_int_name2_2 != usr_int8 and rand_gen_int_name2_2 != usr_int9 and rand_gen_int_name2_2 != usr_int10 and rand_gen_int_name2_2 != usr_int11 and rand_gen_int_name2_2 != usr_int12 and rand_gen_int_name2_2 != usr_int13 and rand_gen_int_name2_2 != usr_int14 and rand_gen_int_name2_2 != usr_int15:
                            if rand_gen_int_cat2_2 != rand_gen_int_cat2_1:
                                randpicname2_2= secure_filename(rand_gen_int_num2_2+i+".jpg")
                                img2_2 = Image.open(intimgpath+"/"+randpicname2_2)
                                width, hight = img2_2.size
                                new_width= width//2
                                new_hight= hight//2
                                resized_img2_2=img2_2.resize((new_width,new_hight))
                                area2_2=(960,0)
                                BGimg2.paste(resized_img2_2,area2_2)
                                break
                            else:
                                randintid2_2 = random.randrange(1, db.session.query(interestsimg).count())
                        else:
                            randintid2_2 = random.randrange(1, db.session.query(interestsimg).count())
                    else:
                        randintid2_2 = random.randrange(1, db.session.query(interestsimg).count())
                #----------------------------------------------------------------------------------
                randintid2_3 = random.randrange(1, db.session.query(interestsimg).count())
                while True:
                    if randintid2_3 != randintid2_1 and randintid2_3 != randintid2_2:
                        rand_gen_int_id2_3 = db.session.query(interestsimg).filter_by(id=randintid2_3).first()
                        rand_gen_int_num2_3 = rand_gen_int_id2_3.imgnum[:-1]
                        rand_gen_int_cat2_3 = rand_gen_int_id2_3.imgcategory
                        rand_gen_int_name2_3 = rand_gen_int_id2_3.interestname
                        i=str(random.randrange(1,4))
                        if rand_gen_int_name2_3 != usr_int1 and rand_gen_int_name2_3 != usr_int2 and rand_gen_int_name2_3 != usr_int3 and rand_gen_int_name2_3 != usr_int4 and rand_gen_int_name2_3 != usr_int5 and rand_gen_int_name2_3 != usr_int6 and rand_gen_int_name2_3 != usr_int7 and rand_gen_int_name2_3 != usr_int8 and rand_gen_int_name2_3 != usr_int9 and rand_gen_int_name2_3 != usr_int10 and rand_gen_int_name2_3 != usr_int11 and rand_gen_int_name2_3 != usr_int12 and rand_gen_int_name2_3 != usr_int13 and rand_gen_int_name2_3 != usr_int14 and rand_gen_int_name2_3 != usr_int15:
                            if rand_gen_int_cat2_3 != rand_gen_int_cat2_1 and rand_gen_int_cat2_3 != rand_gen_int_cat2_2:
                                randpicname2_3= secure_filename(rand_gen_int_num2_3+i+".jpg")
                                img2_3 = Image.open(intimgpath+"/"+randpicname2_3)
                                width, hight = img2_3.size
                                new_width= width//2
                                new_hight= hight//2
                                resized_img2_3=img2_3.resize((new_width,new_hight))
                                area2_3=(0,540)
                                BGimg2.paste(resized_img2_3,area2_3)
                                break
                            else:
                                randintid2_3 = random.randrange(1, db.session.query(interestsimg).count())
                        else:
                            randintid2_3 = random.randrange(1, db.session.query(interestsimg).count())
                    else:
                        randintid2_3 = random.randrange(1, db.session.query(interestsimg).count())
                #----------------------------------------------------------------------------------
                randintid2_4 = random.randrange(1, db.session.query(interestsimg).count())
                while True:
                    if randintid2_4 != randintid2_1 and randintid2_4 != randintid2_2 and randintid2_4 != randintid2_3:
                        rand_gen_int_id2_4 = db.session.query(interestsimg).filter_by(id=randintid2_4).first()
                        rand_gen_int_num2_4 = rand_gen_int_id2_4.imgnum[:-1]
                        rand_gen_int_cat2_4 = rand_gen_int_id2_4.imgcategory
                        rand_gen_int_name2_4 = rand_gen_int_id2_4.interestname
                        i=str(random.randrange(1,4))
                        if rand_gen_int_name2_4 != usr_int1 and rand_gen_int_name2_4 != usr_int2 and rand_gen_int_name2_4 != usr_int3 and rand_gen_int_name2_4 != usr_int4 and rand_gen_int_name2_4 != usr_int5 and rand_gen_int_name2_4 != usr_int6 and rand_gen_int_name2_4 != usr_int7 and rand_gen_int_name2_4 != usr_int8 and rand_gen_int_name2_4 != usr_int9 and rand_gen_int_name2_4 != usr_int10 and rand_gen_int_name2_4 != usr_int11 and rand_gen_int_name2_4 != usr_int12 and rand_gen_int_name2_4 != usr_int13 and rand_gen_int_name2_4 != usr_int14 and rand_gen_int_name2_4 != usr_int15:
                            if rand_gen_int_cat2_4 != rand_gen_int_cat2_1 and rand_gen_int_cat2_4 != rand_gen_int_cat2_2 and rand_gen_int_cat2_4 != rand_gen_int_cat2_3:
                                randpicname2_4= secure_filename(rand_gen_int_num2_4+i+".jpg")
                                img2_4 = Image.open(intimgpath+"/"+randpicname2_4)
                                width, hight = img2_4.size
                                new_width= width//2
                                new_hight= hight//2
                                resized_img2_4=img2_4.resize((new_width,new_hight))
                                area2_4=(960,540)
                                BGimg2.paste(resized_img2_4,area2_4)
                                break
                            else:
                                randintid2_4 = random.randrange(1, db.session.query(interestsimg).count())
                        else:
                            randintid2_4 = random.randrange(1, db.session.query(interestsimg).count())
                    else:
                        randintid2_4 = random.randrange(1, db.session.query(interestsimg).count())
                data2 = io.BytesIO()
                BGimg2.save(data2,"JPEG")
                encode_img_data2 = base64.b64encode(data2.getvalue())
                #----------------------------------------------------------------------------------
                #----------------------------------------------------------------------------------
                #display 3rd image
                BGimg3=BGimg           
                randintid3_1 = random.randrange(1, db.session.query(interestsimg).count())
                while True:
                    rand_gen_int_id3_1 = db.session.query(interestsimg).filter_by(id=randintid3_1).first()
                    rand_gen_int_num3_1 = rand_gen_int_id3_1.imgnum[:-1]
                    rand_gen_int_cat3_1 = rand_gen_int_id3_1.imgcategory
                    rand_gen_int_name3_1 = rand_gen_int_id3_1.interestname
                    i=str(random.randrange(1,4))
                    if rand_gen_int_name3_1 != usr_int1 and rand_gen_int_name3_1 != usr_int2 and rand_gen_int_name3_1 != usr_int3 and rand_gen_int_name3_1 != usr_int4 and rand_gen_int_name3_1 != usr_int5 and rand_gen_int_name3_1 != usr_int6 and rand_gen_int_name3_1 != usr_int7 and rand_gen_int_name3_1 != usr_int8 and rand_gen_int_name3_1 != usr_int9 and rand_gen_int_name3_1 != usr_int10 and rand_gen_int_name3_1 != usr_int11 and rand_gen_int_name3_1 != usr_int12 and rand_gen_int_name3_1 != usr_int13 and rand_gen_int_name3_1 != usr_int14 and rand_gen_int_name3_1 != usr_int15:
                        randpicname3_1= secure_filename(rand_gen_int_num3_1+i+".jpg")
                        img3_1 = Image.open(intimgpath+"/"+randpicname3_1)
                        width, hight = img3_1.size
                        new_width= width//2
                        new_hight= hight//2
                        resized_img3_1=img3_1.resize((new_width,new_hight))
                        area3_1=(0,0)
                        BGimg3.paste(resized_img3_1,area3_1)
                        break
                    else:
                        randintid3_1 = random.randrange(1, db.session.query(interestsimg).count())
                #----------------------------------------------------------------------------------
                randintid3_2 = random.randrange(1, db.session.query(interestsimg).count())
                while True:
                    if randintid3_2 != randintid3_1:
                        rand_gen_int_id3_2 = db.session.query(interestsimg).filter_by(id=randintid3_2).first()
                        rand_gen_int_num3_2 = rand_gen_int_id3_2.imgnum[:-1]
                        rand_gen_int_cat3_2 = rand_gen_int_id3_2.imgcategory
                        rand_gen_int_name3_2 = rand_gen_int_id3_2.interestname
                        i=str(random.randrange(1,4))
                        if rand_gen_int_name3_2 != usr_int1 and rand_gen_int_name3_2 != usr_int2 and rand_gen_int_name3_2 != usr_int3 and rand_gen_int_name3_2 != usr_int4 and rand_gen_int_name3_2 != usr_int5 and rand_gen_int_name3_2 != usr_int6 and rand_gen_int_name3_2 != usr_int7 and rand_gen_int_name3_2 != usr_int8 and rand_gen_int_name3_2 != usr_int9 and rand_gen_int_name3_2 != usr_int10 and rand_gen_int_name3_2 != usr_int11 and rand_gen_int_name3_2 != usr_int12 and rand_gen_int_name3_2 != usr_int13 and rand_gen_int_name3_2 != usr_int14 and rand_gen_int_name3_2 != usr_int15:
                            if rand_gen_int_cat3_2 != rand_gen_int_cat3_1:
                                randpicname3_2= secure_filename(rand_gen_int_num3_2+i+".jpg")
                                img3_2 = Image.open(intimgpath+"/"+randpicname3_2)
                                width, hight = img3_2.size
                                new_width= width//2
                                new_hight= hight//2
                                resized_img3_2=img3_2.resize((new_width,new_hight))
                                area3_2=(960,0)
                                BGimg3.paste(resized_img3_2,area3_2)
                                break
                            else:
                                randintid3_2 = random.randrange(1, db.session.query(interestsimg).count())
                        else:
                            randintid3_2 = random.randrange(1, db.session.query(interestsimg).count())
                    else:
                        randintid3_2 = random.randrange(1, db.session.query(interestsimg).count())
                #----------------------------------------------------------------------------------
                randintid3_3 = random.randrange(1, db.session.query(interestsimg).count())
                while True:
                    if randintid3_3 != randintid3_1 and randintid3_3 != randintid3_2:
                        rand_gen_int_id3_3 = db.session.query(interestsimg).filter_by(id=randintid3_3).first()
                        rand_gen_int_num3_3 = rand_gen_int_id3_3.imgnum[:-1]
                        rand_gen_int_cat3_3 = rand_gen_int_id3_3.imgcategory
                        rand_gen_int_name3_3 = rand_gen_int_id3_3.interestname
                        i=str(random.randrange(1,4))
                        if rand_gen_int_name3_3 != usr_int1 and rand_gen_int_name3_3 != usr_int2 and rand_gen_int_name3_3 != usr_int3 and rand_gen_int_name3_3 != usr_int4 and rand_gen_int_name3_3 != usr_int5 and rand_gen_int_name3_3 != usr_int6 and rand_gen_int_name3_3 != usr_int7 and rand_gen_int_name3_3 != usr_int8 and rand_gen_int_name3_3 != usr_int9 and rand_gen_int_name3_3 != usr_int10 and rand_gen_int_name3_3 != usr_int11 and rand_gen_int_name3_3 != usr_int12 and rand_gen_int_name3_3 != usr_int13 and rand_gen_int_name3_3 != usr_int14 and rand_gen_int_name3_3 != usr_int15:
                            if rand_gen_int_cat3_3 != rand_gen_int_cat3_1 and rand_gen_int_cat3_3 != rand_gen_int_cat3_2:
                                randpicname3_3= secure_filename(rand_gen_int_num3_3+i+".jpg")
                                img3_3 = Image.open(intimgpath+"/"+randpicname3_3)
                                width, hight = img3_3.size
                                new_width= width//2
                                new_hight= hight//2
                                resized_img3_3=img3_3.resize((new_width,new_hight))
                                area3_3=(0,540)
                                BGimg3.paste(resized_img3_3,area3_3)
                                break
                            else:
                                randintid3_3 = random.randrange(1, db.session.query(interestsimg).count())
                        else:
                            randintid3_3 = random.randrange(1, db.session.query(interestsimg).count())
                    else:
                        randintid3_3 = random.randrange(1, db.session.query(interestsimg).count())
                #----------------------------------------------------------------------------------
                randintid3_4 = random.randrange(1, db.session.query(interestsimg).count())
                while True:
                    if randintid3_4 != randintid3_1 and randintid3_4 != randintid3_2 and randintid3_4 != randintid3_3:
                        rand_gen_int_id3_4 = db.session.query(interestsimg).filter_by(id=randintid3_4).first()
                        rand_gen_int_num3_4 = rand_gen_int_id3_4.imgnum[:-1]
                        rand_gen_int_cat3_4 = rand_gen_int_id3_4.imgcategory
                        rand_gen_int_name3_4 = rand_gen_int_id3_4.interestname
                        i=str(random.randrange(1,4))
                        if rand_gen_int_name3_4 != usr_int1 and rand_gen_int_name3_4 != usr_int2 and rand_gen_int_name3_4 != usr_int3 and rand_gen_int_name3_4 != usr_int4 and rand_gen_int_name3_4 != usr_int5 and rand_gen_int_name3_4 != usr_int6 and rand_gen_int_name3_4 != usr_int7 and rand_gen_int_name3_4 != usr_int8 and rand_gen_int_name3_4 != usr_int9 and rand_gen_int_name3_4 != usr_int10 and rand_gen_int_name3_4 != usr_int11 and rand_gen_int_name3_4 != usr_int12 and rand_gen_int_name3_4 != usr_int13 and rand_gen_int_name3_4 != usr_int14 and rand_gen_int_name3_4 != usr_int15:
                            if rand_gen_int_cat3_4 != rand_gen_int_cat3_1 and rand_gen_int_cat3_4 != rand_gen_int_cat3_2 and rand_gen_int_cat3_4 != rand_gen_int_cat3_3:
                                randpicname3_4= secure_filename(rand_gen_int_num3_4+i+".jpg")
                                img3_4 = Image.open(intimgpath+"/"+randpicname3_4)
                                width, hight = img3_4.size
                                new_width= width//2
                                new_hight= hight//2
                                resized_img3_4=img3_4.resize((new_width,new_hight))
                                area3_4=(960,540)
                                BGimg3.paste(resized_img3_4,area3_4)
                                break
                            else:
                                randintid3_4 = random.randrange(1, db.session.query(interestsimg).count())
                        else:
                            randintid3_4 = random.randrange(1, db.session.query(interestsimg).count())
                    else:
                        randintid3_4 = random.randrange(1, db.session.query(interestsimg).count())
                data3 = io.BytesIO()
                BGimg3.save(data3,"JPEG")
                encode_img_data3 = base64.b64encode(data3.getvalue())
                #----------------------------------------------------------------------------------
                #----------------------------------------------------------------------------------
                #display 4th image
                BGimg4=BGimg           
                randintid4_1 = random.randrange(1, db.session.query(interestsimg).count())
                while True:
                    rand_gen_int_id4_1 = db.session.query(interestsimg).filter_by(id=randintid4_1).first()
                    rand_gen_int_num4_1 = rand_gen_int_id4_1.imgnum[:-1]
                    rand_gen_int_cat4_1 = rand_gen_int_id4_1.imgcategory
                    rand_gen_int_name4_1 = rand_gen_int_id4_1.interestname
                    i=str(random.randrange(1,4))
                    if rand_gen_int_name4_1 != usr_int1 and rand_gen_int_name4_1 != usr_int2 and rand_gen_int_name4_1 != usr_int3 and rand_gen_int_name4_1 != usr_int4 and rand_gen_int_name4_1 != usr_int5 and rand_gen_int_name4_1 != usr_int6 and rand_gen_int_name4_1 != usr_int7 and rand_gen_int_name4_1 != usr_int8 and rand_gen_int_name4_1 != usr_int9 and rand_gen_int_name4_1 != usr_int10 and rand_gen_int_name4_1 != usr_int11 and rand_gen_int_name4_1 != usr_int12 and rand_gen_int_name4_1 != usr_int13 and rand_gen_int_name4_1 != usr_int14 and rand_gen_int_name4_1 != usr_int15:
                        randpicname4_1= secure_filename(rand_gen_int_num4_1+i+".jpg")
                        img4_1 = Image.open(intimgpath+"/"+randpicname4_1)
                        width, hight = img4_1.size
                        new_width= width//2
                        new_hight= hight//2
                        resized_img4_1=img4_1.resize((new_width,new_hight))
                        area4_1=(0,0)
                        BGimg4.paste(resized_img4_1,area4_1)
                        break
                    else:
                        randintid4_1 = random.randrange(1, db.session.query(interestsimg).count())
                #----------------------------------------------------------------------------------
                randintid4_2 = random.randrange(1, db.session.query(interestsimg).count())
                while True:
                    if randintid4_2 != randintid4_1:
                        rand_gen_int_id4_2 = db.session.query(interestsimg).filter_by(id=randintid4_2).first()
                        rand_gen_int_num4_2 = rand_gen_int_id4_2.imgnum[:-1]
                        rand_gen_int_cat4_2 = rand_gen_int_id4_2.imgcategory
                        rand_gen_int_name4_2 = rand_gen_int_id4_2.interestname
                        i=str(random.randrange(1,4))
                        if rand_gen_int_name4_2 != usr_int1 and rand_gen_int_name4_2 != usr_int2 and rand_gen_int_name4_2 != usr_int3 and rand_gen_int_name4_2 != usr_int4 and rand_gen_int_name4_2 != usr_int5 and rand_gen_int_name4_2 != usr_int6 and rand_gen_int_name4_2 != usr_int7 and rand_gen_int_name4_2 != usr_int8 and rand_gen_int_name4_2 != usr_int9 and rand_gen_int_name4_2 != usr_int10 and rand_gen_int_name4_2 != usr_int11 and rand_gen_int_name4_2 != usr_int12 and rand_gen_int_name4_2 != usr_int13 and rand_gen_int_name4_2 != usr_int14 and rand_gen_int_name4_2 != usr_int15:
                            if rand_gen_int_cat4_2 != rand_gen_int_cat4_1:
                                randpicname4_2= secure_filename(rand_gen_int_num4_2+i+".jpg")
                                img4_2 = Image.open(intimgpath+"/"+randpicname4_2)
                                width, hight = img4_2.size
                                new_width= width//2
                                new_hight= hight//2
                                resized_img4_2=img4_2.resize((new_width,new_hight))
                                area4_2=(960,0)
                                BGimg4.paste(resized_img4_2,area4_2)
                                break
                            else:
                                randintid4_2 = random.randrange(1, db.session.query(interestsimg).count())
                        else:
                            randintid4_2 = random.randrange(1, db.session.query(interestsimg).count())
                    else:
                        randintid4_2 = random.randrange(1, db.session.query(interestsimg).count())
                #----------------------------------------------------------------------------------
                randintid4_3 = random.randrange(1, db.session.query(interestsimg).count())
                while True:
                    if randintid4_3 != randintid4_1 and randintid4_3 != randintid4_2:
                        rand_gen_int_id4_3 = db.session.query(interestsimg).filter_by(id=randintid4_3).first()
                        rand_gen_int_num4_3 = rand_gen_int_id4_3.imgnum[:-1]
                        rand_gen_int_cat4_3 = rand_gen_int_id4_3.imgcategory
                        rand_gen_int_name4_3 = rand_gen_int_id4_3.interestname
                        i=str(random.randrange(1,4))
                        if rand_gen_int_name4_3 != usr_int1 and rand_gen_int_name4_3 != usr_int2 and rand_gen_int_name4_3 != usr_int3 and rand_gen_int_name4_3 != usr_int4 and rand_gen_int_name4_3 != usr_int5 and rand_gen_int_name4_3 != usr_int6 and rand_gen_int_name4_3 != usr_int7 and rand_gen_int_name4_3 != usr_int8 and rand_gen_int_name4_3 != usr_int9 and rand_gen_int_name4_3 != usr_int10 and rand_gen_int_name4_3 != usr_int11 and rand_gen_int_name4_3 != usr_int12 and rand_gen_int_name4_3 != usr_int13 and rand_gen_int_name4_3 != usr_int14 and rand_gen_int_name4_3 != usr_int15:
                            if rand_gen_int_cat4_3 != rand_gen_int_cat4_1 and rand_gen_int_cat4_3 != rand_gen_int_cat4_2:
                                randpicname4_3= secure_filename(rand_gen_int_num4_3+i+".jpg")
                                img4_3 = Image.open(intimgpath+"/"+randpicname4_3)
                                width, hight = img4_3.size
                                new_width= width//2
                                new_hight= hight//2
                                resized_img4_3=img4_3.resize((new_width,new_hight))
                                area4_3=(0,540)
                                BGimg4.paste(resized_img4_3,area4_3)
                                break
                            else:
                                randintid4_3 = random.randrange(1, db.session.query(interestsimg).count())
                        else:
                            randintid4_3 = random.randrange(1, db.session.query(interestsimg).count())
                    else:
                        randintid4_3 = random.randrange(1, db.session.query(interestsimg).count())
                #----------------------------------------------------------------------------------
                randintid4_4 = random.randrange(1, db.session.query(interestsimg).count())
                while True:
                    if randintid4_4 != randintid4_1 and randintid4_4 != randintid4_2 and randintid4_4 != randintid4_3:
                        rand_gen_int_id4_4 = db.session.query(interestsimg).filter_by(id=randintid4_4).first()
                        rand_gen_int_num4_4 = rand_gen_int_id4_4.imgnum[:-1]
                        rand_gen_int_cat4_4 = rand_gen_int_id4_4.imgcategory
                        rand_gen_int_name4_4 = rand_gen_int_id4_4.interestname
                        i=str(random.randrange(1,4))
                        if rand_gen_int_name4_4 != usr_int1 and rand_gen_int_name4_4 != usr_int2 and rand_gen_int_name4_4 != usr_int3 and rand_gen_int_name4_4 != usr_int4 and rand_gen_int_name4_4 != usr_int5 and rand_gen_int_name4_4 != usr_int6 and rand_gen_int_name4_4 != usr_int7 and rand_gen_int_name4_4 != usr_int8 and rand_gen_int_name4_4 != usr_int9 and rand_gen_int_name4_4 != usr_int10 and rand_gen_int_name4_4 != usr_int11 and rand_gen_int_name4_4 != usr_int12 and rand_gen_int_name4_4 != usr_int13 and rand_gen_int_name4_4 != usr_int14 and rand_gen_int_name4_4 != usr_int15:
                            if rand_gen_int_cat4_4 != rand_gen_int_cat4_1 and rand_gen_int_cat4_4 != rand_gen_int_cat4_2 and rand_gen_int_cat4_4 != rand_gen_int_cat4_3:
                                randpicname4_4= secure_filename(rand_gen_int_num4_4+i+".jpg")
                                img4_4 = Image.open(intimgpath+"/"+randpicname4_4)
                                width, hight = img4_4.size
                                new_width= width//2
                                new_hight= hight//2
                                resized_img4_4=img4_4.resize((new_width,new_hight))
                                area4_4=(960,540)
                                BGimg4.paste(resized_img4_4,area4_4)
                                break
                            else:
                                randintid4_4 = random.randrange(1, db.session.query(interestsimg).count())
                        else:
                            randintid4_4 = random.randrange(1, db.session.query(interestsimg).count())
                    else:
                        randintid4_4 = random.randrange(1, db.session.query(interestsimg).count())
                data4 = io.BytesIO()
                BGimg4.save(data4,"JPEG")
                encode_img_data4 = base64.b64encode(data4.getvalue())
                #----------------------------------------------------------------------------------
                #----------------------------------------------------------------------------------
                #display 5th image
                BGimg5=BGimg           
                randintid5_1 = random.randrange(1, db.session.query(interestsimg).count())
                while True:
                    rand_gen_int_id5_1 = db.session.query(interestsimg).filter_by(id=randintid5_1).first()
                    rand_gen_int_num5_1 = rand_gen_int_id5_1.imgnum[:-1]
                    rand_gen_int_cat5_1 = rand_gen_int_id5_1.imgcategory
                    rand_gen_int_name5_1 = rand_gen_int_id5_1.interestname
                    i=str(random.randrange(1,4))
                    if rand_gen_int_name5_1 != usr_int1 and rand_gen_int_name5_1 != usr_int2 and rand_gen_int_name5_1 != usr_int3 and rand_gen_int_name5_1 != usr_int4 and rand_gen_int_name5_1 != usr_int5 and rand_gen_int_name5_1 != usr_int6 and rand_gen_int_name5_1 != usr_int7 and rand_gen_int_name5_1 != usr_int8 and rand_gen_int_name5_1 != usr_int9 and rand_gen_int_name5_1 != usr_int10 and rand_gen_int_name5_1 != usr_int11 and rand_gen_int_name5_1 != usr_int12 and rand_gen_int_name5_1 != usr_int13 and rand_gen_int_name5_1 != usr_int14 and rand_gen_int_name5_1 != usr_int15:
                        randpicname5_1= secure_filename(rand_gen_int_num5_1+i+".jpg")
                        img5_1 = Image.open(intimgpath+"/"+randpicname5_1)
                        width, hight = img5_1.size
                        new_width= width//2
                        new_hight= hight//2
                        resized_img5_1=img5_1.resize((new_width,new_hight))
                        area5_1=(0,0)
                        BGimg5.paste(resized_img5_1,area5_1)
                        break
                    else:
                        randintid5_1 = random.randrange(1, db.session.query(interestsimg).count())
                #----------------------------------------------------------------------------------
                randintid5_2 = random.randrange(1, db.session.query(interestsimg).count())
                while True:
                    if randintid5_2 != randintid5_1:
                        rand_gen_int_id5_2 = db.session.query(interestsimg).filter_by(id=randintid5_2).first()
                        rand_gen_int_num5_2 = rand_gen_int_id5_2.imgnum[:-1]
                        rand_gen_int_cat5_2 = rand_gen_int_id5_2.imgcategory
                        rand_gen_int_name5_2 = rand_gen_int_id5_2.interestname
                        i=str(random.randrange(1,4))
                        if rand_gen_int_name5_2 != usr_int1 and rand_gen_int_name5_2 != usr_int2 and rand_gen_int_name5_2 != usr_int3 and rand_gen_int_name5_2 != usr_int4 and rand_gen_int_name5_2 != usr_int5 and rand_gen_int_name5_2 != usr_int6 and rand_gen_int_name5_2 != usr_int7 and rand_gen_int_name5_2 != usr_int8 and rand_gen_int_name5_2 != usr_int9 and rand_gen_int_name5_2 != usr_int10 and rand_gen_int_name5_2 != usr_int11 and rand_gen_int_name5_2 != usr_int12 and rand_gen_int_name5_2 != usr_int13 and rand_gen_int_name5_2 != usr_int14 and rand_gen_int_name5_2 != usr_int15:
                            if rand_gen_int_cat5_2 != rand_gen_int_cat5_1:
                                randpicname5_2= secure_filename(rand_gen_int_num5_2+i+".jpg")
                                img5_2 = Image.open(intimgpath+"/"+randpicname5_2)
                                width, hight = img5_2.size
                                new_width= width//2
                                new_hight= hight//2
                                resized_img5_2=img5_2.resize((new_width,new_hight))
                                area5_2=(960,0)
                                BGimg5.paste(resized_img5_2,area5_2)
                                break
                            else:
                                randintid5_2 = random.randrange(1, db.session.query(interestsimg).count())
                        else:
                            randintid5_2 = random.randrange(1, db.session.query(interestsimg).count())
                    else:
                        randintid5_2 = random.randrange(1, db.session.query(interestsimg).count())
                #----------------------------------------------------------------------------------
                randintid5_3 = random.randrange(1, db.session.query(interestsimg).count())
                while True:
                    if randintid5_3 != randintid5_1 and randintid5_3 != randintid5_2:
                        rand_gen_int_id5_3 = db.session.query(interestsimg).filter_by(id=randintid5_3).first()
                        rand_gen_int_num5_3 = rand_gen_int_id5_3.imgnum[:-1]
                        rand_gen_int_cat5_3 = rand_gen_int_id5_3.imgcategory
                        rand_gen_int_name5_3 = rand_gen_int_id5_3.interestname
                        i=str(random.randrange(1,4))
                        if rand_gen_int_name5_3 != usr_int1 and rand_gen_int_name5_3 != usr_int2 and rand_gen_int_name5_3 != usr_int3 and rand_gen_int_name5_3 != usr_int4 and rand_gen_int_name5_3 != usr_int5 and rand_gen_int_name5_3 != usr_int6 and rand_gen_int_name5_3 != usr_int7 and rand_gen_int_name5_3 != usr_int8 and rand_gen_int_name5_3 != usr_int9 and rand_gen_int_name5_3 != usr_int10 and rand_gen_int_name5_3 != usr_int11 and rand_gen_int_name5_3 != usr_int12 and rand_gen_int_name5_3 != usr_int13 and rand_gen_int_name5_3 != usr_int14 and rand_gen_int_name5_3 != usr_int15:
                            if rand_gen_int_cat5_3 != rand_gen_int_cat5_1 and rand_gen_int_cat5_3 != rand_gen_int_cat5_2:
                                randpicname5_3= secure_filename(rand_gen_int_num5_3+i+".jpg")
                                img5_3 = Image.open(intimgpath+"/"+randpicname5_3)
                                width, hight = img5_3.size
                                new_width= width//2
                                new_hight= hight//2
                                resized_img5_3=img5_3.resize((new_width,new_hight))
                                area5_3=(0,540)
                                BGimg5.paste(resized_img5_3,area5_3)
                                break
                            else:
                                randintid5_3 = random.randrange(1, db.session.query(interestsimg).count())
                        else:
                            randintid5_3 = random.randrange(1, db.session.query(interestsimg).count())
                    else:
                        randintid5_3 = random.randrange(1, db.session.query(interestsimg).count())
                #----------------------------------------------------------------------------------
                randintid5_4 = random.randrange(1, db.session.query(interestsimg).count())
                while True:
                    if randintid5_4 != randintid5_1 and randintid5_4 != randintid5_2 and randintid5_4 != randintid5_3:
                        rand_gen_int_id5_4 = db.session.query(interestsimg).filter_by(id=randintid5_4).first()
                        rand_gen_int_num5_4 = rand_gen_int_id5_4.imgnum[:-1]
                        rand_gen_int_cat5_4 = rand_gen_int_id5_4.imgcategory
                        rand_gen_int_name5_4 = rand_gen_int_id5_4.interestname
                        i=str(random.randrange(1,4))
                        if rand_gen_int_name5_4 != usr_int1 and rand_gen_int_name5_4 != usr_int2 and rand_gen_int_name5_4 != usr_int3 and rand_gen_int_name5_4 != usr_int4 and rand_gen_int_name5_4 != usr_int5 and rand_gen_int_name5_4 != usr_int6 and rand_gen_int_name5_4 != usr_int7 and rand_gen_int_name5_4 != usr_int8 and rand_gen_int_name5_4 != usr_int9 and rand_gen_int_name5_4 != usr_int10 and rand_gen_int_name5_4 != usr_int11 and rand_gen_int_name5_4 != usr_int12 and rand_gen_int_name5_4 != usr_int13 and rand_gen_int_name5_4 != usr_int14 and rand_gen_int_name5_4 != usr_int15:
                            if rand_gen_int_cat5_4 != rand_gen_int_cat5_1 and rand_gen_int_cat5_4 != rand_gen_int_cat5_2 and rand_gen_int_cat5_4 != rand_gen_int_cat5_3:
                                randpicname5_4= secure_filename(rand_gen_int_num5_4+i+".jpg")
                                img5_4 = Image.open(intimgpath+"/"+randpicname5_4)
                                width, hight = img5_4.size
                                new_width= width//2
                                new_hight= hight//2
                                resized_img5_4=img5_4.resize((new_width,new_hight))
                                area5_4=(960,540)
                                BGimg5.paste(resized_img5_4,area5_4)
                                break
                            else:
                                randintid5_4 = random.randrange(1, db.session.query(interestsimg).count())
                        else:
                            randintid5_4 = random.randrange(1, db.session.query(interestsimg).count())
                    else:
                        randintid5_4 = random.randrange(1, db.session.query(interestsimg).count())
                data5 = io.BytesIO()
                BGimg5.save(data5,"JPEG")
                encode_img_data5 = base64.b64encode(data5.getvalue())
                #----------------------------------------------------------------------------------
                #----------------------------------------------------------------------------------
                #display 6th image
                BGimg6=BGimg           
                randintid6_1 = random.randrange(1, db.session.query(interestsimg).count())
                while True:
                    rand_gen_int_id6_1 = db.session.query(interestsimg).filter_by(id=randintid6_1).first()
                    rand_gen_int_num6_1 = rand_gen_int_id6_1.imgnum[:-1]
                    rand_gen_int_cat6_1 = rand_gen_int_id6_1.imgcategory
                    rand_gen_int_name6_1 = rand_gen_int_id6_1.interestname
                    i=str(random.randrange(1,4))
                    if rand_gen_int_name6_1 != usr_int1 and rand_gen_int_name6_1 != usr_int2 and rand_gen_int_name6_1 != usr_int3 and rand_gen_int_name6_1 != usr_int4 and rand_gen_int_name6_1 != usr_int5 and rand_gen_int_name6_1 != usr_int6 and rand_gen_int_name6_1 != usr_int7 and rand_gen_int_name6_1 != usr_int8 and rand_gen_int_name6_1 != usr_int9 and rand_gen_int_name6_1 != usr_int10 and rand_gen_int_name6_1 != usr_int11 and rand_gen_int_name6_1 != usr_int12 and rand_gen_int_name6_1 != usr_int13 and rand_gen_int_name6_1 != usr_int14 and rand_gen_int_name6_1 != usr_int15:
                        randpicname6_1= secure_filename(rand_gen_int_num6_1+i+".jpg")
                        img6_1 = Image.open(intimgpath+"/"+randpicname6_1)
                        width, hight = img6_1.size
                        new_width= width//2
                        new_hight= hight//2
                        resized_img6_1=img6_1.resize((new_width,new_hight))
                        area6_1=(0,0)
                        BGimg6.paste(resized_img6_1,area6_1)
                        break
                    else:
                        randintid6_1 = random.randrange(1, db.session.query(interestsimg).count())
                #----------------------------------------------------------------------------------
                randintid6_2 = random.randrange(1, db.session.query(interestsimg).count())
                while True:
                    if randintid6_2 != randintid6_1:
                        rand_gen_int_id6_2 = db.session.query(interestsimg).filter_by(id=randintid5_2).first()
                        rand_gen_int_num6_2 = rand_gen_int_id6_2.imgnum[:-1]
                        rand_gen_int_cat6_2 = rand_gen_int_id6_2.imgcategory
                        rand_gen_int_name6_2 = rand_gen_int_id6_2.interestname
                        i=str(random.randrange(1,4))
                        if rand_gen_int_name6_2 != usr_int1 and rand_gen_int_name6_2 != usr_int2 and rand_gen_int_name6_2 != usr_int3 and rand_gen_int_name6_2 != usr_int4 and rand_gen_int_name6_2 != usr_int5 and rand_gen_int_name6_2 != usr_int6 and rand_gen_int_name6_2 != usr_int7 and rand_gen_int_name6_2 != usr_int8 and rand_gen_int_name6_2 != usr_int9 and rand_gen_int_name6_2 != usr_int10 and rand_gen_int_name6_2 != usr_int11 and rand_gen_int_name6_2 != usr_int12 and rand_gen_int_name6_2 != usr_int13 and rand_gen_int_name6_2 != usr_int14 and rand_gen_int_name6_2 != usr_int15:
                            if rand_gen_int_cat6_2 != rand_gen_int_cat6_1:
                                randpicname6_2= secure_filename(rand_gen_int_num6_2+i+".jpg")
                                img6_2 = Image.open(intimgpath+"/"+randpicname6_2)
                                width, hight = img6_2.size
                                new_width= width//2
                                new_hight= hight//2
                                resized_img6_2=img6_2.resize((new_width,new_hight))
                                area6_2=(960,0)
                                BGimg6.paste(resized_img6_2,area6_2)
                                break
                            else:
                                randintid6_2 = random.randrange(1, db.session.query(interestsimg).count())
                        else:
                            randintid6_2 = random.randrange(1, db.session.query(interestsimg).count())
                    else:
                        randintid6_2 = random.randrange(1, db.session.query(interestsimg).count())
                #----------------------------------------------------------------------------------
                randintid6_3 = random.randrange(1, db.session.query(interestsimg).count())
                while True:
                    if randintid6_3 != randintid6_1 and randintid6_3 != randintid6_2:
                        rand_gen_int_id6_3 = db.session.query(interestsimg).filter_by(id=randintid6_3).first()
                        rand_gen_int_num6_3 = rand_gen_int_id6_3.imgnum[:-1]
                        rand_gen_int_cat6_3 = rand_gen_int_id6_3.imgcategory
                        rand_gen_int_name6_3 = rand_gen_int_id6_3.interestname
                        i=str(random.randrange(1,4))
                        if rand_gen_int_name6_3 != usr_int1 and rand_gen_int_name6_3 != usr_int2 and rand_gen_int_name6_3 != usr_int3 and rand_gen_int_name6_3 != usr_int4 and rand_gen_int_name6_3 != usr_int5 and rand_gen_int_name6_3 != usr_int6 and rand_gen_int_name6_3 != usr_int7 and rand_gen_int_name6_3 != usr_int8 and rand_gen_int_name6_3 != usr_int9 and rand_gen_int_name6_3 != usr_int10 and rand_gen_int_name6_3 != usr_int11 and rand_gen_int_name6_3 != usr_int12 and rand_gen_int_name6_3 != usr_int13 and rand_gen_int_name6_3 != usr_int14 and rand_gen_int_name6_3 != usr_int15:
                            if rand_gen_int_cat6_3 != rand_gen_int_cat6_1 and rand_gen_int_cat6_3 != rand_gen_int_cat6_2:
                                randpicname6_3= secure_filename(rand_gen_int_num6_3+i+".jpg")
                                img6_3 = Image.open(intimgpath+"/"+randpicname6_3)
                                width, hight = img6_3.size
                                new_width= width//2
                                new_hight= hight//2
                                resized_img6_3=img6_3.resize((new_width,new_hight))
                                area6_3=(0,540)
                                BGimg6.paste(resized_img6_3,area6_3)
                                break
                            else:
                                randintid6_3 = random.randrange(1, db.session.query(interestsimg).count())
                        else:
                            randintid6_3 = random.randrange(1, db.session.query(interestsimg).count())
                    else:
                        randintid6_3 = random.randrange(1, db.session.query(interestsimg).count())
                #----------------------------------------------------------------------------------
                randintid6_4 = random.randrange(1, db.session.query(interestsimg).count())
                while True:
                    if randintid6_4 != randintid6_1 and randintid6_4 != randintid6_2 and randintid6_4 != randintid6_3:
                        rand_gen_int_id6_4 = db.session.query(interestsimg).filter_by(id=randintid5_4).first()
                        rand_gen_int_num6_4 = rand_gen_int_id6_4.imgnum[:-1]
                        rand_gen_int_cat6_4 = rand_gen_int_id6_4.imgcategory
                        rand_gen_int_name6_4 = rand_gen_int_id6_4.interestname
                        i=str(random.randrange(1,4))
                        if rand_gen_int_name6_4 != usr_int1 and rand_gen_int_name6_4 != usr_int2 and rand_gen_int_name6_4 != usr_int3 and rand_gen_int_name6_4 != usr_int4 and rand_gen_int_name6_4 != usr_int5 and rand_gen_int_name6_4 != usr_int6 and rand_gen_int_name6_4 != usr_int7 and rand_gen_int_name6_4 != usr_int8 and rand_gen_int_name6_4 != usr_int9 and rand_gen_int_name6_4 != usr_int10 and rand_gen_int_name6_4 != usr_int11 and rand_gen_int_name6_4 != usr_int12 and rand_gen_int_name6_4 != usr_int13 and rand_gen_int_name6_4 != usr_int14 and rand_gen_int_name6_4 != usr_int15:
                            if rand_gen_int_cat6_4 != rand_gen_int_cat6_1 and rand_gen_int_cat6_4 != rand_gen_int_cat6_2 and rand_gen_int_cat6_4 != rand_gen_int_cat6_3:
                                randpicname6_4= secure_filename(rand_gen_int_num6_4+i+".jpg")
                                img6_4 = Image.open(intimgpath+"/"+randpicname6_4)
                                width, hight = img6_4.size
                                new_width= width//2
                                new_hight= hight//2
                                resized_img6_4=img6_4.resize((new_width,new_hight))
                                area6_4=(960,540)
                                BGimg6.paste(resized_img6_4,area6_4)
                                break
                            else:
                                randintid6_4 = random.randrange(1, db.session.query(interestsimg).count())
                        else:
                            randintid6_4 = random.randrange(1, db.session.query(interestsimg).count())
                    else:
                        randintid6_4 = random.randrange(1, db.session.query(interestsimg).count())
                data6 = io.BytesIO()
                BGimg6.save(data6,"JPEG")
                encode_img_data6 = base64.b64encode(data6.getvalue())
                #----------------------------------------------------------------------------------
                #----------------------------------------------------------------------------------
                #img display randomization

                ranloc=random.randrange(1,7)
                if ranloc==1:
                    im1=encode_img_data5
                    im2=encode_img_data6
                    im3=encode_img_data4
                    im4=encode_img_data3
                    im5=encode_img_data2
                    im6=encode_img_data1
                elif ranloc==2:
                    im1=encode_img_data6
                    im2=encode_img_data4
                    im3=encode_img_data5
                    im4=encode_img_data2
                    im5=encode_img_data1
                    im6=encode_img_data3
                elif ranloc==3:
                    im1=encode_img_data4
                    im2=encode_img_data2
                    im3=encode_img_data1
                    im4=encode_img_data5
                    im5=encode_img_data3
                    im6=encode_img_data6
                elif ranloc==4:
                    im1=encode_img_data2
                    im2=encode_img_data5
                    im3=encode_img_data3
                    im4=encode_img_data1
                    im5=encode_img_data6
                    im6=encode_img_data4
                elif ranloc==5:
                    im1=encode_img_data1
                    im2=encode_img_data3
                    im3=encode_img_data2
                    im4=encode_img_data6
                    im5=encode_img_data4
                    im6=encode_img_data5
                else:
                    im1=encode_img_data3
                    im2=encode_img_data1
                    im3=encode_img_data6
                    im4=encode_img_data4
                    im5=encode_img_data5
                    im6=encode_img_data2
                return render_template("login2.html", user=current_user, email=email,ranloc=ranloc, picname1=im1.decode("UTF-8"), picname2=im2.decode("UTF-8"), picname3=im3.decode("UTF-8"), picname4=im4.decode("UTF-8"), picname5=im5.decode("UTF-8"), picname6=im6.decode("UTF-8"))
            else:
                flash('Email does not exist.', category='error')
            

    if request.form.get('btn')=="next2":
        if request.method == 'POST':
            isauth=False
            usr_choice= request.form.get('intimg')
            if ranloc==1 and usr_choice.casefold()=="f":
                isauth=True
                email=email
            elif ranloc==2 and usr_choice.casefold()=="e":
                isauth=True
                email=email
            elif ranloc==3 and usr_choice.casefold()=="c":
                isauth=True
                email=email
            elif ranloc==4 and usr_choice.casefold()=="d":
                isauth=True
                email=email
            elif ranloc==5 and usr_choice.casefold()=="a":
                isauth=True
                email=email
            elif ranloc==6 and usr_choice.casefold()=="b":
                isauth=True
                email=email
            else:
                isauth=False
                email=email
        return render_template("login3.html", user=current_user, email=email,isauth=isauth) 

    if request.form.get('btn')=="login":
        if request.method =='POST':
            ranobjname= request.form.get('ranObj').casefold()
            user = db.session.query(User).filter_by(email=email).first()
            

            if isauth and check_password_hash(user.imgname, ranobjname):
                name=user.first_name
                flash('Logged in successfully! Welcome Back '+name, category='success')
                login_user(user)
                return redirect(url_for('home'))
            else:
                flash('Incorrect Image Choice or Object Name, try again.', category='error')
                return redirect(url_for('auth.login'))
        return render_template("login3.html", user=current_user)            
    return render_template("login.html", user=current_user)


       
    


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():

    key= b'_-IlTXCOOJc5TOzQsJOKHqnDzIdB7uIihDuihL05GfY='
    fernet= Fernet(key)
    randimg= str(random.randrange(1, len(os.listdir(RanObjpath))))
    picname = secure_filename(randimg+".jpg")
    img = Image.open(RanObjpath+"/"+picname)
    data = io.BytesIO()
    img.save(data,"JPEG")
    encode_img_data = base64.b64encode(data.getvalue())
    

    if request.method == 'POST':

        email = request.form.get('email')
        first_name = request.form.get('firstName')
        sport = fernet.encrypt(request.form.get('sport').encode())
        outact = fernet.encrypt(request.form.get('outact').encode())
        inact = fernet.encrypt(request.form.get('inact').encode())
        flower = fernet.encrypt(request.form.get('flower').encode())
        ftact = fernet.encrypt(request.form.get('ftact').encode())
        food = fernet.encrypt(request.form.get('food').encode())
        dessert = fernet.encrypt(request.form.get('dessert').encode())
        drink = fernet.encrypt(request.form.get('drink').encode())
        cities = fernet.encrypt(request.form.get('cities').encode())
        place = fernet.encrypt(request.form.get('place').encode())
        pet = fernet.encrypt(request.form.get('pet').encode())
        socapp = fernet.encrypt(request.form.get('socapp').encode())
        craft = fernet.encrypt(request.form.get('craft').encode())
        scsub = fernet.encrypt(request.form.get('scsub').encode())
        transport = fernet.encrypt(request.form.get('transport').encode())
        str_imgname = request.form.get('objname').casefold()
                
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        else:
            new_user = User(email=email, first_name=first_name, imgname=generate_password_hash(
                str_imgname, method='sha256', salt_length=32))
            db.session.add(new_user)
            db.session.commit()
            user_id= db.session.query(User.id).filter_by(email=email)
            new_user_interest= userinterests(user_id=user_id, interestname=sport)
            db.session.add(new_user_interest)
            db.session.commit()
            new_user_interest= userinterests(user_id=user_id, interestname=outact)
            db.session.add(new_user_interest)
            db.session.commit()
            new_user_interest= userinterests(user_id=user_id, interestname=inact)
            db.session.add(new_user_interest)
            db.session.commit()
            new_user_interest= userinterests(user_id=user_id, interestname=flower)
            db.session.add(new_user_interest)
            db.session.commit()
            new_user_interest= userinterests(user_id=user_id, interestname=ftact)
            db.session.add(new_user_interest)
            db.session.commit()
            new_user_interest= userinterests(user_id=user_id, interestname=food)
            db.session.add(new_user_interest)
            db.session.commit()
            new_user_interest= userinterests(user_id=user_id, interestname=dessert)
            db.session.add(new_user_interest)
            db.session.commit()
            new_user_interest= userinterests(user_id=user_id, interestname=drink)
            db.session.add(new_user_interest)
            db.session.commit()
            new_user_interest= userinterests(user_id=user_id, interestname=cities)
            db.session.add(new_user_interest)
            db.session.commit()
            new_user_interest= userinterests(user_id=user_id, interestname=place)
            db.session.add(new_user_interest)
            db.session.commit()
            new_user_interest= userinterests(user_id=user_id, interestname=pet)
            db.session.add(new_user_interest)
            db.session.commit()
            new_user_interest= userinterests(user_id=user_id, interestname=socapp)
            db.session.add(new_user_interest)
            db.session.commit()
            new_user_interest= userinterests(user_id=user_id, interestname=craft)
            db.session.add(new_user_interest)
            db.session.commit()
            new_user_interest= userinterests(user_id=user_id, interestname=scsub)
            db.session.add(new_user_interest)
            db.session.commit()
            new_user_interest= userinterests(user_id=user_id, interestname=transport)
            db.session.add(new_user_interest)
            db.session.commit()
            name=new_user.first_name
      
            flash('Account Created! Nice To Have You '+name, category='success')
            login_user(new_user)
            return redirect(url_for('home'))
        


    return render_template("sign_up.html", user=current_user, picname=encode_img_data.decode("UTF-8"))
