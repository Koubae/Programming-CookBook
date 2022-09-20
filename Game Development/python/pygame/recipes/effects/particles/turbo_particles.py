def make_particle_trail(screen: pg.Surface, entity_pos: Vector2, enitty_size: Vector2) -> None:
    """Generates a trail of particle behind a entity Good for turbo effects

    :param screen: pg.Surface Screen where the particle is drawn
    :param entity_pos:  Vector2  x, y position coordinates
    :param enitty_size: Vector2  x, y entity size
    :return: None
    """
    particle_color: pg.Color = pg.Color("white")
    total_particle: int = 25
    particle_min_size: int = 1
    particle_max_size: int = 10
    # by increasing the number, we draw particle more far away from the entity
    # creating a trail behind it
    for particle_x_pos in range(total_particle):
        particle_y_side = (entity_pos.y + (enitty_size.y - random.randint(1, 10)))
        if move_left:
            particle_x_side = (entity_pos.x + (random.randint(1,
                                                              10) * particle_x_pos))  # depending on the player direction , draw particle on the opposite side
        else:
            particle_x_side = (entity_pos.x - (random.randint(1,
                                                              10) * particle_x_pos))  # depending on the player direction , draw particle on the opposite side
        pg.draw.circle(
            screen,
            particle_color,
            (particle_x_side, particle_y_side),
            random.randint(particle_min_size, particle_max_size)
        )

