import random
#Used to call random plants 1-20 from biomes already decided by user

#Welcome message/ ask for input
print ("Welcome to your random plant finder.") 
print()
more_plants = 'y'
while more_plants.lower() == 'y':
    #ask user to input biome type
    print ("Please enter a Biome and season Number")
    print ('Example: "desert2" for Desert biome in the Summer season')
    try:
        biome_type = (input("Please enter HERE: \t\t"))
#if arctic
#check for glint to store value if glint is found, then print "and you had found glint in the ___" at end of statement.
#associative array for desert - sand, ocean - water, etc        
        if biome_type.lower() == 'arctic1' or biome_type.lower() == 'tundra1' or biome_type.lower() == 'polar' or biome_type.lower() == 'boreal1':
            arc_plant1 = ['nothing', 'Elvish Galingale', 'Xanthoria', 'Pasque flower', 'Bryoria', 'Saxifrage', 'an Evergreen',
                          'Guardseye', 'Thyme']
            arc_weigh1 = [0.3, 0.3, 0.4, 0.3, 0.4, 0.3, 0.25,
                          0.05, 0.15]
            print('You have found   ' +str(random.choices(arc_plant1, arc_weigh1 ,k=3)))
            print()
        elif biome_type.lower() == 'arctic2' or biome_type.lower() == 'tundra2' or biome_type.lower() == 'polar2' or biome_type.lower() == 'boreal2':
            arc_plant2 = ['nothing', 'Elvish Galingale', 'Xanthoria', 'Pasque flower', 'Bryoria', 'Bearberry', 'Arctic Poppy', 'an Evergreen',
                          'Dragonwort', 'Gefnul near a hot spring', 'Guardseye', 'Laishaberry', 'Lesser Centaury', 'Bouncing Bet']
            arc_weigh2 = [0.3, 0.35, 0.45, 0.4, 0.6, 0.3, 0.1, 0.3,
                          0.25, 0.1, 0.05, 0.1, 0.15, 0.3]
            print('You have found   ' +str(random.choices(arc_plant2, arc_weigh2,k=3)))
            print()
        elif biome_type.lower() == 'arctic3' or biome_type.lower() == 'tundra3' or biome_type.lower() == 'polar3' or biome_type.lower() == 'boreal3':
            arc_plant3 = ['nothing', 'Bryoria', 'Bearberry', 'an Evergreen', 'Arfandas', 'Arlan', 'Arnuminas', 'Arpusar',
                          'Guardseye', 'Jojojopo', 'Laishaberry', 'Bouncing Bet']
            arc_weigh3 = [0.3, 0.4, 0.2, 0.25, 0.2, 0.6, 0.25, 0.2,
                          0.05, 0.4, 0.1, 0.25]
            print('You have found   ' +str(random.choices(arc_plant3, arc_weigh3,k=3)))
            print()
        elif biome_type.lower() == 'arctic4' or biome_type.lower() == 'tundra4' or biome_type.lower() == 'polar4' or biome_type.lower() == 'boreal4':
            arc_plant4 = ['nothing', 'Xanthoria', 'Saxifrage', 'an Evergreen', 'Palma Eldath', 'Arfandas', 'Bittermourn',
                          'Guardseye', 'Melander', 'Olus Veritis', 'Olvar']
            arc_weigh4 = [0.3, 0.4, 0.1, 0.15, 0.6, 0.3, 0.05,
                          0.05, 0.25, 0.1, 0.2]
            print('You have found   ' +str(random.choices(arc_plant4, arc_weigh4,k=3)))
            print()   
#CAVERNS
#editready
        elif biome_type.lower() == 'cave1' or biome_type.lower()== 'cavern1' or biome_type.lower() == 'caves1' or biome_type.lower() == 'underground1' or biome_type.lower() == 'caverns1':
            cave_plant1 = ['nothing', 'Agraricus', 'some cave mold', 'Calcena', 'Cephalophage on a nearby corpse']
            cave_weigh1 = [0.3, 0.1, 0.4, 0.02, 0.05]
            print('You have found   ' +str(random.choices(cave_plant1, cave_weigh1, k=3))) 
            print()
        elif biome_type.lower() == 'cave2' or biome_type.lower()== 'cavern2' or biome_type.lower() == 'caves2' or biome_type.lower() == 'underground2' or biome_type.lower() == 'caverns2':
            cave_plant2 =['nothing', 'Agraricus', 'Zulsendra', 'some cave mold', 'Calcena', 'Cephalophage on a nearby corpse']
            cave_weigh2 = [0.3, 0.2, 0.3, 0.4, 0.02, 0.05]
            print('You have found   ' +str(random.choices(cave_plant2, cave_weigh2, k=3))) 
            print()
        elif biome_type.lower() == 'cave3' or biome_type.lower()== 'cavern3' or biome_type.lower() == 'caves3' or biome_type.lower() == 'underground3' or biome_type.lower() == 'caverns3':
            cave_plant3 =['nothing', 'Agraricus', 'Zur', 'some cave mold', 'Calcena', 'Cephalophage on a nearby corpse']
            cave_weigh3 = [0.3, 0.3, 0.2, 0.4, 0.02, 0.05]
            print('You have found   ' +str(random.choices(cave_plant3, cave_weigh3, k=3))) 
            print()
        elif biome_type.lower() == 'cave4' or biome_type.lower()== 'cavern4' or biome_type.lower() == 'caves4' or biome_type.lower() == 'underground4' or biome_type.lower() == 'caverns4':
            cave_plant4 =['nothing', 'Agraricus', 'Zur', 'some cave mold', 'Calcena', 'Cephalophage on a nearby corpse']
            cave_weigh4 = [0.3, 0.25, 0.6, 0.4, 0.02, 0.05]
            print('You have found   ' +str(random.choices(cave_plant4, cave_weigh4, k=3))) 
            print()    
