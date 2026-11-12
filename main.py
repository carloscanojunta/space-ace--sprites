@namespace
class SpriteKind:
    StatusBar = SpriteKind.create()
    satellite = SpriteKind.create()
    Healing = SpriteKind.create()
    button = SpriteKind.create()
    ammo = SpriteKind.create()
    reload = SpriteKind.create()
    console = SpriteKind.create()
    title = SpriteKind.create()
    credit = SpriteKind.create()

def on_on_overlap(sprite, otherSprite):
    global healthBar
    sprites.destroy(healingDrop, effects.blizzard, 200)
    if healthBar < 101:
        music.play(music.melody_playable(music.magic_wand),
            music.PlaybackMode.IN_BACKGROUND)
        healthBar = healthBar + 25
        if healthBar > 100:
            healthBar = 100
    checkHealth()
sprites.on_overlap(SpriteKind.Healing, SpriteKind.player, on_on_overlap)

def on_up_pressed():
    global menuIndex
    if gameState == menu:
        menuIndex += -1
        updateMenu()
        if menuIndex < 0:
            menuIndex = 2
            updateMenu()
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_b_pressed():
    if gameState == 0:
        showMenu()
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_a_pressed():
    if gameState == 0:
        if menuIndex == 0:
            startMyGame()
        elif menuIndex == 1:
            howToPlayMenu()
        elif menuIndex == 2:
            shopMenu()
        else:
            pass
    elif gameState == 1:
        
        def on_throttle():
            global ammoCount
            if ammoCount > 0:
                ammoCount += -1
                myWeapons()
                pause(50)
                updateAmmo()
                if ammoCount == 0:
                    
                    def on_after():
                        reloadAmmo()
                    timer.after(100, on_after)
                    
                else:
                    pass
            else:
                music.play(music.melody_playable(music.small_crash),
                    music.PlaybackMode.IN_BACKGROUND)
                pause(100)
        timer.throttle("action", 100, on_throttle)
        
    else:
        pass
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def updateMenu():
    if menuIndex == 0:
        btnStart.set_image(assets.image("""
            startGame2
            """))
        btnHowToPlay.set_image(assets.image("""
            howToPlay1
            """))
        btnShipShop.set_image(assets.image("""
            settings1
            """))
    elif menuIndex == 1:
        btnStart.set_image(assets.image("""
            startGame1
            """))
        btnHowToPlay.set_image(assets.image("""
            howToPlay2
            """))
        btnShipShop.set_image(assets.image("""
            settings1
            """))
    else:
        btnStart.set_image(assets.image("""
            startGame1
            """))
        btnHowToPlay.set_image(assets.image("""
            howToPlay1
            """))
        btnShipShop.set_image(assets.image("""
            settings2
            """))
def shopMenu():
    global btnBack
    sprites.destroy_all_sprites_of_kind(SpriteKind.button)
    sprites.destroy_all_sprites_of_kind(SpriteKind.title)
    scene.set_background_image(assets.image("""
        myShop
        """))
    btnBack = sprites.create(assets.image("""
            myBackButton
            """),
        SpriteKind.button)
    btnBack.set_position(30, 108)

def on_on_overlap2(sprite2, otherSprite2):
    global shipLevel, weaponLevel
    sprites.destroy(sprite2, effects.blizzard, 200)
    shipLevel += 1
    weaponLevel += 1
    music.play(music.melody_playable(music.power_up),
        music.PlaybackMode.IN_BACKGROUND)
    if shipLevel == 1:
        myShip.set_image(assets.image("""
            myShip1
            """))
        animation.run_image_animation(myShip,
            assets.animation("""
                myShipMove
                """),
            200,
            True)
    elif shipLevel == 2:
        myShip.set_image(assets.image("""
            myShip2
            """))
        animation.run_image_animation(myShip,
            assets.animation("""
                myShip1Move
                """),
            200,
            True)
    elif shipLevel == 3:
        myShip.set_image(assets.image("""
            myShip3
            """))
        animation.run_image_animation(myShip,
            assets.animation("""
                myShip2Move
                """),
            200,
            True)
    else:
        myShip.set_image(assets.image("""
            myShip4
            """))
        animation.run_image_animation(myShip,
            assets.animation("""
                myShip4Move
                """),
            200,
            True)
sprites.on_overlap(SpriteKind.food, SpriteKind.player, on_on_overlap2)

