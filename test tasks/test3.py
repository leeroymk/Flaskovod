class Elevator:

    def __init__(self, levels=5, stage=3):
        self.levels = levels
        self.stage = stage

    def up(self):
        if self.stage < self.levels:
            self.stage += 1
            print(f'Лифт поднимается на {self.stage} этаж')
        else:
            print('Лифт не может подняться выше')

    def down(self):
        if self.stage > 1:
            self.stage -= 1
            print(f'Лифт опускается на {self.stage} этаж')
        else:
            print('Лифт не может опуститься ниже')