#COASTAL
        elif biome_type.lower() == 'coastal1' or biome_type.lower() == 'ocean1' or biome_type.lower()== 'coast1' or biome_type.lower()== 'beach1':
            cst_plant1 = ['nothing', 'Eucalyptus', 'Felmather', 'Fumitore', 'Bloodkeep', 'Draaf',
                          'Ebur', 'Eldaas', 'Marsh Mallow', 'Ribwort Plantain', 'Sessali', 'Snakespike',
                          'Tephrosia', 'Anise']
            cst_weigh1 = [0.2, 0.2, 0.3, 0.8, 0.2, 0.5,
                          0.45, 0.05, 0.2, 0.3, 0.1, 0.15,
                          0.3, 0.4]
            print('You have found   ' +str(random.choices(cst_plant1, cst_weigh1, k=3)))
            print()
        elif biome_type.lower() == 'coastal2' or biome_type.lower() == 'ocean2' or biome_type.lower() == 'coast2' or biome_type.lower()== 'beach2':
            cst_plant2 =['nothing', 'Eucalyptus', 'Fumitore', 'Anserke', 'Belan', 'Degiik',
                         'Eldaas', 'Horehound', 'Marsh Mallow', 'Sabito', 'Sessali', 'Tephrosia',
                         'Anise', 'Chicory', 'Curry']
            cst_weigh2 = [0.2, 0.3, 0.8, 0.3, 0.35, 0.25,
                          0.05, 0.9, 0.2, 0.02, 0.1, 0.3,
                          0.4, 0.3, 0.4]
            print('You have found   ' +str(random.choices(cst_plant2, cst_weigh2, k=3)))
            print()
        elif biome_type.lower() == 'coastal3' or biome_type.lower() == 'ocean3' or biome_type.lower() == 'coast3' or biome_type.lower()== 'beach3':
            cst_plant3 = ['nothing', 'Gylvir', 'Eucalyptus', 'Marsh Mallow', 'Sessali', 'Tephrosia',
                          'Artichoke', 'Cassava']
            cst_weigh3 = [0.2, 0.1, 0.3, 0.2, 0.1, 0.3,
                          0.4, 0.3] 
            print('You have found   ' +str(random.choices(cst_plant3, cst_weigh3, k=3)))
            print()
        elif biome_type.lower() == 'coastal4' or biome_type.lower() == 'ocean4' or biome_type.lower() == 'coast4' or biome_type.lower()== 'beach4':
            cst_plant4 = ['nothing', 'some Bryoria on a nearby log', 'Febfendu', 'Marsh Mallow', 'Olvar']
            cst_weigh4 = [0.2, 0.3, 0.05, 0.2, 0.3]
            print('You have found   ' +str(random.choices(cst_plant4, cst_weigh4, k=3)))
            print()
#DESERT
#needs generics like aloe            
        elif biome_type.lower() == 'desert1' or biome_type.lower() == 'dessert1':
            des_plant1 = ['nothing', 'Cactus Fruit', 'Culkas', 'Dragontears', 'Makebate', 'Myrrh', 'Hoodia']
            des_weigh1 = [0.3, 0.8, 0.4, 0.1, 0.35, 0.2, 0.5]
            print('You have found   ' +str(random.choices(des_plant1, des_weigh1, k=3)))
            print()
        elif biome_type.lower() == 'desert2' or biome_type.lower() == 'dessert2':
            des_plant2 = ['nothing', 'Cactus Fruit', 'Caffar', 'Culkas', 'Entriste', 'Gariig',
                          'Jaffray', 'Makebate', 'Myrrh', 'Nightcall', 'Hoodia']
            des_weigh2 = [0.4, 0.1, 0.05, 0.4, 0.3, 0.6, 0.1, 0.25, 0.15, 0.1, 0.3]
            print('You have found   ' +str(random.choices(des_plant2, des_weigh2, k=3)))
            print()
        elif biome_type.lower() == 'desert3' or biome_type.lower() == 'dessert3':
            des_plant3 = ['nothing', 'Cactus Fruit', 'Caffar', 'Culkas', 'Makebate', 'Myrrh',
                          'Hoodia', 'Aloe']
            des_weigh3 = [0.3, 0.3, 0.05, 0.4, 0.3, 0.2, 0.4, 0.5]
            print('You have found   ' +str(random.choices(des_plant3, des_weigh3, k=3)))
            print()
        elif biome_type.lower() == 'desert4' or biome_type.lower() == 'dessert4':
            des_plant4 = ['nothing', 'Cactus Fruit', 'Culkas', 'Makebate', 'Myrrh', 'Hoodia', 'Aloe']
            des_weigh4 = [0.3, 0.5, 0.4, 0.35, 0.4, 0.5, 0.55]
            print('You have found   ' +str(random.choices(des_plant4, des_weigh4, k=3)))
            print()
