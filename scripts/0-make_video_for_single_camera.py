import os
import shutil
import sys



# output_Dir='/Users/clc/Documents/EPFL/NeLy/Data/ANproj/dlc/training_frames/'

# if not os.path.exists(output_Dir):
#     os.makedirs(output_Dir)


video_cam=6


#for training DLC network
rawdatalist_PERperiod=[ #(filepath, camera frame# start, camera frame# end)

# ('/Users/clc/Documents/EPFL/NeLy/Data/ANproj/200305_SS31232-tdTomGC6fopt/Fly1/CO2xzGG/behData_002/', 2810, 3250),
# ('/Users/clc/Documents/EPFL/NeLy/Data/ANproj/200305_SS31232-tdTomGC6fopt/Fly3/CO2xzGG/behData_001/images/', 933, 1180),
# ('/Users/clc/Documents/EPFL/NeLy/Data/ANproj/200305_SS31232-tdTomGC6fopt/Fly3/CO2xzGG/behData_001/images/', 5193, 5566),
# ('/Volumes/data/CLC/200207_SS31232-tdTomGC6fopt/Fly2/CO2xzGG/behData_001/images/', 121, 548),
# ('/Volumes/data/CLC/200211_SS31232-tdTomGC6fopt/Fly2/CO2xzGG/behData_002/images/', 3050, 4166),
# ('/Volumes/data/CLC/200217_SS31232-tdTomGC6fopt/Fly1/CO2xzGG/behData_001/images/', 4006, 4600),
# ('/Volumes/data/CLC/200217_SS31232-tdTomGC6fopt/Fly2/CO2xzGG/behData_002/images/', 4700, 5556),
# ('/Volumes/data/CLC/200304_SS31232-tdTomGC6fopt/Fly1/CO2xzGG/behData_004/images/', 6400, 7202),

]

