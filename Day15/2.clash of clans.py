#1. Design a dummy game like clash of clans
#sai kumar satapathy
from abc import ABC,abstractmethod

class heal(ABC):
   @abstractmethod
   def healer(self):
      pass
class self_heal(heal):
   def healer(self):
      print("************initialising the self heal mode************")

class external(heal):
   def healer(self):
      print("**********external boosters are enabled to heal***********")
   
class refillable(ABC):
   @abstractmethod
   def refill(self):
      pass

class time(refillable):
   def refill(self):
      print("**********time based refill accomplished***********")

class weapon(refillable):
   def refill(self):
      print("***********weapons are reloaded***********")

class soldier(ABC):
   def gather(self):
      print("**************squad gathering**************")
   @abstractmethod
   def attack(self):
      pass

class archer(soldier):
   def attack(self):
      print("*************archers are in a hunt*************")
   def refill(self):
      return time().refill()
   def healer(self):
      return external().healer()

class spearmen(soldier):
   def attack(self):
      print("*********spearmen are on the frontline to attack********")
   def healer(self):
      return self_heal().healer()

class gunmen(soldier):
   def attack(self):
      print("**********gunmen aiming for the headshot***********")
   def refill(self):
      return weapon().refill()


a1=archer()
g1=gunmen()
s1=spearmen()

ch=input("press enter to start the game")
while ch!='e':
   if ch!='e':
      print("ga-gather archer",end='\n'+"aa- archer attack")
      print("\ngg-gather gunmen",end='\n'+"ga-gunmen attack")
      print("\ngs-spearmen gather",end='\n'+"sa-spearmen attack")
      print("\nhs-heal spearmen",end='\n'+"ha-arher heal")
    
      
      ch=input("\nenter the options above to play and enter 'e' to exit:")
      if ch=='ga':
         a1.gather()
         print("\n")
      elif ch=='aa':
         a1.attack()
         print("\n")
      elif ch=='gg':
         g1.gather()
         print("\n")
      elif ch=='ga':
         g1.attack()
         print("\n")
      elif ch=='gs':
         s1.gather()
         print("\n")
      elif ch=='sa':
         s1.attack()
         print("\n")
      elif ch=='hg':
         g1.healer()
         print("\n")
      elif ch=='ha':
         a1.healer()
         print("\n")
      elif ch=='hs':
         s1.healer()
         print("\n")
     
   else:
      exit(0)
      
   
      
      







   
