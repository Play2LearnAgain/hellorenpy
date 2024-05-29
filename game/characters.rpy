screen eileen():
  imagebutton:
    xpos 0.25
    ypos 0.2
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
    action Function(renpy.call, "eileen_greeting")

screen bertram():
  imagebutton:
    xpos 0.75
    ypos 0.2
    idle Composite(
        (556, 1000),
        (0, 0), im.Flip("assets/m01/m01-body.png", horizontal=True),
        (0, 0), im.Flip("assets/m01/m01-eyes-smile.png", horizontal=True),
        (0, 0), im.Flip("assets/m01/m01-mouth-smile00.png", horizontal=True),
    )
    hover Composite(
        (556, 1000),
        (0, 0), im.Flip("assets/m01/m01-body.png", horizontal=True),
        (0, 0), im.Flip("assets/m01/m01-eyes-smile.png", horizontal=True),
        (0, 0), im.Flip("assets/m01/m01-mouth-smile00.png", horizontal=True),
    )
    action Function(renpy.call, "bertram_greeting")