#for analyzing whole data
rawdatalist=[
# ('20181227', 'R15E08-tdTomGC6fopt', 'fly2', '001'),#axoid
# ('20181227', 'R15E08-tdTomGC6fopt', 'fly2', '002'),#axoid
# ('20181227', 'R15E08-tdTomGC6fopt', 'fly2', '003'),#axoid
# ('20181227', 'R15E08-tdTomGC6fopt', 'fly2', '004'),#axoid
# ('20181227', 'R15E08-tdTomGC6fopt', 'fly2', '005'),#axoid

# ('20181202', 'R70H06-tdTomGC6fopt', 'fly1', '001'), #UsrCorrected
# ('20181202', 'R70H06-tdTomGC6fopt', 'fly1', '002'), #UsrCorrected
# ('20181202', 'R70H06-tdTomGC6fopt', 'fly1', '003'), #UsrCorrected
# ('20181202', 'R70H06-tdTomGC6fopt', 'fly1', '004'),
# ('20181202', 'R70H06-tdTomGC6fopt', 'fly1', '005'),
# ('20181202', 'R70H06-tdTomGC6fopt', 'fly1', '006'),
# ('20181202', 'R70H06-tdTomGC6fopt', 'fly1', '007'),

# ('20181123', 'R30A08-tdTomGC6fopt', 'fly1', '001'),#axoid
# ('20181123', 'R30A08-tdTomGC6fopt', 'fly1', '002'),#axoid
# ('20181123', 'R30A08-tdTomGC6fopt', 'fly1', '003'), 
# ('20181123', 'R30A08-tdTomGC6fopt', 'fly1', '004'),#axoid
# ('20181123', 'R30A08-tdTomGC6fopt', 'fly1', '005'),#axoid
# ('20181123', 'R30A08-tdTomGC6fopt', 'fly1', '006'),#axoid
# ('20181123', 'R30A08-tdTomGC6fopt', 'fly1', '007'),#axoid
# ('20181123', 'R30A08-tdTomGC6fopt', 'fly1', '008'), 
# ('20181123', 'R30A08-tdTomGC6fopt', 'fly1', '009'),#axoid
# ('20181123', 'R30A08-tdTomGC6fopt', 'fly1', '010'),#axoid
# ('20181123', 'R30A08-tdTomGC6fopt', 'fly1', '011'),#axoid
# ('20181123', 'R30A08-tdTomGC6fopt', 'fly1', '012'),#axoid
# ('20181123', 'R30A08-tdTomGC6fopt', 'fly1', '013'), 
# ('20181123', 'R30A08-tdTomGC6fopt', 'fly1', '014'),#axoid
# ('20181123', 'R30A08-tdTomGC6fopt', 'fly1', '015'),#axoid
# ('20181123', 'R30A08-tdTomGC6fopt', 'fly1', '016'),#axoid

# ('20181128', 'R30A08-tdTomGC6fopt', 'fly1', '001'),#axoid
# ('20181128', 'R30A08-tdTomGC6fopt', 'fly1', '002'),#axoid
# ('20181128', 'R30A08-tdTomGC6fopt', 'fly1', '003'), 
# ('20181128', 'R30A08-tdTomGC6fopt', 'fly1', '004'),#axoid
# ('20181128', 'R30A08-tdTomGC6fopt', 'fly1', '005'),#axoid

# ('20181128', 'R30A08-tdTomGC6fopt', 'fly2', '001'),#axoid
# ('20181128', 'R30A08-tdTomGC6fopt', 'fly2', '002'),#axoid
# ('20181128', 'R30A08-tdTomGC6fopt', 'fly2', '003'), # first of few frames are dark, so there is no warp results
# ('20181128', 'R30A08-tdTomGC6fopt', 'fly2', '004'),#axoid
# ('20181128', 'R30A08-tdTomGC6fopt', 'fly2', '005'),#axoid
# ('20181128', 'R30A08-tdTomGC6fopt', 'fly2', '006'),#axoid
# ('20181128', 'R30A08-tdTomGC6fopt', 'fly2', '007'),#axoid
# ('20181128', 'R30A08-tdTomGC6fopt', 'fly2', '008'),#axoid
# ('20181128', 'R30A08-tdTomGC6fopt', 'fly2', '009'),#axoid

# ('20181230', 'R36G04-tdTomGC6fopt', 'fly1', '001'),
# ('20181230', 'R36G04-tdTomGC6fopt', 'fly1', '002'),
# ('20181230', 'R36G04-tdTomGC6fopt', 'fly1', '003'),
# ('20181230', 'R36G04-tdTomGC6fopt', 'fly1', '004'),
# ('20181230', 'R36G04-tdTomGC6fopt', 'fly1', '005'),
# ('20181230', 'R36G04-tdTomGC6fopt', 'fly1', '006'),

# ('20181221', 'R65D11-tdTomGC6fopt', 'fly1', '001'),
# ('20181221', 'R65D11-tdTomGC6fopt', 'fly1', '002'),
# ('20181221', 'R65D11-tdTomGC6fopt', 'fly1', '003'),
# ('20181221', 'R65D11-tdTomGC6fopt', 'fly1', '004'),
# ('20181221', 'R65D11-tdTomGC6fopt', 'fly1', '005'),
# ('20181221', 'R65D11-tdTomGC6fopt', 'fly1', '006'),
# ('20181221', 'R65D11-tdTomGC6fopt', 'fly1', '007'),
# ('20181221', 'R65D11-tdTomGC6fopt', 'fly1', '008'),
# ('20181221', 'R65D11-tdTomGC6fopt', 'fly1', '009'),
# ('20181221', 'R65D11-tdTomGC6fopt', 'fly1', '010'),

# ('20181125', 'R85A11-tdTomGC6fopt', 'fly1', '001'),
# ('20181125', 'R85A11-tdTomGC6fopt', 'fly1', '002'),
# ('20181125', 'R85A11-tdTomGC6fopt', 'fly1', '003'),
# ('20181125', 'R85A11-tdTomGC6fopt', 'fly1', '004'),
# ('20181125', 'R85A11-tdTomGC6fopt', 'fly1', '005'),
# ('20181125', 'R85A11-tdTomGC6fopt', 'fly1', '006'),
# ('20181125', 'R85A11-tdTomGC6fopt', 'fly1', '007'),
# ('20181125', 'R85A11-tdTomGC6fopt', 'fly1', '008'),
# ('20181125', 'R85A11-tdTomGC6fopt', 'fly1', '009'),

# ('20190220', 'SS25469-tdTomGC6fopt', 'fly1', '001'),#axoid
# ('20190220', 'SS25469-tdTomGC6fopt', 'fly1', '002'),#axoid
# ('20190220', 'SS25469-tdTomGC6fopt', 'fly1', '003'),#axoid
# ('20190220', 'SS25469-tdTomGC6fopt', 'fly1', '004'),#axoid
# ('20190220', 'SS25469-tdTomGC6fopt', 'fly1', '005'),#axoid
# ('20190220', 'SS25469-tdTomGC6fopt', 'fly1', '006'),#axoid
# ('20190220', 'SS25469-tdTomGC6fopt', 'fly1', '007'),#axoid
# ('20190220', 'SS25469-tdTomGC6fopt', 'fly1', '008'),#axoid

# ('20190308', 'SS27485-tdTomGC6fopt', 'fly1', '001'),#axoid
# ('20190308', 'SS27485-tdTomGC6fopt', 'fly1', '002'),#axoid
# ('20190308', 'SS27485-tdTomGC6fopt', 'fly1', '003'),#axoid
# ('20190308', 'SS27485-tdTomGC6fopt', 'fly1', '004'),#axoid
# ('20190308', 'SS27485-tdTomGC6fopt', 'fly1', '005'),#axoid
# ('20190308', 'SS27485-tdTomGC6fopt', 'fly1', '006'),#axoid
# ('20190308', 'SS27485-tdTomGC6fopt', 'fly1', '007'),#axoid
# ('20190308', 'SS27485-tdTomGC6fopt', 'fly1', '008'),#axoid

# ('20190311', 'SS27485-tdTomGC6fopt', 'fly2', '001'),#axoid
# ('20190311', 'SS27485-tdTomGC6fopt', 'fly2', '002'),#axoid
# ('20190311', 'SS27485-tdTomGC6fopt', 'fly2', '003'),#axoid
# ('20190311', 'SS27485-tdTomGC6fopt', 'fly2', '004'),#axoid
# ('20190311', 'SS27485-tdTomGC6fopt', 'fly2', '005'),#axoid
# ('20190311', 'SS27485-tdTomGC6fopt', 'fly2', '006'),#axoid
# ('20190311', 'SS27485-tdTomGC6fopt', 'fly2', '007'),#axoid

# ('20190322', 'SS28596-tdTomGC6fopt', 'fly1', '001'),#axoid
# ('20190322', 'SS28596-tdTomGC6fopt', 'fly1', '002'),#axoid
# ('20190322', 'SS28596-tdTomGC6fopt', 'fly1', '003'),#axoid
# ('20190322', 'SS28596-tdTomGC6fopt', 'fly1', '004'),#axoid
# ('20190322', 'SS28596-tdTomGC6fopt', 'fly1', '005'),#axoid

# ('20190318', 'SS29621-tdTomGC6fopt', 'fly1', '001'),#axoid
# ('20190318', 'SS29621-tdTomGC6fopt', 'fly1', '002'),#axoid
# ('20190318', 'SS29621-tdTomGC6fopt', 'fly1', '003'),#axoid
# ('20190318', 'SS29621-tdTomGC6fopt', 'fly1', '004'),#axoid
# ('20190318', 'SS29621-tdTomGC6fopt', 'fly1', '005'),#axoid
# ('20190318', 'SS29621-tdTomGC6fopt', 'fly1', '006'),#axoid
# ('20190318', 'SS29621-tdTomGC6fopt', 'fly1', '007'),#axoid
# ('20190318', 'SS29621-tdTomGC6fopt', 'fly1', '008'),#axoid
# ('20190318', 'SS29621-tdTomGC6fopt', 'fly1', '009'),#axoid

# ('20190328', 'SS29893-tdTomGC6fopt', 'fly3', '001'),#axoid
# ('20190328', 'SS29893-tdTomGC6fopt', 'fly3', '002'),#axoid
# ('20190328', 'SS29893-tdTomGC6fopt', 'fly3', '003'),#axoid
# ('20190328', 'SS29893-tdTomGC6fopt', 'fly3', '004'),#axoid
# ('20190328', 'SS29893-tdTomGC6fopt', 'fly3', '005'),#axoid
# ('20190328', 'SS29893-tdTomGC6fopt', 'fly3', '006'),#axoid
# ('20190328', 'SS29893-tdTomGC6fopt', 'fly3', '007'),#axoid
# ('20190328', 'SS29893-tdTomGC6fopt', 'fly3', '008'),#axoid
# ('20190328', 'SS29893-tdTomGC6fopt', 'fly3', '009'),#axoid

# ('20190415', 'SS29633-tdTomGC6fopt', 'fly1', '001'),#axoid
# ('20190415', 'SS29633-tdTomGC6fopt', 'fly1', '002'),#axoid
# ('20190415', 'SS29633-tdTomGC6fopt', 'fly1', '003'),#axoid
# ('20190415', 'SS29633-tdTomGC6fopt', 'fly1', '004'),#axoid
# ('20190415', 'SS29633-tdTomGC6fopt', 'fly1', '005'),#axoid
# ('20190415', 'SS29633-tdTomGC6fopt', 'fly1', '006'),#axoid
# ('20190415', 'SS29633-tdTomGC6fopt', 'fly1', '007'),#axoid
# ('20190415', 'SS29633-tdTomGC6fopt', 'fly1', '008'),#axoid
# ('20190415', 'SS29633-tdTomGC6fopt', 'fly1', '009'),#axoid
# ('20190415', 'SS29633-tdTomGC6fopt', 'fly1', '010'),#axoid

# ('20190405', 'SS30303-tdTomGC6fopt', 'fly2', '001'),#axoid
# ('20190405', 'SS30303-tdTomGC6fopt', 'fly2', '002'),#axoid
# ('20190405', 'SS30303-tdTomGC6fopt', 'fly2', '003'),#axoid
# ('20190405', 'SS30303-tdTomGC6fopt', 'fly2', '004'),#axoid
# ('20190405', 'SS30303-tdTomGC6fopt', 'fly2', '005'),#axoid
# ('20190405', 'SS30303-tdTomGC6fopt', 'fly2', '006'),#axoid

# ('20190412', 'SS31232-tdTomGC6fopt', 'fly3', '001'),#axoid
# ('20190412', 'SS31232-tdTomGC6fopt', 'fly3', '002'),#axoid
# ('20190412', 'SS31232-tdTomGC6fopt', 'fly3', '003'),#axoid
# ('20190412', 'SS31232-tdTomGC6fopt', 'fly3', '004'),#axoid
# ('20190412', 'SS31232-tdTomGC6fopt', 'fly3', '005'),#axoid
# ('20190412', 'SS31232-tdTomGC6fopt', 'fly3', '006'),#axoid

# ('20190408', 'SS31219-tdTomGC6fopt', 'fly1', '001'),#axoid
# ('20190408', 'SS31219-tdTomGC6fopt', 'fly1', '002'),#axoid
# ('20190408', 'SS31219-tdTomGC6fopt', 'fly1', '003'),#axoid
# ('20190408', 'SS31219-tdTomGC6fopt', 'fly1', '004'),#axoid

# ('20190410', 'SS31456-tdTomGC6fopt', 'fly1', '001'),#axoid
# ('20190410', 'SS31456-tdTomGC6fopt', 'fly1', '002'),#axoid
# ('20190410', 'SS31456-tdTomGC6fopt', 'fly1', '003'),#axoid
# ('20190410', 'SS31456-tdTomGC6fopt', 'fly1', '004'),#axoid
# ('20190410', 'SS31456-tdTomGC6fopt', 'fly1', '005'),#axoid
# ('20190410', 'SS31456-tdTomGC6fopt', 'fly1', '006'),#axoid
# ('20190410', 'SS31456-tdTomGC6fopt', 'fly1', '007'),#axoid
# ('20190410', 'SS31456-tdTomGC6fopt', 'fly1', '008'),#axoid
# ('20190410', 'SS31456-tdTomGC6fopt', 'fly1', '009'),#axoid
# ('20190410', 'SS31456-tdTomGC6fopt', 'fly1', '010'),#axoid


# ('20190417', 'SS31480-tdTomGC6fopt', 'fly1', '001'),#axoid
# ('20190417', 'SS31480-tdTomGC6fopt', 'fly1', '003'),#axoid
# ('20190417', 'SS31480-tdTomGC6fopt', 'fly1', '004'),#axoid
# ('20190417', 'SS31480-tdTomGC6fopt', 'fly1', '005'),#axoid
# ('20190417', 'SS31480-tdTomGC6fopt', 'fly1', '007'),#axoid

# ('20190506', 'SS32365-tdTomGC6fopt', 'fly1', '004'),#axoid
# ('20190506', 'SS32365-tdTomGC6fopt', 'fly1', '005'),#axoid
# ('20190506', 'SS32365-tdTomGC6fopt', 'fly1', '006'),#axoid
# ('20190506', 'SS32365-tdTomGC6fopt', 'fly1', '007'),#axoid
# ('20190506', 'SS32365-tdTomGC6fopt', 'fly1', '008'),#axoid

# ('20190522', 'SS34574-tdTomGC6fopt', 'fly2', '001'),#axoid
# ('20190522', 'SS34574-tdTomGC6fopt', 'fly2', '002'),#axoid
# ('20190522', 'SS34574-tdTomGC6fopt', 'fly2', '003'),#axoid
# ('20190522', 'SS34574-tdTomGC6fopt', 'fly2', '004'),#axoid
# ('20190522', 'SS34574-tdTomGC6fopt', 'fly2', '005'),#axoid
# ('20190522', 'SS34574-tdTomGC6fopt', 'fly2', '006'),#axoid

# ('20190517', 'SS36112-tdTomGC6fopt', 'fly1', '001'),#axoid
# ('20190517', 'SS36112-tdTomGC6fopt', 'fly1', '002'),#axoid
# ('20190517', 'SS36112-tdTomGC6fopt', 'fly1', '003'),#axoid
# ('20190517', 'SS36112-tdTomGC6fopt', 'fly1', '004'),#axoid
# ('20190517', 'SS36112-tdTomGC6fopt', 'fly1', '005'),#axoid
# ('20190517', 'SS36112-tdTomGC6fopt', 'fly1', '006'),#axoid
# ('20190517', 'SS36112-tdTomGC6fopt', 'fly1', '007'),#axoid
# ('20190517', 'SS36112-tdTomGC6fopt', 'fly1', '008'),#axoid
# ('20190517', 'SS36112-tdTomGC6fopt', 'fly1', '009'),#axoid

# ('20190516', 'SS36118-tdTomGC6fopt', 'fly4', '001'),#axoid
# ('20190516', 'SS36118-tdTomGC6fopt', 'fly4', '002'),#axoid
# ('20190516', 'SS36118-tdTomGC6fopt', 'fly4', '003'),#axoid
# ('20190516', 'SS36118-tdTomGC6fopt', 'fly4', '004'),#axoid
# ('20190516', 'SS36118-tdTomGC6fopt', 'fly4', '005'),#axoid
# ('20190516', 'SS36118-tdTomGC6fopt', 'fly4', '006'),#axoid
# ('20190516', 'SS36118-tdTomGC6fopt', 'fly4', '007'),#axoid

# ('20190520', 'SS36131-tdTomGC6fopt', 'fly1', '001'),#axoid
# ('20190520', 'SS36131-tdTomGC6fopt', 'fly1', '003'),#axoid
# ('20190520', 'SS36131-tdTomGC6fopt', 'fly1', '004'),#axoid
# ('20190520', 'SS36131-tdTomGC6fopt', 'fly1', '005'),#axoid
# ('20190520', 'SS36131-tdTomGC6fopt', 'fly1', '006'),#axoid
# ('20190520', 'SS36131-tdTomGC6fopt', 'fly1', '007'),#axoid

# ('20190521', 'SS36131-tdTomGC6fopt', 'fly1', '001'),#axoid
# ('20190521', 'SS36131-tdTomGC6fopt', 'fly1', '003'),#axoid
# ('20190521', 'SS36131-tdTomGC6fopt', 'fly1', '004'),#axoid
# ('20190521', 'SS36131-tdTomGC6fopt', 'fly1', '005'),#axoid
# ('20190521', 'SS36131-tdTomGC6fopt', 'fly1', '006'),#axoid
# ('20190521', 'SS36131-tdTomGC6fopt', 'fly1', '007'),#axoid
# ('20190521', 'SS36131-tdTomGC6fopt', 'fly1', '008'),#axoid

# ('20190606', 'SS38624-tdTomGC6fopt', 'fly3', '001'),#axoid
# ('20190606', 'SS38624-tdTomGC6fopt', 'fly3', '002'),#axoid
# ('20190606', 'SS38624-tdTomGC6fopt', 'fly3', '003'),#axoid
# ('20190606', 'SS38624-tdTomGC6fopt', 'fly3', '004'),#axoid

# ('20190604', 'SS38631-tdTomGC6fopt', 'fly2', '001'),#axoid
# ('20190604', 'SS38631-tdTomGC6fopt', 'fly2', '002'),#axoid
# ('20190604', 'SS38631-tdTomGC6fopt', 'fly2', '003'),#axoid
# ('20190604', 'SS38631-tdTomGC6fopt', 'fly2', '004'),#axoid
# ('20190604', 'SS38631-tdTomGC6fopt', 'fly2', '005'),#axoid
# ('20190604', 'SS38631-tdTomGC6fopt', 'fly2', '006'),#axoid
# ('20190604', 'SS38631-tdTomGC6fopt', 'fly2', '007'),#axoid
# ('20190604', 'SS38631-tdTomGC6fopt', 'fly2', '008'),#axoid

# ('20190628', 'SS41815-tdTomGC6fopt', 'fly4', '001'),#axoid
# ('20190628', 'SS41815-tdTomGC6fopt', 'fly4', '002'),#axoid
# ('20190628', 'SS41815-tdTomGC6fopt', 'fly4', '003'),#axoid
# ('20190628', 'SS41815-tdTomGC6fopt', 'fly4', '004'),#axoid
# ('20190628', 'SS41815-tdTomGC6fopt', 'fly4', '005'),#axoid
# ('20190628', 'SS41815-tdTomGC6fopt', 'fly4', '006'),#axoid
# ('20190628', 'SS41815-tdTomGC6fopt', 'fly4', '007'),#axoid
# ('20190628', 'SS41815-tdTomGC6fopt', 'fly4', '008'),#axoid
# ('20190628', 'SS41815-tdTomGC6fopt', 'fly4', '009'),#axoid
# ('20190628', 'SS41815-tdTomGC6fopt', 'fly4', '010'),#axoid

# ('20190629', 'SS41815-tdTomGC6fopt', 'fly1', '001'),#axoid
# ('20190629', 'SS41815-tdTomGC6fopt', 'fly1', '002'),#axoid
# ('20190629', 'SS41815-tdTomGC6fopt', 'fly1', '003'),#axoid
# ('20190629', 'SS41815-tdTomGC6fopt', 'fly1', '004'),#axoid
# ('20190629', 'SS41815-tdTomGC6fopt', 'fly1', '005'),#axoid
# ('20190629', 'SS41815-tdTomGC6fopt', 'fly1', '006'),#axoid
# ('20190629', 'SS41815-tdTomGC6fopt', 'fly1', '007'),#axoid
# ('20190629', 'SS41815-tdTomGC6fopt', 'fly1', '008'),#axoid
# ('20190629', 'SS41815-tdTomGC6fopt', 'fly1', '009'),#axoid

# ('20190627', 'SS41815-tdTomGC6fopt', 'fly2', '001'),#axoid

# ('20190628', 'SS41815-tdTomGC6fopt', 'fly1', '001'),#axoid
# ('20190628', 'SS41815-tdTomGC6fopt', 'fly1', '002'),#axoid

# ('20190628', 'SS41815-tdTomGC6fopt', 'fly2', '001'),#axoid
# ('20190628', 'SS41815-tdTomGC6fopt', 'fly2', '002'),#axoid
# ('20190628', 'SS41815-tdTomGC6fopt', 'fly2', '003'),#axoid

# ('20190628', 'SS41815-tdTomGC6fopt', 'fly3', '001'),#axoid
# ('20190628', 'SS41815-tdTomGC6fopt', 'fly3', '002'),#axoid
# ('20190628', 'SS41815-tdTomGC6fopt', 'fly3', '003'),#axoid

# ('20190709', 'SS41815-tdTomGC6fopt', 'fly1', '001'),#axoid
# ('20190709', 'SS41815-tdTomGC6fopt', 'fly1', '002'),#axoid

# ('20190710', 'SS41815-tdTomGC6fopt', 'fly1', '001'),#axoid
# ('20190710', 'SS41815-tdTomGC6fopt', 'fly1', '002'),#axoid
# ('20190710', 'SS41815-tdTomGC6fopt', 'fly1', '003'),#axoid

# ('20190710', 'SS41815-tdTomGC6fopt', 'fly2', '001'),#axoid
# ('20190710', 'SS41815-tdTomGC6fopt', 'fly2', '002'),#axoid
# ('20190710', 'SS41815-tdTomGC6fopt', 'fly2', '003'),#axoid
# ('20190710', 'SS41815-tdTomGC6fopt', 'fly2', '004'),#axoid
# ('20190710', 'SS41815-tdTomGC6fopt', 'fly2', '005'),#axoid
# ('20190710', 'SS41815-tdTomGC6fopt', 'fly2', '006'),#axoid

# ('20190710', 'SS41815-tdTomGC6fopt', 'fly3', '001'),#axoid
# ('20190710', 'SS41815-tdTomGC6fopt', 'fly3', '002'),#axoid

# ('20190615', 'SS40134-tdTomGC6fopt', 'fly1', '001'),#axoid
# ('20190615', 'SS40134-tdTomGC6fopt', 'fly1', '002'),#axoid
# ('20190615', 'SS40134-tdTomGC6fopt', 'fly1', '003'),#axoid
# ('20190615', 'SS40134-tdTomGC6fopt', 'fly1', '004'),#axoid
# ('20190615', 'SS40134-tdTomGC6fopt', 'fly1', '005'),#axoid
# ('20190615', 'SS40134-tdTomGC6fopt', 'fly1', '006'),#axoid
# ('20190615', 'SS40134-tdTomGC6fopt', 'fly1', '007'),#axoid
# ('20190615', 'SS40134-tdTomGC6fopt', 'fly1', '008'),#axoid

# ('20190621', 'SS40619-tdTomGC6fopt', 'fly1', '001'),#axoid
# ('20190621', 'SS40619-tdTomGC6fopt', 'fly1', '002'),#axoid
# ('20190621', 'SS40619-tdTomGC6fopt', 'fly1', '003'),#axoid
# ('20190621', 'SS40619-tdTomGC6fopt', 'fly1', '004'),#axoid
# ('20190621', 'SS40619-tdTomGC6fopt', 'fly1', '005'),#axoid
# ('20190621', 'SS40619-tdTomGC6fopt', 'fly1', '006'),#axoid

# ('20190619', 'SS41605-tdTomGC6fopt', 'fly3', '001'),#axoid
# ('20190619', 'SS41605-tdTomGC6fopt', 'fly3', '002'),#axoid
# ('20190619', 'SS41605-tdTomGC6fopt', 'fly3', '003'),#axoid
# ('20190619', 'SS41605-tdTomGC6fopt', 'fly3', '004'),#axoid
# ('20190619', 'SS41605-tdTomGC6fopt', 'fly3', '005'),#axoid
# ('20190619', 'SS41605-tdTomGC6fopt', 'fly3', '006'),#axoid
# ('20190619', 'SS41605-tdTomGC6fopt', 'fly3', '007'),#axoid
# ('20190619', 'SS41605-tdTomGC6fopt', 'fly3', '008'),#axoid

# ('20190701', 'SS42008-tdTomGC6fopt', 'fly4', '001'),#axoid
# ('20190701', 'SS42008-tdTomGC6fopt', 'fly4', '002'),#axoid
# ('20190701', 'SS42008-tdTomGC6fopt', 'fly4', '003'),#axoid
# ('20190701', 'SS42008-tdTomGC6fopt', 'fly4', '004'),#axoid
# ('20190701', 'SS42008-tdTomGC6fopt', 'fly4', '005'),#axoid
# ('20190701', 'SS42008-tdTomGC6fopt', 'fly4', '006'),#axoid

# ('20190703', 'SS42740-tdTomGC6fopt', 'fly1', '001'),#axoid
# ('20190703', 'SS42740-tdTomGC6fopt', 'fly1', '002'),#axoid
# ('20190703', 'SS42740-tdTomGC6fopt', 'fly1', '003'),#axoid
# ('20190703', 'SS42740-tdTomGC6fopt', 'fly1', '004'),#axoid
# ('20190703', 'SS42740-tdTomGC6fopt', 'fly1', '005'),#axoid
# ('20190703', 'SS42740-tdTomGC6fopt', 'fly1', '006'),#axoid

# ('20190703', 'SS42740-tdTomGC6fopt', 'fly2', '001'),#axoid
# ('20190703', 'SS42740-tdTomGC6fopt', 'fly2', '002'),#axoid
# ('20190703', 'SS42740-tdTomGC6fopt', 'fly2', '003'),#axoid
# ('20190703', 'SS42740-tdTomGC6fopt', 'fly2', '004'),#axoid
# ('20190703', 'SS42740-tdTomGC6fopt', 'fly2', '005'),#axoid
# ('20190703', 'SS42740-tdTomGC6fopt', 'fly2', '006'),#axoid
# ('20190703', 'SS42740-tdTomGC6fopt', 'fly2', '007'),#axoid
# ('20190703', 'SS42740-tdTomGC6fopt', 'fly2', '008'),#axoid
# ('20190703', 'SS42740-tdTomGC6fopt', 'fly2', '009'),#axoid
# ('20190703', 'SS42740-tdTomGC6fopt', 'fly2', '010'),#axoid
# ('20190703', 'SS42740-tdTomGC6fopt', 'fly2', '011'),#axoid
# ('20190703', 'SS42740-tdTomGC6fopt', 'fly2', '012'),#axoid
# ('20190703', 'SS42740-tdTomGC6fopt', 'fly2', '013'),#axoid

# ('20190723', 'SS45363-tdTomGC6fopt', 'fly1', '001'),#axoid
# ('20190723', 'SS45363-tdTomGC6fopt', 'fly1', '002'),#axoid
# ('20190723', 'SS45363-tdTomGC6fopt', 'fly1', '003'),#axoid
# ('20190723', 'SS45363-tdTomGC6fopt', 'fly1', '004'),#axoid
# ('20190723', 'SS45363-tdTomGC6fopt', 'fly1', '005'),#axoid
# ('20190723', 'SS45363-tdTomGC6fopt', 'fly1', '006'),#axoid
# ('20190723', 'SS45363-tdTomGC6fopt', 'fly1', '007'),#axoid
# ('20190723', 'SS45363-tdTomGC6fopt', 'fly1', '008'),#axoid
# ('20190723', 'SS45363-tdTomGC6fopt', 'fly1', '009'),#axoid
# ('20190723', 'SS45363-tdTomGC6fopt', 'fly1', '010'),#axoid
# ('20190723', 'SS45363-tdTomGC6fopt', 'fly1', '011'),#axoid
# ('20190723', 'SS45363-tdTomGC6fopt', 'fly1', '012'),#axoid
# ('20190723', 'SS45363-tdTomGC6fopt', 'fly1', '013'),#axoid
# ('20190723', 'SS45363-tdTomGC6fopt', 'fly1', '014'),#axoid
# ('20190723', 'SS45363-tdTomGC6fopt', 'fly1', '015'),#axoid
# ('20190723', 'SS45363-tdTomGC6fopt', 'fly1', '016'),#axoid
# ('20190723', 'SS45363-tdTomGC6fopt', 'fly1', '017'),#axoid
# ('20190723', 'SS45363-tdTomGC6fopt', 'fly1', '018'),#axoid

# ('20190704', 'SS42749-tdTomGC6fopt', 'fly1', '001'),#axoid
# ('20190704', 'SS42749-tdTomGC6fopt', 'fly1', '002'),#axoid
# ('20190704', 'SS42749-tdTomGC6fopt', 'fly1', '003'),#axoid
# ('20190704', 'SS42749-tdTomGC6fopt', 'fly1', '004'),#axoid
# ('20190704', 'SS42749-tdTomGC6fopt', 'fly1', '005'),#axoid
# ('20190704', 'SS42749-tdTomGC6fopt', 'fly1', '006'),#axoid
# ('20190704', 'SS42749-tdTomGC6fopt', 'fly1', '007'),#axoid
# ('20190704', 'SS42749-tdTomGC6fopt', 'fly1', '008'),#axoid

# ('20190704', 'SS42749-tdTomGC6fopt', 'fly3', '001'),#axoid
# ('20190704', 'SS42749-tdTomGC6fopt', 'fly3', '002'),#axoid
# ('20190704', 'SS42749-tdTomGC6fopt', 'fly3', '003'),#axoid
# ('20190704', 'SS42749-tdTomGC6fopt', 'fly3', '004'),#axoid
# ('20190704', 'SS42749-tdTomGC6fopt', 'fly3', '005'),#axoid
# ('20190704', 'SS42749-tdTomGC6fopt', 'fly3', '006'),#axoid
# ('20190704', 'SS42749-tdTomGC6fopt', 'fly3', '007'),#axoid
# ('20190704', 'SS42749-tdTomGC6fopt', 'fly3', '008'),#axoid
# ('20190704', 'SS42749-tdTomGC6fopt', 'fly3', '009'),#axoid
# ('20190704', 'SS42749-tdTomGC6fopt', 'fly3', '010'),#axoid

# ('20190704', 'SS42749-tdTomGC6fopt', 'fly2', '001'),#axoid

# ('20190704', 'SS42749-tdTomGC6fopt', 'fly5', '001'),#axoid
# ('20190704', 'SS42749-tdTomGC6fopt', 'fly5', '002'),#axoid

# ('20190924', 'SS51021-tdTomGC6fopt', 'fly1', '001'),
# ('20190924', 'SS51021-tdTomGC6fopt', 'fly1', '002'),
# ('20190924', 'SS51021-tdTomGC6fopt', 'fly1', '003'),
# ('20190924', 'SS51021-tdTomGC6fopt', 'fly1', '004'),
# ('20190924', 'SS51021-tdTomGC6fopt', 'fly1', '005'),
# ('20190924', 'SS51021-tdTomGC6fopt', 'fly1', '006'),

# ('20190906', 'SS51029-tdTomGC6fopt', 'fly4', '001'),
# ('20190906', 'SS51029-tdTomGC6fopt', 'fly4', '002'),
# ('20190906', 'SS51029-tdTomGC6fopt', 'fly4', '003'),
# ('20190906', 'SS51029-tdTomGC6fopt', 'fly4', '004'),
# ('20190906', 'SS51029-tdTomGC6fopt', 'fly4', '005'),
# ('20190906', 'SS51029-tdTomGC6fopt', 'fly4', '006'),
# ('20190906', 'SS51029-tdTomGC6fopt', 'fly4', '007'),

# ('20190910', 'SS51038-tdTomGC6fopt', 'fly1', '001'),
# ('20190910', 'SS51038-tdTomGC6fopt', 'fly1', '002'),
# ('20190910', 'SS51038-tdTomGC6fopt', 'fly1', '003'),
# ('20190910', 'SS51038-tdTomGC6fopt', 'fly1', '004'),
# ('20190910', 'SS51038-tdTomGC6fopt', 'fly1', '005'), #hind leg GC event
# ('20190910', 'SS51038-tdTomGC6fopt', 'fly1', '006'),
# ('20190910', 'SS51038-tdTomGC6fopt', 'fly1', '007'),
# ('20190910', 'SS51038-tdTomGC6fopt', 'fly1', '008'),
# ('20190910', 'SS51038-tdTomGC6fopt', 'fly1', '009'),

# ('20190926', 'SS51046-tdTomGC6fopt', 'fly2', '001'),
# ('20190926', 'SS51046-tdTomGC6fopt', 'fly2', '002'),
# ('20190926', 'SS51046-tdTomGC6fopt', 'fly2', '003'),
# ('20190926', 'SS51046-tdTomGC6fopt', 'fly2', '004'),
# ('20190926', 'SS51046-tdTomGC6fopt', 'fly2', '005'),
# ('20190926', 'SS51046-tdTomGC6fopt', 'fly2', '006'),
# ('20190926', 'SS51046-tdTomGC6fopt', 'fly2', '007'),
# ('20190926', 'SS51046-tdTomGC6fopt', 'fly2', '008'),
# ('20190926', 'SS51046-tdTomGC6fopt', 'fly2', '009'),
# ('20190926', 'SS51046-tdTomGC6fopt', 'fly2', '010'),
# ('20190926', 'SS51046-tdTomGC6fopt', 'fly2', '011'),

# ('20191002', 'SS51046-tdTomGC6fopt', 'fly1', '001'),
# ('20191002', 'SS51046-tdTomGC6fopt', 'fly1', '002'),
# ('20191002', 'SS51046-tdTomGC6fopt', 'fly1', '003'),
# ('20191002', 'SS51046-tdTomGC6fopt', 'fly1', '004'),
# ('20191002', 'SS51046-tdTomGC6fopt', 'fly1', '005'),
# ('20191002', 'SS51046-tdTomGC6fopt', 'fly1', '006'),
# ('20191002', 'SS51046-tdTomGC6fopt', 'fly1', '007'),
# ('20191002', 'SS51046-tdTomGC6fopt', 'fly1', '008'),
# ('20191002', 'SS51046-tdTomGC6fopt', 'fly1', '009'),

# ('20190918', 'SS52147-tdTomGC6fopt', 'fly1', '001'),
# ('20190918', 'SS52147-tdTomGC6fopt', 'fly1', '002'),
# ('20190918', 'SS52147-tdTomGC6fopt', 'fly1', '003'),
# ('20190918', 'SS52147-tdTomGC6fopt', 'fly1', '004'),
# ('20190918', 'SS52147-tdTomGC6fopt', 'fly1', '005'),
# ('20190918', 'SS52147-tdTomGC6fopt', 'fly1', '006'),
# ('20190918', 'SS52147-tdTomGC6fopt', 'fly1', '007'),
# ('20190918', 'SS52147-tdTomGC6fopt', 'fly1', '008'),
# ('20190918', 'SS52147-tdTomGC6fopt', 'fly1', '009'),
# ('20190918', 'SS52147-tdTomGC6fopt', 'fly1', '010'),
# ('20190918', 'SS52147-tdTomGC6fopt', 'fly1', '011'),
# ('20190918', 'SS52147-tdTomGC6fopt', 'fly1', '012'),
# ('20190918', 'SS52147-tdTomGC6fopt', 'fly1', '013'),
# ('20190918', 'SS52147-tdTomGC6fopt', 'fly1', '014'),
# ('20190918', 'SS52147-tdTomGC6fopt', 'fly1', '015'),


# ('20190610', 'SS40489-tdTomGC6fopt', 'fly3', '002'),
# ('20190610', 'SS40489-tdTomGC6fopt', 'fly3', '003'),
# ('20190610', 'SS40489-tdTomGC6fopt', 'fly3', '004'),
# ('20190610', 'SS40489-tdTomGC6fopt', 'fly3', '005'),
# ('20190610', 'SS40489-tdTomGC6fopt', 'fly3', '006'),

# ('20190625', 'SS41806-tdTomGC6fopt', 'fly4', '001'),
# ('20190625', 'SS41806-tdTomGC6fopt', 'fly4', '002'),
# ('20190625', 'SS41806-tdTomGC6fopt', 'fly4', '003'),
# ('20190625', 'SS41806-tdTomGC6fopt', 'fly4', '004'),
# ('20190625', 'SS41806-tdTomGC6fopt', 'fly4', '005'),
# ('20190625', 'SS41806-tdTomGC6fopt', 'fly4', '006'),
# ('20190625', 'SS41806-tdTomGC6fopt', 'fly4', '007'),

# ('20180822', 'SS25451-tdTomGC6fopt', 'fly4', '002'),
# ('20180822', 'SS25451-tdTomGC6fopt', 'fly4', '009'),
# ('20180822', 'SS25451-tdTomGC6fopt', 'fly4', '010'), 
# ('20180822', 'SS25451-tdTomGC6fopt', 'fly4', '011'),
# ('20180822', 'SS25451-tdTomGC6fopt', 'fly4', '012'),
# ('20180822', 'SS25451-tdTomGC6fopt', 'fly4', '013'),
# ('20180822', 'SS25451-tdTomGC6fopt', 'fly4', '014'),
# ('20180822', 'SS25451-tdTomGC6fopt', 'fly4', '015'),
# ('20180822', 'SS25451-tdTomGC6fopt', 'fly4', '017'),

# ('20190719', 'SS45605-tdTomGC6fopt', 'fly1', '002'),
# ('20190719', 'SS45605-tdTomGC6fopt', 'fly1', '003'),
# ('20190719', 'SS45605-tdTomGC6fopt', 'fly1', '004'),
# ('20190719', 'SS45605-tdTomGC6fopt', 'fly1', '006'),
# ('20190719', 'SS45605-tdTomGC6fopt', 'fly1', '007'),

# ('20190221', 'SS29579-tdTomGC6fopt', 'fly1', '001'),
# ('20190221', 'SS29579-tdTomGC6fopt', 'fly1', '002'),
# ('20190221', 'SS29579-tdTomGC6fopt', 'fly1', '003'),
# ('20190221', 'SS29579-tdTomGC6fopt', 'fly1', '004'),
# ('20190221', 'SS29579-tdTomGC6fopt', 'fly1', '005'),
# ('20190221', 'SS29579-tdTomGC6fopt', 'fly1', '006'),
# ('20190221', 'SS29579-tdTomGC6fopt', 'fly1', '007'),
# ('20190221', 'SS29579-tdTomGC6fopt', 'fly1', '008'),
# ('20190221', 'SS29579-tdTomGC6fopt', 'fly1', '009'),

# ('20190717', 'SS44270-tdTomGC6fopt', 'fly1', '001'),
# ('20190717', 'SS44270-tdTomGC6fopt', 'fly1', '002'),
# ('20190717', 'SS44270-tdTomGC6fopt', 'fly1', '003'),
# ('20190717', 'SS44270-tdTomGC6fopt', 'fly1', '004'),
# ('20190717', 'SS44270-tdTomGC6fopt', 'fly1', '005'),

# ('20190730', 'SS46233-tdTomGC6fopt', 'fly2', '001'),
# ('20190730', 'SS46233-tdTomGC6fopt', 'fly2', '002'),
# ('20190730', 'SS46233-tdTomGC6fopt', 'fly2', '005'),

# ('20191001', 'SS49172-tdTomGC6fopt', 'fly1', '001'),
# ('20191001', 'SS49172-tdTomGC6fopt', 'fly1', '002'),
# ('20191001', 'SS49172-tdTomGC6fopt', 'fly1', '003'),
# ('20191001', 'SS49172-tdTomGC6fopt', 'fly1', '004'),
# ('20191001', 'SS49172-tdTomGC6fopt', 'fly1', '005'),
# ('20191001', 'SS49172-tdTomGC6fopt', 'fly1', '006'),
# ('20191001', 'SS49172-tdTomGC6fopt', 'fly1', '007'),
# ('20191001', 'SS49172-tdTomGC6fopt', 'fly1', '008'),

# ('20190712', 'SS43652-tdTomGC6fopt', 'fly2', '001'),
# ('20190712', 'SS43652-tdTomGC6fopt', 'fly2', '002'),
# ('20190712', 'SS43652-tdTomGC6fopt', 'fly2', '003'),

# ('20190531', 'SS38592-tdTomGC6fopt', 'fly3', '002'),#axoid
# ('20190531', 'SS38592-tdTomGC6fopt', 'fly3', '003'),#axoid
# ('20190531', 'SS38592-tdTomGC6fopt', 'fly3', '004'),#axoid
# ('20190531', 'SS38592-tdTomGC6fopt', 'fly3', '005'),#axoid
# ('20190531', 'SS38592-tdTomGC6fopt', 'fly3', '006'),#axoid
# ('20190531', 'SS38592-tdTomGC6fopt', 'fly3', '007'),#axoid

# ('20190904', 'SS51017-tdTomGC6fopt', 'fly3', '001'),
# ('20190904', 'SS51017-tdTomGC6fopt', 'fly3', '002'),
# ('20190904', 'SS51017-tdTomGC6fopt', 'fly3', '003'),
# ('20190904', 'SS51017-tdTomGC6fopt', 'fly3', '004'),
# ('20190904', 'SS51017-tdTomGC6fopt', 'fly3', '005'),
# ('20190904', 'SS51017-tdTomGC6fopt', 'fly3', '007'),
# ('20190904', 'SS51017-tdTomGC6fopt', 'fly3', '008'),


# ('20190326', 'SS28596-tdTomGC6fopt', 'fly2', '001'),#axoid
# ('20190326', 'SS28596-tdTomGC6fopt', 'fly2', '002'),#axoid
# ('20190326', 'SS28596-tdTomGC6fopt', 'fly2', '003'),#axoid
# ('20190326', 'SS28596-tdTomGC6fopt', 'fly2', '004'),#axoid
# ('20190326', 'SS28596-tdTomGC6fopt', 'fly2', '005'),#axoid
# ('20190326', 'SS28596-tdTomGC6fopt', 'fly2', '006'),#axoid
# ('20190326', 'SS28596-tdTomGC6fopt', 'fly2', '007'),#axoid
# ('20190326', 'SS28596-tdTomGC6fopt', 'fly2', '008'),#axoid

# ('20190723', 'SS45363-tdTomGC6fopt', 'fly1', '001'),#axoid
# ('20190723', 'SS45363-tdTomGC6fopt', 'fly1', '002'),#axoid
# ('20190723', 'SS45363-tdTomGC6fopt', 'fly1', '003'),#axoid
# ('20190723', 'SS45363-tdTomGC6fopt', 'fly1', '007'),#axoid
# ('20190723', 'SS45363-tdTomGC6fopt', 'fly1', '008'),#axoid
# ('20190723', 'SS45363-tdTomGC6fopt', 'fly1', '009'),#axoid
# ('20190723', 'SS45363-tdTomGC6fopt', 'fly1', '010'),#axoid
# ('20190723', 'SS45363-tdTomGC6fopt', 'fly1', '011'),#axoid
# ('20190723', 'SS45363-tdTomGC6fopt', 'fly1', '012'),#axoid
# ('20190723', 'SS45363-tdTomGC6fopt', 'fly1', '013'),#axoid
# ('20190723', 'SS45363-tdTomGC6fopt', 'fly1', '014'),#axoid
# ('20190723', 'SS45363-tdTomGC6fopt', 'fly1', '015'),#axoid
# ('20190723', 'SS45363-tdTomGC6fopt', 'fly1', '016'),#axoid
# ('20190723', 'SS45363-tdTomGC6fopt', 'fly1', '017'),#axoid
# ('20190723', 'SS45363-tdTomGC6fopt', 'fly1', '018'),#axoid

# ('20180720', 'MAN-tdTomGC6fopt', 'fly2', '001'), #UsrCorrected
# ('20180720', 'MAN-tdTomGC6fopt', 'fly2', '002'), #UsrCorrected
# ('20180720', 'MAN-tdTomGC6fopt', 'fly2', '003'), #UsrCorrected
# ('20180720', 'MAN-tdTomGC6fopt', 'fly2', '004'),
# ('20180720', 'MAN-tdTomGC6fopt', 'fly2', '005'),
# ('20180720', 'MAN-tdTomGC6fopt', 'fly2', '006'),
# ('20180720', 'MAN-tdTomGC6fopt', 'fly2', '007'),

# ('20181226', 'R15E08-tdTomGC6fopt', 'fly1', '001'),#axoid
# ('20181226', 'R15E08-tdTomGC6fopt', 'fly1', '002'),#axoid
# ('20181226', 'R15E08-tdTomGC6fopt', 'fly1', '008'),#axoid
# ('20181226', 'R15E08-tdTomGC6fopt', 'fly1', '009'),#axoid
# ('20181226', 'R15E08-tdTomGC6fopt', 'fly1', '011'),#axoid



('20190105', 'R39G01-tdTomGC6fopt', 'fly1', '001'),
# ('20190105', 'R39G01-tdTomGC6fopt', 'fly1', '002'),
# ('20190105', 'R39G01-tdTomGC6fopt', 'fly1', '003'),
# ('20190105', 'R39G01-tdTomGC6fopt', 'fly1', '004'),
# ('20190105', 'R39G01-tdTomGC6fopt', 'fly1', '005'),
# ('20190105', 'R39G01-tdTomGC6fopt', 'fly1', '006'),
# ('20190105', 'R39G01-tdTomGC6fopt', 'fly1', '007'),

# ('20190118', 'R69H10-tdTomGC6fopt', 'fly2', '001'),
# ('20190118', 'R69H10-tdTomGC6fopt', 'fly2', '003'),
# ('20190118', 'R69H10-tdTomGC6fopt', 'fly2', '004'),
# ('20190118', 'R69H10-tdTomGC6fopt', 'fly2', '005'),
# ('20190118', 'R69H10-tdTomGC6fopt', 'fly2', '006'),
# ('20190118', 'R69H10-tdTomGC6fopt', 'fly2', '007'),
# ('20190118', 'R69H10-tdTomGC6fopt', 'fly2', '008'),
# ('20190118', 'R69H10-tdTomGC6fopt', 'fly2', '009'),

# ('20181227', 'R87H02-tdTomGC6fopt', 'fly3', '001'),
# ('20181227', 'R87H02-tdTomGC6fopt', 'fly3', '002'),
# ('20181227', 'R87H02-tdTomGC6fopt', 'fly3', '003'),
# ('20181227', 'R87H02-tdTomGC6fopt', 'fly3', '004'),
# ('20181227', 'R87H02-tdTomGC6fopt', 'fly3', '005'),
# ('20181227', 'R87H02-tdTomGC6fopt', 'fly3', '006'),
# ('20181227', 'R87H02-tdTomGC6fopt', 'fly3', '007'),

# ('20190624', 'SS41822-tdTomGC6fopt', 'fly2', '001'),
# ('20190624', 'SS41822-tdTomGC6fopt', 'fly2', '002'),
# ('20190624', 'SS41822-tdTomGC6fopt', 'fly2', '003'),
# ('20190624', 'SS41822-tdTomGC6fopt', 'fly2', '004'),
# ('20190624', 'SS41822-tdTomGC6fopt', 'fly2', '005'),
# ('20190624', 'SS41822-tdTomGC6fopt', 'fly2', '006'),

]



