import sqlite3
import sys

class Students:
 
 def __init__(self,baza):

  print("wpisz 1 aby wyszukać studenta lub 2 by wyświetlić listę zapisanych")
         
  try:
         
   self.connect = sqlite3.connect(baza)
   dane = self.connect.execute("SELECT * FROM students")
   self.lista_studentów = dane.fetchmany()

  except:
          print("wystapił bład")
          sys.exit()


 def lista_all_students(self):
     
     search = int(input(''))

     match search:
      case 1:
        podaj_pesel = int(input("podaj pesel : "))
      case 2:
       return "liczba studentów na liście " , len(self.lista_studentów)

     for lists in self.lista_studentów:
       
       if podaj_pesel == lists[2]:
          return lists[1]
       
       else:
         return "nic nie odnaleziono "
    
baza = 'baza\students.sqlite'
student = Students(baza)

lists = student.lista_all_students()

if lists == None:
  print('lista jest pusta')

else:
 print(lists)


 









  






 

  



 


    



      
     
     





      
 
     
       
 

 

     




 











