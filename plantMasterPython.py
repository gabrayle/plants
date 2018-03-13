import random
#Used to call random plants 1-20 from biomes already decided by user

#Welcome message/ ask for input
print ("Welcome to your random plant finder.") 
print()
more_plants = 'y'
while more_plants.lower() == 'y':
    #ask user to input biome type
    print ("Please enter a Biome")
    print ("or Generic type; Tree, Plant, Edible, Magic, etc")
    try:
        biome_type = (input("Please enter a Biome: \t\t"))
#if cavern
#actually, this gets executed even if anything "not accepted" is typed
        if biome_type.lower() == "cavern" or biome_type.lower() == "cave":
#you need at  least 20 plants here
            cave_plant = ["Zulsendra", "Zur", "nothing", "an iron ore vein", "nothing", "a rich copper ore vein", "something shiny in the wall"]
            print('You have found  '+str(random.choice(cave_plant)))
            print()
#coastal
        if biome_type.lower() == "coastal" or biome_type.lower() == "coast" or biome_type.lower() == "caostal" or biome_type.lower() == "caost" or biome_type.lower() == "ocean":
            coast_plant = ['Felmather', 'Fumitore', 'Gylvir', 'Horehound', 'Pokeweed', 'Cranberry', 'Rice', 'Oleander',
                           'Serviceberry', 'Bleeding Heart', 'Squill', 'Samphire', 'Mangrove', 'something shiny in the sand']
            print('You have found  '+str(random.choice(coast_plant)))
            print()
#if desert
#either needs more plants or duplicate responce choice possible            
        elif biome_type.lower() == "desert" or biome_type.lower() == "dessert":
            desert_plant = ['Caffar', 'Aloe', 'Culkas', 'Dragon Tears', 'Makebite','Myrrh', 'Entriste', 'Gariig', 'Jaffray', 'Nightcall',
                            'Cactus Fruit', 'Hoodia', 'nothing', 'something shiny in the sand']
            print('You have found  '+str(random.choice(desert_plant)))
            print()
        elif biome_type.lower() == "farm" or biome_type.lower() == "rural" or biome_type.lower() == 'farmland' or biome_type.lower() == 'farmlands':
#farm has enough plants
            farm_plant = ["Onion", "Mint", "Basil", "Dandelion", "Corn", "Masterwort", "Henbane", "Tobacco", "Barley", "some greens", "Philodendron",
                          "Zucchini", "Carrot", "Apple", "Lilac", "Wood Sorrel", "Pea", "Clover", "Mugwort", "Milkeworte", "Healwell", "Base Mullein", "something shiny in the dirt"]
            print('You have found  '+str(random.choice(farm_plant)))
            print()
#forest needs at least 20 plants
        elif biome_type.lower() == "forest" or biome_type.lower() == 'forrest' or biome_type.lower() == "woods" or biome_type.lower() == "woodland":
            forest_plant = ['Fetherfew', 'nothing but trees', "Goat's Rue", 'Golden Lungwort', 'Hawkweed', 'Mint', 'Kelventari', 'Mandrake', 'Orach',
                            'Pattran', 'some legumes', 'Skullcap', 'Yellowwood', "something shiny among the roots", 'Black Rose']
            print('You have found  '+str(random.choice(forest_plant)))
            print()
#Banks need 16 plants
        elif biome_type.lower() == "freshwater" or biome_type.lower() == "river" or biome_type.lower() == "rivers" or biome_type.lower() == 'bank' or biome_type.lower() == 'banks':
            banks_plant = ['Melander', 'Watercress', 'Birch', 'Navew', 'Comfrey', 'Catalpa', 'quality clay', 'something shiny in the water', 'Squill',
                           'Brooklime', 'Samphire']
            print('You have found  '+str(random.choice(banks_plant)))
            print()
#grasslands needs 20 plants
        elif biome_type.lower() == "grassland" or biome_type.lower() == "grass" or biome_type.lower() == "plains" or biome_type.lower() == "savannah" or biome_type.lower() == "field" or biome_type.lower() == "fields" or biome_type.lower() == 'grasslands' or biome_type.lower() == 'prairie': 
            grass_plant = ['Sunflower', 'Fleur-de-Luce', 'Harfy', 'Dandelion', 'Mint', 'Kilmakur', 'Klagul', "Leopard's Bane", 'Marjoram', 'Lavender',
                           'Squirrelcorn', 'Gum or Eucalyptus', 'something shiny in the grass']
            print('You have found  '+str(random.choice(grass_plant)))
            print()