#FARM,  
        elif biome_type.lower() == 'farmland1' or biome_type.lower() == 'farm1' or biome_type.lower() == 'rural1' or biome_type.lower() == 'pasture1':
            farm_plant1 = ["Adder's Tongue", 'Adgana', 'Alether', 'Amrans', 'Base Mullein', 'Bastit',
                           'Blackberry', 'Black Rose', 'Burdock', 'Cephalophage on a nearby corpse', 'Elecampane',
                           'Footleaf', 'Garden Flax', 'Larnurma', 'Lungwort', 'Marigold', 'Napweed',
                           'Oede', 'Pennyroyal', 'Peony', 'Periwinkle', 'Spiderwort in chalky soil',
                           'Tamariske', 'Thorn Apple', 'Thyme', 'Alder', 'Collard Greens', 'Cucumber',
                           'Dandelion', 'Alfalfa']
            farm_weigh1 = [0.1, 0.1, 0.05, 0.3, 0.9, 0.2,
                           0.65, 0.05, 0.35, 0.05, 0.15,
                           0.1, 0.4, 0.03, 0.1, 0.4, 0.4,
                           0.01, 0.25, 0.05, 0.45, 0.5,
                           0.2, 0.2, 0.15, 0.3, 0.75, 0.4,
                           0.6, 0.3]
            print('You have found   ' +str(random.choices(farm_plant1, farm_weigh1, k=3)))
            print()
        elif biome_type.lower() == 'farmland2' or biome_type.lower() == 'farm2' or biome_type.lower() == 'rural2' or biome_type.lower() == 'pasture2':
            farm_plant2 = ['Masterwort', 'Milkworte', 'Alether', 'Alkanet', 'Cephalophage on a nerby corpse',
                           'Base Mullein', 'Basil', 'Bastit', "Bishop's Weed", 'Blackberry', 'Black Rose',
                           'Chamomile', 'Cinquefoil', 'Comfrey', 'Dog Rose', 'Marigold',
                           'Footleaf', 'Garden Flax', 'Healwell', 'Henbane', 'Mugwort', "Prince's Feather",
                           'Rue', "Saracen's Confound", 'Spiderwort in chalky soil', 'Strawberry', 'Tamariske',
                           'Thorn Apple', 'Alder', 'Anise', 'Barley', 'Canteloupe', 'Corn', 'Dandelion',
                           'Elderberry', 'Alfalfa']
            farm_weigh2 = [0.95, 0.65, 0.05, 0.3, 0.05,
                           0.9, 0.3, 0.2, 0.45, 0.4, 0.05,
                           0.3, 0.1, 0.5, 0.7, 0.4,
                           0.1, 0.4, 0.3, 0.9, 0.55, 0.45,
                           0.25, 0.8, 0.5, 0.4, 0.2,
                           0.2, 0.5, 0.3, 0.5, 0.35, 0.7, 0.9,
                           0.45, 0.5]
            print('You have found   ' +str(random.choices(farm_plant2, farm_weigh2, k=3)))
            print()
        elif biome_type.lower() == 'farmland3' or biome_type.lower() == 'farm3' or biome_type.lower() == 'rural3' or biome_type.lower() == 'pasture3':
            farm_plant3 = ['Base Mullein', 'Bastit', 'Cephalophage on a nearby corpse', 'Dog Rose', 'Fennel or Anise',
                           'Footleaf', 'Henbane', "Prince's Feather", 'Rewk', 'Tamariske', 'Alder',
                           'Apple', 'Barley', 'Carrot', 'Dandelion', 'Alfalfa']
            farm_weigh3 = [0.9, 0.2, 0.05, 0.7, 0.2,
                           0.1, 0.9, 0.45, 0.6, 0.2, 0.2,
                           0.4, 0.7, 0.4, 0.5, 0.4]
            print('You have found   ' +str(random.choices(farm_plant3, farm_weigh3, k=3)))
            print()
        elif biome_type.lower() == 'farmland4' or biome_type.lower() == 'farm4' or biome_type.lower() == 'rural4' or biome_type.lower() == 'pasture4':
            farm_plant4 = ['Base Mullein', 'Bastit', 'Cephalophage on a nearby corpse', 'Elecampane', 'Footleaf',
                           'Gallowbrush', 'Tamariske']
            farm_weigh4 = [0.9, 0.2, 0.05, 0.15, 0.1,
                           0.05, 0.2]
            print('You have found   ' +str(random.choices(farm_plant4, farm_weigh4, k=3)))
            print()
#FOREST 
        elif biome_type.lower() == 'forest1' or biome_type.lower() == 'woods1' or biome_type.lower() == 'woodlands1':
            wood_plant1 = ['Foxglove', 'Asarabacca', 'Ash', 'Bastit', 'Bilberry', 'Blackberry',
                           'Black Rose', 'Borage', 'Cephalophage on a nearby corpse', 'Cherubil', 'Colewort',
                           'Cow Parsnip', 'Garden Flax', "Hart's Tongue", 'Hawkweed', 'Kelventari', 'Laumspur',
                           'Mandrake', 'Ribwort Plantain', 'Salix or Willow', 'Spanish Nut', 'Spiderwort in chalky soil',
                           'Sweet Trefoile', 'Terbas', 'Throw-Waxe', 'Alder', 'Bead Tree', 'Beech',
                           'Birch', 'Black Tupelo', 'Clove', 'Dandelion', 'Elder', 'Elm']
            wood_weigh1 = [0.15, 0.1, 0.5, 0.2, 0.01, 0.65,
                           0.05, 0.3, 0.05, 0.1, 0.7,
                           0.45, 0.55, 0.1, 0.75, 0.5, 0.1,
                           0.4, 0.3, 0.2, 0.8, 0.5,
                           0.6, 0.75, 0.45, 0.3, 0.2, 0.3,
                           0.3, 0.5, 0.35, 0.6, 0.5, 0.4]
            print('You have found   ' +str(random.choices(wood_plant1, wood_weigh1, k=3))) 
            print()
        elif biome_type.lower() == 'forest2' or biome_type.lower() == 'woods2' or biome_type.lower() == 'woodlands2':
            wood_plant2 = ['Foxglove', 'Orach', 'Agrimony', 'Bastit', 'Belramba', 'Blackberry',
                           'Blackroot', 'Black Rose', "Cat's Tail", 'Cephalophage on a nearby corpse', 'Cherubil',
                           'Colewort', 'Cow Parsnip', 'Deadly-Nightshade', 'Fetherfew', 'Garden Flax',
                           "Goat's Rue", "Hart's Tongue", 'Hawkweed', 'Healwell', 'Kelventari', 'Laishaberry',
                           'Pattran', 'Rampalt', 'Rose Campion', 'Sanicle', 'Salix or Willow', 'Scented Mayweed',
                           'Spanish Nut', 'Spiderwort in chalky soil', 'Sweet Trefoile', 'Tempin', 'Throw-Waxe',
                           'Alder', 'Basswood', 'Beech', 'Cassia', 'Clove', 'Dandelion',
                           'Elderberry', 'Elm']
            wood_weigh2 = [0.2, 0.45, 0.3, 0.2, 0.3, 0.4,
                           0.3, 0.05, 0.75, 0.05, 0.1,
                           0.7, 0.45, 0.75, 0.65, 0.55,
                           0.6, 0.1, 0.75, 0.3, 0.5, 0.1,
                           0.2, 0.2, 0.8, 0.9, 0.2, 0.4,
                           0.8, 0.5, 0.6, 0.2, 0.45,
                           0.5, 0.2, 0.4, 0.1, 0.4, 0.9,
                           0.45, 0.35]
            print('You have found   ' +str(random.choices(wood_plant2, wood_weigh2, k=3))) 
            print()
        elif biome_type.lower() == 'forest3' or biome_type.lower() == 'woods3' or biome_type.lower() == 'woodlands3':
            wood_plant3 = ['Agraricus', 'Foxglove', 'All-Heale', 'Athelas or Kingsfoil', 'Bastit', 'Cephalophage on a nearby corpse',
                           'Cherubil', 'Cow Parsnip', 'Darnell', "Hart's Tongue", 'Hawkweed', 'Kelventari',
                           'Laishaberry', 'Saffron', 'Sanicle', 'Salix or Willow', 'Spanish Nut', 'Suaeysit',
                           'Thurl', 'White Bryony', 'Alder', 'Apple', 'Artichoke', 'Beech', 'Bleeding Heart',
                           'Buckeye', 'Cedar', 'Clove', 'Dandelion']
            wood_weigh3 = [0.8, 0.15, 0.75, 0.45, 0.2, 0.05,
                           0.1, 0.45, 0.4, 0.1, 0.75, 0.5,
                           0.1, 0.6, 0.9, 0.2, 0.8, 0.2,
                           0.9, 0.3, 0.5, 0.5, 0.3, 0.3, 0.35,
                           0.4, 0.2, 0.3, 0.5]
            print('You have found   ' +str(random.choices(wood_plant3, wood_weigh3, k=3))) 
            print()
        elif biome_type.lower() == 'forest4' or biome_type.lower() == 'woods4' or biome_type.lower() == 'woodlands4':
            wood_plant4 = ['Bastit', 'Cephalophage on a nearby corpse', 'Cherubil', 'Cow Parsnip', 'Delrean', "Hart's Tongue",
                           'Hawkweed', 'Kelventari', 'Oiolosse among some strange light', 'Saffron', 'Sanicle', 'Salix or Willow',
                           'Spanish Nut', 'Black Tupelo', 'Cedar', 'Chokecherry', 'Elder']
            wood_weigh4 = [0.2, 0.05, 0.1, 0.45, 0.8, 0.1,
                           0.75, 0.5, 0.01, 0.6, 0.9, 0.15,
                           0.8, 0.2, 0.1, 0.6, 0.65]
            print('You have found   ' +str(random.choices(wood_plant4, wood_weigh4, k=3))) 
            print()   
