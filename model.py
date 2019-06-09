import random

class Advertisement:

    def __init__(self, ctr):
        
        self._ctr = ctr
        self._total_showed = 0 # 広告が表示された総数(mi)
        self._total_clicked = 0 # クリックされた総数(ni)
        
    def is_clicked(self):

        if random.random() <= self._ctr:
            self._total_clicked += 1
            return True
        else:
            return False

    def show(self):
        self._total_showed += 1
    
    @property
    def total_showed(self):
        return self._total_showed
    
    @property
    def total_clicked(self):
        return self._total_clicked

    