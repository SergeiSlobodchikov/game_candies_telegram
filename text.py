import emoji

def emo(text):
  return emoji.emojize(text)

greeting = emo(f''' , :winking_face: приветствую! 
Это игра в Candies стандартно там 150 конфет,
если хотите поменять например на 300 введите '/set 300' 
Для начала новой игры введите команду /new_game
брать можно не более 28 штук за раз,
игрок выбирается рандомно''')

step = emo(f', твой ход! Сколько возьмешь :candy: ? ')

take_people = emo(f' :candy: и на столе осталось')
robot = emo('ходит :robot:...')
error = emo(':angry_face: Ты взял не правильное количество :candy: надо от 1 до 28 ')
def error_total(text):
  return emo(f':angry_face: Ты взял не правильное количество :candy: надо от 1 до {text}')

def take_bot(take, remnant):
 return emo(f':robot: взял {take} :candy: и их осталось {remnant}')

win_bot = emo(f':robot: забрал оставшиеся :candy: и победил :person_standing:')
win_people = emo(f' забрал оставшиеся :candy: и победил :desktop_computer:')