#BANKS  
        elif biome_type.lower() == 'river1' or biome_type.lower() == 'freshwater1' or biome_type.lower() == 'wetland1' or biome_type.lower() == 'riverbank1' or biome_type.lower() == 'estuary1' or biome_type.lower() == 'banks1':
            bank_plant1 = ['nothing', 'Amrans', 'Bastit', 'Black Rose', 'Cephalophage on a nearby corpse', 'Ribwort Plantain',
                           'Salix or Willow', 'Spiderwort in chalky soil', 'Birch', 'Dandelion', 'Aspen', 'Esculenta']
            bank_weigh1 = [0.05, 0.4, 0.2, 0.05, 0.05, 0.3,
                           0.4, 0.5, 0.4, 0.6, 0.2, 0.25]
            print('You have found   ' +str(random.choices(bank_plant1, bank_weigh1, k=3)))
            print()
        elif biome_type.lower() == 'river2' or biome_type.lower() == 'freshwater2' or biome_type.lower() == 'wetland2' or biome_type.lower() == 'riverbank2' or biome_type.lower() == 'estuary2' or biome_type.lower() == 'banks2':
            bank_plant2 = ['nothing', 'Bastit', 'Blackroot', 'Black Rose', 'Cephalophage on a nearby corpse', 'Dittany',
                           'Healwell', 'Salix or Willow', 'Spiderwort in chalky soil', 'Brooklime', 'Dandelion', 'Elderberry',
                           'Aspen', 'Esculenta']
            bank_weigh2 = [0.05, 0.2, 0.3, 0.05, 0.05, 0.55,
                           0.3, 0.4, 0.5, 0.35, 0.9, 0.45,
                           0.3, 0.4]
            print('You have found   ' +str(random.choices(bank_plant2, bank_weigh2, k=3)))
            print()
        elif biome_type.lower() == 'river3' or biome_type.lower() == 'freshwater3' or biome_type.lower() == 'wetland3' or biome_type.lower() == 'riverbank3' or biome_type.lower() == 'estuary3' or biome_type.lower() == 'banks3':
            bank_plant3 = ['nothing', 'Arfandas', 'Arnuminas', 'Arpusar', 'Attanar', 'Bastit',
                           'Cephalophage on a nearby corpse', 'Dainaberry', 'Dittany', 'Salix or Willow',
                           'Dandelion']
            bank_weigh3 = [0.05, 0.5, 0.4, 0.4, 0.45, 0.2,
                           0.05, 0.2, 0.55, 0.4,
                           0.5]
            print('You have found   ' +str(random.choices(bank_plant3, bank_weigh3, k=3)))
            print()
        elif biome_type.lower() == 'river4' or biome_type.lower() == 'freshwater4' or biome_type.lower() == 'wetland4' or biome_type.lower() == 'riverbank4' or biome_type.lower() == 'estuary4' or biome_type.lower() == 'banks4':
            bank_plant4 = ['nothing', 'Arfandas', 'Attanar', 'Bastit', 'Cephalophage on a nearby corpse', 'Edram',
                           'Febfendu', 'Melander', 'Navew', 'Olus Veritis', 'Salix or Willow']
            bank_weigh4 = [0.05, 0.5, 0.45, 0.2, 0.05, 0.15,
                           0.05, 0.65, 0.2, 0.15, 0.3]
            print('You have found   ' +str(random.choices(bank_plant4, bank_weigh4, k=3)))
            print()    
