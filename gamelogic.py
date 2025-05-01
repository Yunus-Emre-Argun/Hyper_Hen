


class GameLogic:
    @staticmethod
    def passControl(chapterOne):
        if chapterOne.missionPass is True:
            chapterOne.enemy=None


    @staticmethod
    def drawChapters(chapterOne,screen):
        chapterOne.enemy.moveEnemy()
        chapterOne.enemy.enemyRangeControl()
        chapterOne.enemy.drawEnemy(screen)





