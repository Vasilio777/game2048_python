import turtle 

class GameMode():
    def __init__(self):
        self.screensize = (800, 800)
        self.paused = False
        self.t = turtle.Turtle()
        self.t.ht()
        self.t.screen.tracer(0)
        self.objects = set()

    def init_game(self, *objects):
        for obj in objects:
            self.objects.add(obj)

        self.t.screen.setup(self.screensize[0], self.screensize[1])
        self.t.screen.onscreenclick(self.toggle_pause, 1)

        self.render_tick()

        self.t.pen(speed=0, shown=False)
        self.t.screen.listen()
        self.t.screen.mainloop()

    def toggle_pause(self, x, y):
        self.paused = not self.paused
        
    def render_tick(self):
        if not self.paused:
            for obj in self.objects:
                obj.render_tick()

        self.t.screen.update()
        
        turtle.ontimer(self.render_tick, 100)
