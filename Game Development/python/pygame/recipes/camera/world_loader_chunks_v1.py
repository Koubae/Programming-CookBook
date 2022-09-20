def generate_world() -> list:
    """Generates a World adding its talese in multidimensional array by its tall"""

    tales = []
    for height_index, row in enumerate(map_level):
        tale_rows = []
        for width_index, col in enumerate(row):
            block_type = blocks[col]
            # get the block
            block = block_type['img']
            rect = pg.Rect(width_index * TILE_SIZE, height_index * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            # add it to the screen
            background.blit(block, rect.topleft)
            block_id = f"{height_index}-{width_index}"
            tale_struct = {
                'terrain': col,
                'terrain_label': TERRAIN_LABELS[col],
                'block_id': block_id,
                'height_index': height_index,
                'width_index': width_index,
                'img': block,
                'rect': rect,
                'collision': False
            }
            # has Collision?
            if block_type['collision']:
                tale_struct['collision'] = True
            tale_rows.append(tale_struct)
        tales.append(tale_rows)

    return tales


def render_world(world: list):
    """Render the world in chunks"""
    tales_with_collisions = []

    cell_count = 0

    # ------------
    #  Chunk Loader
    # ------------
    # | In order to laod a chunk of the world map we need to follow this algorithm
    # | 1) Get Player position
    # | 2) Calculate the block index by deviding x-y coordinates by the Tile px sixe. Also a margin is added
    # | 3) Get the current off x -y block index
    # | 4) Get the max block index on the view chunk by adding the MAP_TALL|MAP_LENGTH + some margin
    # | 5) Iterate through row line (by its tall)
    # | 6) Iterate through col line (by its lenght)
    # | 7) Move The camera accordingly

    view_margin: int = 10  # arbitrary additional 'padding' to add in the camera view. so that the actual block rendered is bigger than the camera
    player_pos = Vector2(player.rect.topleft)  # | 1) Get Player position
    block_position_index = Vector2((player_pos.x / TILE_SIZE) - view_margin,
                                   (player_pos.y / TILE_SIZE) - view_margin)  # | 2) Calculate the block index

    block_length_index = int(block_position_index.x)  # | 3) Get the current off x -y block index
    block_height_index = int(block_position_index.y)
    block_length_index = 0 if block_length_index < 0 else block_length_index
    block_height_index = 0 if block_height_index < 0 else block_height_index
    # | 4) Get the max block index on the view chunk by adding the MAP_TALL|MAP_LENGTH + some margin
    block_length_index_max = int(block_position_index.x + MAP_LENGTH + view_margin)
    block_height_index_max = int(block_position_index.y + MAP_TALL + view_margin)

    for height_index, row in enumerate(
            world[block_height_index:block_height_index_max]):  # | 5) Iterate through row line (by its tall)
        for width_index, block_data in enumerate(
                row[block_length_index:block_length_index_max]):  # | 6) Iterate through col line (by its lenght)

            cell_count += 1
            block_img: pg.Surface = block_data['img']
            block_rect: pg.Rect = block_data['rect']  # | 7) Move The camera accordingly
            block_pos_updated = Vector2(block_rect.x - camera.x(), block_rect.y - camera.y())
            # add it to the screen
            background.blit(block_img, block_pos_updated)
            if block_data['collision']:

                # Check if block is close enugh to entity to check the collision
                # by loading collisions only if are close enough to the entity
                player_position = player.pos
                diff_x = abs(block_pos_updated.x - player_position.x)
                diff_y = abs(block_pos_updated.y - player_position.y)
                if diff_x < TILE_MAX_COLLISION and diff_y < TILE_MAX_COLLISION:
                    tales_with_collisions.append(block_rect)

    return tales_with_collisions