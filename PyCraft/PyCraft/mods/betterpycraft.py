from ursina import *


def initialize(game_api):
    class BlueWoolVoxel(Button):
        block_texture='PyCraft/Textures/blue_wool.png'
        block_icon = 'PyCraft/Textures/bluewoolblock.png'
        block_color = color.hsv(0, 0, .9)
        def __init__(self, position=(0,0,0)):
            base_color = color.hsv(0, 0, .9)
            super().__init__(parent=scene,
                position=position,
                model='cube',
                origin_y=.5,
                texture='PyCraft/Textures/blue_wool.png',
                color=base_color,
                isblock = True
            )
            r = min(base_color.r + 0.1, 1.0)
            g = min(base_color.g + 0.1, 1.0)
            b = min(base_color.b + 0.1, 1.0)
            self.highlight_color = color.rgb(r, g, b)
    game_api['block_class_mapping']['BlueWoolVoxel'] = BlueWoolVoxel

    game_api['inventory_blocks_pg2'].append({
        'voxel_class': BlueWoolVoxel, 
        'texture': BlueWoolVoxel.block_icon, 
        'color': color.hsv(0,0,0.9), 
        'name': 'Blue Wool'
    })

    print('BetterPyCraft Mod Initialized!')

def deinitialize(game_api):
    game_api['inventory_blocks_pg2'] = [
        block for block in game_api['inventory_blocks_pg2'] if block['name'] != 'Blue Wool'
    ]
    print('BetterPyCraft Mod Deinitialized')