#PRAIRIE, 
        elif biome_type.lower() == 'prairie1' or biome_type.lower()== 'grasslands1' or biome_type.lower()== 'meadow1' or biome_type.lower() == 'savanna1' or biome_type.lower()== 'plains1':
            grs_plant1 = ['nothing', 'Base Mullein', 'Bastit', 'Black Rose', 'Cephalophage on a nearby corpse', 'Blue Flag',
                          'Garden Flax', 'Horseweed', 'Marjerome', 'Ribwort Plantain', 'Serapias Turbith', "Shepherd's Purse",
                          'Spiderwort in chalky soil', 'Valerian', 'Birch', 'Camphor', 'Lemongrass', 'Dandelion',
                          'Alfalfa']
            grs_weigh1 = [0.05, 0.7, 0.2, 0.05, 0.05, 0.6,
                          0.4, 0.1, 0.35, 0.3, 0.45, 0.85,
                          0.5, 0.2, 0.1, 0.15, 0.4, 0.6,
                          0.3]
            print('You have found   ' +str(random.choices(grs_plant1, grs_weigh1, k=3)))
            print()
        elif biome_type.lower() == 'prairie2' or biome_type.lower()== 'grasslands2' or biome_type.lower()== 'meadow2' or biome_type.lower() == 'savanna2' or biome_type.lower()== 'plains2':
            grs_plant2 = ['nothing', 'Base Mullein', 'Bastit', 'Blackroot', 'Black Rose', 'Bursthelas',
                          'Cephalophage on a nearby corpse', 'Cow-wheat', 'Dagmather', 'Blue Flag', 'Garden Flax',
                          'Harfy', 'Healwell', 'Horseweed', 'Kilmakur', 'Klagul', "Leopard's Bane",
                          'Marjerome', 'Saddilia', 'Serapias Turbith', "Shepherd's Purse", 'Spiderwort in chalky soil',
                          'Vinuk', 'Barley', 'Camphor', 'Lemongrass', 'Corn', 'Dandelion',
                          'Elderberry', 'Alfalfa']
            grs_weigh2 =  [0.05, 0.7, 0.2, 0.3, 0.05, 0.05,
                           0.05, 0.5, 0.4, 0.6, 0.4,
                           0.1, 0.3, 0.1, 0.45, 0.6, 0.25,
                           0.35, 0.01, 0.45, 0.85, 0.5,
                           0.3, 0.6, 0.15, 0.55, 0.5, 0.9,
                           0.45, 0.5]
            print('You have found   ' +str(random.choices(grs_plant2, grs_weigh2, k=3)))
            print()
        elif biome_type.lower() == 'prairie3' or biome_type.lower()== 'grasslands3' or biome_type.lower()== 'meadow3' or biome_type.lower() == 'savanna3' or biome_type.lower()== 'plains3':
            grs_plant3 = ['nothing', 'Arkasu', 'Base Mullein', 'Bastit', 'Cephalophage on a nearby corpse', 'Blue Flag',
                          'Horseweed', 'Marjerome', 'Saddilia', "Shepherd's Purse", 'Barley', 'Bleeding Heart',
                          'Catechu', 'Dandelion', 'Alfalfa']
            grs_weigh3 = [0.1, 0.55, 0.7, 0.2, 0.05, 0.6,
                          0.1, 0.35, 0.01, 0.85, 0.8, 0.5,
                          0.25, 0.5, 0.4]
            print('You have found   ' +str(random.choices(grs_plant3, grs_weigh3, k=3)))
            print()
        elif biome_type.lower() == 'prairie4' or biome_type.lower()== 'grasslands4' or biome_type.lower()== 'meadow4' or biome_type.lower() == 'savanna4' or biome_type.lower()== 'plains4':
            grs_plant4 = ['nothing', 'Pasque flower', 'Arlan', 'Atigax', 'Base Mullein', 'Bastit',
                          'Cephalophage on a nearby corpse', 'Blue Flag', 'Marjerome', "Shepherd's Purse",
                          'Ur']
            grs_weigh4 = [0.15, 0.2, 0.3, 0.4, 0.7, 0.2,
                          0.05, 0.6, 0.35, 0.85,
                          0.7]
            print('You have found   ' +str(random.choices(grs_plant4, grs_weigh4, k=3)))
            print()    
#MARSHES
        elif biome_type.lower() == 'marsh1' or biome_type.lower() == 'swamp1' or biome_type.lower() ==  'mangrove1' or biome_type.lower()== 'bog1':
            bog_plant1 = ['nothing', 'Bastit', 'Black Rose', 'Bull-Rush', 'Calamus','Cephalophage on a nearby corpse', 'Dwarf Mallow',
                          'Falsifal', 'Ribwort Plantain', 'Tateesha', 'Dandelion']
            bog_weigh1 = [0.05, 0.2, 0.05, 0.55, 0.15, 0.05, 0.1,
                          0.3, 0.3, 0.2, 0.6]
            print('You have found   ' +str(random.choices(bog_plant1, bog_weigh1, k=3)))
            print
        elif biome_type.lower() == 'marsh2' or biome_type.lower() == 'swamp2' or biome_type.lower() ==  'mangrove2' or biome_type.lower()== 'bog2':
            bog_plant2 = ['nothing', 'Archangelica', 'Bastit', 'Blackroot', 'Black Rose', 'Bull-Rush', 'Calamus',
                          'Cephalophage on a nearby corpse', 'Healwell', 'Tateesha', 'Dandelion', 'Elderberry']
            bog_weigh2 = [0.05, 0.3, 0.2, 0.3, 0.05, 0.55, 0.15,
                          0.05, 0.3, 0.2, 0.9, 0.45]
            print('You have found   ' +str(random.choices(bog_plant2, bog_weigh2, k=3)))
            print
        elif biome_type.lower() == 'marsh3' or biome_type.lower() == 'swamp3' or biome_type.lower() ==  'mangrove3' or biome_type.lower()== 'bog3':
            bog_plant3 = ['nothing', 'Bastit', 'Bull-Rush', 'Cephalophage on a nearby corpse', 'Tateesha', 'Dandelion']
            bog_weigh3 = [0.05, 0.2, 0.55, 0.05, 0.2, 0.5]
            print('You have found   ' +str(random.choices(bog_plant3, bog_weigh3, k=3)))
            print
        elif biome_type.lower() == 'marsh4' or biome_type.lower() == 'swamp4' or biome_type.lower() ==  'mangrove4' or biome_type.lower()== 'bog4':
            bog_plant4 = ['nothing', 'Bastit', 'Bull-Rush', 'Cephalophage on a nearby corpse', 'Tateesha']
            bog_weigh4 = [0.05, 0.2, 0.55, 0.05, 0.2]
            print('You have found   ' +str(random.choices(bog_plant4, bog_weigh4, k=3)))
            print    
