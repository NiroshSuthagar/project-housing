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
