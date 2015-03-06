import sfml as sf

wx = 640
wy = 480


window = sf.RenderWindow(sf.VideoMode(wx, wy), "Mah' Window")

try:
   # load a sprite to display
   # texture = sf.Texture.from_file("cute_image.png")
   # sprite = sf.Sprite(texture)

   # create some graphical text to display
   # font = sf.Font.from_file("arial.ttf")
   # text = sf.Text("Hello SFML", font, 50)

   # load music to play
   # music = sf.Music.from_file("nice_music.ogg")
   game = Game()

except IOError: exit(1)

# play the music
# music.play()
# start the game loop

while window.is_open:
   # process events
   for event in window.events:
      # close window: exit
      if type(event) is sf.CloseEvent:
         window.close()
      else:
        game.handleEvent(event)
        
      
   window.clear() # clear screen
   game.draw (window)
   # window.draw(sprite) # draw the sprite
   # window.draw(text) # draw the string
   window.display() # update the window

