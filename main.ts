music._playDefaultBackground(music.builtInPlayableMelody(Melodies.Entertainer), music.PlaybackMode.LoopingInBackground)
basic.forever(function () {
    images.iconImage(IconNames.Target).scrollImage(1, 300)
    images.iconImage(IconNames.SmallDiamond).showImage(0)
})
