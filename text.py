import emoji

def emo(text):
  return emoji.emojize(text)

greeting = emo(f''' , :winking_face: приветствую! 
Для начала новой игры введите команду /new_game
это игра в Candies''')

step = emo(f', твой ход! Сколько возьмешь :candy: ? ')

take_people = emo(f' :candy: и на столе осталось')
robot = emo('ходит :robot:...')
error = emo(':angry_face: Ты взял не правильное количество :candy: надо от 1 до 28 ')

def take_bot(take, remnant):
 return emo(f':robot: взял {take} :candy: и их осталось {remnant}')

win_bot = emo(f':robot: забрал оставшиеся :candy: и победил :person_standing:')
win_people = emo(f' забрал оставшиеся :candy: и победил :desktop_computer:')