#TROPICS
        elif biome_type.lower() == 'tropics1' or biome_type.lower() == 'tropical1' or biome_type.lower() == 'rainforest1' or biome_type.lower() == 'jungle1':
            trop_plant1 = ['Eucalyptus', 'Draaf', 'Golden Crown', 'Jinab', 'Maruera', 'Ribwort Plantain',
                           'Sessali by the sea', 'Spanish Nut', 'Tamarindes', 'Tateesha', 'Teriko Weed',
                           'Thorn Apple', 'Bamboo', 'Banana', 'Canteloupe', 'Cashew']
            trop_weigh1 = [0.2, 0.3, 0.1, 0.1, 0.01, 0.3,
                           0.1, 0.8, 0.85, 0.2, 0.05,
                           0.2, 0.8, 0.4, 0.35, 0.3]
            print('You have found   ' +str(random.choices(trop_plant1, trop_weigh1, k=3)))
            print
        elif biome_type.lower() == 'tropics2' or biome_type.lower() == 'tropical2' or biome_type.lower() == 'rainforest2' or biome_type.lower() == 'jungle2':
            trop_plant2 = ['Eucalyptus', 'Anserke', 'Belan', 'Degiik', 'Fetherfew', 'Fire-Flower',
                           'Jinab', 'Juniper', 'Kylathar', 'Land Caltrops', 'Maruera', 'Pargen',
                           'Petiveria', 'Sabito', 'Sessali by the sea', 'Sinquoi', 'Spanish Nut', 'Tai-gi',
                           'Tamarindes', 'Tateesha', 'Teriko Weed', 'Thorn Apple', 'Bamboo', 'Banana',
                           'Canteloupe', 'Cashew', 'Cassia', ' Chocolate', 'Curry']
            trop_weigh2 = [0.3, 0.2, 0.2, 0.2, 0.65, 0.01,
                           0.1, 0.2, 0.1, 0.6, 0.01, 0.01,
                           0.2, 0.02, 0.1, 0.15, 0.8, 0.1,
                           0.85, 0.2, 0.05, 0.2, 0.8, 0.3,
                           0.35, 0.45, 0.4, 0.3, 0.25]
            print('You have found   ' +str(random.choices(trop_plant2, trop_weigh2, k=3)))
            print
        elif biome_type.lower() == 'tropics3' or biome_type.lower() == 'tropical3' or biome_type.lower() == 'rainforest3' or biome_type.lower() == 'jungle3':
            trop_plant3 = ['Eucalyptus', 'Callin', 'Jinab', 'Kylathar', 'Sessali by the sea', 'Spanish Nut',
                           'Tamarindes', 'Tateesha', 'Bamboo', 'Cassava', 'Chocolate', 'Coconut',
                           'Dragonfruit']
            trop_weigh3 = [0.2, 0.3, 0.1, 0.1, 0.1, 0.8,
                           0.85, 0.2, 0.8, 0.3, 0.25, 0.35,
                           0.35]
            print('You have found   ' +str(random.choices(trop_plant3, trop_weigh3, k=3)))
            print
        elif biome_type.lower() == 'tropics4' or biome_type.lower() == 'tropical4' or biome_type.lower() == 'rainforest4' or biome_type.lower() == 'jungle4':
            trop_plant4 = ['Eucalyptus', 'Jinab', 'Navew', 'Spanish Nut', 'Tamarindes', 'Tateesha',
                           'Bamboo', 'Catalpa', 'Clove', 'Coconut', 'Dragonfruit']
            trop_weigh4 = [0.1, 0.1, 0.6, 0.8, 0.85, 0.2,
                           0.6, 0.15, 0.4, 0.45, 0.55]
            print('You have found   ' +str(random.choices(trop_plant4, trop_weigh4, k=3)))
            print    
#CHAPARRAL
#editready
        elif biome_type.lower() == 'scrub1' or biome_type.lower() == 'chaparral1' or biome_type.lower() ==  'shrub1' or biome_type.lower() ==  'dry1' or biome_type.lower() == 'arid1' or biome_type.lower() == 'steppe1' or biome_type.lower() == 'mesa1':
            arid_plant1 = ['nothing', 'tumbleweed', 'Eucalyptus', 'Ribwort Plantain', 'Anise', ' Cinchona' ]
            arid_weigh1 = [0.2, 0.1, 0.2, 0.3, 0.4, 0.25]
            print('You have found   '+str(random.choices(arid_plant1, arid_weigh1, k=3)))
            print()
        elif biome_type.lower() == 'scrub2' or biome_type.lower() == 'chaparral2' or biome_type.lower() ==  'shrub2' or biome_type.lower() ==  'dry2' or biome_type.lower() == 'arid2' or biome_type.lower() == 'steppe2' or biome_type.lower() == 'mesa2':
            arid_plant2 = ['nothing', 'tumbleweed', 'Cactus Fruit', 'Anise', 'Chicory', 'Cinchona',
                           'Curry']
            arid_weigh2 = [0.2, 0.1, 0.2, 0.4, 0.45, 0.3,
                           0.3]
            print('You have found   '+str(random.choices(arid_plant2, arid_weigh2, k=3)))
            print()
        elif biome_type.lower() == 'scrub3' or biome_type.lower() == 'chaparral3' or biome_type.lower() ==  'shrub3' or biome_type.lower() ==  'dry3' or biome_type.lower() == 'arid3' or biome_type.lower() == 'steppe3' or biome_type.lower() == 'mesa3':
            arid_plant3 = ['nothing', 'tumbleweed', 'Eucalyptus', 'Aloe', 'Almond', 'Artichoke',
                           'Cassava', 'Catechu']
            arid_weigh3 = [0.2, 0.1, 0.2, 0.5, 0.2, 0.6,
                           0.2, 0.3]
            print('You have found   '+str(random.choices(arid_plant3, arid_weigh3, k=3)))
            print()
        elif biome_type.lower() == 'scrub4' or biome_type.lower() == 'chaparral4' or biome_type.lower() ==  'shrub4' or biome_type.lower() ==  'dry4' or biome_type.lower() == 'arid4' or biome_type.lower() == 'steppe4' or biome_type.lower() == 'mesa4':
            arid_plant4 = ['nothing', 'tumbleweed', 'Aloe', 'Crampbark', 'Tenlas']
            arid_weigh4 = [0.2, 0.1, 0.55, 0.65, 0.05]
            print('You have found   '+str(random.choices(arid_plant4, arid_weigh4, k=3)))
            print()    
