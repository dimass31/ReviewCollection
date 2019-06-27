from parsing import Parser

start = 298 #Стартовое значение
end = 299 #Конечное занчение

#Функция удаления переноса строки в одном отзыве
def cclear(spis):
   if len(spis) > 0:
      for i in range(len(spis)):
         spis[i] = spis[i].replace('\n', "")

#Функция записи отзывов в файл
def zap(spis, file):
   if len(spis)>0:
      f = open(file, "a", encoding="UTF-8")
      for i in spis:
         string = i + '\n'
         f.write(string)
      f.close()

#Цикл хождения по фильмам, сбора и записи отзывов
for i in range(start, end+1):

   parser = Parser('https://www.kinopoisk.ru/film/'+ str(i) +'/')
   parser.start()


   positiv = parser.positiv()
   negativ = parser.negativ()
   neutral = parser.neutral()

   cclear(positiv)
   cclear(negativ)
   cclear(neutral)


   zap(positiv, "kinopoisk_pos.txt")
   zap(negativ, "kinopoisk_neg.txt")
   zap(neutral, "kinopoisk_neutral.txt")

   print(len(positiv))
   print(len(negativ))
   print(len(neutral))

   parser.close()