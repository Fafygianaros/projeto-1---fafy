music._play_default_background(music.built_in_playable_melody(Melodies.ENTERTAINER),
    music.PlaybackMode.LOOPING_IN_BACKGROUND)

def on_forever():
    images.icon_image(IconNames.TARGET).scroll_image(1, 300)
    images.icon_image(IconNames.SMALL_DIAMOND).show_image(0)
basic.forever(on_forever)
