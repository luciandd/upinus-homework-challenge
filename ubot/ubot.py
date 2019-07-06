import re
import sys

class Ubot:
  def __init__(self):
    self.x = 0
    self.y = 0
    # 0 is N, 1 is E, 2 is S, 3 is W 
    self.direction = 0

  def _get_commands_array(self, commands):
    p = re.compile('[RL]|[W].+?(?=[RLW]|$)')
    return p.findall(commands)

  def _run_command(self, command):
    if command == "R":
      self.direction = self.direction + 1
    elif command == "L":
      self.direction = self.direction - 1
    else:
      steps = int(command[1:])
      if (self.direction % 4) == 0:
        self.y = self.y + steps
      elif (self.direction % 4) == 1:
        self.x = self.x + steps
      elif (self.direction % 4) == 2:
        self.y = self.y - steps
      else:
        self.x = self.x - steps

  def run(self, commands):
    commands_array = self._get_commands_array(commands)
    for command in commands_array:
      self._run_command(command)

  def get_position(self):
    print(self.direction)
    if (self.direction % 4) == 0:
      direction = "North"
    elif (self.direction % 4) == 1:
      direction = "East"
    elif (self.direction % 4) == 2:
      direction = "South"
    else:
      direction = "West"
    return "X: {} Y: {} Direction: {}".format(self.x, self.y, direction)

if __name__ == '__main__':
   commands = sys.argv[1]
   ubot = Ubot()
   ubot.run(commands)
   result = ubot.get_position()
   print(result)