#MOUNTAINS
        elif biome_type.lower() == 'mountain1' or biome_type.lower() == 'mountains1' or biome_type.lower() == 'plateau1' or biome_type.lower() == 'mesa1':
            mesa_plant1 = ['nothing', 'an Evergreen', 'Aldaka', 'Arnica', 'Ashline','Birthnot',
                           'Cephalophage on a nearby corpse', 'Coltsfoot', 'Dragonwort', 'Mountain Garlick',
                           'Mountain Setwall', 'Ribwort Plantain', 'Silverthorn', 'Spring Adonis', 'Thyme',
                           'Dandelion']
            mesa_weigh1 = [0.05, 0.3, 0.01, 0.25, 0.05, 0.3,
                           0.05, 0.25, 0.15, 0.3,
                           0.4, 0.3, 0.01, 0.4, 0.15,
                           0.6]
            print('You have found  '+str(random.choices(mesa_plant1, mesa_weigh1, k=3)))
            print()
        elif biome_type.lower() == 'mountain2' or biome_type.lower() == 'mountains2' or biome_type.lower() == 'plateau2' or biome_type.lower() == 'mesa2':
            mesa_plant2 = ['nothing', 'an Evergreen', 'Birthnot', 'Cephalophage on a nearby corpse', 'Coltsfoot', 'Fire-Flower',
                           "Hare's Ears", 'Healwell', 'Ironhard', 'Juniper', 'Lesser Centaury', 'Maruera',
                           'Mountain Garlick', 'Mountain Setwall', 'Silverthorn', 'Barley', 'Dandelion']
            mesa_weigh2 = [0.05, 0.3, 0.3, 0.05, 0.25, 0.01,
                           0.55, 0.3, 0.1, 0.2, 0.25, 0.01,
                           0.3, 0.4, 0.01, 0.1, 0.9]
            print('You have found  '+str(random.choices(mesa_plant2, mesa_weigh2, k=3)))
            print()
        elif biome_type.lower() == 'mountain3' or biome_type.lower() == 'mountains3' or biome_type.lower() == 'plateau3' or biome_type.lower() == 'mesa3':
            mesa_plant3 = ['nothing', 'an Evergreen', 'Birthnot', 'Cephalophage on a nearby corpse', 'Ironhard',
                           'Jojojopo', 'Mountain Garlick', 'Mountain Setwall', 'Silverthorn', 'Barley', 'Cedar',
                           'Dandelion']
            mesa_weigh3 = [0.05, 0.3, 0.3, 0.05, 0.1,
                           0.6, 0.3, 0.4, 0.01, 0.3, 0.45,
                           0.5]
            print('You have found  '+str(random.choices(mesa_plant3, mesa_weigh3, k=3)))
            print()
        elif biome_type.lower() == 'mountain4' or biome_type.lower() == 'mountains4' or biome_type.lower() == 'plateau4' or biome_type.lower() == 'mesa4':
            mesa_plant4 = ['nothing', 'an Evergreen', 'Aldaka', 'Ashline', 'Birthnot', 'Bittermourn',
                           'Cephalophage on a nearby corpse', 'Darsurion', 'Megillos', 'Mirenna', 'Mountain Garlick',
                           'Mountain Setwall', 'Silverthorn', 'Bearberry', 'Cedar']
            mesa_weigh4 = [0.05, 0.3, 0.05, 0.05, 0.3, 0.03,
                           0.05, 0.5, 0.75, 0.6, 0.3,
                           0.4, 0.01, 0.1, 0.35]
            print('You have found  '+str(random.choices(mesa_plant4, mesa_weigh4, k=3)))
            print()    
#VOLCANO
        elif biome_type.lower() == 'volcano1':
#test if weights work
            print('You have found   '+str(random.choices(['nothing', 'Brorkwilb', 'an active Geyser. Take 3 damage', 'Breldiar', 'Disastro'], [0.9, 0.15, 0.2, 0.35, 0.05], k=3)))
            print()
        elif biome_type.lower() == 'volcano2':
            print('You have found   '+str(random.choices(['nothing', 'Brorkwilb', 'an active Geyser. Take 3 damage', "Widow's Rest", 'Gefnul', 'Disastro'], [0.9, 0.15, 0.2, 0.05, 0.6, 0.05], k=3)))
            print()
        elif biome_type.lower() == 'volcano3':
            print('You have found   '+str(random.choices(['nothing', 'Brorkwilb', 'an active Geyser. Take 3 damage', "Widow's Rest", 'Disastro'], [0.9, 0.15, 0.2, 0.15, 0.05], k=3)))
            print()
        elif biome_type.lower() == 'volcano4':
            print('You have found   '+str(random.choices(['nothing', 'Brorkwilb', 'an active Geyser. Take 3 damage', 'Disastro'], [0.9, 0.15, 0.2, 0.05], k=3)))
            print()    
#WASTES            
        elif biome_type.lower() == 'wastes1' or biome_type.lower() == 'wastelands1' or biome_type.lower() == 'badlands1' or biome_type.lower() == 'wasteland1':