#marshes need 20 plants        
        elif biome_type.lower() == "marsh" or biome_type.lower() == "marshes" or biome_type.lower() == "swamp" or biome_type.lower() == "swampland" or biome_type.lower() == "wetlands":
            marsh_plant = ['Falsifal', 'Winterberry', 'Comfrey', 'Black Tupelo', 'Archangelica', 'Jewelweed', 'something shiny in the muck']
            print('You have found  '+str(random.choice(marsh_plant)))
            print()
#mountains probably done
        elif biome_type.lower() == "mountain" or biome_type.lower() == "mountains" or biome_type.lower() == "montains" or biome_type.lower() == "montain" or biome_type.lower() == 'mountainous' or biome_type.lower() == 'taiga':
            mountain_plant = ["Hare's Ears", 'Jojojopo', 'Megillos', 'Mirenna', 'Mountain Garlick', 'Mountain Setwall', 'Palma Edath', 'a Fruit Tree',
                              'a Conifer(ous Tree)', 'Ferns', 'Silverberry', 'Lobaria', 'an edible Fungus', 'Xanthoria', 'something shiny in the dirt'] 
            print('You have found  '+str(random.choice(mountain_plant)))
            print()
#chaparral needs 20 plants
        elif biome_type.lower() == "scrub" or biome_type.lower() == "dry" or biome_type.lower() == "arid" or biome_type.lower() == "brushland" or biome_type.lower() == "chaparral" or biome_type.lower() == "brush":
            chaparral_plant = ['Olive', 'Grape', 'Aloe', 'something shiny in the dirt']
            print('You have found  '+str(random.choice(chaparral_plant)))
            print()
        elif biome_type.lower() == "tropics" or biome_type.lower() == "tropical" or biome_type.lower() == "rainforest":
#tropics neeeds about 6 plants
            tropical_plant = ['Cacao', 'Coconut', 'Bamboo', 'Land Caltrops', 'Pargen', 'a Nut tree', 'Coffee', 'Curry', 'Vanilla', 'Orchids,' 'Catechu',
                              'Rubber', 'Gum or Eucalyptus', 'Cassava', 'something shiny at your feet']
            print('You have found  '+str(random.choice(tropical_plant)))
            print()
        elif biome_type.lower() == "tundra" or biome_type.lower() == "arctic" or biome_type.lower() == "ice" or biome_type.lower() == "frozen" or biome_type.lower() == "cold":
#tundra needs more plants
            tundra_plant = ['Suaeysit', 'Elvish Galingale', 'Xanthoria', 'Palma Eldath', 'nothing', 'something shiny in the snow']
            print('You have found   '+str(random.choice(tundra_plant)))
            print()
        elif biome_type.lower() == "wastes" or biome_type.lower() == "wasteland" or biome_type.lower() == "badlands":
#wastelands need something
            wastes_plant = ['nothing', 'Gefnul, as long as a volcano is nearby.', 'Xanthoria', 'Kathkusa', 'nothing', 'nothing', 'nothing', 'nothing',
                            'nothing', 'nothing', 'nothing', 'nothing', 'something shiny']  
            print('You have found  '+str(random.choice(wastes_plant)))
            print()                
        elif biome_type.lower() == "etc":
            vermin_plant = ['a snake', 'a bug', 'a mouse']
            print ('You have found a plant, algae, fungus or lichen and been bitten by '+str(random.choice(vermin_plant)))
            print ('for being a smartass. Take 2 damage')
            print()
#YOU STILL NEED
        
        elif biome_type.lower() == 'nuts' or biome_type.lower() == 'nut':
#you're a nut
            nut_plant = ['Pecan', 'Walnut', 'Chestnut', 'Hazelnut', 'Belan', 'Cashew', 'Nutmeg', 'Pistachio', 'Hickory', 'Almond', 'Avocado']
            print('You have found  '+str(random.choice(nut_plant)))
            print()
        elif biome_type.lower() == 'conifer' or biome_type.lower() == 'coniferous':
            conifer_plant = ['Pine', 'Cedar', 'Hemlock', 'Cypress', 'Juniper', 'Fir', 'Spruce', 'Yew']
            print('You have found  '+str(random.choice(conifer_plant)))
            print()    
            
        #elif fruit
        #elif legume
        #elif berry
        elif biome_type.lower() == 'berry' or biome_type.lower() == 'berries':
            berry_plant = ['Strawberry', 'Blueberry', 'Pokeberry', 'black Raspberry', 'Raspberry', 'white Strawberry', 'Teaberry', 'cranberry', 'Tomato',
                           'Huckleberry', 'Mulberry', 'Dogwood', 'Bead Tree', 'Sumac. Roll intelligence']
            print('You have found  ' +str(random.choice(berry_plant)))
            print()
