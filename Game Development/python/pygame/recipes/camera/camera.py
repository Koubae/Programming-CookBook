from pygame.math import Vector2
from player import Player
from typing import Optional, Union


class Camera2D:
    """Camera for 2D games that fixes to a entity"""
    CAMERA_SMOOTHER: int = 20  # smooths the camera movements
    CAMERA_PADDING_Y: int = 200

    def __init__(self, entity: Player, win_width_half: float, win_height_half: float):
        self.entity: Player = entity
        self.lens: Vector2 = Vector2(0, 0)
        self.camera_center_x = win_width_half / 2
        self.camera_center_y = (win_height_half / 2) + self.CAMERA_PADDING_Y  # add some padding

        # add player size to camera
        self.camera_center_x += (self.entity.size.x / 2)
        self.camera_center_y += (self.entity.size.y / 2)

        self.camera_offset_x: Optional[float] = None
        self.camera_offset_y: Optional[float] = None

    def x(self, in_float: bool = False) -> Union[int, float]:
        """Get the current len X position

        :param in_float: bool if True returns the original FLoat value else int
        :return: int|float X Value of the camera curren len position
        """
        if in_float:
            return self.lens.x
        return int(self.lens.x)

    def y(self, in_float: bool = False) -> Union[int, float]:
        """Get the current len Y position

        :param in_float: bool if True returns the original FLoat value else int
        :return: int|float Y Value of the camera curren len position
        """
        if in_float:
            return self.lens.y
        return int(self.lens.y)

    def calcualte_len_position(self, move_left: bool = False) -> None:
        """Calculates the new len position of the camera relative to its fix Entity

        :param move_left: bool If True, entity is moving to the left and some additional X value is added
        :return: None
        """

        # Set camera
        camera_center_x_add = 0
        if move_left:
            camera_center_x_add = 300  # This makes sure that when turning to the left, the player is still visible
        camera_center_x_add += self.camera_center_x

        self.camera_offset_x = (self.entity.rect.x - self.lens.x - camera_center_x_add) / self.CAMERA_SMOOTHER
        self.camera_offset_y = (self.entity.rect.y - self.lens.y - self.camera_center_y) / self.CAMERA_SMOOTHER
        self.lens.x += self.camera_offset_x
        self.lens.y += self.camera_offset_y