#test if weights work
            print('You have found   '+str(random.choices(['nothing', 'a dead rodent', 'Cephalophage on a nearby corpse', 'Disastro'], [0.9, 0.3, 0.05, 0.01], k=3)))
            print()
        elif biome_type.lower() == 'wastes2' or biome_type.lower() == 'wastelands2' or biome_type.lower() == 'badlands2' or biome_type.lower() == 'wasteland2':
            print('You have found   '+str(random.choices(['nothing', 'a dead rodent', 'wastesplant1'], [0.9, 0.3, 0.1], k=3)))
            print()
        elif biome_type.lower() == 'wastes3' or biome_type.lower() == 'wastelands3' or biome_type.lower() == 'badlands3' or biome_type.lower() == 'wasteland3':
            print('You have found   '+str(random.choices(['nothing', 'a dead rodent', 'wastesplant1'], [0.9, 0.3, 0.1], k=3)))
            print()
        elif biome_type.lower() == 'wastes4' or biome_type.lower() == 'wastelands4' or biome_type.lower() == 'badlands4' or biome_type.lower() == 'wasteland4':
            print('You have found   '+str(random.choices(['nothing', 'a dead rodent', 'Kathkusa'], [0.9, 0.3, 0.3], k=3)))
            print()    
#VALLEY,
        elif biome_type.lower() == 'valley1' or biome_type.lower() == 'canyon1':
            val_plant1 = ['nothing', 'Base Mullein', 'Bastit', 'Amrans', 'Birthnot', 'Black Rose',
                          'Cephalophage on a nearby corpse', 'Comfrey', 'Garden Flax', 'Larnurma', 'Ribwort Plantain',
                          'Spiderwort in chalky soil', 'Black Rose', 'Catnip', 'Chia', 'Collard Greens',
                          'Cucumber', 'Dandelion', 'Dove Tree', 'Aspen', 'Esculenta']
            val_weigh1 = [0.05, 0.5, 0.2, 0.3, 0.3, 0.05,
                          0.05, 0.5, 0.4, 0.03, 0.3,
                          0.5, 0.05, 0.4, 0.5, 0.75,
                          0.45, 0.6, 0.4, 0.2, 0.2]
            print('You have found   '+str(random.choices(val_plant1, val_weigh1, k=3)))
            print()
        elif biome_type.lower() == 'valley2' or biome_type.lower() == 'canyon2':
            val_plant2 = ['nothing', "Widow's Rest", 'Base Mullein', 'Bastit', 'Birthnot', 'Blackroot',
                          'Black Rose', 'Cephalophage on a nearby corpse', 'Dittany', 'Garden Flax', 'Healwell',
                          'Spiderwort in chalky soil', 'Barley', 'Bell Pepper', 'Black Rose', 'Blackroot', 'Catnip',
                          'Chia', 'Corn', 'Dandelion', 'Dove Tree', 'Elderberry', 'Aspen',
                          'Esculenta']
            val_weigh2 = [0.05, 0.05, 0.5, 0.2, 0.3, 0.3,
                          0.05, 0.05, 0.35, 0.4, 0.3,
                          0.5, 0.2, 0.6, 0.05, 0.3, 0.6,
                          0.6, 0.5, 0.9, 0.45, 0.45, 0.3,
                          0.3]
            print('You have found   '+str(random.choices(val_plant2, val_weigh2, k=3)))
            print()
        elif biome_type.lower() == 'valley3' or biome_type.lower() == 'canyon3':
            val_plant3 = ['nothing', 'Attanar', "Widow's Rest", 'Base Mullein', 'Bastit', 'Birthnot',
                          'Cephalophage on a nearby corpse', 'Dainaberry', 'Dittany', 'Barley', 'Bell Pepper',
                          'Chia', 'Dandelion']
            val_weigh3 = [0.05, 0.45, 0.1, 0.5, 0.2, 0.3,
                          0.05, 0.2, 0.35, 0.4, 0.8,
                          0.45, 0.5]
            print('You have found   '+str(random.choices(val_plant3, val_weigh3, k=3)))
            print()
        elif biome_type.lower() == 'valley4' or biome_type.lower() == 'canyon4':
            val_plant4 = ['nothing', 'Attanar', 'Base Mullein', 'Bastit', 'Birthnot', 'Cephalophage on a nearby corpse',
                          'Febfendu']
            val_weigh4 = [0.05, 0.45, 0.5, 0.2, 0.3, 0.05,
                          0.03]
            print('You have found  '+str(random.choices(val_plant4, val_weigh4, k=3)))
            print()    
#do you want the berry bushes and nut trees?
#add more common nuts and berries but that also means more common trees, oh my            
        elif biome_type.lower() == 'nut' or biome_type.lower() == 'nuts':
            nut_plant = ['Belan', 'Caffar', 'Saddilia', 'Spanish Nut', 'Almond', 'Hickory']
            nut_weight = [0.30, 0.05, 0.01, 0.8, 0.05, 0.75]
            print('You have found   '+str(random.choices(nut_plant, nut_weight, k=1)))
        elif biome_type.lower() == 'berry':
            berry_plant = ['Alether', 'Bilberry', 'Blackberry', 'Dainaberry', 'Deadly-Nightshade', 'Kelventari', 'Changeberry',
                           'Strawberry', 'Aldaka', 'Bead Tree']
            berry_weight = [0.1, 0.02, 0.6, 0.2, 0.7, 0.5, 0.1,
                            0.4, 0.05, 0.2]
            print('You have found   '+str(random.choices(berry_plant, berry_weight, k=1)))
            print()
        elif biome_type.lower() == 'citrus':
            citrus_plant = ['Lemon', 'Grapefruit', 'Orange', 'Lime']
            print('You have found   '+str(random.choices(citrus_plant)))
            print()

        elif biome_type.lower() == 'evergreen':
            #these don't need to be weighted
            evergreen_plant = ['Laurus or Bay', 'Cedar', 'Pine', 'Holly', 'Hemlock']
            print('You have found   '+str(random.choices(evergreen_plant)))
            print()
#NO GENERIC TREE OR PLANT TABLES HERE because
             #weighting would be a fucking nightmare
        else:
            print("Please enter a valid biome type")
            print()


    except(Exception):
        print(e)
                

    more_plants = input('More plants? (y/n):\t\t')    
