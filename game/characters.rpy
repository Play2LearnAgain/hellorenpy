screen HelloScreen():
  text "Hello Screen"


screen EileenScreen():
  imagebutton:
    xpos 0.1
    ypos 0.1
    idle Composite(
      (556, 1000),
      (0, 0), "assets/fm01/fm01-body.png",
      (0, 0), "assets/fm01/fm01-eyes-smile.png",
      (0, 0), "assets/fm01/fm01-mouth-smile00.png",
    )
    hover Composite(
      (556, 1000),
      (0, 0), "assets/fm01/fm01-body.png",
      (0, 0), "assets/fm01/fm01-eyes-wow.png",
      (0, 0), "assets/fm01/fm01-mouth-wow.png",
    )

screen BertramScreen():
  imagebutton:
    xpos 0.6
    ypos 0.1
    idle Composite(
        (556, 1000),
        (0, 0), im.Flip("assets/m01/m01-body.png", horizontal=True),
        (0, 0), im.Flip("assets/m01/m01-eyes-smile.png", horizontal=True),
        (0, 0), im.Flip("assets/m01/m01-mouth-smile00.png", horizontal=True),
    )
    hover Composite(
        (556, 1000),
        (0, 0), im.Flip("assets/m01/m01-body.png", horizontal=True),
        (0, 0), im.Flip("assets/m01/m01-eyes-wow.png", horizontal=True),
        (0, 0), im.Flip("assets/m01/m01-mouth-wow.png", horizontal=True),
    )
    action Call("bertram_greeting")