def startMyGame():
    global isGameStarted, gameState, myConsole, myHealth, healthBar, myShip, shipLevel, weaponLevel, enemySpeed, myCredits
    if not (isGameStarted):
        isGameStarted = True
        gameState = 1
        sprites.destroy_all_sprites_of_kind(SpriteKind.title)
        sprites.destroy_all_sprites_of_kind(SpriteKind.button)
        pause(200)
        effects.star_field.start_screen_effect()
        scene.set_background_image(assets.image("""
            mySpace
            """))
        scroller.scroll_background_with_speed(0, 10)
        myConsole = sprites.create(assets.image("""
            myConsole1
            """), SpriteKind.console)
        animation.run_image_animation(myConsole,
            assets.animation("""
                myConsole1Move
                """),
            200,
            True)
        myConsole.set_position(80, 114)
        myConsole.z = 20
        updateAmmo()
        myHealth = sprites.create(assets.image("""
            myHealth
            """), SpriteKind.StatusBar)
        myHealth.set_position(23, 114)
        myHealth.z = 21
        healthBar = 100
        myShip = sprites.create(assets.image("""
            myShip1
            """), SpriteKind.player)
        myShip.set_position(78, 102)
        myShip.z = 22
        myShip.set_stay_in_screen(True)
        controller.move_sprite(myShip)
        animation.run_image_animation(myShip,
            assets.animation("""
                myShipMove
                """),
            200,
            True)
        shipLevel = 1
        weaponLevel = 1
        enemySpeed = 30
        myCredits = 0
        info.set_score(0)
def reloadAmmo():
    global isReloading, reloading, myRedDot, ammoCount
    isReloading = True
    reloading = sprites.create(assets.image("""
        reloading
        """), SpriteKind.reload)
    reloading.set_position(124, 115)
    reloading.z = 21
    pause(1000)
    myRedDot = sprites.create(assets.image("""
        myRedDot
        """), SpriteKind.reload)
    myRedDot.set_position(144, 116)
    myRedDot.z = 21
    pause(1000)
    myRedDot = sprites.create(assets.image("""
        myRedDot
        """), SpriteKind.reload)
    myRedDot.set_position(148, 116)
    myRedDot.z = 21
    pause(1000)
    myRedDot = sprites.create(assets.image("""
        myRedDot
        """), SpriteKind.reload)
    myRedDot.set_position(152, 116)
    myRedDot.z = 21
    pause(1000)
    ammoCount = 10
    music.play(music.melody_playable(music.jump_up),
        music.PlaybackMode.IN_BACKGROUND)
    sprites.destroy_all_sprites_of_kind(SpriteKind.reload)
    updateAmmo()
    isReloading = False
def howToPlayMenu():
    global btnBack, howToPlayArrows
    sprites.destroy_all_sprites_of_kind(SpriteKind.button)
    sprites.destroy_all_sprites_of_kind(SpriteKind.title)
    scene.set_background_image(assets.image("""
        myHowToPlayScreen1
        """))
    btnBack = sprites.create(assets.image("""
            myBackButton
            """),
        SpriteKind.button)
    btnBack.set_position(30, 108)
    howToPlayArrows = sprites.create(assets.image("""
            howToPlayArrows
            """),
        SpriteKind.button)
    howToPlayArrows.set_position(80, 108)

def on_on_overlap3(sprite3, otherSprite3):
    global healingDrop
    sprites.destroy(sprite3)
    sprites.destroy(otherSprite3)
    music.play(music.melody_playable(music.knock),
        music.PlaybackMode.UNTIL_DONE)
    if randint(0, 100) < 40:
        healingDrop = sprites.create_projectile_from_sprite(assets.image("""
            myHealing
            """), otherSprite3, 0, 20)
        healingDrop.set_kind(SpriteKind.Healing)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.satellite, on_on_overlap3)

def on_on_overlap4(sprite4, otherSprite4):
    global healthBar
    scene.camera_shake(4, 500)
    sprites.destroy(sprite4, effects.fire, 200)
    healthBar += -25
    checkHealth()
    pause(100)
    music.play(music.melody_playable(music.big_crash),
        music.PlaybackMode.IN_BACKGROUND)
    if healthBar == 0:
        game.set_game_over_playable(False, music.melody_playable(music.power_down), False)
        game.game_over(False)
        game.set_game_over_scoring_type(game.ScoringType.HIGH_SCORE)
