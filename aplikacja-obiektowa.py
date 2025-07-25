import sys

class Students:

 def lista_all_students(self):
     
     student = {"pawel":7777}
     search = int(input(''))

     match search:
      case 1:
        podaj_pesel = int(input("podaj pesel : "))
      case 2:
       return "liczba studentów na liście " , len(student)

     for dane in student.keys():
       if podaj_pesel == student.get(dane):
         return dane
       else:
         return "nic nie odnaleziono " 

print("wpisz 1 aby wyszukać studenta lub 2 by wyświetlić listę zapisanych")
student = Students()

full= student.lista_all_students()

if full==None:
  print('lista jest pusta')
else:
 print(full)


 









  






 

  



 


    



      
     
     





      
 
     
       
 

 

     




 











