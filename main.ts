namespace SpriteKind {
    export const StatusBar = SpriteKind.create()
    export const satellite = SpriteKind.create()
    export const Healing = SpriteKind.create()
    export const button = SpriteKind.create()
    export const ammo = SpriteKind.create()
    export const reload = SpriteKind.create()
    export const console = SpriteKind.create()
    export const title = SpriteKind.create()
    export const credit = SpriteKind.create()
    export const shipFlames = SpriteKind.create()
}
info.onScore(100, function () {
	
})
scene.setBackgroundImage(assets.image`mySpace`)
scroller.scrollBackgroundWithSpeed(0, -50)
