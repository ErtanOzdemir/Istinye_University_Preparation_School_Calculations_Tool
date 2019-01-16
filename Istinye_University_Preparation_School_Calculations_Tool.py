###This Progam was Made by Ertan Özdemir###
###Bu Program Ertan Özdemir Tarafından Yapıldı###
import os


creator=""" This program was created by Ertan Özdemir"""

sunum= """
*****************************************
  Istinye University Preparation School
      Points Calculation Program v1.0
*****************************************
"""

tanim_tr=""" 
Aşağıda verilen değerler, notlarınızı etkileyen yüzdeliklerdir.
Not: Değerler güncelliklerini yitirmişse bu programı kullanmayın.

			---- SINAVLAR ----

			Quarter Exam         = %20
			Conten Based Test    = %20
			2 Quizes 	     = %10

			 
			---- AKTİVİTELER ----
			Self Checklist (Toplam 5 tane) = %5
			Book Report (Toplam 5 tane)    = %5
			Online Assigment	       = %10
			Derse Aktif Katılım	       = %10
			Task Completion		       = %5
			Yoklama	    		       = %10

"""

tanim_en=""" 
			 You can see percentages of your exam and of your activites notes below.
			 Note: If these percentages not current, you can't use this program.

			 ---- EXAMS ----
			 Quarter Exam	     = %20
			 Conten Based Test   = %20
			 2 Quizes  	     = %10

			 
			 ---- ACTIVITIES ----
			 Self Checklist (Toplam 5 tane) = %5
			 Book Report (Toplam 5 tane)    = %5
			 Online Assigment		= %10
			 Class Partipication		= %10
			 Task Completion		= %5
			 Attendance			= %10

			 """
print(creator)
print(sunum)

while True:
    secim_ekranı="""
    1)Ortalama Hesaplama / Avarage Calculation
    2)Content Base'den kaç almalıyım? / How many should I take from the Content Base?"""

    print(secim_ekranı)
    secim=input("\nSeçiminiz (1 veya 2) / Your choice (1 or 2):")



    if secim=="1":

        dil="""

        1)Türkçe
        2)English
        """
        print(dil)

        dil_sec=input("Hangi dil? (1 veya 2) / Which languege? (1 or 2): ")

   

        if dil_sec == "1":
            print(tanim_tr)
            print("""Türkçe seçtiniz. Aşağıya sonuçlarınızı yazınız. Yanlarında yazabileceğiniz en yüksek puan yazmaktadır.""")

            quarter_tr=int(input("Quarter Sonucu (100p): "))
            content_tr=int(input("Content Base Test (100p): "))
            quiz_tr=int(input("2 Quizinizin 50 üzerinden toplamlam sonucunu yazın (örn: 44+46 = 90)(100p): "))

            self_tr=int(input("Self Checklist Puanınız (5p): "))
            book_tr=int(input("Book Report Puanınız (10p): "))
            assigment_tr=int(input("Online Assigment Puanınız (10p): "))
            ders_tr=int(input("Derse Aktif Katılım Puanınız (10p): "))
            task_tr=int(input("Task Completion Puanınız(5p): "))
            yoklama_tr=int(input("Yoklama Puanı (10p) : "))

            adim1=quarter_tr+content_tr+quiz_tr+self_tr+book_tr+assigment_tr+ders_tr+task_tr+yoklama_tr
            adim2=(adim1*100)/350
            print(adim2)

            if adim2>=75:
                print("Bravo! ortalamanız {} olduğu için Level Achievement sınavına girebilirsiniz. ".format(int(adim2)))
                input("Enter'a basın.")
                os.system('cls' if os.name=="nt" else "clear")
            else:
                print("Maalesef, ortalamanız {} olduğu için Level Achievement sınavına giremezsiniz.".format(int(adim2)))
                input("Enter'a basın.")
                os.system('cls' if os.name=="nt" else "clear")

        elif dil_sec == "2":
            print(tanim_en)
            print("""You chose English. You must write your results below. You can see max point next the commands.""")

            quarter_en=int(input("Quarter Results (100p): "))
            content_en=int(input("Content Base Test (100p): "))
            quiz_en=int(input("You must write 2 exams sum (example: 44+46 = 90)(100p): "))

            self_en=int(input("Self Checklist Point (5p): "))
            book_en=int(input("Book Report Point (10p): "))
            assigment_en=int(input("Online Assigment Point (10p): "))
            class_en=int(input("Class Partipication Point (10p): "))
            task_en=int(input("Task Completion Point(5p): "))
            attendance_en=int(input("Attendance Point (10p) : "))

            step1=quarter_en+content_en+quiz_en+self_en+book_en+assigment_en+class_en+task_en+attendance_en
            step2=(step1*100)/350

            if step2>=75:
                print("Bravo! Your avarage is {}. You can enter Level Achievement. ".format(int(step2)))
                input("Press Enter")
                os.system('cls' if os.name=="nt" else "clear")
            else:
                print("Unfortunately! Your avarage is {}. You musn't enter Level Achievement. ".format(int(step2)))
                input("Press Enter")
                os.system('cls' if os.name=="nt" else "clear")
        else:
            print("Yanlış işlem!/Wrong operation!")
            input("Enter'a basın./Press Enter!")
            os.system('cls' if os.name=="nt" else "clear")

    elif secim=="2":
        quarter_en=int(input("Quarter Results (100p): "))
        quiz_en=int(input("You must write 2 exams sum (example: 44+46 = 90)(100p): "))

        self_en=int(input("Self Checklist Point (5p): "))
        book_en=int(input("Book Report Point (10p): "))
        assigment_en=int(input("Online Assigment Point (10p): "))
        class_en=int(input("Class Partipication Point (10p): "))
        task_en=int(input("Task Completion Point(5p): "))
        attendance_en=int(input("Attendance Point (10p) : "))

        step3=quarter_en+quiz_en+self_en+book_en+assigment_en+class_en+task_en+attendance_en
        step4=262.5-step3
        print("You must take {} points".format(step4))
        input("Press Enter")
        os.system('cls' if os.name=="nt" else "clear")

    else:
        print("Yanlış işlem!/Wrong operation!")
        input("Enter'a basın./Press Enter!")
        os.system('cls' if os.name=="nt" else "clear")

    
