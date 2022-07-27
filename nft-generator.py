# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 12:57:07 2022

@author: kilros
"""

from PIL import Image
import random
import json
import os
####for creating field images
from bunnyModel import background_data
from bunnyModel import weapon_data
from bunnyModel import species_data
from bunnyModel import eyes_data
from bunnyModel import hat_data
from bunnyModel import neck_data
from bunnyModel import clothes_data

#total nft count : have to change for each type of token. 
TOTAL_NFT_COUNT = 3000

#####path for source traits.
asset_path = "assets"

bunny_path = "data"

os.mkdir(bunny_path)
os.mkdir(f"{bunny_path}/image")
os.mkdir(f"{bunny_path}/json")


def choose_by_rarity(data):
    return random.choices(data)

def generate_bunny_nfts():
    
    i = 0
    while i < TOTAL_NFT_COUNT:
        i += 1
        background = choose_by_rarity(background_data)[0]
        weapon = choose_by_rarity(weapon_data)[0]
        species = choose_by_rarity(species_data)[0]
        clothes = choose_by_rarity(clothes_data)[0]
        neck = choose_by_rarity(neck_data)[0]
        hat = choose_by_rarity(hat_data)[0]
        eyes = choose_by_rarity(eyes_data)[0]
            
        print(f"generating {i}th NFT...")
        image = generate_bunny_nft(background, weapon, species, clothes, neck, 
                                   hat, eyes)
        
        json_data = {
            "name": f"Cloudbunny #{i}",
            "description": "A collection of unique and glorious Cloudbunnies just vibin and chillin in their Flower Garden. Join the Cloudbunnies and hang out in the metaverse!",
            "external_url": "",
            "image": f"replace/{i}.jpg",
            "attributes": [
                {
                    "trait_type": "background",
                    "value": background
                }, {
                    "trait_type": "species",
                    "value": species
                }, {
                    "trait_type": "eyes",
                    "value": eyes
                }, {
                    "trait_type": "hat",
                    "value": hat
                }, {
                    "trait_type": "clothes",
                    "value": clothes
                }, {
                    "trait_type": "neck",
                    "value": neck
                }, {
                    "trait_type": "weapon",
                    "value": weapon
                }
            ],
        }
        
        json_str = json.dumps(json_data, indent=2)
        json_path = f"{bunny_path}/json/{i}.json"
        f = open(json_path, "w")
        f.write(json_str)
        f.close()
        
        image_path = f"{bunny_path}/image/{i}.jpg"
            
            
        # save image
        image = image.convert('RGB')
        image.save(image_path)
        
    print("finished generating all field NFTs.")
    
    
def generate_bunny_nft(background, weapon, species, clothes, neck, 
                  hat, eyes):

    
    background = Image.open(f"{asset_path}/background/{background}.png").convert("RGBA")
    weaponI = Image.open(f"{asset_path}/weapon/{weapon}.png").convert("RGBA")
    speciesI = Image.open(f"{asset_path}/species/{species}.png").convert("RGBA")
    clothesI = Image.open(f"{asset_path}/clothes/{clothes}.png").convert("RGBA")
    neckI = Image.open(f"{asset_path}/neck/{neck}.png").convert("RGBA")
    eyesI = Image.open(f"{asset_path}/eyes/{eyes}.png").convert("RGBA")
    hatI = Image.open(f"{asset_path}/hat/{hat}.png").convert("RGBA")
    
    if weapon != "Busketball" and weapon != "Soccer" :    
        background.paste(weaponI, (0, 0), weaponI)
    
    background.paste(speciesI, (0, 0), speciesI)
    background.paste(clothesI, (0, 0), clothesI)
    background.paste(neckI, (0, 0), neckI)
    background.paste(eyesI, (0, 0), eyesI)
    background.paste(hatI, (0, 0), hatI)

    
    if weapon == "Busketball" or weapon == "Soccer" :    
        background.paste(weaponI, (0, 0), weaponI)
        
    return background


if __name__ == '__main__':
    generate_bunny_nfts()