sprites.on_overlap(SpriteKind.enemy, SpriteKind.player, on_on_overlap4)

def on_down_pressed():
    global menuIndex
    if gameState == menu:
        menuIndex += 1
        updateMenu()
        if menuIndex > 2:
            menuIndex = 0
            updateMenu()
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

def myWeapons():
    global myPlasma
    if weaponLevel == 1:
        myPlasma = sprites.create_projectile_from_sprite(assets.image("""
            myPlasma1
            """), myShip, 0, -75)
        animation.run_image_animation(myPlasma,
            assets.animation("""
                myPlasmaMove
                """),
            300,
            True)
        music.play(music.melody_playable(music.pew_pew),
            music.PlaybackMode.IN_BACKGROUND)
    elif weaponLevel == 2:
        myPlasma = sprites.create_projectile_from_sprite(assets.image("""
            myPlasma2
            """), myShip, 0, -100)
        animation.run_image_animation(myPlasma,
            assets.animation("""
                myPlasma2Move
                """),
            300,
            True)
        music.play(music.melody_playable(music.pew_pew),
            music.PlaybackMode.IN_BACKGROUND)
    elif weaponLevel == 3:
        myPlasma = sprites.create_projectile_from_sprite(assets.image("""
            myPlasma3
            """), myShip, 0, -125)
        animation.run_image_animation(myPlasma,
            assets.animation("""
                myPlasma3Move
                """),
            200,
            True)
        music.play(music.melody_playable(music.pew_pew),
            music.PlaybackMode.IN_BACKGROUND)
    else:
        myPlasma = sprites.create_projectile_from_sprite(assets.image("""
            myPlasma4
            """), myShip, 0, -150)
        animation.run_image_animation(myPlasma,
            assets.animation("""
                myPlasma4Move
                """),
            200,
            True)
        music.play(music.melody_playable(music.pew_pew),
            music.PlaybackMode.IN_BACKGROUND)

def on_on_overlap5(sprite5, otherSprite5):
    global myCredits
    sprites.destroy(sprite5)
    music.play(music.melody_playable(music.ba_ding),
        music.PlaybackMode.IN_BACKGROUND)
    myCredits += 1
    myConsole.say_text(myCredits)
sprites.on_overlap(SpriteKind.credit, SpriteKind.player, on_on_overlap5)

def showMenu():
    global menuIndex, btnStart, btnHowToPlay, btnShipShop
    sprites.destroy_all_sprites_of_kind(SpriteKind.button)
    menuIndex = 0
    scene.set_background_image(assets.image("""
        titleScreen
        """))
    btnStart = sprites.create(assets.image("""
        startGame2
        """), SpriteKind.button)
    btnStart.set_position(30, 80)
    btnHowToPlay = sprites.create(assets.image("""
        howToPlay1
        """), SpriteKind.button)
    btnHowToPlay.set_position(30, 94)
    btnShipShop = sprites.create(assets.image("""
        settings1
        """), SpriteKind.button)
    btnShipShop.set_position(30, 108)
def updateAmmo():
    global ammoShell, ammoShellLow
    sprites.destroy_all_sprites_of_kind(SpriteKind.ammo)
    if ammoCount > 0:
        index = 0
        while index <= ammoCount - 1:
            ammoShell = sprites.create(assets.image("""
                myAmmo
                """), SpriteKind.ammo)
            ammoShell.z = 40
            ammoShellLow = sprites.create(assets.image("""
                myAmmoLow
                """), SpriteKind.ammo)
            ammoShellLow.z = 40
            sprites.destroy(ammoShellLow)
            if ammoCount < 4:
                ammoShell.set_image(assets.image("""
                    myAmmoLow
                    """))
            else:
                ammoShell.set_image(assets.image("""
                    myAmmo
                    """))
            ammoShell.set_position(index * 6 + 103, 114)
            index += 1
def checkHealth():
    if healthBar == 100:
        myHealth.set_image(assets.image("""
            myHealth
            """))
    elif healthBar == 75:
        myHealth.set_image(assets.image("""
            myHealth1
            """))
    elif healthBar == 50:
        myHealth.set_image(assets.image("""
            myHealth2
            """))
    elif healthBar == 25:
        myHealth.set_image(assets.image("""
            myHealth3
            """))
    elif healthBar == 0:
        myHealth.set_image(assets.image("""
            myHealth4
            """))
    else:
        myHealth.set_image(assets.image("""
            myHealth
            """))