#edible has 30 plants
        elif biome_type.lower() == 'edible' or biome_type.lower() == 'edibles':
            edible_plant = ['Gariig', 'Gylvir', 'Hawkweed', 'Belan', 'some greens.', 'some grain.', 'Taraxacum', 'Mint', 'Marshmallow', 'Pargen', 'some edible roots.',
                            'a tuber.', 'Mirenna', 'fruit', 'birch', 'a nut.', 'a legume.', 'a farm Crop.', 'an edible Fungus.', 'Pine nut', 'Parsley', 'Cilantro',
                            'some greens', 'a gourd or pepper.', 'Golden Rain', 'Cactus Fruit', 'Rose hips', 'Winterberry', 'a Legume or Herb']
            print('You have found  ' +str(random.choice(edible_plant)))
            print()
        #elif fungus
        elif biome_type.lower() == 'fungus':
            edible_fungus = ['Esculenta', 'Ur', 'Bryoria', 'Suaeysit', 'Agaricus', 'Zur', 'Zulsendra', 'Lichen', 'Mold', 'Mildew']
            print('You have found   ' +str(random.choice(edible_fungus)))
            print()
#plant has 100 plants
    #first lines have 8, then lines have 10
        elif biome_type.lower() == 'plant':
            generic_plant = ["Snakespite", 'Spiderwort', 'Saffron', 'Land Caltrops', 'a nearby farm.', "Saracen's Confound", 'Kelventari', 'Orach',
                             'Dittany', 'Yaran', 'Willowherb', 'Hawkweed', 'Throw-waxe', 'All-heale', "Bishop's weed", 'Terbas',
                             'Bloodkeep', 'Darnell', 'a common Rose', 'Colewort', 'an edible plant.', 'fleur-de-Luce', 'Thurl', 'Rose Campion',
                             'Palma Eldath', 'Draaf', 'Falsifal', 'Jewelweed', 'Fumitore', 'Anserke', "Hare's Ears", 'Rampalt',
                             'Anise or Fennel', 'Cow Parsnip', 'Amrans', 'Mugwort', 'Hypericum', 'Cow-wheat', 'deadly Nightshade', 'Comfrey',
                             'Serapias Turbith', 'Golden Lungwort', 'Makebite', 'Mint', 'Ebur', 'Eldaas', 'Woodrose', 'Henbane', 'Vinuk', 'Skullcap',
                             'Gylvir', 'Sweet Trefoile',  'Callin', 'Birthnot', 'Yavethalion', 'Marshmallow', 'Bastit', 'a fungus.', 'Belan', 'Marjoram',
                             'Base Mullein', 'Belramba', 'Whitecandle', 'Winclamit', 'Horehound', 'Archangelica', 'Mistletoe', 'Taraxacum', 'a flower.',
                             'Entriste', 'Tempin', 'Yarrow', 'Kilmakur', 'Hemp', 'Harfy', 'Mandrake', 'Spanish Nut', 'Wood Sorrel', 'Bull-rush',  'Masterwort',
                             'Tamariske', 'Mountain Setwall', 'Rewk', 'Chicory', "Goat's Rue'", 'Dagmather', 'Healwell', 'Felmather', "Leopard's Bane",
                             "Cat's Tail", 'Mountain Garlic', 'Black Rose', 'Jojojopo', 'Bursthelas', 'Degiik', 'Milkeworte', 'a common plant.', 'Fetherfew',
                             'Klagul', 'Pattran', 'a legume.']
            print('You have found  '+str(random.choice(generic_plant)))
            print()
        #elif tree needs nothing
        elif biome_type.lower() == 'tree' or biome_type.lower() == 'trees':
            tree_plant = ['Kratom', 'Salix', 'Bamboo', 'Hamamelis', 'Apple', 'Maple', 'Dogwood', 'Juniper', 'Walnut', 'Pecan', 'Delrean', 'Hemlock',
                          'Hawthorne', 'Fig', 'Ginko', 'Cedar', 'Birch', 'an edible citrus', 'an edible nut', 'Laurus', 'Camphor', 'Bay', 'an edible fruit',
                          'a conifer', 'Elderberry', 'Ash', 'Beech', 'Tea', 'Oak', 'Buckeye', 'Oleander', 'Black Tupelo', 'Serviceberry', 'Sassafras',
                          'Yew', 'Pine', 'Teak', 'Mahogany', 'Curry', 'Palm', 'Coconut', 'Cacao', 'Papaya', 'some Lichen', 'only some dead trees',
                          'Sumac', 'Monkeyball', 'Sacred Bark', 'Basswood', 'Crampbark', 'Cinnamon', 'Cassia', 'Cinchona', 'Fir', 'Catechu', 'Gum', 'Rubber',
                          'Tamarind', 'Sycamore', 'Spindle', 'Lilac', 'some ivy (roll for poison)', 'Olive', 'Mulberry', 'Zelkova', 'Bead Tree', 'Foxglove',
                          'Joshua Tree', 'Dove Tree', 'Fringe Tree', 'Magnolia', 'Catalpa', 'Golden Rain', 'Sequoia', 'Gordonia',
                          'Wax Tree', 'Bottle Tree', 'Guava', 'Pepper', 'Cypress']
            print('You have found   ' +str(random.choice(tree_plant)))
            print()
        elif biome_type.lower() == 'fruit tree':
            fruit_tree = ['Apple', 'Citrus', 'Peach', 'Plum', 'Nectarine', 'Pomegranate', 'Holly', 'Cherry', 'Banana', 'Coconut',
                          'Cacao', 'Orange', 'Tamarind', 'Papaya', 'Dragonfruit', 'Olive', 'Pear', 'Lychee', 'a Grape vine.', 'Fig']
            print('You have found   ' +str(random.choice(fruit_tree)))
            print()
        elif biome_type.lower() == 'citrus':
            citrus_plant = ['Mango', 'Orange', 'Lemon', 'Lime', 'Tamarind', 'Peach', 'Nectarine', 'Apricot', 'Grapefruit']
            print('You have found   ' +str(random.choice(citrus_plant)))
            print()
        #elif crop
        #elif grain or greens
        elif biome_type.lower() == 'grains' or biome_type.lower() == 'greens' or biome_type.lower() == 'green' or biome_type.lower() == 'grain':
            grains_plant = ['Chicory', 'Greens', 'Corn', 'Sunflower', 'Millet', 'Wheat', 'Oats', 'Barley', 'Lettuce', 'Turnip', 'Collard', 'Rhubarb',
                            'Nettle. Roll an intelligence check.', 'Spinach', 'Kale', 'Chia', 'Rice', 'Quinoa', 'Safflower']
            print('You have found  ' +str(random.choice(grains_plant)))
            print()
        #still needs more tubers
        elif biome_type.lower() == 'roots' or biome_type.lower() == 'tubers' or biome_type.lower() == 'root' or biome_type.lower() == 'tuber' or biome_type.lower() == 'bulb':    
            roots_plant = ['Radish', 'Carrot', 'Ginger', 'Beets', 'Potato', 'Yam', 'Onion', 'Scallion', 'Chives', 'Turnips', 'Parsnip',
                           'Garlic', 'Fennel', 'Jicama', 'Cassava']
            print('You have found  ' +str(random.choice(roots_plant)))
            print()
        elif biome_type.lower() == 'common':
            common_plant = ['Dandelion', 'common Rose', 'Grass', 'some Trees', 'a pretty flower.'] 
            print('You have found   ' +str(random.choice(common_plant)))
            print()                
        elif biome_type.lower() == 'legume':
            legume_plant = ['Hogpeanut', 'Alfalfa', 'Pea', 'Soy', 'Peanut', 'green Beans', 'pinto Beans', 'black Beans', 'Vanilla']
            print('You have found  ' +str(random.choice(legume_plant)))
            print()
        elif biome_type.lower() == 'herb':
            herb_plant = ['Thyme', 'Sage', 'Rosemary', 'Clover', 'Basil', 'Marjoram', 'Oregano', 'Yellowwood', 'Coriander', 'Cilantro']
            print('You have found   ' +str(random.choice(herb_plant)))
        elif biome_type.lower() == 'flower' or biome_type.lower() == 'flowers':
            flower_plant = ['Rose', 'Carnation', "Baby's Breath", 'Phlox', 'Chives or Allium', 'Lavender', 'some pretty blossoms', 'some sweet blossoms',
                            'Poppy', 'Passionflower', 'Hops', 'Kava Kava', 'Hemp', 'Tulip', 'Squirrelcorn', 'Bleeding Heart', 'Orchid (and vanilla)', 'Magnolia',
                            'Dove Tree', 'Golden Rain', 'Safflower', 'Sunflower', 'Artichoke']
            print('You have found  ' +str(random.choice(flower_plant)))
        elif biome_type.lower() == 'magic' or biome_type.lower() == 'magical':
#only for special use
            magic_plant = ['Caffar', 'Tenlas', 'Gefnul', 'Gariig', 'Adalka', 'Ginko'] 
            print('You have found  ' +str(random.choice(magic_plant)))
            print()
        else:
            print("Please enter a valid biome type")
            print()
    except(Exception):
        print(e)
                

    more_plants = input('More plants? (y/n):\t\t')    

#make able to be continued instead of run only once
#assign ALL values to unique plant name
#print plant name and "roll d6 to find quantity" and/or "DC roll 15 to properly prepare" 


