# project-housing

To Do:

1. Filter the EPC data by postcode start. - DONE
2. Clean both datasets and ensure data types align. - DO PROPERLY
3. Create an "Address" co -> DONE
4. Match on Address and identify records not matched.  - FUZZY MATCED
5. EDA: Explore General Statistics to add to commentary
6. Create Train/Test Spit
7. Build SLR and XGBoost models + EVALUATE + SAVE MODELS
8. Build Agentic Models + EVALUATE + SAVE MODELS
9. Optimise & Tune Further. 
10. Final Conclusions. 


Important:
- Discuss the fuzzy match threshold and calculate some error rates with random sampling. Establish WHY you arrived at 85% being optimal...

Merged Data Dictionary (118 Columns):

Unnamed: 0
unique_id - Not needed (better to de-identify)
price_paid
deed_date - Date of sale??
postcode - Remove
property_type - Important: Encode
new_build - Delete (as only NON new builds)
estate_type - Delete (as only freehold)
saon - remove
paon - remove
street - remove
locality - Maybe keep for experimentations?
town - Maybe Keep Instead of locality?
district - Maybe Keep?
county - Maybe Keep 
transaction_category - Delete
linked_data_uri - Remove for de-identification
source_file_x - Remove for de-identification
combined_address_x 
ADDRESS_V1 - Remove?
fuzzy_match - Matched on
match_confidence - Important
LMK_KEY - Remove for de-identification
ADDRESS1 - Remove
ADDRESS2 - Remove
ADDRESS3 - Remove
POSTCODE - Remove
BUILDING_REFERENCE_NUMBER - Leave as identifier
CURRENT_ENERGY_RATING  - Encode
POTENTIAL_ENERGY_RATING
CURRENT_ENERGY_EFFICIENCY - Could use this instead of energy rating?
POTENTIAL_ENERGY_EFFICIENCY - ^
PROPERTY_TYPE - Encode
BUILT_FORM - Encode 
INSPECTION_DATE - Good for data "staleness"
LOCAL_AUTHORITY - Encode but could fall under the district or town cols.
CONSTITUENCY - Find our what but could encode?
COUNTY - Duplicate col. 
LODGEMENT_DATE - Remove
TRANSACTION_TYPE - Remove to reduce dimensions.
ENVIRONMENT_IMPACT_CURRENT
ENVIRONMENT_IMPACT_POTENTIAL
ENERGY_CONSUMPTION_CURRENT
ENERGY_CONSUMPTION_POTENTIAL
CO2_EMISSIONS_CURRENT
CO2_EMISS_CURR_PER_FLOOR_AREA
CO2_EMISSIONS_POTENTIAL
LIGHTING_COST_CURRENT
LIGHTING_COST_POTENTIAL
HEATING_COST_CURRENT
HEATING_COST_POTENTIAL
HOT_WATER_COST_CURRENT
HOT_WATER_COST_POTENTIAL
TOTAL_FLOOR_AREA
ENERGY_TARIFF - Keep for experimentation
MAINS_GAS_FLAG - Y/N so encode
FLOOR_LEVEL - Unclean so remove
FLAT_TOP_STOREY - Missing lots of data so remove
FLAT_STOREY_COUNT - Remove for this data (no flats included)
MAIN_HEATING_CONTROLS - What is this?
MULTI_GLAZE_PROPORTION - 
GLAZED_TYPE - remove as not clean
GLAZED_AREA - Could be good to see if it helps
EXTENSION_COUNT - Keep
NUMBER_HABITABLE_ROOMS
NUMBER_HEATED_ROOMS
LOW_ENERGY_LIGHTING - What does this mean? 
NUMBER_OPEN_FIREPLACES 
HOTWATER_DESCRIPTION - Remove as unclean? 
HOT_WATER_ENERGY_EFF - Encode and keep!
HOT_WATER_ENV_EFF - What is this?
FLOOR_DESCRIPTION - Remove as unclean
FLOOR_ENERGY_EFF - Mostly unavailable. See % first.
FLOOR_ENV_EFF - What is this?
WINDOWS_DESCRIPTION - Could be grouped then encoded?
WINDOWS_ENERGY_EFF - Might be better than the above
WINDOWS_ENV_EFF - What is this?
WALLS_DESCRIPTION - Unclean
WALLS_ENERGY_EFF - Better to use this
WALLS_ENV_EFF - What is this?
SECONDHEAT_DESCRIPTION - Turn this to a Y/N flag (if it has secondary heating or not)
SHEATING_ENERGY_EFF - Remove as no vlaue
SHEATING_ENV_EFF - Remove
ROOF_DESCRIPTION - Keep for AI input to test. 
ROOF_ENERGY_EFF 
ROOF_ENV_EFF - Re,pve
MAINHEAT_DESCRIPTION
MAINHEAT_ENERGY_EFF -
MAINHEAT_ENV_EFF - Remove
MAINHEATCONT_DESCRIPTION - What is this? 
MAINHEATC_ENERGY_EFF
MAINHEATC_ENV_EFF - Remove
LIGHTING_DESCRIPTION
LIGHTING_ENERGY_EFF
LIGHTING_ENV_EFF - Remove
MAIN_FUEL - Remove 
WIND_TURBINE_COUNT - Remove
HEAT_LOSS_CORRIDOR - Remove as mostly no data
UNHEATED_CORRIDOR_LENGTH
FLOOR_HEIGHT
PHOTO_SUPPLY - What is this?? 
SOLAR_WATER_HEATING_FLAG -  Y/N/NA
MECHANICAL_VENTILATION - clean and encode 
ADDRESS
LOCAL_AUTHORITY_LABEL - Remove
CONSTITUENCY_LABEL - Remove
POSTTOWN - Remove
CONSTRUCTION_AGE_BAND - Clean and encode
LODGEMENT_DATETIME - Remove?
TENURE - Important for owner ocupied etc status
FIXED_LIGHTING_OUTLETS_COUNT - Experiment with but not important
LOW_ENERGY_FIXED_LIGHT_COUNT - What is this?
UPRN - Remove?
UPRN_SOURCE - Remove
REPORT_TYPE - Remove
source_file_y - Remove
combined_address_y
_merge - Remove values were not matched ('left_only')