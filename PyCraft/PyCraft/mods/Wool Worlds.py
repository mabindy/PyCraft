from ursina import *


def initialize(game_api):
    WhiteWoolVoxel = game_api['block_class_mapping']['WhiteWoolVoxel']
    RedWoolVoxel = game_api['block_class_mapping']['RedWoolVoxel']
    BlackWoolVoxel = game_api['block_class_mapping']['BlackWoolVoxel']
    game_api['worldgenerationvoxels']['surfacevoxel'] = WhiteWoolVoxel
    game_api['worldgenerationvoxels']['undersurfacevoxel'] = RedWoolVoxel
    game_api['worldgenerationvoxels']['deepvoxel'] = BlackWoolVoxel




    print('Wool Worlds Mod Initialized!')

def deinitialize(game_api):

    print('BetterPyCraft Mod Deinitialized')