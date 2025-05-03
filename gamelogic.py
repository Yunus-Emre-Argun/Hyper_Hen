class GameLogic:
    @staticmethod
    def passControl(chapterOne):
        if chapterOne.missionPass is True:
            chapterOne.enemy = None

    @staticmethod
    def drawChapters(chapterOne, screen):
        if chapterOne.enemy is not None:
            chapterOne.enemy.update()
            chapterOne.enemy.drawEnemy(screen)