NAS_Dir='/mnt/data/CLC/'
NAS_AN_Proj_Dir=NAS_Dir+'Ascending_Project/'

AN_Proj_Dir = NAS_AN_Proj_Dir


#for date, genotype, fly, recrd_num, CamStartFrame, CamStopFrame in rawdatalist:
for date, genotype, fly, recrd_num in rawdatalist:


	Gal4=genotype.split('-')[0]
	fly_beh=fly[0].upper()+fly[1:]


	foroutDirtemp=AN_Proj_Dir+Gal4+'/2P/'+date+'/'+genotype+'-'+fly+'/'+genotype+'-'+fly+'-'+recrd_num
	outputDir = foroutDirtemp+'/output/'

	PER_h5_Dir= outputDir + 'dlc/PER/camera_6/'
	input_Dir=NAS_Dir+date[2:]+'_'+genotype+'/'+fly_beh+'/CO2xzGG/behData_'+recrd_num+'/images/'

	if os.path.exists(input_Dir+'camera_6_img_7439.jpg'):
		print(input_Dir+' exists!')
	else:
		print(input_Dir+"camera_6_img_7439.jpg doesn't exists!")
		#sys.exit(0)

print('\n*** Input files all exists!! ***\n')
#sys.exit(0)




#count_photo=0
for date, genotype, fly, recrd_num in rawdatalist:
#for date, genotype, fly, recrd_num in experiments:
	

	Gal4=genotype.split('-')[0]
	fly_beh=fly[0].upper()+fly[1:]

	foroutDirtemp=AN_Proj_Dir+Gal4+'/2P/'+date+'/'+genotype+'-'+fly+'/'+genotype+'-'+fly+'-'+recrd_num
	outputDir = foroutDirtemp+'/output/'

	PER_h5_Dir= outputDir + 'dlc/PER/camera_6/'

	input_Dir=NAS_Dir+date[2:]+'_'+genotype+'/'+fly_beh+'/CO2xzGG/behData_'+recrd_num+'/images/'

	filename = date[2:]+'_'+genotype+'-'+fly+'-'+recrd_num+'_camera_'+str(video_cam)
	print('filename', filename)

	output_Dir = PER_h5_Dir

	#output_Dir = '/Users/clc/Documents/EPFL/NeLy/Data/ANproj/'+date_genotype+'/'+Fly_num+'/'+CO2xzGG+'/'+recrd_num+'/'+'OptFlowData/'

	print('output_Dir', output_Dir)

	if not os.path.exists(output_Dir):
		print(output_Dir)
		os.makedirs(output_Dir)



	#for i in range(CamStartFrame, CamStopFrame+1):
	#for i in range(0, 30):
		#currentPhoto='camera_'+str(video_cam)+'_img_'+str(i)+'.jpg'
		#shutil.copyfile(filepath+currentPhoto, output_Dir+currentPhoto)
		#count_photo+=1

	#sys.exit(0)

	os.chdir(input_Dir)
	
	#os.system('/usr/local/Cellar/ffmpeg -r 30 -start_number 0 -i %d.jpg -vcodec libx264 -vf format=yuv420p -crf 0 output.mp4')
	#os.system('ffmpeg -y -r 30 -start_number 0 -i '+'camera_'+str(video_cam)+'_img_%d.jpg -vcodec libx264 -pix_fmt yuv420p -crf 10 '+filename+'.mp4')
	os.system('ffmpeg -y -r 30 -start_number 0 -i '+'camera_'+str(video_cam)+'_img_%d.jpg -vcodec libx264 -pix_fmt yuv420p -crf 20 '+filename+'.mp4')
	os.system('cp -r '+ input_Dir+filename+'.mp4' + ' ' + output_Dir) # need to change into /mnt/


#output_Dir='/Users/clc/Documents/EPFL/NeLy/Data/ANproj/dlc/training_frames/'

#os.chdir(output_Dir)
#os.system('/usr/local/Cellar/ffmpeg -r 30 -start_number 0 -i %d.jpg -vcodec libx264 -vf format=yuv420p -crf 0 output.mp4')
#os.system('ffmpeg -y -r 30 -start_number 0 -i %d.jpg -vcodec libx264 -pix_fmt yuv420p -crf 10 output.mp4')
















