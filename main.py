AssistentName="Кишмиш."
print("Привет! давай знкомться, меня зовут "+AssistentName)
UserName=input("А тебя как зовут?")
print("Приятно познакомиться"+UserName+".")
UserAge=int(input("A лет тебе сколько?"))
print("ОГО! тебе через десять лет уже",UserAge+10," будет.")
UserRise=float(input("крутяк а рост тебя какой?Вот мой 0.53."))
print("да ты меня выше на", round( UserRise-0.53,2))
print("Приятно познакомиться:",UserName,UserAge, "лет!рост", UserRise,"." )
print ("А давай поиграем, вот что я могу:")
print ("1 рассказать анекдот")
print ("2 показать фокус")
print ("3 угадать твой знак зодиака")
WhatNeed=int(input("Выбери 1,2 или 3"))
if WhatNeed==1:
  print("""От мужика ушла жена. Едет он в машине расстроенный, на своей волне. Бац, мента насмерть сбивает. Что делать? Он – мента в багажник, сам – на кладбище. Приезжает, там сторож водку хлещет. Мужик сторожу говорит: 
   – Слушай, закопай его где-нибудь, а я тебе 100 баксов заплачу. 
   Сторож согласился. Мужик с кладбища едет в шоке: жена ушла, мента сбил. Бац, второго мента сбивает и тоже насмерть. Что делать? Денег-то больше нет. Думает: "Подброшу сторожу по-тихому, может не заметит." 
   Подъезжает на кладбище и тихонько сторожу мента подбрасывает. Сторож только первого закопал, оборачивается, мент лежит. Что за хрень? Ну, делать нечего, пришлось закапывать. А около кладбища стоит пост ДПС. Гаишник смотрит, машина одна и та же туда-сюда мотается, решил проверить, в чём дело. 
   Идёт на кладбище, там сторож только второго мента закопал. Гаишник спрашивает: 
   – Что у вас тут происходит? 
   А сторож его по голове лопатой хрясь: 
   – Да, ты уляжешься сегодня или нет!?""")
if WhatNeed==2:
  Number=int(input("задумай число от одного  до десяти умножь\n на само себя округли до  следующего десятка умножь на 2 на 3 прибавь 100 и запиши последнюю цифру  получившегося числа умноженную на саму себя"))
  if  Number==1:
   print("ты загадал 1!")
  if  Number==4:
   print("ты загадал 2!")
  if  Number==9:
   print("ты загадал 3!")
  if  Number==16:
   print("ты загадал 4!")
  if  Number==25:
   print("ты загадал 5!")
  if  Number==36:
   print("ты загадал 6!")
  if  Number==49:
   print("ты загадал 7!")
  if  Number==64:
   print("ты загадал 8!")
  if  Number==81:
   print("ты загадал 9!")
  if  Number==100:
   print("ты загадал 10!")
if WhatNeed==3:
  CHAK1=int(input("посчитай в каком по счету дне в месяце ты родился")) 
  CHAK2=int(input("посчитай в каком по счету месяце ты родился"))
  if (CHAK2==12 and CHAK1>=22) or (CHAK2==1 and CHAK1<=20):
    print("ты козерог!")
  elif (CHAK2==1 and CHAK1>=21) or (CHAK2==2 and CHAK1<=18):
    print("ты водолей!")  
  elif (CHAK2==2 and CHAK1>=19) or (CHAK2==3 and CHAK1<=20):
    print("ты рыбы!")
  elif (CHAK2==3 and CHAK1>=21) or (CHAK2==4 and CHAK1<=20):
    print("ты овен!")
  elif (CHAK2==4 and CHAK1>=21) or (CHAK2==5 and CHAK1<=21):
    print("ты телец!")  
  elif (CHAK2==5 and CHAK1>=22) or (CHAK2==6 and CHAK1<=21):
    print("ты близнецы!")
  elif (CHAK2==6 and CHAK1>=22) or (CHAK2==7 and CHAK1<=22):
      print("ты рак!")
  elif (CHAK2==7 and CHAK1>=23) or (CHAK2==8 and CHAK1<=23):                  
      print("ты лев!")  
  elif (CHAK2==8 and CHAK1>=24) or (CHAK2==9 and CHAK1<=23):
      print("ты дева!")
  elif (CHAK2==10 and CHAK1>=24) or (CHAK2==11 and CHAK1<=23):
      print("ты весы!")
  elif (CHAK2==1 and CHAK1>=24) or (CHAK2==12 and CHAK1<=22):
      print("ты скорпион!")  
  elif (CHAK2==12 and CHAK1>=23) or (CHAK2==1 and CHAK1<=21):
      print("ты стрелец!")
    
    
    