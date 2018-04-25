"""游戏状态相关"""
class Game_State():
    def __init__(self,setting):
        self.set=setting
        self.reset_geme()
        self.game_active=False
        """最高记录"""
        self.high_score=0



    """初始化数据"""
    def reset_geme(self):
        self.ships_left=self.set.ship_limit
        self.alines_speed=2
        self.score=0;

