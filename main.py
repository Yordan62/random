tiles.set_current_tilemap(tilemap("level1"))
guy = sprites.create(assets.image("Guy1"), SpriteKind.player)
guy.set_scale(2, ScaleAnchor.MIDDLE)

controller.move_sprite(guy)

scene.camera_follow_sprite(guy)