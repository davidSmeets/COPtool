## General tab ##


#type of sink ('Water', 'Air', 'Advanced')
sinkType = 'Air'

#type of source ('Water', 'Air', 'Advanced')
sourceType = 'Air'

#temperature of sink (Celcius) in case of sinkType water: also water return temperature
sinkTemp = 35
sinkTemp_return = 25

#temperature of source (Celsius)
sourceTemp = 7

#refrigerant ('r1233zd'	'r1234yf'	'r134a'	'r23'	'r236fa'	'r245fa'	'r290'	'r32'	'r404a'	'r407a'	'r407c'	'r410a'	'r438a'	'r449a'	'r452a'	'r455a'	'r507a'	'r508b'	'r513a'	'r600a'	'r717'	'r744')
refrigerant = 'r134a'

#capacity (kiloWatt), only to be used for SCOP calculation
capacity  = 10


## Advanced tab ##


#delta T source/evaporator (Kelvin), only to be used if sourceType = 'Advanced'
deltaT_sourceEvaporator = 6

#delta T sink/condensor (Kelvin), only to be used if sinkType = 'Advanced'
deltaT_sinkCondensor = 5

#delta T superheating in suction line (K), default value 5K
deltaT_superheatSuction = 5

#type of compressor ('Unknown', 'Screw', 'Scroll', 'Reciprocating', 'Centrifugal')
compressorType = 'Scroll'

#isentropic efficiency ('Estimate', 'Value', 'Do not include in calculation')
isentropicEfficiency = 'Estimate'
isentropicEfficiencyVal = 65            #(%) in case of 'Value'

#ideal pressure ratio (-), default value 3
idealPressureRatio = 3 

#motor efficiency
motorEfficiency = 85 #(%)


## SCOP tab ##


#climate profile ('Average', 'Warmer', 'Colder')
climateProfile = 'Average'

#Detailed source type ('Air/other', 'Ground (closed, vertical)', 'Ground (closed, horizontal)', 'Groundwater', 'Surface water - Lake', 'Surface water - River', 'Surface water - Sea')
detailedSourceType = 'Air/other'