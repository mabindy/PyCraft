from ursina import *


def initialize(game_api):
    WhiteWoolVoxel = game_api['block_class_mapping']['WhiteWoolVoxel']
    inventory_blocks_pg3 = [
    {'voxel_class': WhiteWoolVoxel, 'texture': WhiteWoolVoxel.block_icon, 'color': color.hsv(0,0,0.9), 'name': 'White Wool'},
    {'voxel_class': WhiteWoolVoxel, 'texture': WhiteWoolVoxel.block_icon, 'color': color.hsv(0,0,0.9), 'name': 'White Wool'},
    {'voxel_class': WhiteWoolVoxel, 'texture': WhiteWoolVoxel.block_icon, 'color': color.hsv(0,0,0.9), 'name': 'White Wool'},
    {'voxel_class': WhiteWoolVoxel, 'texture': WhiteWoolVoxel.block_icon, 'color': color.hsv(0,0,0.9), 'name': 'White Wool'},
    {'voxel_class': WhiteWoolVoxel, 'texture': WhiteWoolVoxel.block_icon, 'color': color.hsv(0,0,0.9), 'name': 'White Wool'},
    {'voxel_class': WhiteWoolVoxel, 'texture': WhiteWoolVoxel.block_icon, 'color': color.hsv(0,0,0.9), 'name': 'White Wool'},
    {'voxel_class': WhiteWoolVoxel, 'texture': WhiteWoolVoxel.block_icon, 'color': color.hsv(0,0,0.9), 'name': 'White Wool'},
    {'voxel_class': WhiteWoolVoxel, 'texture': WhiteWoolVoxel.block_icon, 'color': color.hsv(0,0,0.9), 'name': 'White Wool'},
    {'voxel_class': WhiteWoolVoxel, 'texture': WhiteWoolVoxel.block_icon, 'color': color.hsv(0,0,0.9), 'name': 'White Wool'},
    ]
    game_api['pages'][3] = inventory_blocks_pg3
    game_api['pagelabels']['3'] = 'Mod Blocks'

    print('3rd Page Mod Initialized!')

def deinitialize(game_api):

    print('BetterPyCraft Mod Deinitialized')