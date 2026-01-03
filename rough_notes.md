# Notes

district and county seem the same 

ID Cols:
Fuzzy Match, Match Confidence, Building Reference Number, combined_address_x, combimed_address_y

Qs:
Local Authority vs Constituency


# Data Type Conversions Needed:
DATE:
deed_date
INSPECTION_DATE

STR:
property_type 
town 
district
county
combined_address_x
fuzzy_match
CURRENT_ENERGY_RATING
POTENTIAL_ENERGY_RATING
PROPERTY_TYPE
BUILT_FORM
LOCAL_AUTHORITY
CONSTITUENCY
ENERGY_TARIFF
MAINS_GAS_FLAG
GLAZED_AREA
HOTWATER_DESCRIPTION
HOT_WATER_ENERGY_EFF
HOT_WATER_ENV_EFF
FLOOR_DESCRIPTION
WINDOWS_DESCRIPTION
WINDOWS_ENERGY_EFF
WINDOWS_ENV_EFF
WALLS_DESCRIPTION
WALLS_ENERGY_EFF
WALLS_ENV_EFF
ROOF_DESCRIPTION
ROOF_ENERGY_EFF
MAINHEAT_DESCRIPTION
MAINHEAT_ENERGY_EFF
MAINHEATCONT_DESCRIPTION
MAINHEATC_ENERGY_EFF
LIGHTING_DESCRIPTION
LIGHTING_ENERGY_EFF
SOLAR_WATER_HEATING_FLAG
MECHANICAL_VENTILATION
CONSTRUCTION_AGE_BAND
TENURE
combined_address_y
_merge


NA PERCENTAGE:
5% -> 8 Cols
6% -> 43 Cols
7% -> 56 Cols
8% -> 60 Cols
9% -> 60 Cols
10% -> 61 Cols

NA Fillers:
Look at imputing strategy. Median works best for skewed data!

For Skewed Data: 
- Fill with median

Core Features For Agentic Frameworks to focus on:
1HE_district
1HE_PROPERTY TYPE
1HE_BUILT_FORM
CORE_TOTAL_FLOOR_AREA
CORE_EXTENSION_COUNT
CORE_NUMBER_OF_HABITABLE_ROOMS

1HE Drop IMPORTANT:
- 1HE drops of one of the features is only important for Linear Models due to colinearity. XGBoost doesn't get impacted as much. SEE WHY and WRITE.

NEST STEPS: 
- Evaluate OpenAI preds for Batch 0. 
- Establish whether it's worth testing the rest or we do an early stop. 
- Try building the same but with RAG.
- Evaluate Advanced Models
- Write Up Methodlogy Section
- FINAL TWEAK FOR ALL MODELS AND RETEST! 

SQL Agent Prompt (FAIL):
    "AnalystAgent":
        """
        You're a critically thinking Data Analyst that provides helpful supporting information by creating SQL scripts with the following column names:
        '1HE_district', '1HE_CURRENT_ENERGY_RATING',
        '1HE_POTENTIAL_ENERGY_RATING', '1HE_PROPERTY_TYPE', '1HE_BUILT_FORM',
        '1HE_ENERGY_TARIFF', '1HE_MAINS_GAS_FLAG', '1HE_GLAZED_AREA',
        '1HE_HOT_WATER_ENERGY_EFF', '1HE_HOT_WATER_ENV_EFF',
        '1HE_WINDOWS_ENERGY_EFF', '1HE_WINDOWS_ENV_EFF', '1HE_WALLS_ENERGY_EFF',
        '1HE_WALLS_ENV_EFF', '1HE_ROOF_ENERGY_EFF', '1HE_MAINHEAT_ENERGY_EFF',
        '1HE_MAINHEATC_ENERGY_EFF', '1HE_LIGHTING_ENERGY_EFF',
        '1HE_MECHANICAL_VENTILATION', '1HE_TENURE', 'CORE_match_confidence',
        'CORE_BUILDING_REFERENCE_NUMBER', 'CORE_CURRENT_ENERGY_EFFICIENCY',
        'CORE_POTENTIAL_ENERGY_EFFICIENCY', 'CORE_ENVIRONMENT_IMPACT_CURRENT',
        'CORE_ENVIRONMENT_IMPACT_POTENTIAL', 'CORE_ENERGY_CONSUMPTION_CURRENT',
        'CORE_ENERGY_CONSUMPTION_POTENTIAL', 'CORE_CO2_EMISSIONS_CURRENT',
        'CORE_CO2_EMISS_CURR_PER_FLOOR_AREA', 'CORE_CO2_EMISSIONS_POTENTIAL',
        'CORE_LIGHTING_COST_CURRENT', 'CORE_LIGHTING_COST_POTENTIAL',
        'CORE_HEATING_COST_CURRENT', 'CORE_HEATING_COST_POTENTIAL',
        'CORE_HOT_WATER_COST_CURRENT', 'CORE_HOT_WATER_COST_POTENTIAL',
        'CORE_TOTAL_FLOOR_AREA', 'CORE_MULTI_GLAZE_PROPORTION',
        'CORE_EXTENSION_COUNT', 'CORE_NUMBER_HABITABLE_ROOMS',
        'CORE_NUMBER_HEATED_ROOMS', 'CORE_LOW_ENERGY_LIGHTING',
        'CORE_NUMBER_OPEN_FIREPLACES', 'TRANSACTION_PRICE'. 
        
        Don't use all the above, the most important ones are:
        1HE_district
        1HE_PROPERTY TYPE 
        1HE_BUILT_FORM 
        CORE_TOTAL_FLOOR_AREA 
        CORE_EXTENSION_COUNT 
        CORE_NUMBER_OF_HABITABLE_ROOMS
        
        
        Generate a single SQL Script that is simple and aggreate house prices and generate supporting data relating to the input JSON. 
        Remember the datapoint is not in the database so search for summary data on similar properties without being too restrictive.
        Check your SQL Script carefully!
        
        Output Format Guidance (ONE SCRIPT):
        SELECT <Criteria>
        FROM masterRAG 
        LIMIT 10

NEXT STEPS (FINAL DAY):

- Current Status: All three models are working with a performance score!! 
- Naive Model: Create loop to run on more chunks and track error metrics
	- 17min per chunk so 22 chunks in 6 hours.
	- Or do 10 chunks so 1000 records tested!  
- Advanced Model: Run overnight for 1h/chunk spread
	- Run 5 chunks so 500 records tested. 

- Experimentation runs: 
	- XG Boost: Run hyperparameter tuning and track error metrics/models.
		- Track as experiments 
	- Naive Model: Test at least 3 prompts.
		- Store results as experiements.
	- Advanced Model: 
		- Keep it the same but test chunk performance for 5-10 chunks? 
	













































