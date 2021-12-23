from Partes import Partes

class Forma:
 
   partes = []
   minhaForma = []

   
   def __init__(self,x,y,forma) -> None:
      
        self.minhaForma = forma
        self.x = x
        self.y = y
        for i in range(0,3):
            for j in range(0,3):
                if forma[i][j] == 1:
                    self.partes.append(Partes(self,j,i))
        

   def down(self):
       for i in self.partes:
           i.y += 2

   def move(self,side):
       if side == "RIGHT":
          for i in self.partes:
              i.x += 20

       if side == "LEFT":
            for i in self.partes:
                i.x -= 20

    
        
    
    


        