def on_on_overlap6(sprite6, otherSprite6):
    global powerUpDrop, creditDrop
    sprites.destroy(sprite6)
    music.play(music.melody_playable(music.knock),
        music.PlaybackMode.IN_BACKGROUND)
    info.change_score_by(1)
    animation.run_image_animation(otherSprite6,
        assets.animation("""
            enemyExplosion
            """),
        200,
        False)
    otherSprite6.set_velocity(0, 0)
    pause(500)
    sprites.destroy(otherSprite6)
    otherSprite6.start_effect(effects.fire, 150)
    if randint(0, 100) < 15:
        powerUpDrop = sprites.create_projectile_from_sprite(assets.image("""
            myPowerup
            """), otherSprite6, 0, 20)
        powerUpDrop.set_kind(SpriteKind.food)
    if randint(0, 100) < 50:
        creditDrop = sprites.create_projectile_from_sprite(assets.image("""
            credit1
            """), otherSprite6, 0, 20)
        creditDrop.set_kind(SpriteKind.credit)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap6)

myAsteroid: Sprite = None
myEnemy2: Sprite = None
myEnemy1: Sprite = None
startTime = 0
creditDrop: Sprite = None
powerUpDrop: Sprite = None
ammoShellLow: Sprite = None
ammoShell: Sprite = None
myPlasma: Sprite = None
howToPlayArrows: Sprite = None
myRedDot: Sprite = None
reloading: Sprite = None
isReloading = False
myCredits = 0
enemySpeed = 0
myHealth: Sprite = None
myConsole: Sprite = None
myShip: Sprite = None
weaponLevel = 0
shipLevel = 0
btnBack: Sprite = None
btnShipShop: Sprite = None
btnHowToPlay: Sprite = None
btnStart: Sprite = None
menu = 0
healthBar = 0
healingDrop: Sprite = None
ammoCount = 0
isGameStarted = False
menuIndex = 0
gameState = 0
gameState = 0
menuIndex = 0
isGameStarted = False
ammoCount = 10
showMenu()

def on_on_update():
    if gameState == 1:
        if myShip:
            if myShip.y > 93:
                myShip.y = 93
game.on_update(on_on_update)

def on_on_update2():
    global startTime
    if gameState == 1:
        startTime += 1
game.on_update(on_on_update2)

def on_update_interval():
    global myEnemy1
    if gameState == 1:
        if startTime > 2:
            myEnemy1 = sprites.create_projectile_from_side(assets.image("""
                myEnemy1
                """), 0, enemySpeed)
            myEnemy1.x = randint(10, 150)
            myEnemy1.z = 5
            myEnemy1.set_kind(SpriteKind.enemy)
            animation.run_image_animation(myEnemy1,
                assets.animation("""
                    myEnemy1Move
                    """),
                200,
                True)
game.on_update_interval(randint(2000, 5000), on_update_interval)

def on_update_interval2():
    global myEnemy2
    if gameState == 1:
        if startTime > 1000:
            myEnemy2 = sprites.create_projectile_from_side(assets.image("""
                myEnemy2
                """), 0, enemySpeed)
            myEnemy2.x = randint(10, 150)
            myEnemy2.z = 5
            myEnemy2.set_kind(SpriteKind.enemy)
            animation.run_image_animation(myEnemy2,
                assets.animation("""
                    myEnemy2Move
                    """),
                200,
                True)
game.on_update_interval(randint(2000, 5000), on_update_interval2)

def on_forever():
    global enemySpeed
    if gameState == 1:
        if game.runtime() > 5000:
            enemySpeed += 5
            pause(5000)
forever(on_forever)

def on_update_interval3():
    global myAsteroid
    if gameState == 1:
        if startTime > 800:
            myAsteroid = sprites.create_projectile_from_side(assets.image("""
                myAsteroid
                """), 0, 100)
            myAsteroid.x = randint(0, 160)
            myAsteroid.z = 1
            myAsteroid.set_kind(SpriteKind.satellite)
            animation.run_image_animation(myAsteroid,
                assets.animation("""
                    myAsteroidMove
                    """),
                200,
                True)
game.on_update_interval(randint(10000, 20000), on_update_interval3)
