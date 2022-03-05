## random name stuff

import random

first_names = ['John', 'Mike', 'Kyra', 'Sarah', 'Rishi', 'Pete', 'Satan', 'Dave', 'Ahmed','Bruce', 'Christine', 'Phil','Charlotte', 'Leah', 'Erin', 'Seth', 'Erica', 'Rachel', 'Shep', 'Deuce']
last_initials = ['B.', 'Q.', 'S.', 'T.', 'W.', 'L.', 'V.', 'G.', 'Z.', 'A.', 'C,', 'D', 'F.', 'J']

def random_name():
  random_name = first_names[random.randint(0, len(first_names)-1)] + " " + last_initials[random.randint(0, len(last_initials)-1)]
  return random_name

