class Settings:
  screen_width = 1200
  screen_height = 800
  bg_color = 'green'
  ship_speed = 1.5
  ship_limit = 3
  bullet_speed = 1.5
  bullet_width = 3
  bullet_height = 15
  bullet_color = 'dark gray'
  bullet_allowed = 3
  alien_speed = 3
  fleet_drop_speed = 5
  fleet_direction = 1
  
  
  def _init_(self):
    self.screen_width = 1200
    self.screen_height = 800
    self.bg_color = (230, 230, 230)
    self.ship_speed = 1.5
    self.ship_limit = 3
    self.bullet_speed = 1.5
    self.bullet_width = 3
    self.bullet_height = 15
    self.bullet_color = (60, 60, 60)
    self.bullet_allowed = 3

    self.alien_speed = 3
    self.fleet_drop_speed = 5
    self.fleet_direction = 1 