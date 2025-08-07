-- =====================================================
-- DUI Views Creation Script - Pure SQL Server
-- Generated on: 2025-08-07T04:32:19.898145
-- Execute this directly in SQL Server Management Studio
-- =====================================================

-- Drop existing views
IF OBJECT_ID('DUI.v_additionaloffense', 'V') IS NOT NULL DROP VIEW DUI.v_additionaloffense
IF OBJECT_ID('DUI.v_additionaloffense_with_caseoffenses', 'V') IS NOT NULL DROP VIEW DUI.v_additionaloffense_with_caseoffenses
IF OBJECT_ID('DUI.v_archivecases', 'V') IS NOT NULL DROP VIEW DUI.v_archivecases
IF OBJECT_ID('DUI.v_archivecases_with_caseheaders', 'V') IS NOT NULL DROP VIEW DUI.v_archivecases_with_caseheaders
IF OBJECT_ID('DUI.v_caseaddenda', 'V') IS NOT NULL DROP VIEW DUI.v_caseaddenda
IF OBJECT_ID('DUI.v_caseexpunged', 'V') IS NOT NULL DROP VIEW DUI.v_caseexpunged
IF OBJECT_ID('DUI.v_caseheaders', 'V') IS NOT NULL DROP VIEW DUI.v_caseheaders
IF OBJECT_ID('DUI.v_caseheaders_with_tbl_opt_status', 'V') IS NOT NULL DROP VIEW DUI.v_caseheaders_with_tbl_opt_status
IF OBJECT_ID('DUI.v_caseoffenses', 'V') IS NOT NULL DROP VIEW DUI.v_caseoffenses
IF OBJECT_ID('DUI.v_caseoffenses_with_caseheaders', 'V') IS NOT NULL DROP VIEW DUI.v_caseoffenses_with_caseheaders
IF OBJECT_ID('DUI.v_casereviewhistory', 'V') IS NOT NULL DROP VIEW DUI.v_casereviewhistory
IF OBJECT_ID('DUI.v_casesearchwarrant', 'V') IS NOT NULL DROP VIEW DUI.v_casesearchwarrant
IF OBJECT_ID('DUI.v_casesearchwarrantactivity', 'V') IS NOT NULL DROP VIEW DUI.v_casesearchwarrantactivity
IF OBJECT_ID('DUI.v_casesearchwarrantfile', 'V') IS NOT NULL DROP VIEW DUI.v_casesearchwarrantfile
IF OBJECT_ID('DUI.v_casevehiclepassengers', 'V') IS NOT NULL DROP VIEW DUI.v_casevehiclepassengers
IF OBJECT_ID('DUI.v_casevehiclepassengers_with_casevehicles', 'V') IS NOT NULL DROP VIEW DUI.v_casevehiclepassengers_with_casevehicles
IF OBJECT_ID('DUI.v_casevehicles', 'V') IS NOT NULL DROP VIEW DUI.v_casevehicles
IF OBJECT_ID('DUI.v_casevehicles_with_caseheaders', 'V') IS NOT NULL DROP VIEW DUI.v_casevehicles_with_caseheaders
IF OBJECT_ID('DUI.v_caseviolations', 'V') IS NOT NULL DROP VIEW DUI.v_caseviolations
IF OBJECT_ID('DUI.v_caseviolations_with_caseheaders', 'V') IS NOT NULL DROP VIEW DUI.v_caseviolations_with_caseheaders
IF OBJECT_ID('DUI.v_casewarrantform', 'V') IS NOT NULL DROP VIEW DUI.v_casewarrantform
IF OBJECT_ID('DUI.v_conditionreasonforstop', 'V') IS NOT NULL DROP VIEW DUI.v_conditionreasonforstop
IF OBJECT_ID('DUI.v_conditionreasonforstop_with_conditions', 'V') IS NOT NULL DROP VIEW DUI.v_conditionreasonforstop_with_conditions
IF OBJECT_ID('DUI.v_conditions', 'V') IS NOT NULL DROP VIEW DUI.v_conditions
IF OBJECT_ID('DUI.v_conditions_with_caseheaders', 'V') IS NOT NULL DROP VIEW DUI.v_conditions_with_caseheaders
IF OBJECT_ID('DUI.v_duireportrequest', 'V') IS NOT NULL DROP VIEW DUI.v_duireportrequest
IF OBJECT_ID('DUI.v_duireportrequest_with_caseheaders', 'V') IS NOT NULL DROP VIEW DUI.v_duireportrequest_with_caseheaders
IF OBJECT_ID('DUI.v_defendantadditionalinfo', 'V') IS NOT NULL DROP VIEW DUI.v_defendantadditionalinfo
IF OBJECT_ID('DUI.v_defendantadditionalinfo_with_defendants', 'V') IS NOT NULL DROP VIEW DUI.v_defendantadditionalinfo_with_defendants
IF OBJECT_ID('DUI.v_defendantaddresses', 'V') IS NOT NULL DROP VIEW DUI.v_defendantaddresses
IF OBJECT_ID('DUI.v_defendantaddresses_with_defendants', 'V') IS NOT NULL DROP VIEW DUI.v_defendantaddresses_with_defendants
IF OBJECT_ID('DUI.v_defendantemcontacts', 'V') IS NOT NULL DROP VIEW DUI.v_defendantemcontacts
IF OBJECT_ID('DUI.v_defendantemcontacts_with_defendants', 'V') IS NOT NULL DROP VIEW DUI.v_defendantemcontacts_with_defendants
IF OBJECT_ID('DUI.v_defendantinterview', 'V') IS NOT NULL DROP VIEW DUI.v_defendantinterview
IF OBJECT_ID('DUI.v_defendantinterview_with_defendants', 'V') IS NOT NULL DROP VIEW DUI.v_defendantinterview_with_defendants
IF OBJECT_ID('DUI.v_defendantinterviewquestions', 'V') IS NOT NULL DROP VIEW DUI.v_defendantinterviewquestions
IF OBJECT_ID('DUI.v_defendantinterviewquestions_with_defendantinterview', 'V') IS NOT NULL DROP VIEW DUI.v_defendantinterviewquestions_with_defendantinterview
IF OBJECT_ID('DUI.v_defendantobservations', 'V') IS NOT NULL DROP VIEW DUI.v_defendantobservations
IF OBJECT_ID('DUI.v_defendantobservations_with_defendants', 'V') IS NOT NULL DROP VIEW DUI.v_defendantobservations_with_defendants
IF OBJECT_ID('DUI.v_defendantoccupationaddress', 'V') IS NOT NULL DROP VIEW DUI.v_defendantoccupationaddress
IF OBJECT_ID('DUI.v_defendantoccupationaddress_with_tbl_opt_states', 'V') IS NOT NULL DROP VIEW DUI.v_defendantoccupationaddress_with_tbl_opt_states
IF OBJECT_ID('DUI.v_defendantstatement', 'V') IS NOT NULL DROP VIEW DUI.v_defendantstatement
IF OBJECT_ID('DUI.v_defendantstatement_with_defendants', 'V') IS NOT NULL DROP VIEW DUI.v_defendantstatement_with_defendants
IF OBJECT_ID('DUI.v_defendants', 'V') IS NOT NULL DROP VIEW DUI.v_defendants
IF OBJECT_ID('DUI.v_defendants_with_caseheaders', 'V') IS NOT NULL DROP VIEW DUI.v_defendants_with_caseheaders
IF OBJECT_ID('DUI.v_documents', 'V') IS NOT NULL DROP VIEW DUI.v_documents
IF OBJECT_ID('DUI.v_documents_with_tbl_opt_documentfiletypes', 'V') IS NOT NULL DROP VIEW DUI.v_documents_with_tbl_opt_documentfiletypes
IF OBJECT_ID('DUI.v_duicasenotetype', 'V') IS NOT NULL DROP VIEW DUI.v_duicasenotetype
IF OBJECT_ID('DUI.v_duicasenotetype_with_systempages', 'V') IS NOT NULL DROP VIEW DUI.v_duicasenotetype_with_systempages
IF OBJECT_ID('DUI.v_duicasenotes', 'V') IS NOT NULL DROP VIEW DUI.v_duicasenotes
IF OBJECT_ID('DUI.v_duicasenotes_with_caseheaders', 'V') IS NOT NULL DROP VIEW DUI.v_duicasenotes_with_caseheaders
IF OBJECT_ID('DUI.v_duicasetoxspec', 'V') IS NOT NULL DROP VIEW DUI.v_duicasetoxspec
IF OBJECT_ID('DUI.v_duitoxicologydrug', 'V') IS NOT NULL DROP VIEW DUI.v_duitoxicologydrug
IF OBJECT_ID('DUI.v_duitoxilyzerreport', 'V') IS NOT NULL DROP VIEW DUI.v_duitoxilyzerreport
IF OBJECT_ID('DUI.v_evidencedocuments', 'V') IS NOT NULL DROP VIEW DUI.v_evidencedocuments
IF OBJECT_ID('DUI.v_evidencedocuments_with_caseheaders', 'V') IS NOT NULL DROP VIEW DUI.v_evidencedocuments_with_caseheaders
IF OBJECT_ID('DUI.v_evidencerecordings', 'V') IS NOT NULL DROP VIEW DUI.v_evidencerecordings
IF OBJECT_ID('DUI.v_evidencerecordings_with_physicalevidence', 'V') IS NOT NULL DROP VIEW DUI.v_evidencerecordings_with_physicalevidence
IF OBJECT_ID('DUI.v_fstfingertonosetest', 'V') IS NOT NULL DROP VIEW DUI.v_fstfingertonosetest
IF OBJECT_ID('DUI.v_fstfingertonosetest_with_caseheaders', 'V') IS NOT NULL DROP VIEW DUI.v_fstfingertonosetest_with_caseheaders
IF OBJECT_ID('DUI.v_fsthandcoordination', 'V') IS NOT NULL DROP VIEW DUI.v_fsthandcoordination
IF OBJECT_ID('DUI.v_fsthandcoordination_with_caseheaders', 'V') IS NOT NULL DROP VIEW DUI.v_fsthandcoordination_with_caseheaders
IF OBJECT_ID('DUI.v_fsthgntest', 'V') IS NOT NULL DROP VIEW DUI.v_fsthgntest
IF OBJECT_ID('DUI.v_fsthgntest_with_caseheaders', 'V') IS NOT NULL DROP VIEW DUI.v_fsthgntest_with_caseheaders
IF OBJECT_ID('DUI.v_fstonelegstandtest', 'V') IS NOT NULL DROP VIEW DUI.v_fstonelegstandtest
IF OBJECT_ID('DUI.v_fstonelegstandtest_with_caseheaders', 'V') IS NOT NULL DROP VIEW DUI.v_fstonelegstandtest_with_caseheaders
IF OBJECT_ID('DUI.v_fstothertest', 'V') IS NOT NULL DROP VIEW DUI.v_fstothertest
IF OBJECT_ID('DUI.v_fstothertest_with_caseheaders', 'V') IS NOT NULL DROP VIEW DUI.v_fstothertest_with_caseheaders
IF OBJECT_ID('DUI.v_fstpalmpattest', 'V') IS NOT NULL DROP VIEW DUI.v_fstpalmpattest
IF OBJECT_ID('DUI.v_fstpalmpattest_with_caseheaders', 'V') IS NOT NULL DROP VIEW DUI.v_fstpalmpattest_with_caseheaders
IF OBJECT_ID('DUI.v_fstsupplementfingertonosetest', 'V') IS NOT NULL DROP VIEW DUI.v_fstsupplementfingertonosetest
IF OBJECT_ID('DUI.v_fstsupplementhgntest', 'V') IS NOT NULL DROP VIEW DUI.v_fstsupplementhgntest
IF OBJECT_ID('DUI.v_fstsupplementhandcoordination', 'V') IS NOT NULL DROP VIEW DUI.v_fstsupplementhandcoordination
IF OBJECT_ID('DUI.v_fstsupplementonelegstandtest', 'V') IS NOT NULL DROP VIEW DUI.v_fstsupplementonelegstandtest
IF OBJECT_ID('DUI.v_fstsupplementothertest', 'V') IS NOT NULL DROP VIEW DUI.v_fstsupplementothertest
IF OBJECT_ID('DUI.v_fstsupplementpalmpattest', 'V') IS NOT NULL DROP VIEW DUI.v_fstsupplementpalmpattest
IF OBJECT_ID('DUI.v_fstsupplementwalkandturntest', 'V') IS NOT NULL DROP VIEW DUI.v_fstsupplementwalkandturntest
IF OBJECT_ID('DUI.v_fstwalkandturntest', 'V') IS NOT NULL DROP VIEW DUI.v_fstwalkandturntest
IF OBJECT_ID('DUI.v_fstwalkandturntest_with_caseheaders', 'V') IS NOT NULL DROP VIEW DUI.v_fstwalkandturntest_with_caseheaders
IF OBJECT_ID('DUI.v_fieldsobrietytests', 'V') IS NOT NULL DROP VIEW DUI.v_fieldsobrietytests
IF OBJECT_ID('DUI.v_fieldsobrietytests_with_caseheaders', 'V') IS NOT NULL DROP VIEW DUI.v_fieldsobrietytests_with_caseheaders
IF OBJECT_ID('DUI.v_narrativeailogs', 'V') IS NOT NULL DROP VIEW DUI.v_narrativeailogs
IF OBJECT_ID('DUI.v_officerstepshifts', 'V') IS NOT NULL DROP VIEW DUI.v_officerstepshifts
IF OBJECT_ID('DUI.v_officerstepshifts_with_stepshifts', 'V') IS NOT NULL DROP VIEW DUI.v_officerstepshifts_with_stepshifts
IF OBJECT_ID('DUI.v_otherofficers', 'V') IS NOT NULL DROP VIEW DUI.v_otherofficers
IF OBJECT_ID('DUI.v_otherofficers_with_caseheaders', 'V') IS NOT NULL DROP VIEW DUI.v_otherofficers_with_caseheaders
IF OBJECT_ID('DUI.v_physicalevidence', 'V') IS NOT NULL DROP VIEW DUI.v_physicalevidence
IF OBJECT_ID('DUI.v_physicalevidence_with_caseheaders', 'V') IS NOT NULL DROP VIEW DUI.v_physicalevidence_with_caseheaders
IF OBJECT_ID('DUI.v_questionforai', 'V') IS NOT NULL DROP VIEW DUI.v_questionforai
IF OBJECT_ID('DUI.v_specimenbloodtest', 'V') IS NOT NULL DROP VIEW DUI.v_specimenbloodtest
IF OBJECT_ID('DUI.v_specimenbloodtest_with_specimenreport', 'V') IS NOT NULL DROP VIEW DUI.v_specimenbloodtest_with_specimenreport
IF OBJECT_ID('DUI.v_specimenbreathtest', 'V') IS NOT NULL DROP VIEW DUI.v_specimenbreathtest
IF OBJECT_ID('DUI.v_specimenbreathtest_with_specimenreport', 'V') IS NOT NULL DROP VIEW DUI.v_specimenbreathtest_with_specimenreport
IF OBJECT_ID('DUI.v_specimenreport', 'V') IS NOT NULL DROP VIEW DUI.v_specimenreport
IF OBJECT_ID('DUI.v_specimenreport_with_caseheaders', 'V') IS NOT NULL DROP VIEW DUI.v_specimenreport_with_caseheaders
IF OBJECT_ID('DUI.v_specimenurinetest', 'V') IS NOT NULL DROP VIEW DUI.v_specimenurinetest
IF OBJECT_ID('DUI.v_specimenurinetest_with_specimenreport', 'V') IS NOT NULL DROP VIEW DUI.v_specimenurinetest_with_specimenreport
IF OBJECT_ID('DUI.v_stepofficershiftcases', 'V') IS NOT NULL DROP VIEW DUI.v_stepofficershiftcases
IF OBJECT_ID('DUI.v_stepofficershiftcases_with_caseheaders', 'V') IS NOT NULL DROP VIEW DUI.v_stepofficershiftcases_with_caseheaders
IF OBJECT_ID('DUI.v_stepofficershiftzones', 'V') IS NOT NULL DROP VIEW DUI.v_stepofficershiftzones
IF OBJECT_ID('DUI.v_stepofficershiftzones_with_officerstepshifts', 'V') IS NOT NULL DROP VIEW DUI.v_stepofficershiftzones_with_officerstepshifts
IF OBJECT_ID('DUI.v_stepshifts', 'V') IS NOT NULL DROP VIEW DUI.v_stepshifts
IF OBJECT_ID('DUI.v_stepshifts_with_tbl_opt_step_grant_type', 'V') IS NOT NULL DROP VIEW DUI.v_stepshifts_with_tbl_opt_step_grant_type
IF OBJECT_ID('DUI.v_stepzones', 'V') IS NOT NULL DROP VIEW DUI.v_stepzones
IF OBJECT_ID('DUI.v_stepzones_with_tbl_opt_step_grant_type', 'V') IS NOT NULL DROP VIEW DUI.v_stepzones_with_tbl_opt_step_grant_type
IF OBJECT_ID('DUI.v_supplement', 'V') IS NOT NULL DROP VIEW DUI.v_supplement
IF OBJECT_ID('DUI.v_supplementdocuments', 'V') IS NOT NULL DROP VIEW DUI.v_supplementdocuments
IF OBJECT_ID('DUI.v_supplementdocuments_with_documents', 'V') IS NOT NULL DROP VIEW DUI.v_supplementdocuments_with_documents
IF OBJECT_ID('DUI.v_supplementfieldsobrietytests', 'V') IS NOT NULL DROP VIEW DUI.v_supplementfieldsobrietytests
IF OBJECT_ID('DUI.v_supplementintoxilyzerreport', 'V') IS NOT NULL DROP VIEW DUI.v_supplementintoxilyzerreport
IF OBJECT_ID('DUI.v_supplementwitnesses', 'V') IS NOT NULL DROP VIEW DUI.v_supplementwitnesses
IF OBJECT_ID('DUI.v_systemmodecontrols', 'V') IS NOT NULL DROP VIEW DUI.v_systemmodecontrols
IF OBJECT_ID('DUI.v_systemmodecontrols_with_systempages', 'V') IS NOT NULL DROP VIEW DUI.v_systemmodecontrols_with_systempages
IF OBJECT_ID('DUI.v_systempages', 'V') IS NOT NULL DROP VIEW DUI.v_systempages
IF OBJECT_ID('DUI.v_tabcnotificationlog', 'V') IS NOT NULL DROP VIEW DUI.v_tabcnotificationlog
IF OBJECT_ID('DUI.v_tbl_options_master', 'V') IS NOT NULL DROP VIEW DUI.v_tbl_options_master
IF OBJECT_ID('DUI.v_tbl_opt_accidents', 'V') IS NOT NULL DROP VIEW DUI.v_tbl_opt_accidents
IF OBJECT_ID('DUI.v_tbl_opt_activitytypes', 'V') IS NOT NULL DROP VIEW DUI.v_tbl_opt_activitytypes
IF OBJECT_ID('DUI.v_tbl_opt_addressgroup', 'V') IS NOT NULL DROP VIEW DUI.v_tbl_opt_addressgroup
IF OBJECT_ID('DUI.v_tbl_opt_alcoholtypes', 'V') IS NOT NULL DROP VIEW DUI.v_tbl_opt_alcoholtypes
IF OBJECT_ID('DUI.v_tbl_opt_bwi_motors', 'V') IS NOT NULL DROP VIEW DUI.v_tbl_opt_bwi_motors
IF OBJECT_ID('DUI.v_tbl_opt_bwi_vessels', 'V') IS NOT NULL DROP VIEW DUI.v_tbl_opt_bwi_vessels
IF OBJECT_ID('DUI.v_tbl_opt_bodywaters', 'V') IS NOT NULL DROP VIEW DUI.v_tbl_opt_bodywaters
IF OBJECT_ID('DUI.v_tbl_opt_case_outcome_dismissals', 'V') IS NOT NULL DROP VIEW DUI.v_tbl_opt_case_outcome_dismissals
IF OBJECT_ID('DUI.v_tbl_opt_case_outcome_pleas', 'V') IS NOT NULL DROP VIEW DUI.v_tbl_opt_case_outcome_pleas
IF OBJECT_ID('DUI.v_tbl_opt_case_outcome_trials', 'V') IS NOT NULL DROP VIEW DUI.v_tbl_opt_case_outcome_trials
IF OBJECT_ID('DUI.v_tbl_opt_counties', 'V') IS NOT NULL DROP VIEW DUI.v_tbl_opt_counties
IF OBJECT_ID('DUI.v_tbl_opt_dps_drugs', 'V') IS NOT NULL DROP VIEW DUI.v_tbl_opt_dps_drugs
IF OBJECT_ID('DUI.v_tbl_opt_dismissals', 'V') IS NOT NULL DROP VIEW DUI.v_tbl_opt_dismissals
IF OBJECT_ID('DUI.v_tbl_opt_documentfiletypes', 'V') IS NOT NULL DROP VIEW DUI.v_tbl_opt_documentfiletypes
IF OBJECT_ID('DUI.v_tbl_opt_documenttypes', 'V') IS NOT NULL DROP VIEW DUI.v_tbl_opt_documenttypes
IF OBJECT_ID('DUI.v_tbl_opt_educations', 'V') IS NOT NULL DROP VIEW DUI.v_tbl_opt_educations
IF OBJECT_ID('DUI.v_tbl_opt_employed_pwd', 'V') IS NOT NULL DROP VIEW DUI.v_tbl_opt_employed_pwd
IF OBJECT_ID('DUI.v_tbl_opt_ethnicity', 'V') IS NOT NULL DROP VIEW DUI.v_tbl_opt_ethnicity
IF OBJECT_ID('DUI.v_tbl_opt_eye_colors', 'V') IS NOT NULL DROP VIEW DUI.v_tbl_opt_eye_colors
IF OBJECT_ID('DUI.v_tbl_opt_foot_wear_types', 'V') IS NOT NULL DROP VIEW DUI.v_tbl_opt_foot_wear_types
IF OBJECT_ID('DUI.v_tbl_opt_genders', 'V') IS NOT NULL DROP VIEW DUI.v_tbl_opt_genders
IF OBJECT_ID('DUI.v_tbl_opt_hgn_estimated_angle', 'V') IS NOT NULL DROP VIEW DUI.v_tbl_opt_hgn_estimated_angle
IF OBJECT_ID('DUI.v_tbl_opt_hair_colors', 'V') IS NOT NULL DROP VIEW DUI.v_tbl_opt_hair_colors
IF OBJECT_ID('DUI.v_tbl_opt_intox_verifytemp', 'V') IS NOT NULL DROP VIEW DUI.v_tbl_opt_intox_verifytemp
IF OBJECT_ID('DUI.v_tbl_opt_injury', 'V') IS NOT NULL DROP VIEW DUI.v_tbl_opt_injury
IF OBJECT_ID('DUI.v_tbl_opt_integration_vendors', 'V') IS NOT NULL DROP VIEW DUI.v_tbl_opt_integration_vendors
IF OBJECT_ID('DUI.v_tbl_opt_interview_questions', 'V') IS NOT NULL DROP VIEW DUI.v_tbl_opt_interview_questions
IF OBJECT_ID('DUI.v_tbl_opt_light_conditions', 'V') IS NOT NULL DROP VIEW DUI.v_tbl_opt_light_conditions
IF OBJECT_ID('DUI.v_tbl_opt_mark43_lookup', 'V') IS NOT NULL DROP VIEW DUI.v_tbl_opt_mark43_lookup
IF OBJECT_ID('DUI.v_tbl_opt_more_less_intoxicated', 'V') IS NOT NULL DROP VIEW DUI.v_tbl_opt_more_less_intoxicated
IF OBJECT_ID('DUI.v_tbl_opt_ncic_colors', 'V') IS NOT NULL DROP VIEW DUI.v_tbl_opt_ncic_colors
IF OBJECT_ID('DUI.v_tbl_opt_ncic_instructions', 'V') IS NOT NULL DROP VIEW DUI.v_tbl_opt_ncic_instructions
IF OBJECT_ID('DUI.v_tbl_opt_ncic_labels', 'V') IS NOT NULL DROP VIEW DUI.v_tbl_opt_ncic_labels
IF OBJECT_ID('DUI.v_tbl_opt_ncic_transport_make', 'V') IS NOT NULL DROP VIEW DUI.v_tbl_opt_ncic_transport_make
IF OBJECT_ID('DUI.v_tbl_opt_ncic_transport_mode', 'V') IS NOT NULL DROP VIEW DUI.v_tbl_opt_ncic_transport_mode
IF OBJECT_ID('DUI.v_tbl_opt_ncic_transport_type', 'V') IS NOT NULL DROP VIEW DUI.v_tbl_opt_ncic_transport_type
IF OBJECT_ID('DUI.v_tbl_opt_ncic_vehcile_style_types', 'V') IS NOT NULL DROP VIEW DUI.v_tbl_opt_ncic_vehcile_style_types
IF OBJECT_ID('DUI.v_tbl_opt_ncic_vehicle_body_style', 'V') IS NOT NULL DROP VIEW DUI.v_tbl_opt_ncic_vehicle_body_style
IF OBJECT_ID('DUI.v_tbl_opt_ncic_vehicle_model', 'V') IS NOT NULL DROP VIEW DUI.v_tbl_opt_ncic_vehicle_model
IF OBJECT_ID('DUI.v_tbl_opt_offense', 'V') IS NOT NULL DROP VIEW DUI.v_tbl_opt_offense
IF OBJECT_ID('DUI.v_tbl_opt_offense_types', 'V') IS NOT NULL DROP VIEW DUI.v_tbl_opt_offense_types
IF OBJECT_ID('DUI.v_tbl_opt_operation_occupation', 'V') IS NOT NULL DROP VIEW DUI.v_tbl_opt_operation_occupation
IF OBJECT_ID('DUI.v_tbl_opt_outcomes', 'V') IS NOT NULL DROP VIEW DUI.v_tbl_opt_outcomes
IF OBJECT_ID('DUI.v_tbl_opt_plea', 'V') IS NOT NULL DROP VIEW DUI.v_tbl_opt_plea
IF OBJECT_ID('DUI.v_tbl_opt_races', 'V') IS NOT NULL DROP VIEW DUI.v_tbl_opt_races
IF OBJECT_ID('DUI.v_tbl_opt_radar_types', 'V') IS NOT NULL DROP VIEW DUI.v_tbl_opt_radar_types
IF OBJECT_ID('DUI.v_tbl_opt_reason_for_stop', 'V') IS NOT NULL DROP VIEW DUI.v_tbl_opt_reason_for_stop
IF OBJECT_ID('DUI.v_tbl_opt_road_conditions', 'V') IS NOT NULL DROP VIEW DUI.v_tbl_opt_road_conditions
IF OBJECT_ID('DUI.v_tbl_opt_road_surface', 'V') IS NOT NULL DROP VIEW DUI.v_tbl_opt_road_surface
IF OBJECT_ID('DUI.v_tbl_opt_skin_complexion', 'V') IS NOT NULL DROP VIEW DUI.v_tbl_opt_skin_complexion
IF OBJECT_ID('DUI.v_tbl_opt_specimensubmittedmethod', 'V') IS NOT NULL DROP VIEW DUI.v_tbl_opt_specimensubmittedmethod
IF OBJECT_ID('DUI.v_tbl_opt_specimen_storage', 'V') IS NOT NULL DROP VIEW DUI.v_tbl_opt_specimen_storage
IF OBJECT_ID('DUI.v_tbl_opt_states', 'V') IS NOT NULL DROP VIEW DUI.v_tbl_opt_states
IF OBJECT_ID('DUI.v_tbl_opt_status', 'V') IS NOT NULL DROP VIEW DUI.v_tbl_opt_status
IF OBJECT_ID('DUI.v_tbl_opt_step_dar_event_types', 'V') IS NOT NULL DROP VIEW DUI.v_tbl_opt_step_dar_event_types
IF OBJECT_ID('DUI.v_tbl_opt_step_grant_type', 'V') IS NOT NULL DROP VIEW DUI.v_tbl_opt_step_grant_type
IF OBJECT_ID('DUI.v_tbl_opt_surfaces', 'V') IS NOT NULL DROP VIEW DUI.v_tbl_opt_surfaces
IF OBJECT_ID('DUI.v_tbl_opt_system_mode', 'V') IS NOT NULL DROP VIEW DUI.v_tbl_opt_system_mode
IF OBJECT_ID('DUI.v_tbl_opt_system_mode_with_tbl_opt_ncic_transport_mode', 'V') IS NOT NULL DROP VIEW DUI.v_tbl_opt_system_mode_with_tbl_opt_ncic_transport_mode
IF OBJECT_ID('DUI.v_tbl_opt_tox_spec_types', 'V') IS NOT NULL DROP VIEW DUI.v_tbl_opt_tox_spec_types
IF OBJECT_ID('DUI.v_tbl_opt_tox_screen_result', 'V') IS NOT NULL DROP VIEW DUI.v_tbl_opt_tox_screen_result
IF OBJECT_ID('DUI.v_tbl_opt_violation', 'V') IS NOT NULL DROP VIEW DUI.v_tbl_opt_violation
IF OBJECT_ID('DUI.v_tbl_opt_water_surfaces', 'V') IS NOT NULL DROP VIEW DUI.v_tbl_opt_water_surfaces
IF OBJECT_ID('DUI.v_tbl_opt_wave_height', 'V') IS NOT NULL DROP VIEW DUI.v_tbl_opt_wave_height
IF OBJECT_ID('DUI.v_tbl_opt_wave_types', 'V') IS NOT NULL DROP VIEW DUI.v_tbl_opt_wave_types
IF OBJECT_ID('DUI.v_tbl_opt_weather', 'V') IS NOT NULL DROP VIEW DUI.v_tbl_opt_weather
IF OBJECT_ID('DUI.v_tbl_opt_wind_speed', 'V') IS NOT NULL DROP VIEW DUI.v_tbl_opt_wind_speed
IF OBJECT_ID('DUI.v_tbl_opt_zones', 'V') IS NOT NULL DROP VIEW DUI.v_tbl_opt_zones
IF OBJECT_ID('DUI.v_vehicle_watercraft', 'V') IS NOT NULL DROP VIEW DUI.v_vehicle_watercraft
IF OBJECT_ID('DUI.v_vehicle_watercraft_with_casevehicles', 'V') IS NOT NULL DROP VIEW DUI.v_vehicle_watercraft_with_casevehicles
IF OBJECT_ID('DUI.v_vehicle_watercraft_owner', 'V') IS NOT NULL DROP VIEW DUI.v_vehicle_watercraft_owner
IF OBJECT_ID('DUI.v_vehicle_watercraft_owner_with_casevehicles', 'V') IS NOT NULL DROP VIEW DUI.v_vehicle_watercraft_owner_with_casevehicles
IF OBJECT_ID('DUI.v_witnesses', 'V') IS NOT NULL DROP VIEW DUI.v_witnesses
IF OBJECT_ID('DUI.v_witnesses_with_caseheaders', 'V') IS NOT NULL DROP VIEW DUI.v_witnesses_with_caseheaders
IF OBJECT_ID('DUI.v___efmigrationshistory', 'V') IS NOT NULL DROP VIEW DUI.v___efmigrationshistory
IF OBJECT_ID('DUI.v_case_summary', 'V') IS NOT NULL DROP VIEW DUI.v_case_summary
IF OBJECT_ID('DUI.v_evidence_summary', 'V') IS NOT NULL DROP VIEW DUI.v_evidence_summary
IF OBJECT_ID('DUI.v_officer_performance', 'V') IS NOT NULL DROP VIEW DUI.v_officer_performance
IF OBJECT_ID('DUI.v_defendant_summary', 'V') IS NOT NULL DROP VIEW DUI.v_defendant_summary

-- Create all views

-- Simple view for AdditionalOffense
-- Provides secure access to AdditionalOffense data excluding sensitive information
CREATE VIEW DUI.v_additionaloffense AS
SELECT AdditionalOffenseId, CaseOffenseId, AdditionalOffenseDesc, OldAdditionalOffenseId
FROM DUI.AdditionalOffense
WHERE AdditionalOffenseId IS NOT NULL


-- Relationship view: AdditionalOffense with CaseOffenses
-- Provides AdditionalOffense data joined with related CaseOffenses information
CREATE VIEW DUI.v_additionaloffense_with_caseoffenses AS
SELECT t1.AdditionalOffenseId, t1.CaseOffenseId, t1.AdditionalOffenseDesc, t1.OldAdditionalOffenseId, t2.CaseOffenseId as CaseOffenses_CaseOffenseId, t2.Explanation as CaseOffenses_Explanation, t2.CaseId as CaseOffenses_CaseId, t2.OpenContainers as CaseOffenses_OpenContainers, t2.ContainersDesc as CaseOffenses_ContainersDesc, t2.OffenseId as CaseOffenses_OffenseId, t2.TimeOfOff as CaseOffenses_TimeOfOff, t2.OffStateId as CaseOffenses_OffStateId, t2.OffCountyId as CaseOffenses_OffCountyId, t2.OffLat as CaseOffenses_OffLat, t2.OffLng as CaseOffenses_OffLng, t2.TimeOfArrest as CaseOffenses_TimeOfArrest, t2.TimeOfBooking as CaseOffenses_TimeOfBooking, t2.TimeOfEventEnd as CaseOffenses_TimeOfEventEnd, t2.ArrestStateId as CaseOffenses_ArrestStateId, t2.ArrestCountyId as CaseOffenses_ArrestCountyId, t2.ArrestLat as CaseOffenses_ArrestLat, t2.ArrestLng as CaseOffenses_ArrestLng, t2.OffenseAccidentId as CaseOffenses_OffenseAccidentId, t2.OffenseInjuriesId as CaseOffenses_OffenseInjuriesId
FROM DUI.AdditionalOffense t1
LEFT JOIN DUI.CaseOffenses t2 ON t1.CaseOffenseId = t2.CaseOffenseId
WHERE t1.CaseOffenseId IS NOT NULL


-- Simple view for ArchiveCases
-- Provides secure access to ArchiveCases data excluding sensitive information
CREATE VIEW DUI.v_archivecases AS
SELECT CaseId, OffenseBodyOfWaterId, CondWaveTypeId, EvVideoCar, EvVideoStation, EvVideoTimeStart, EvVideoTimeStop, OtherSobrietyTestGiven, AiDic2325, AiHandcuffs, AiBsSearchPrior, AiDefBelt, AiBsSearchAfter, AiBsContraband, CondConstructionZone, AiWeapSecure, SearchConducted, SearchConsent, SearchContraband, OffenseInventory, CondRaceBeforeStop, OffenseLocationBlock, OffenseArrestBlock, EvVideoOther, SearchContrabandResults, SearchResults, AiWeapSecureText, AiBsContrabandText, OldCaseId, Id
FROM DUI.ArchiveCases
WHERE Id IS NOT NULL


-- Relationship view: ArchiveCases with CaseHeaders
-- Provides ArchiveCases data joined with related CaseHeaders information
CREATE VIEW DUI.v_archivecases_with_caseheaders AS
SELECT t1.CaseId, t1.OffenseBodyOfWaterId, t1.CondWaveTypeId, t1.EvVideoCar, t1.EvVideoStation, t1.EvVideoTimeStart, t1.EvVideoTimeStop, t1.OtherSobrietyTestGiven, t1.AiDic2325, t1.AiHandcuffs, t1.AiBsSearchPrior, t1.AiDefBelt, t1.AiBsSearchAfter, t1.AiBsContraband, t1.CondConstructionZone, t1.AiWeapSecure, t1.SearchConducted, t1.SearchConsent, t1.SearchContraband, t1.OffenseInventory, t1.CondRaceBeforeStop, t1.OffenseLocationBlock, t1.OffenseArrestBlock, t1.EvVideoOther, t1.SearchContrabandResults, t1.SearchResults, t1.AiWeapSecureText, t1.AiBsContrabandText, t1.OldCaseId, t1.Id, t2.CaseId as CaseHeaders_CaseId, t2.UniqueId as CaseHeaders_UniqueId, t2.StatusId as CaseHeaders_StatusId, t2.ModelId as CaseHeaders_ModelId, t2.LockedByOfficerId as CaseHeaders_LockedByOfficerId, t2.ApprovedByOfficerId as CaseHeaders_ApprovedByOfficerId, t2.OrganizationId as CaseHeaders_OrganizationId, t2.LocationId as CaseHeaders_LocationId, t2.District as CaseHeaders_District, t2.Grid as CaseHeaders_Grid, t2.Version as CaseHeaders_Version, t2.Active as CaseHeaders_Active, t2.ModeId as CaseHeaders_ModeId, t2.ProbableCause as CaseHeaders_ProbableCause, t2.IsTrainingPurpose as CaseHeaders_IsTrainingPurpose, t2.PaidTxDOT as CaseHeaders_PaidTxDOT, t2.StepGrantTypeId as CaseHeaders_StepGrantTypeId, t2.CaseOwnerAgency as CaseHeaders_CaseOwnerAgency, t2.CaseOwnerBadge as CaseHeaders_CaseOwnerBadge, t2.CaseOwnerDepartmentId as CaseHeaders_CaseOwnerDepartmentId, t2.CaseOwnerId as CaseHeaders_CaseOwnerId, t2.CaseOwnerName as CaseHeaders_CaseOwnerName, t2.CaseOwnerRank as CaseHeaders_CaseOwnerRank, t2.TABC as CaseHeaders_TABC, t2.AdditionalInformation as CaseHeaders_AdditionalInformation, t2.ActivityType as CaseHeaders_ActivityType, t2.OfficerStepShiftId as CaseHeaders_OfficerStepShiftId, t2.StepZoneId as CaseHeaders_StepZoneId, t2.OldCaseID as CaseHeaders_OldCaseID
FROM DUI.ArchiveCases t1
LEFT JOIN DUI.CaseHeaders t2 ON t1.CaseId = t2.CaseId
WHERE t1.CaseId IS NOT NULL


-- Simple view for CaseAddenda
-- Provides secure access to CaseAddenda data excluding sensitive information
CREATE VIEW DUI.v_caseaddenda AS
SELECT CaseAddendumId, CaseId, OfficerDepartment, OfficerName, Addendum, OldCaseADDendumId
FROM DUI.CaseAddenda
WHERE CaseAddendumId IS NOT NULL


-- Simple view for CaseExpunged
-- Provides secure access to CaseExpunged data excluding sensitive information
CREATE VIEW DUI.v_caseexpunged AS
SELECT ExpungeId, CaseId, OrganizationId, LocationId, OfficerId, Reason, OldCaseExpungedId
FROM DUI.CaseExpunged
WHERE ExpungeId IS NOT NULL


-- Simple view for CaseHeaders
-- Provides secure access to CaseHeaders data excluding sensitive information
CREATE VIEW DUI.v_caseheaders AS
SELECT CaseId, UniqueId, StatusId, ModelId, LockedByOfficerId, ApprovedByOfficerId, OrganizationId, LocationId, District, Grid, Version, Active, ModeId, ProbableCause, IsTrainingPurpose, PaidTxDOT, StepGrantTypeId, CaseOwnerAgency, CaseOwnerBadge, CaseOwnerDepartmentId, CaseOwnerId, CaseOwnerName, CaseOwnerRank, TABC, AdditionalInformation, ActivityType, OfficerStepShiftId, StepZoneId, OldCaseID
FROM DUI.CaseHeaders
WHERE CaseId IS NOT NULL


-- Relationship view: CaseHeaders with TBL_OPT_Status
-- Provides CaseHeaders data joined with related TBL_OPT_Status information
CREATE VIEW DUI.v_caseheaders_with_tbl_opt_status AS
SELECT t1.CaseId, t1.UniqueId, t1.StatusId, t1.ModelId, t1.LockedByOfficerId, t1.ApprovedByOfficerId, t1.OrganizationId, t1.LocationId, t1.District, t1.Grid, t1.Version, t1.Active, t1.ModeId, t1.ProbableCause, t1.IsTrainingPurpose, t1.PaidTxDOT, t1.StepGrantTypeId, t1.CaseOwnerAgency, t1.CaseOwnerBadge, t1.CaseOwnerDepartmentId, t1.CaseOwnerId, t1.CaseOwnerName, t1.CaseOwnerRank, t1.TABC, t1.AdditionalInformation, t1.ActivityType, t1.OfficerStepShiftId, t1.StepZoneId, t1.OldCaseID, t2.StatusId as TBL_OPT_Status_StatusId, t2.Active as TBL_OPT_Status_Active
FROM DUI.CaseHeaders t1
LEFT JOIN DUI.TBL_OPT_Status t2 ON t1.StatusId = t2.StatusId
WHERE t1.StatusId IS NOT NULL


-- Simple view for CaseOffenses
-- Provides secure access to CaseOffenses data excluding sensitive information
CREATE VIEW DUI.v_caseoffenses AS
SELECT CaseOffenseId, Explanation, CaseId, OpenContainers, ContainersDesc, OffenseId, TimeOfOff, OffStateId, OffCountyId, OffLat, OffLng, TimeOfArrest, TimeOfBooking, TimeOfEventEnd, ArrestStateId, ArrestCountyId, ArrestLat, ArrestLng, OffenseAccidentId, OffenseInjuriesId
FROM DUI.CaseOffenses
WHERE CaseOffenseId IS NOT NULL


-- Relationship view: CaseOffenses with CaseHeaders
-- Provides CaseOffenses data joined with related CaseHeaders information
CREATE VIEW DUI.v_caseoffenses_with_caseheaders AS
SELECT t1.CaseOffenseId, t1.Explanation, t1.CaseId, t1.OpenContainers, t1.ContainersDesc, t1.OffenseId, t1.TimeOfOff, t1.OffStateId, t1.OffCountyId, t1.OffLat, t1.OffLng, t1.TimeOfArrest, t1.TimeOfBooking, t1.TimeOfEventEnd, t1.ArrestStateId, t1.ArrestCountyId, t1.ArrestLat, t1.ArrestLng, t1.OffenseAccidentId, t1.OffenseInjuriesId, t2.CaseId as CaseHeaders_CaseId, t2.UniqueId as CaseHeaders_UniqueId, t2.StatusId as CaseHeaders_StatusId, t2.ModelId as CaseHeaders_ModelId, t2.LockedByOfficerId as CaseHeaders_LockedByOfficerId, t2.ApprovedByOfficerId as CaseHeaders_ApprovedByOfficerId, t2.OrganizationId as CaseHeaders_OrganizationId, t2.LocationId as CaseHeaders_LocationId, t2.District as CaseHeaders_District, t2.Grid as CaseHeaders_Grid, t2.Version as CaseHeaders_Version, t2.Active as CaseHeaders_Active, t2.ModeId as CaseHeaders_ModeId, t2.ProbableCause as CaseHeaders_ProbableCause, t2.IsTrainingPurpose as CaseHeaders_IsTrainingPurpose, t2.PaidTxDOT as CaseHeaders_PaidTxDOT, t2.StepGrantTypeId as CaseHeaders_StepGrantTypeId, t2.CaseOwnerAgency as CaseHeaders_CaseOwnerAgency, t2.CaseOwnerBadge as CaseHeaders_CaseOwnerBadge, t2.CaseOwnerDepartmentId as CaseHeaders_CaseOwnerDepartmentId, t2.CaseOwnerId as CaseHeaders_CaseOwnerId, t2.CaseOwnerName as CaseHeaders_CaseOwnerName, t2.CaseOwnerRank as CaseHeaders_CaseOwnerRank, t2.TABC as CaseHeaders_TABC, t2.AdditionalInformation as CaseHeaders_AdditionalInformation, t2.ActivityType as CaseHeaders_ActivityType, t2.OfficerStepShiftId as CaseHeaders_OfficerStepShiftId, t2.StepZoneId as CaseHeaders_StepZoneId, t2.OldCaseID as CaseHeaders_OldCaseID
FROM DUI.CaseOffenses t1
LEFT JOIN DUI.CaseHeaders t2 ON t1.CaseId = t2.CaseId
WHERE t1.CaseId IS NOT NULL


-- Simple view for CaseReviewHistory
-- Provides secure access to CaseReviewHistory data excluding sensitive information
CREATE VIEW DUI.v_casereviewhistory AS
SELECT Id, CaseId, ReviewStatusId, ReviewBy
FROM DUI.CaseReviewHistory
WHERE Id IS NOT NULL


-- Simple view for CaseSearchWarrant
-- Provides secure access to CaseSearchWarrant data excluding sensitive information
CREATE VIEW DUI.v_casesearchwarrant AS
SELECT SearchWarrantId, CaseId, PassKey, Closed, OffAccepted, SecOffAccepted, JudgeAccepted, Rejected, SecOffFirstname, SecOffLastname, SecOffBadgeNum, SecOffPid, SecOffAgency, SecOffIsOtherCounty, SecOffOtherCounty, SecOffRemote, SecOffPassKey, JudgeName, JudgeCourt, JudgeCounty, JudgeRecNo, SecOffIsJudge, SecOffJudgeName, SecOffJudgeCourt, SecOffJudgeId, JudgeId, OldSearchWarrantId
FROM DUI.CaseSearchWarrant
WHERE SearchWarrantId IS NOT NULL


-- Simple view for CaseSearchWarrantActivity
-- Provides secure access to CaseSearchWarrantActivity data excluding sensitive information
CREATE VIEW DUI.v_casesearchwarrantactivity AS
SELECT SearchWarrantActivityId, SearchWarrantFileIdFk, SearchWarrantIdFk, Activity, ClientIp, OtherInfo, ContinentCode, CountryCode, RegionCode, Latitude, Longitude, DtCreated, OldCaseSearchWarrantActivityId
FROM DUI.CaseSearchWarrantActivity
WHERE SearchWarrantActivityId IS NOT NULL


-- Simple view for CaseSearchWarrantFile
-- Provides secure access to CaseSearchWarrantFile data excluding sensitive information
CREATE VIEW DUI.v_casesearchwarrantfile AS
SELECT SearchWarrantFileId, SearchWarrantId, ReportName, OrigFile, OffSignLocX, OffSignLocY, SecOffSignLocX, SecOffSignLocY, JudSignLocX, JudSignLocY, OffSign, FileSignedByOff, SecOffSign, FileSignedBySecOff, JudSign, FinalSigned, FinalPdf, OffAccepted, OffRejected, OffNoSign, SecOffAccepted, SecOffRejected, SecOffNoSign, JudAccepted, JudRejected, JudNoSign, NoReview, OffInstructions, SecOffInstructions, OldCaseSearchWarrantFileId
FROM DUI.CaseSearchWarrantFile
WHERE SearchWarrantFileId IS NOT NULL


-- Simple view for CaseVehiclePassengers
-- Provides secure access to CaseVehiclePassengers data excluding sensitive information
CREATE VIEW DUI.v_casevehiclepassengers AS
SELECT CaseVehiclePassengerId, CaseVehicleId, LastName, FirstName, MothersMaidenName, RaceId, GenderId, CPSNotified, CPSNotifiedBy, CPSNotExplanation, ID, Intoxicated, Arrested, Charge, WearSafetyBelt, WearHelmet, WhereSeated, Comments, StateId, CountyId, Lat, Lng, CountyName
FROM DUI.CaseVehiclePassengers
WHERE CaseVehiclePassengerId IS NOT NULL


-- Relationship view: CaseVehiclePassengers with CaseVehicles
-- Provides CaseVehiclePassengers data joined with related CaseVehicles information
CREATE VIEW DUI.v_casevehiclepassengers_with_casevehicles AS
SELECT t1.CaseVehiclePassengerId, t1.CaseVehicleId, t1.LastName, t1.FirstName, t1.MothersMaidenName, t1.RaceId, t1.GenderId, t1.CPSNotified, t1.CPSNotifiedBy, t1.CPSNotExplanation, t1.ID, t1.Intoxicated, t1.Arrested, t1.Charge, t1.WearSafetyBelt, t1.WearHelmet, t1.WhereSeated, t1.Comments, t1.StateId, t1.CountyId, t1.Lat, t1.Lng, t1.CountyName, t2.CaseVehicleId as CaseVehicles_CaseVehicleId, t2.CaseId as CaseVehicles_CaseId, t2.VehicleTypeId as CaseVehicles_VehicleTypeId, t2.VehicleMakeId as CaseVehicles_VehicleMakeId, t2.VehicleModelId as CaseVehicles_VehicleModelId, t2.VehicleStyleId as CaseVehicles_VehicleStyleId, t2.VehicleColorId as CaseVehicles_VehicleColorId, t2.Year as CaseVehicles_Year, t2.StateId as CaseVehicles_StateId, t2.VIN as CaseVehicles_VIN, t2.Impounded as CaseVehicles_Impounded, t2.ImpoundedBy as CaseVehicles_ImpoundedBy, t2.StoredAt as CaseVehicles_StoredAt, t2.VehiclePlacedOnHold as CaseVehicles_VehiclePlacedOnHold, t2.HoldReason as CaseVehicles_HoldReason, t2.VehicleWatercraftId as CaseVehicles_VehicleWatercraftId, t2.VehicleWatercraftOwnerId as CaseVehicles_VehicleWatercraftOwnerId, t2.VehicleCommercial as CaseVehicles_VehicleCommercial, t2.VehicleHazMat as CaseVehicles_VehicleHazMat, t2.VehicleCondition as CaseVehicles_VehicleCondition, t2.BoatHullShapeId as CaseVehicles_BoatHullShapeId, t2.VehicleBwiMotorYear as CaseVehicles_VehicleBwiMotorYear, t2.VehicleBwiMotorHorsepower as CaseVehicles_VehicleBwiMotorHorsepower, t2.VehicleBwiMotorManufacturer as CaseVehicles_VehicleBwiMotorManufacturer, t2.VehicleBwiMotorSerial as CaseVehicles_VehicleBwiMotorSerial, t2.VehicleBwiTrailerManufacturer as CaseVehicles_VehicleBwiTrailerManufacturer, t2.VehicleBwiTrailerRegistraitonNum as CaseVehicles_VehicleBwiTrailerRegistraitonNum, t2.VehicleModeId as CaseVehicles_VehicleModeId, t2.OldCaseId as CaseVehicles_OldCaseId
FROM DUI.CaseVehiclePassengers t1
LEFT JOIN DUI.CaseVehicles t2 ON t1.CaseVehicleId = t2.CaseVehicleId
WHERE t1.CaseVehicleId IS NOT NULL


-- Simple view for CaseVehicles
-- Provides secure access to CaseVehicles data excluding sensitive information
CREATE VIEW DUI.v_casevehicles AS
SELECT CaseVehicleId, CaseId, VehicleTypeId, VehicleMakeId, VehicleModelId, VehicleStyleId, VehicleColorId, Year, StateId, VIN, Impounded, ImpoundedBy, StoredAt, VehiclePlacedOnHold, HoldReason, VehicleWatercraftId, VehicleWatercraftOwnerId, VehicleCommercial, VehicleHazMat, VehicleCondition, BoatHullShapeId, VehicleBwiMotorYear, VehicleBwiMotorHorsepower, VehicleBwiMotorManufacturer, VehicleBwiMotorSerial, VehicleBwiTrailerManufacturer, VehicleBwiTrailerRegistraitonNum, VehicleModeId, OldCaseId
FROM DUI.CaseVehicles
WHERE CaseVehicleId IS NOT NULL


-- Relationship view: CaseVehicles with CaseHeaders
-- Provides CaseVehicles data joined with related CaseHeaders information
CREATE VIEW DUI.v_casevehicles_with_caseheaders AS
SELECT t1.CaseVehicleId, t1.CaseId, t1.VehicleTypeId, t1.VehicleMakeId, t1.VehicleModelId, t1.VehicleStyleId, t1.VehicleColorId, t1.Year, t1.StateId, t1.VIN, t1.Impounded, t1.ImpoundedBy, t1.StoredAt, t1.VehiclePlacedOnHold, t1.HoldReason, t1.VehicleWatercraftId, t1.VehicleWatercraftOwnerId, t1.VehicleCommercial, t1.VehicleHazMat, t1.VehicleCondition, t1.BoatHullShapeId, t1.VehicleBwiMotorYear, t1.VehicleBwiMotorHorsepower, t1.VehicleBwiMotorManufacturer, t1.VehicleBwiMotorSerial, t1.VehicleBwiTrailerManufacturer, t1.VehicleBwiTrailerRegistraitonNum, t1.VehicleModeId, t1.OldCaseId, t2.CaseId as CaseHeaders_CaseId, t2.UniqueId as CaseHeaders_UniqueId, t2.StatusId as CaseHeaders_StatusId, t2.ModelId as CaseHeaders_ModelId, t2.LockedByOfficerId as CaseHeaders_LockedByOfficerId, t2.ApprovedByOfficerId as CaseHeaders_ApprovedByOfficerId, t2.OrganizationId as CaseHeaders_OrganizationId, t2.LocationId as CaseHeaders_LocationId, t2.District as CaseHeaders_District, t2.Grid as CaseHeaders_Grid, t2.Version as CaseHeaders_Version, t2.Active as CaseHeaders_Active, t2.ModeId as CaseHeaders_ModeId, t2.ProbableCause as CaseHeaders_ProbableCause, t2.IsTrainingPurpose as CaseHeaders_IsTrainingPurpose, t2.PaidTxDOT as CaseHeaders_PaidTxDOT, t2.StepGrantTypeId as CaseHeaders_StepGrantTypeId, t2.CaseOwnerAgency as CaseHeaders_CaseOwnerAgency, t2.CaseOwnerBadge as CaseHeaders_CaseOwnerBadge, t2.CaseOwnerDepartmentId as CaseHeaders_CaseOwnerDepartmentId, t2.CaseOwnerId as CaseHeaders_CaseOwnerId, t2.CaseOwnerName as CaseHeaders_CaseOwnerName, t2.CaseOwnerRank as CaseHeaders_CaseOwnerRank, t2.TABC as CaseHeaders_TABC, t2.AdditionalInformation as CaseHeaders_AdditionalInformation, t2.ActivityType as CaseHeaders_ActivityType, t2.OfficerStepShiftId as CaseHeaders_OfficerStepShiftId, t2.StepZoneId as CaseHeaders_StepZoneId, t2.OldCaseID as CaseHeaders_OldCaseID
FROM DUI.CaseVehicles t1
LEFT JOIN DUI.CaseHeaders t2 ON t1.CaseId = t2.CaseId
WHERE t1.CaseId IS NOT NULL


-- Simple view for CaseViolations
-- Provides secure access to CaseViolations data excluding sensitive information
CREATE VIEW DUI.v_caseviolations AS
SELECT CaseViolationId, CaseId, ViolationId, IsCitation, IsWarning, IsArrest, IsOther
FROM DUI.CaseViolations
WHERE CaseViolationId IS NOT NULL


-- Relationship view: CaseViolations with CaseHeaders
-- Provides CaseViolations data joined with related CaseHeaders information
CREATE VIEW DUI.v_caseviolations_with_caseheaders AS
SELECT t1.CaseViolationId, t1.CaseId, t1.ViolationId, t1.IsCitation, t1.IsWarning, t1.IsArrest, t1.IsOther, t2.CaseId as CaseHeaders_CaseId, t2.UniqueId as CaseHeaders_UniqueId, t2.StatusId as CaseHeaders_StatusId, t2.ModelId as CaseHeaders_ModelId, t2.LockedByOfficerId as CaseHeaders_LockedByOfficerId, t2.ApprovedByOfficerId as CaseHeaders_ApprovedByOfficerId, t2.OrganizationId as CaseHeaders_OrganizationId, t2.LocationId as CaseHeaders_LocationId, t2.District as CaseHeaders_District, t2.Grid as CaseHeaders_Grid, t2.Version as CaseHeaders_Version, t2.Active as CaseHeaders_Active, t2.ModeId as CaseHeaders_ModeId, t2.ProbableCause as CaseHeaders_ProbableCause, t2.IsTrainingPurpose as CaseHeaders_IsTrainingPurpose, t2.PaidTxDOT as CaseHeaders_PaidTxDOT, t2.StepGrantTypeId as CaseHeaders_StepGrantTypeId, t2.CaseOwnerAgency as CaseHeaders_CaseOwnerAgency, t2.CaseOwnerBadge as CaseHeaders_CaseOwnerBadge, t2.CaseOwnerDepartmentId as CaseHeaders_CaseOwnerDepartmentId, t2.CaseOwnerId as CaseHeaders_CaseOwnerId, t2.CaseOwnerName as CaseHeaders_CaseOwnerName, t2.CaseOwnerRank as CaseHeaders_CaseOwnerRank, t2.TABC as CaseHeaders_TABC, t2.AdditionalInformation as CaseHeaders_AdditionalInformation, t2.ActivityType as CaseHeaders_ActivityType, t2.OfficerStepShiftId as CaseHeaders_OfficerStepShiftId, t2.StepZoneId as CaseHeaders_StepZoneId, t2.OldCaseID as CaseHeaders_OldCaseID
FROM DUI.CaseViolations t1
LEFT JOIN DUI.CaseHeaders t2 ON t1.CaseId = t2.CaseId
WHERE t1.CaseId IS NOT NULL


-- Simple view for CaseWarrantForm
-- Provides secure access to CaseWarrantForm data excluding sensitive information
CREATE VIEW DUI.v_casewarrantform AS
SELECT WarrantFormId, CaseId, FormName, DisplayName, Form
FROM DUI.CaseWarrantForm
WHERE WarrantFormId IS NOT NULL


-- Simple view for ConditionReasonForStop
-- Provides secure access to ConditionReasonForStop data excluding sensitive information
CREATE VIEW DUI.v_conditionreasonforstop AS
SELECT ConditionReasonForStopId, ConditionId, ReasonForStopId, ReasonForStopText, Checked, OldCaseReasonForStopId
FROM DUI.ConditionReasonForStop
WHERE ConditionReasonForStopId IS NOT NULL


-- Relationship view: ConditionReasonForStop with Conditions
-- Provides ConditionReasonForStop data joined with related Conditions information
CREATE VIEW DUI.v_conditionreasonforstop_with_conditions AS
SELECT t1.ConditionReasonForStopId, t1.ConditionId, t1.ReasonForStopId, t1.ReasonForStopText, t1.Checked, t1.OldCaseReasonForStopId, t2.ConditionId as Conditions_ConditionId, t2.CaseId as Conditions_CaseId, t2.LightConditionId as Conditions_LightConditionId, t2.WeatherId as Conditions_WeatherId, t2.SurfaceId as Conditions_SurfaceId, t2.RoadConditionId as Conditions_RoadConditionId, t2.RoadSurfaceId as Conditions_RoadSurfaceId, t2.ZoneId as Conditions_ZoneId, t2.RoadMarked as Conditions_RoadMarked, t2.Cause as Conditions_Cause, t2.SpeedAsFactor as Conditions_SpeedAsFactor, t2.ObservedSpeed as Conditions_ObservedSpeed, t2.OfficerRadarTrained as Conditions_OfficerRadarTrained, t2.RadarChecked as Conditions_RadarChecked, t2.RadarTypeId as Conditions_RadarTypeId, t2.HowDefendantWasObserved as Conditions_HowDefendantWasObserved, t2.SuspectResistance as Conditions_SuspectResistance, t2.ResistanceVerbalThreat as Conditions_ResistanceVerbalThreat, t2.ResistancePassive as Conditions_ResistancePassive, t2.ResistancePhysical as Conditions_ResistancePhysical, t2.InjuryId as Conditions_InjuryId, t2.WaterSurfaceId as Conditions_WaterSurfaceId, t2.WindSpeedId as Conditions_WindSpeedId, t2.WaveHeightId as Conditions_WaveHeightId, t2.ResistanceNone as Conditions_ResistanceNone, t2.CondStopReason as Conditions_CondStopReason, t2.OldCaseId as Conditions_OldCaseId
FROM DUI.ConditionReasonForStop t1
LEFT JOIN DUI.Conditions t2 ON t1.ConditionId = t2.ConditionId
WHERE t1.ConditionId IS NOT NULL


-- Simple view for Conditions
-- Provides secure access to Conditions data excluding sensitive information
CREATE VIEW DUI.v_conditions AS
SELECT ConditionId, CaseId, LightConditionId, WeatherId, SurfaceId, RoadConditionId, RoadSurfaceId, ZoneId, RoadMarked, Cause, SpeedAsFactor, ObservedSpeed, OfficerRadarTrained, RadarChecked, RadarTypeId, HowDefendantWasObserved, SuspectResistance, ResistanceVerbalThreat, ResistancePassive, ResistancePhysical, InjuryId, WaterSurfaceId, WindSpeedId, WaveHeightId, ResistanceNone, CondStopReason, OldCaseId
FROM DUI.Conditions
WHERE ConditionId IS NOT NULL


-- Relationship view: Conditions with CaseHeaders
-- Provides Conditions data joined with related CaseHeaders information
CREATE VIEW DUI.v_conditions_with_caseheaders AS
SELECT t1.ConditionId, t1.CaseId, t1.LightConditionId, t1.WeatherId, t1.SurfaceId, t1.RoadConditionId, t1.RoadSurfaceId, t1.ZoneId, t1.RoadMarked, t1.Cause, t1.SpeedAsFactor, t1.ObservedSpeed, t1.OfficerRadarTrained, t1.RadarChecked, t1.RadarTypeId, t1.HowDefendantWasObserved, t1.SuspectResistance, t1.ResistanceVerbalThreat, t1.ResistancePassive, t1.ResistancePhysical, t1.InjuryId, t1.WaterSurfaceId, t1.WindSpeedId, t1.WaveHeightId, t1.ResistanceNone, t1.CondStopReason, t1.OldCaseId, t2.CaseId as CaseHeaders_CaseId, t2.UniqueId as CaseHeaders_UniqueId, t2.StatusId as CaseHeaders_StatusId, t2.ModelId as CaseHeaders_ModelId, t2.LockedByOfficerId as CaseHeaders_LockedByOfficerId, t2.ApprovedByOfficerId as CaseHeaders_ApprovedByOfficerId, t2.OrganizationId as CaseHeaders_OrganizationId, t2.LocationId as CaseHeaders_LocationId, t2.District as CaseHeaders_District, t2.Grid as CaseHeaders_Grid, t2.Version as CaseHeaders_Version, t2.Active as CaseHeaders_Active, t2.ModeId as CaseHeaders_ModeId, t2.ProbableCause as CaseHeaders_ProbableCause, t2.IsTrainingPurpose as CaseHeaders_IsTrainingPurpose, t2.PaidTxDOT as CaseHeaders_PaidTxDOT, t2.StepGrantTypeId as CaseHeaders_StepGrantTypeId, t2.CaseOwnerAgency as CaseHeaders_CaseOwnerAgency, t2.CaseOwnerBadge as CaseHeaders_CaseOwnerBadge, t2.CaseOwnerDepartmentId as CaseHeaders_CaseOwnerDepartmentId, t2.CaseOwnerId as CaseHeaders_CaseOwnerId, t2.CaseOwnerName as CaseHeaders_CaseOwnerName, t2.CaseOwnerRank as CaseHeaders_CaseOwnerRank, t2.TABC as CaseHeaders_TABC, t2.AdditionalInformation as CaseHeaders_AdditionalInformation, t2.ActivityType as CaseHeaders_ActivityType, t2.OfficerStepShiftId as CaseHeaders_OfficerStepShiftId, t2.StepZoneId as CaseHeaders_StepZoneId, t2.OldCaseID as CaseHeaders_OldCaseID
FROM DUI.Conditions t1
LEFT JOIN DUI.CaseHeaders t2 ON t1.CaseId = t2.CaseId
WHERE t1.CaseId IS NOT NULL


-- Simple view for DUIReportRequest
-- Provides secure access to DUIReportRequest data excluding sensitive information
CREATE VIEW DUI.v_duireportrequest AS
SELECT DUIReportRequestId, CaseId, UserId, ReportData, ReportObject, ReportName, FileType, GeneratedReport, ModifiedReport, SigningRequest, IsSigned, LastModified, ReportFormId, IsLocked
FROM DUI.DUIReportRequest
WHERE DUIReportRequestId IS NOT NULL


-- Relationship view: DUIReportRequest with CaseHeaders
-- Provides DUIReportRequest data joined with related CaseHeaders information
CREATE VIEW DUI.v_duireportrequest_with_caseheaders AS
SELECT t1.DUIReportRequestId, t1.CaseId, t1.UserId, t1.ReportData, t1.ReportObject, t1.ReportName, t1.FileType, t1.GeneratedReport, t1.ModifiedReport, t1.SigningRequest, t1.IsSigned, t1.LastModified, t1.ReportFormId, t1.IsLocked, t2.CaseId as CaseHeaders_CaseId, t2.UniqueId as CaseHeaders_UniqueId, t2.StatusId as CaseHeaders_StatusId, t2.ModelId as CaseHeaders_ModelId, t2.LockedByOfficerId as CaseHeaders_LockedByOfficerId, t2.ApprovedByOfficerId as CaseHeaders_ApprovedByOfficerId, t2.OrganizationId as CaseHeaders_OrganizationId, t2.LocationId as CaseHeaders_LocationId, t2.District as CaseHeaders_District, t2.Grid as CaseHeaders_Grid, t2.Version as CaseHeaders_Version, t2.Active as CaseHeaders_Active, t2.ModeId as CaseHeaders_ModeId, t2.ProbableCause as CaseHeaders_ProbableCause, t2.IsTrainingPurpose as CaseHeaders_IsTrainingPurpose, t2.PaidTxDOT as CaseHeaders_PaidTxDOT, t2.StepGrantTypeId as CaseHeaders_StepGrantTypeId, t2.CaseOwnerAgency as CaseHeaders_CaseOwnerAgency, t2.CaseOwnerBadge as CaseHeaders_CaseOwnerBadge, t2.CaseOwnerDepartmentId as CaseHeaders_CaseOwnerDepartmentId, t2.CaseOwnerId as CaseHeaders_CaseOwnerId, t2.CaseOwnerName as CaseHeaders_CaseOwnerName, t2.CaseOwnerRank as CaseHeaders_CaseOwnerRank, t2.TABC as CaseHeaders_TABC, t2.AdditionalInformation as CaseHeaders_AdditionalInformation, t2.ActivityType as CaseHeaders_ActivityType, t2.OfficerStepShiftId as CaseHeaders_OfficerStepShiftId, t2.StepZoneId as CaseHeaders_StepZoneId, t2.OldCaseID as CaseHeaders_OldCaseID
FROM DUI.DUIReportRequest t1
LEFT JOIN DUI.CaseHeaders t2 ON t1.CaseId = t2.CaseId
WHERE t1.CaseId IS NOT NULL


-- Simple view for DefendantAdditionalInfo
-- Provides secure access to DefendantAdditionalInfo data excluding sensitive information
CREATE VIEW DUI.v_defendantadditionalinfo AS
SELECT DefendantAdditionalInfoId, DefendantId, AdditionalInformation, AccidentReport, ImpoundSheet, SFSTCheckList, DIC23, DIC24, DIC25, OfficerSupplement, Intoxilyzer, SearchWarrant, Other, OtherDesc, DefendantInfo, OffenseInfo, Observations, FSTs, SpecimenInfo, PassengerInfo
FROM DUI.DefendantAdditionalInfo
WHERE DefendantAdditionalInfoId IS NOT NULL


-- Relationship view: DefendantAdditionalInfo with Defendants
-- Provides DefendantAdditionalInfo data joined with related Defendants information
CREATE VIEW DUI.v_defendantadditionalinfo_with_defendants AS
SELECT t1.DefendantAdditionalInfoId, t1.DefendantId, t1.AdditionalInformation, t1.AccidentReport, t1.ImpoundSheet, t1.SFSTCheckList, t1.DIC23, t1.DIC24, t1.DIC25, t1.OfficerSupplement, t1.Intoxilyzer, t1.SearchWarrant, t1.Other, t1.OtherDesc, t1.DefendantInfo, t1.OffenseInfo, t1.Observations, t1.FSTs, t1.SpecimenInfo, t1.PassengerInfo, t2.DefendantId as Defendants_DefendantId, t2.CaseId as Defendants_CaseId, t2.LastName as Defendants_LastName, t2.FirstName as Defendants_FirstName, t2.RaceId as Defendants_RaceId, t2.GenderId as Defendants_GenderId, t2.HeightIn as Defendants_HeightIn, t2.HeightFt as Defendants_HeightFt, t2.HairColorId as Defendants_HairColorId, t2.EyeColorId as Defendants_EyeColorId, t2.Weight as Defendants_Weight, t2.SkinId as Defendants_SkinId, t2.SkinComplexionSkinId as Defendants_SkinComplexionSkinId, t2.Tattoos as Defendants_Tattoos, t2.Alias as Defendants_Alias, t2.Occupation as Defendants_Occupation, t2.PlaceEmployment as Defendants_PlaceEmployment, t2.MotherMaiden as Defendants_MotherMaiden, t2.Citizen as Defendants_Citizen, t2.EducationId as Defendants_EducationId, t2.SpecialNeeds as Defendants_SpecialNeeds, t2.Condition as Defendants_Condition, t2.SafetyBelt as Defendants_SafetyBelt, t2.Helmet as Defendants_Helmet, t2.DpsSid as Defendants_DpsSid, t2.StepFunded as Defendants_StepFunded, t2.Training as Defendants_Training, t2.ActivityType as Defendants_ActivityType, t2.OfficerStepShiftId as Defendants_OfficerStepShiftId, t2.StepZoneId as Defendants_StepZoneId, t2.ZoneId as Defendants_ZoneId, t2.StepGrantTypeId as Defendants_StepGrantTypeId, t2.OldCaseID as Defendants_OldCaseID
FROM DUI.DefendantAdditionalInfo t1
LEFT JOIN DUI.Defendants t2 ON t1.DefendantId = t2.DefendantId
WHERE t1.DefendantId IS NOT NULL


-- Simple view for DefendantAddresses
-- Provides secure access to DefendantAddresses data excluding sensitive information
CREATE VIEW DUI.v_defendantaddresses AS
SELECT DefendantId, StateId, CountyId, Lat, Lng, DefOccupation, DefPlaceEmployment, ContactName, EmStateId, OccStateId, Relationship, OccLat, OccLng, EmLat, EmLng
FROM DUI.DefendantAddresses
WHERE DefendantAddressId IS NOT NULL


-- Relationship view: DefendantAddresses with Defendants
-- Provides DefendantAddresses data joined with related Defendants information
CREATE VIEW DUI.v_defendantaddresses_with_defendants AS
SELECT t1.DefendantId, t1.StateId, t1.CountyId, t1.Lat, t1.Lng, t1.DefOccupation, t1.DefPlaceEmployment, t1.ContactName, t1.EmStateId, t1.OccStateId, t1.Relationship, t1.OccLat, t1.OccLng, t1.EmLat, t1.EmLng, t2.DefendantId as Defendants_DefendantId, t2.CaseId as Defendants_CaseId, t2.LastName as Defendants_LastName, t2.FirstName as Defendants_FirstName, t2.RaceId as Defendants_RaceId, t2.GenderId as Defendants_GenderId, t2.HeightIn as Defendants_HeightIn, t2.HeightFt as Defendants_HeightFt, t2.HairColorId as Defendants_HairColorId, t2.EyeColorId as Defendants_EyeColorId, t2.Weight as Defendants_Weight, t2.SkinId as Defendants_SkinId, t2.SkinComplexionSkinId as Defendants_SkinComplexionSkinId, t2.Tattoos as Defendants_Tattoos, t2.Alias as Defendants_Alias, t2.Occupation as Defendants_Occupation, t2.PlaceEmployment as Defendants_PlaceEmployment, t2.MotherMaiden as Defendants_MotherMaiden, t2.Citizen as Defendants_Citizen, t2.EducationId as Defendants_EducationId, t2.SpecialNeeds as Defendants_SpecialNeeds, t2.Condition as Defendants_Condition, t2.SafetyBelt as Defendants_SafetyBelt, t2.Helmet as Defendants_Helmet, t2.DpsSid as Defendants_DpsSid, t2.StepFunded as Defendants_StepFunded, t2.Training as Defendants_Training, t2.ActivityType as Defendants_ActivityType, t2.OfficerStepShiftId as Defendants_OfficerStepShiftId, t2.StepZoneId as Defendants_StepZoneId, t2.ZoneId as Defendants_ZoneId, t2.StepGrantTypeId as Defendants_StepGrantTypeId, t2.OldCaseID as Defendants_OldCaseID
FROM DUI.DefendantAddresses t1
LEFT JOIN DUI.Defendants t2 ON t1.DefendantId = t2.DefendantId
WHERE t1.DefendantId IS NOT NULL


-- Simple view for DefendantEmContacts
-- Provides secure access to DefendantEmContacts data excluding sensitive information
CREATE VIEW DUI.v_defendantemcontacts AS
SELECT EmergencyContactId, DefendantId, ContactName, Relationship, StateId, CountyId, Lat, Lng
FROM DUI.DefendantEmContacts
WHERE EmergencyContactId IS NOT NULL


-- Relationship view: DefendantEmContacts with Defendants
-- Provides DefendantEmContacts data joined with related Defendants information
CREATE VIEW DUI.v_defendantemcontacts_with_defendants AS
SELECT t1.EmergencyContactId, t1.DefendantId, t1.ContactName, t1.Relationship, t1.StateId, t1.CountyId, t1.Lat, t1.Lng, t2.DefendantId as Defendants_DefendantId, t2.CaseId as Defendants_CaseId, t2.LastName as Defendants_LastName, t2.FirstName as Defendants_FirstName, t2.RaceId as Defendants_RaceId, t2.GenderId as Defendants_GenderId, t2.HeightIn as Defendants_HeightIn, t2.HeightFt as Defendants_HeightFt, t2.HairColorId as Defendants_HairColorId, t2.EyeColorId as Defendants_EyeColorId, t2.Weight as Defendants_Weight, t2.SkinId as Defendants_SkinId, t2.SkinComplexionSkinId as Defendants_SkinComplexionSkinId, t2.Tattoos as Defendants_Tattoos, t2.Alias as Defendants_Alias, t2.Occupation as Defendants_Occupation, t2.PlaceEmployment as Defendants_PlaceEmployment, t2.MotherMaiden as Defendants_MotherMaiden, t2.Citizen as Defendants_Citizen, t2.EducationId as Defendants_EducationId, t2.SpecialNeeds as Defendants_SpecialNeeds, t2.Condition as Defendants_Condition, t2.SafetyBelt as Defendants_SafetyBelt, t2.Helmet as Defendants_Helmet, t2.DpsSid as Defendants_DpsSid, t2.StepFunded as Defendants_StepFunded, t2.Training as Defendants_Training, t2.ActivityType as Defendants_ActivityType, t2.OfficerStepShiftId as Defendants_OfficerStepShiftId, t2.StepZoneId as Defendants_StepZoneId, t2.ZoneId as Defendants_ZoneId, t2.StepGrantTypeId as Defendants_StepGrantTypeId, t2.OldCaseID as Defendants_OldCaseID
FROM DUI.DefendantEmContacts t1
LEFT JOIN DUI.Defendants t2 ON t1.DefendantId = t2.DefendantId
WHERE t1.DefendantId IS NOT NULL


-- Simple view for DefendantInterview
-- Provides secure access to DefendantInterview data excluding sensitive information
CREATE VIEW DUI.v_defendantinterview AS
SELECT DefendantInterviewId, DefendantId, MirandaWarningRead, MirandaInEnglish, MirandaInSpanish, StatedUnderstood, ReadBy, TimeRead, Comments, AskOnVideo, DefendantSpeech, DoNotAskQuestion, DoNotAskQuestionForLanguage, Interviewer, InterviewerId, RefuseToAnswer, UnusualActions, TimeOfInterview
FROM DUI.DefendantInterview
WHERE DefendantInterviewId IS NOT NULL


-- Relationship view: DefendantInterview with Defendants
-- Provides DefendantInterview data joined with related Defendants information
CREATE VIEW DUI.v_defendantinterview_with_defendants AS
SELECT t1.DefendantInterviewId, t1.DefendantId, t1.MirandaWarningRead, t1.MirandaInEnglish, t1.MirandaInSpanish, t1.StatedUnderstood, t1.ReadBy, t1.TimeRead, t1.Comments, t1.AskOnVideo, t1.DefendantSpeech, t1.DoNotAskQuestion, t1.DoNotAskQuestionForLanguage, t1.Interviewer, t1.InterviewerId, t1.RefuseToAnswer, t1.UnusualActions, t1.TimeOfInterview, t2.DefendantId as Defendants_DefendantId, t2.CaseId as Defendants_CaseId, t2.LastName as Defendants_LastName, t2.FirstName as Defendants_FirstName, t2.RaceId as Defendants_RaceId, t2.GenderId as Defendants_GenderId, t2.HeightIn as Defendants_HeightIn, t2.HeightFt as Defendants_HeightFt, t2.HairColorId as Defendants_HairColorId, t2.EyeColorId as Defendants_EyeColorId, t2.Weight as Defendants_Weight, t2.SkinId as Defendants_SkinId, t2.SkinComplexionSkinId as Defendants_SkinComplexionSkinId, t2.Tattoos as Defendants_Tattoos, t2.Alias as Defendants_Alias, t2.Occupation as Defendants_Occupation, t2.PlaceEmployment as Defendants_PlaceEmployment, t2.MotherMaiden as Defendants_MotherMaiden, t2.Citizen as Defendants_Citizen, t2.EducationId as Defendants_EducationId, t2.SpecialNeeds as Defendants_SpecialNeeds, t2.Condition as Defendants_Condition, t2.SafetyBelt as Defendants_SafetyBelt, t2.Helmet as Defendants_Helmet, t2.DpsSid as Defendants_DpsSid, t2.StepFunded as Defendants_StepFunded, t2.Training as Defendants_Training, t2.ActivityType as Defendants_ActivityType, t2.OfficerStepShiftId as Defendants_OfficerStepShiftId, t2.StepZoneId as Defendants_StepZoneId, t2.ZoneId as Defendants_ZoneId, t2.StepGrantTypeId as Defendants_StepGrantTypeId, t2.OldCaseID as Defendants_OldCaseID
FROM DUI.DefendantInterview t1
LEFT JOIN DUI.Defendants t2 ON t1.DefendantId = t2.DefendantId
WHERE t1.DefendantId IS NOT NULL


-- Simple view for DefendantInterviewQuestions
-- Provides secure access to DefendantInterviewQuestions data excluding sensitive information
CREATE VIEW DUI.v_defendantinterviewquestions AS
SELECT DefendantInterviewQuestionId, DefendantInterviewId, InterviewQuestionId, Answer, OLD_CASE_QUESTION_ID
FROM DUI.DefendantInterviewQuestions
WHERE DefendantInterviewQuestionId IS NOT NULL


-- Relationship view: DefendantInterviewQuestions with DefendantInterview
-- Provides DefendantInterviewQuestions data joined with related DefendantInterview information
CREATE VIEW DUI.v_defendantinterviewquestions_with_defendantinterview AS
SELECT t1.DefendantInterviewQuestionId, t1.DefendantInterviewId, t1.InterviewQuestionId, t1.Answer, t1.OLD_CASE_QUESTION_ID, t2.DefendantInterviewId as DefendantInterview_DefendantInterviewId, t2.DefendantId as DefendantInterview_DefendantId, t2.MirandaWarningRead as DefendantInterview_MirandaWarningRead, t2.MirandaInEnglish as DefendantInterview_MirandaInEnglish, t2.MirandaInSpanish as DefendantInterview_MirandaInSpanish, t2.StatedUnderstood as DefendantInterview_StatedUnderstood, t2.ReadBy as DefendantInterview_ReadBy, t2.TimeRead as DefendantInterview_TimeRead, t2.Comments as DefendantInterview_Comments, t2.AskOnVideo as DefendantInterview_AskOnVideo, t2.DefendantSpeech as DefendantInterview_DefendantSpeech, t2.DoNotAskQuestion as DefendantInterview_DoNotAskQuestion, t2.DoNotAskQuestionForLanguage as DefendantInterview_DoNotAskQuestionForLanguage, t2.Interviewer as DefendantInterview_Interviewer, t2.InterviewerId as DefendantInterview_InterviewerId, t2.RefuseToAnswer as DefendantInterview_RefuseToAnswer, t2.UnusualActions as DefendantInterview_UnusualActions, t2.TimeOfInterview as DefendantInterview_TimeOfInterview
FROM DUI.DefendantInterviewQuestions t1
LEFT JOIN DUI.DefendantInterview t2 ON t1.DefendantInterviewId = t2.DefendantInterviewId
WHERE t1.DefendantInterviewId IS NOT NULL


-- Simple view for DefendantObservations
-- Provides secure access to DefendantObservations data excluding sensitive information
CREATE VIEW DUI.v_defendantobservations AS
SELECT DefendantObservationId, DefendantId, ClothingDisorderly, ClothingSoiled, ClothingStained, ClothingTorn, ClothingOrderly, BalanceSwaying, BalanceUnsteady, BalanceNeededSupport, BalanceFallingDown, BalanceNormal, WalkingStaggering, WalkingFalling, WalkingSwaying, WalkingHeavyFooted, WalkingNormal, SpeakingSlurred, SpeakingIncoherent, SpeakingThickTongued, SpeakingSlowMumbled, SpeakingNormal, EyesRed, EyesWatering, EyesDilated, EyesDroopyEyelids, EyesNormal, AlcoholTypeId, OdorStrength, AttitudeCooperative, AttitudeCombative, AttitudeIndifferent, AttitudeCocky, AttitudeApologetic, AttitudeUncooperative, UnusualActionsObserved, ImpairmentAlcoholDrug, DrugGroupCNSDepressant, DrugGroupCNSStimulant, DrugGroupHallucinogen, DrugGroupAnesthetics, DrugGroupAnalgesic, DrugGroupInhalant, DrugGroupCannabis, OtherObservationsComments, WhySuspected, DREPresent, DREPerformed, WhoPerformedDRE, DRENotPerformedExplaination, DREComments, OnsetDegree, DreOnly, DrugReasonSuspected, OLD_CASE_OBSERVATION_ID
FROM DUI.DefendantObservations
WHERE DefendantObservationId IS NOT NULL


-- Relationship view: DefendantObservations with Defendants
-- Provides DefendantObservations data joined with related Defendants information
CREATE VIEW DUI.v_defendantobservations_with_defendants AS
SELECT t1.DefendantObservationId, t1.DefendantId, t1.ClothingDisorderly, t1.ClothingSoiled, t1.ClothingStained, t1.ClothingTorn, t1.ClothingOrderly, t1.BalanceSwaying, t1.BalanceUnsteady, t1.BalanceNeededSupport, t1.BalanceFallingDown, t1.BalanceNormal, t1.WalkingStaggering, t1.WalkingFalling, t1.WalkingSwaying, t1.WalkingHeavyFooted, t1.WalkingNormal, t1.SpeakingSlurred, t1.SpeakingIncoherent, t1.SpeakingThickTongued, t1.SpeakingSlowMumbled, t1.SpeakingNormal, t1.EyesRed, t1.EyesWatering, t1.EyesDilated, t1.EyesDroopyEyelids, t1.EyesNormal, t1.AlcoholTypeId, t1.OdorStrength, t1.AttitudeCooperative, t1.AttitudeCombative, t1.AttitudeIndifferent, t1.AttitudeCocky, t1.AttitudeApologetic, t1.AttitudeUncooperative, t1.UnusualActionsObserved, t1.ImpairmentAlcoholDrug, t1.DrugGroupCNSDepressant, t1.DrugGroupCNSStimulant, t1.DrugGroupHallucinogen, t1.DrugGroupAnesthetics, t1.DrugGroupAnalgesic, t1.DrugGroupInhalant, t1.DrugGroupCannabis, t1.OtherObservationsComments, t1.WhySuspected, t1.DREPresent, t1.DREPerformed, t1.WhoPerformedDRE, t1.DRENotPerformedExplaination, t1.DREComments, t1.OnsetDegree, t1.DreOnly, t1.DrugReasonSuspected, t1.OLD_CASE_OBSERVATION_ID, t2.DefendantId as Defendants_DefendantId, t2.CaseId as Defendants_CaseId, t2.LastName as Defendants_LastName, t2.FirstName as Defendants_FirstName, t2.RaceId as Defendants_RaceId, t2.GenderId as Defendants_GenderId, t2.HeightIn as Defendants_HeightIn, t2.HeightFt as Defendants_HeightFt, t2.HairColorId as Defendants_HairColorId, t2.EyeColorId as Defendants_EyeColorId, t2.Weight as Defendants_Weight, t2.SkinId as Defendants_SkinId, t2.SkinComplexionSkinId as Defendants_SkinComplexionSkinId, t2.Tattoos as Defendants_Tattoos, t2.Alias as Defendants_Alias, t2.Occupation as Defendants_Occupation, t2.PlaceEmployment as Defendants_PlaceEmployment, t2.MotherMaiden as Defendants_MotherMaiden, t2.Citizen as Defendants_Citizen, t2.EducationId as Defendants_EducationId, t2.SpecialNeeds as Defendants_SpecialNeeds, t2.Condition as Defendants_Condition, t2.SafetyBelt as Defendants_SafetyBelt, t2.Helmet as Defendants_Helmet, t2.DpsSid as Defendants_DpsSid, t2.StepFunded as Defendants_StepFunded, t2.Training as Defendants_Training, t2.ActivityType as Defendants_ActivityType, t2.OfficerStepShiftId as Defendants_OfficerStepShiftId, t2.StepZoneId as Defendants_StepZoneId, t2.ZoneId as Defendants_ZoneId, t2.StepGrantTypeId as Defendants_StepGrantTypeId, t2.OldCaseID as Defendants_OldCaseID
FROM DUI.DefendantObservations t1
LEFT JOIN DUI.Defendants t2 ON t1.DefendantId = t2.DefendantId
WHERE t1.DefendantId IS NOT NULL


-- Simple view for DefendantOccupationAddress
-- Provides secure access to DefendantOccupationAddress data excluding sensitive information
CREATE VIEW DUI.v_defendantoccupationaddress AS
SELECT DefendantId, StateId
FROM DUI.DefendantOccupationAddress
WHERE DefendantOccupationAddressId IS NOT NULL


-- Relationship view: DefendantOccupationAddress with TBL_OPT_States
-- Provides DefendantOccupationAddress data joined with related TBL_OPT_States information
CREATE VIEW DUI.v_defendantoccupationaddress_with_tbl_opt_states AS
SELECT t1.DefendantId, t1.StateId, t2.StateId as TBL_OPT_States_StateId, t2.StateName as TBL_OPT_States_StateName, t2.Abbreviation as TBL_OPT_States_Abbreviation, t2.Active as TBL_OPT_States_Active
FROM DUI.DefendantOccupationAddress t1
LEFT JOIN DUI.TBL_OPT_States t2 ON t1.StateId = t2.StateId
WHERE t1.StateId IS NOT NULL


-- Simple view for DefendantStatement
-- Provides secure access to DefendantStatement data excluding sensitive information
CREATE VIEW DUI.v_defendantstatement AS
SELECT DefendantId, LeaveBusinessServedAlcohol, NameOfBusiness, WhoObservedDrinking, Under21AlcoholConsumeLocation, StateId, CountyId, Lat, Lng, DidEMSResponse, NamesOfEMSUnit, Unit, WhatTheyDid, LocationBusinessBlock
FROM DUI.DefendantStatement
WHERE DefendantStatementId IS NOT NULL


-- Relationship view: DefendantStatement with Defendants
-- Provides DefendantStatement data joined with related Defendants information
CREATE VIEW DUI.v_defendantstatement_with_defendants AS
SELECT t1.DefendantId, t1.LeaveBusinessServedAlcohol, t1.NameOfBusiness, t1.WhoObservedDrinking, t1.Under21AlcoholConsumeLocation, t1.StateId, t1.CountyId, t1.Lat, t1.Lng, t1.DidEMSResponse, t1.NamesOfEMSUnit, t1.Unit, t1.WhatTheyDid, t1.LocationBusinessBlock, t2.DefendantId as Defendants_DefendantId, t2.CaseId as Defendants_CaseId, t2.LastName as Defendants_LastName, t2.FirstName as Defendants_FirstName, t2.RaceId as Defendants_RaceId, t2.GenderId as Defendants_GenderId, t2.HeightIn as Defendants_HeightIn, t2.HeightFt as Defendants_HeightFt, t2.HairColorId as Defendants_HairColorId, t2.EyeColorId as Defendants_EyeColorId, t2.Weight as Defendants_Weight, t2.SkinId as Defendants_SkinId, t2.SkinComplexionSkinId as Defendants_SkinComplexionSkinId, t2.Tattoos as Defendants_Tattoos, t2.Alias as Defendants_Alias, t2.Occupation as Defendants_Occupation, t2.PlaceEmployment as Defendants_PlaceEmployment, t2.MotherMaiden as Defendants_MotherMaiden, t2.Citizen as Defendants_Citizen, t2.EducationId as Defendants_EducationId, t2.SpecialNeeds as Defendants_SpecialNeeds, t2.Condition as Defendants_Condition, t2.SafetyBelt as Defendants_SafetyBelt, t2.Helmet as Defendants_Helmet, t2.DpsSid as Defendants_DpsSid, t2.StepFunded as Defendants_StepFunded, t2.Training as Defendants_Training, t2.ActivityType as Defendants_ActivityType, t2.OfficerStepShiftId as Defendants_OfficerStepShiftId, t2.StepZoneId as Defendants_StepZoneId, t2.ZoneId as Defendants_ZoneId, t2.StepGrantTypeId as Defendants_StepGrantTypeId, t2.OldCaseID as Defendants_OldCaseID
FROM DUI.DefendantStatement t1
LEFT JOIN DUI.Defendants t2 ON t1.DefendantId = t2.DefendantId
WHERE t1.DefendantId IS NOT NULL


-- Simple view for Defendants
-- Provides secure access to Defendants data excluding sensitive information
CREATE VIEW DUI.v_defendants AS
SELECT DefendantId, CaseId, LastName, FirstName, RaceId, GenderId, HeightIn, HeightFt, HairColorId, EyeColorId, Weight, SkinId, SkinComplexionSkinId, Tattoos, Alias, Occupation, PlaceEmployment, MotherMaiden, Citizen, EducationId, SpecialNeeds, Condition, SafetyBelt, Helmet, DpsSid, StepFunded, Training, ActivityType, OfficerStepShiftId, StepZoneId, ZoneId, StepGrantTypeId, OldCaseID
FROM DUI.Defendants
WHERE DefendantId IS NOT NULL


-- Relationship view: Defendants with CaseHeaders
-- Provides Defendants data joined with related CaseHeaders information
CREATE VIEW DUI.v_defendants_with_caseheaders AS
SELECT t1.DefendantId, t1.CaseId, t1.LastName, t1.FirstName, t1.RaceId, t1.GenderId, t1.HeightIn, t1.HeightFt, t1.HairColorId, t1.EyeColorId, t1.Weight, t1.SkinId, t1.SkinComplexionSkinId, t1.Tattoos, t1.Alias, t1.Occupation, t1.PlaceEmployment, t1.MotherMaiden, t1.Citizen, t1.EducationId, t1.SpecialNeeds, t1.Condition, t1.SafetyBelt, t1.Helmet, t1.DpsSid, t1.StepFunded, t1.Training, t1.ActivityType, t1.OfficerStepShiftId, t1.StepZoneId, t1.ZoneId, t1.StepGrantTypeId, t1.OldCaseID, t2.CaseId as CaseHeaders_CaseId, t2.UniqueId as CaseHeaders_UniqueId, t2.StatusId as CaseHeaders_StatusId, t2.ModelId as CaseHeaders_ModelId, t2.LockedByOfficerId as CaseHeaders_LockedByOfficerId, t2.ApprovedByOfficerId as CaseHeaders_ApprovedByOfficerId, t2.OrganizationId as CaseHeaders_OrganizationId, t2.LocationId as CaseHeaders_LocationId, t2.District as CaseHeaders_District, t2.Grid as CaseHeaders_Grid, t2.Version as CaseHeaders_Version, t2.Active as CaseHeaders_Active, t2.ModeId as CaseHeaders_ModeId, t2.ProbableCause as CaseHeaders_ProbableCause, t2.IsTrainingPurpose as CaseHeaders_IsTrainingPurpose, t2.PaidTxDOT as CaseHeaders_PaidTxDOT, t2.StepGrantTypeId as CaseHeaders_StepGrantTypeId, t2.CaseOwnerAgency as CaseHeaders_CaseOwnerAgency, t2.CaseOwnerBadge as CaseHeaders_CaseOwnerBadge, t2.CaseOwnerDepartmentId as CaseHeaders_CaseOwnerDepartmentId, t2.CaseOwnerId as CaseHeaders_CaseOwnerId, t2.CaseOwnerName as CaseHeaders_CaseOwnerName, t2.CaseOwnerRank as CaseHeaders_CaseOwnerRank, t2.TABC as CaseHeaders_TABC, t2.AdditionalInformation as CaseHeaders_AdditionalInformation, t2.ActivityType as CaseHeaders_ActivityType, t2.OfficerStepShiftId as CaseHeaders_OfficerStepShiftId, t2.StepZoneId as CaseHeaders_StepZoneId, t2.OldCaseID as CaseHeaders_OldCaseID
FROM DUI.Defendants t1
LEFT JOIN DUI.CaseHeaders t2 ON t1.CaseId = t2.CaseId
WHERE t1.CaseId IS NOT NULL


-- Simple view for Documents
-- Provides secure access to Documents data excluding sensitive information
CREATE VIEW DUI.v_documents AS
SELECT DocumentId, DocumentTypeId, FileTypeId, DocumentName, OriginalFileName, PhysicalFileName, Active, Created, CreatedBy, ObjectId, ObjectTypeId, OldDocumentId
FROM DUI.Documents
WHERE DocumentId IS NOT NULL


-- Relationship view: Documents with TBL_OPT_DocumentFileTypes
-- Provides Documents data joined with related TBL_OPT_DocumentFileTypes information
CREATE VIEW DUI.v_documents_with_tbl_opt_documentfiletypes AS
SELECT t1.DocumentId, t1.DocumentTypeId, t1.FileTypeId, t1.DocumentName, t1.OriginalFileName, t1.PhysicalFileName, t1.Active, t1.Created, t1.CreatedBy, t1.ObjectId, t1.ObjectTypeId, t1.OldDocumentId, t2.FileTypeId as TBL_OPT_DocumentFileTypes_FileTypeId, t2.FileName as TBL_OPT_DocumentFileTypes_FileName, t2.Extension as TBL_OPT_DocumentFileTypes_Extension, t2.Icon as TBL_OPT_DocumentFileTypes_Icon, t2.Image as TBL_OPT_DocumentFileTypes_Image, t2.MimeType as TBL_OPT_DocumentFileTypes_MimeType, t2.Active as TBL_OPT_DocumentFileTypes_Active, t2.Created as TBL_OPT_DocumentFileTypes_Created
FROM DUI.Documents t1
LEFT JOIN DUI.TBL_OPT_DocumentFileTypes t2 ON t1.FileTypeId = t2.FileTypeId
WHERE t1.FileTypeId IS NOT NULL


-- Simple view for DuiCaseNoteType
-- Provides secure access to DuiCaseNoteType data excluding sensitive information
CREATE VIEW DUI.v_duicasenotetype AS
SELECT DuiCaseNoteTypeId, DuiCasePageId, Section, Active, NoteOrder
FROM DUI.DuiCaseNoteType
WHERE DuiCaseNoteTypeId IS NOT NULL


-- Relationship view: DuiCaseNoteType with SystemPages
-- Provides DuiCaseNoteType data joined with related SystemPages information
CREATE VIEW DUI.v_duicasenotetype_with_systempages AS
SELECT t1.DuiCaseNoteTypeId, t1.DuiCasePageId, t1.Section, t1.Active, t1.NoteOrder, t2.SystemPageId as SystemPages_SystemPageId, t2.Title as SystemPages_Title, t2.PageName as SystemPages_PageName, t2.Active as SystemPages_Active, t2.Created as SystemPages_Created, t2.OldSystemPageId as SystemPages_OldSystemPageId
FROM DUI.DuiCaseNoteType t1
LEFT JOIN DUI.SystemPages t2 ON t1.DuiCasePageId = t2.SystemPageId
WHERE t1.DuiCasePageId IS NOT NULL


-- Simple view for DuiCaseNotes
-- Provides secure access to DuiCaseNotes data excluding sensitive information
CREATE VIEW DUI.v_duicasenotes AS
SELECT DuiCaseNoteId, DuiCaseId, DuiCaseNoteTypeId, ParentId, CreatedById
FROM DUI.DuiCaseNotes
WHERE DuiCaseNoteId IS NOT NULL


-- Relationship view: DuiCaseNotes with CaseHeaders
-- Provides DuiCaseNotes data joined with related CaseHeaders information
CREATE VIEW DUI.v_duicasenotes_with_caseheaders AS
SELECT t1.DuiCaseNoteId, t1.DuiCaseId, t1.DuiCaseNoteTypeId, t1.ParentId, t1.CreatedById, t2.CaseId as CaseHeaders_CaseId, t2.UniqueId as CaseHeaders_UniqueId, t2.StatusId as CaseHeaders_StatusId, t2.ModelId as CaseHeaders_ModelId, t2.LockedByOfficerId as CaseHeaders_LockedByOfficerId, t2.ApprovedByOfficerId as CaseHeaders_ApprovedByOfficerId, t2.OrganizationId as CaseHeaders_OrganizationId, t2.LocationId as CaseHeaders_LocationId, t2.District as CaseHeaders_District, t2.Grid as CaseHeaders_Grid, t2.Version as CaseHeaders_Version, t2.Active as CaseHeaders_Active, t2.ModeId as CaseHeaders_ModeId, t2.ProbableCause as CaseHeaders_ProbableCause, t2.IsTrainingPurpose as CaseHeaders_IsTrainingPurpose, t2.PaidTxDOT as CaseHeaders_PaidTxDOT, t2.StepGrantTypeId as CaseHeaders_StepGrantTypeId, t2.CaseOwnerAgency as CaseHeaders_CaseOwnerAgency, t2.CaseOwnerBadge as CaseHeaders_CaseOwnerBadge, t2.CaseOwnerDepartmentId as CaseHeaders_CaseOwnerDepartmentId, t2.CaseOwnerId as CaseHeaders_CaseOwnerId, t2.CaseOwnerName as CaseHeaders_CaseOwnerName, t2.CaseOwnerRank as CaseHeaders_CaseOwnerRank, t2.TABC as CaseHeaders_TABC, t2.AdditionalInformation as CaseHeaders_AdditionalInformation, t2.ActivityType as CaseHeaders_ActivityType, t2.OfficerStepShiftId as CaseHeaders_OfficerStepShiftId, t2.StepZoneId as CaseHeaders_StepZoneId, t2.OldCaseID as CaseHeaders_OldCaseID
FROM DUI.DuiCaseNotes t1
LEFT JOIN DUI.CaseHeaders t2 ON t1.DuiCaseId = t2.CaseId
WHERE t1.DuiCaseId IS NOT NULL


-- Simple view for DuiCaseToxSpec
-- Provides secure access to DuiCaseToxSpec data excluding sensitive information
CREATE VIEW DUI.v_duicasetoxspec AS
SELECT DuiCaseToxSpecId, CaseToxId, ToxSpecTypeId, BacResult, HospSerResult, WholeBloodResult, Active, DtCreated, NoAlcohol, OldCaseToxSpecId
FROM DUI.DuiCaseToxSpec
WHERE DuiCaseToxSpecId IS NOT NULL


-- Simple view for DuiToxicologyDrug
-- Provides secure access to DuiToxicologyDrug data excluding sensitive information
CREATE VIEW DUI.v_duitoxicologydrug AS
SELECT DuiCaseToxDrugId, IntoxilyzerReportId, DuiCaseToxSpecId, DpsDrugListId, DrugResult, DrugMeasurement, OldToxicologyDrugId
FROM DUI.DuiToxicologyDrug
WHERE DuiCaseToxDrugId IS NOT NULL


-- Simple view for DuiToxilyzerReport
-- Provides secure access to DuiToxilyzerReport data excluding sensitive information
CREATE VIEW DUI.v_duitoxilyzerreport AS
SELECT ToxilyzerReportId, OfficerId, DefLastName, DefFirstName, DeptId, CaseId, Submitted, Active, DtCreated, CreatedBy, OldCaseToxId
FROM DUI.DuiToxilyzerReport
WHERE ToxilyzerReportId IS NOT NULL


-- Simple view for EvidenceDocuments
-- Provides secure access to EvidenceDocuments data excluding sensitive information
CREATE VIEW DUI.v_evidencedocuments AS
SELECT EvidenceDocumentId, CaseId, DocumentId, UploadedBy, Uploaded, DocumentTypeId
FROM DUI.EvidenceDocuments
WHERE EvidenceDocumentId IS NOT NULL


-- Relationship view: EvidenceDocuments with CaseHeaders
-- Provides EvidenceDocuments data joined with related CaseHeaders information
CREATE VIEW DUI.v_evidencedocuments_with_caseheaders AS
SELECT t1.EvidenceDocumentId, t1.CaseId, t1.DocumentId, t1.UploadedBy, t1.Uploaded, t1.DocumentTypeId, t2.CaseId as CaseHeaders_CaseId, t2.UniqueId as CaseHeaders_UniqueId, t2.StatusId as CaseHeaders_StatusId, t2.ModelId as CaseHeaders_ModelId, t2.LockedByOfficerId as CaseHeaders_LockedByOfficerId, t2.ApprovedByOfficerId as CaseHeaders_ApprovedByOfficerId, t2.OrganizationId as CaseHeaders_OrganizationId, t2.LocationId as CaseHeaders_LocationId, t2.District as CaseHeaders_District, t2.Grid as CaseHeaders_Grid, t2.Version as CaseHeaders_Version, t2.Active as CaseHeaders_Active, t2.ModeId as CaseHeaders_ModeId, t2.ProbableCause as CaseHeaders_ProbableCause, t2.IsTrainingPurpose as CaseHeaders_IsTrainingPurpose, t2.PaidTxDOT as CaseHeaders_PaidTxDOT, t2.StepGrantTypeId as CaseHeaders_StepGrantTypeId, t2.CaseOwnerAgency as CaseHeaders_CaseOwnerAgency, t2.CaseOwnerBadge as CaseHeaders_CaseOwnerBadge, t2.CaseOwnerDepartmentId as CaseHeaders_CaseOwnerDepartmentId, t2.CaseOwnerId as CaseHeaders_CaseOwnerId, t2.CaseOwnerName as CaseHeaders_CaseOwnerName, t2.CaseOwnerRank as CaseHeaders_CaseOwnerRank, t2.TABC as CaseHeaders_TABC, t2.AdditionalInformation as CaseHeaders_AdditionalInformation, t2.ActivityType as CaseHeaders_ActivityType, t2.OfficerStepShiftId as CaseHeaders_OfficerStepShiftId, t2.StepZoneId as CaseHeaders_StepZoneId, t2.OldCaseID as CaseHeaders_OldCaseID
FROM DUI.EvidenceDocuments t1
LEFT JOIN DUI.CaseHeaders t2 ON t1.CaseId = t2.CaseId
WHERE t1.CaseId IS NOT NULL


-- Simple view for EvidenceRecordings
-- Provides secure access to EvidenceRecordings data excluding sensitive information
CREATE VIEW DUI.v_evidencerecordings AS
SELECT EvidenceRecordingId, PhysicalEvidenceId, TimeBegan, TimeStop, OnBoatRecording, OnShoreRecording, OnBodyCameraRecording, IntoxicationInvestigation, FST, TransportToJail, OtherActions, NameOfOfficer, HasVideoTape, NoTapeExplain, EvVideoMade, EvVideoHgn, EvVideoWalkTurn, EvVideoLegStand, EvVideoDisposition, EvVideoCar, EvVideoStation, EvVideoOtherMade
FROM DUI.EvidenceRecordings
WHERE EvidenceRecordingId IS NOT NULL


-- Relationship view: EvidenceRecordings with PhysicalEvidence
-- Provides EvidenceRecordings data joined with related PhysicalEvidence information
CREATE VIEW DUI.v_evidencerecordings_with_physicalevidence AS
SELECT t1.EvidenceRecordingId, t1.PhysicalEvidenceId, t1.TimeBegan, t1.TimeStop, t1.OnBoatRecording, t1.OnShoreRecording, t1.OnBodyCameraRecording, t1.IntoxicationInvestigation, t1.FST, t1.TransportToJail, t1.OtherActions, t1.NameOfOfficer, t1.HasVideoTape, t1.NoTapeExplain, t1.EvVideoMade, t1.EvVideoHgn, t1.EvVideoWalkTurn, t1.EvVideoLegStand, t1.EvVideoDisposition, t1.EvVideoCar, t1.EvVideoStation, t1.EvVideoOtherMade, t2.PhysicalEvidenceId as PhysicalEvidence_PhysicalEvidenceId, t2.CaseId as PhysicalEvidence_CaseId, t2.DispatchRecordingInclude as PhysicalEvidence_DispatchRecordingInclude, t2.ExplainDispatchRecording as PhysicalEvidence_ExplainDispatchRecording, t2.OtherPhysicalEvidence as PhysicalEvidence_OtherPhysicalEvidence, t2.HasVideoTape as PhysicalEvidence_HasVideoTape, t2.NoTapeExplain as PhysicalEvidence_NoTapeExplain, t2.EvEvidenceDisposition as PhysicalEvidence_EvEvidenceDisposition, t2.Ev911TapeDisposition as PhysicalEvidence_Ev911TapeDisposition, t2.OldCaseID as PhysicalEvidence_OldCaseID
FROM DUI.EvidenceRecordings t1
LEFT JOIN DUI.PhysicalEvidence t2 ON t1.PhysicalEvidenceId = t2.PhysicalEvidenceId
WHERE t1.PhysicalEvidenceId IS NOT NULL


-- Simple view for FSTFingerToNoseTest
-- Provides secure access to FSTFingerToNoseTest data excluding sensitive information
CREATE VIEW DUI.v_fstfingertonosetest AS
SELECT FingerToNoseId, CaseId, TestGiven, ReasonNotGiven, StoppedTest, StatedFingerToNose, UnableToFollow, UnableToFollowDesc, StartWrongTime, StartWrongTimeDesc, NotCloseEyes, NotCloseEyesDesc, NotTiltHead, NotTiltHeadDesc, OpenEyes, OpenEyesDesc, MovedHead, MovedHeadDesc, WrongHandRight1, WrongHandRight2, WrongHandRight3, WrongFingerLeft1, WrongFingerRight1, WrongFingerLeft2, WrongFingerRight2, WrongFingerLeft3, WrongFingerRight3, HesitatedRight1, HesitatedRight2, HesitatedRight3, SearchedRight1, SearchedRight2, SearchedRight3, FingerTipLeft1, FingerTipRight1, FingerTipLeft2, FingerTipRight2, FingerTipLeft3, FingerTipRight3, MissedNoseLeft1, MissedNoseRight1, MissedNoseLeft2, MissedNoseRight2, MissedNoseLeft3, MissedNoseRight3, BringDownLeft1, BringDownRight1, BringDownLeft2, BringDownRight2, BringDownLeft3, BringDownRight3, Comments
FROM DUI.FSTFingerToNoseTest
WHERE FingerToNoseId IS NOT NULL


-- Relationship view: FSTFingerToNoseTest with CaseHeaders
-- Provides FSTFingerToNoseTest data joined with related CaseHeaders information
CREATE VIEW DUI.v_fstfingertonosetest_with_caseheaders AS
SELECT t1.FingerToNoseId, t1.CaseId, t1.TestGiven, t1.ReasonNotGiven, t1.StoppedTest, t1.StatedFingerToNose, t1.UnableToFollow, t1.UnableToFollowDesc, t1.StartWrongTime, t1.StartWrongTimeDesc, t1.NotCloseEyes, t1.NotCloseEyesDesc, t1.NotTiltHead, t1.NotTiltHeadDesc, t1.OpenEyes, t1.OpenEyesDesc, t1.MovedHead, t1.MovedHeadDesc, t1.WrongHandRight1, t1.WrongHandRight2, t1.WrongHandRight3, t1.WrongFingerLeft1, t1.WrongFingerRight1, t1.WrongFingerLeft2, t1.WrongFingerRight2, t1.WrongFingerLeft3, t1.WrongFingerRight3, t1.HesitatedRight1, t1.HesitatedRight2, t1.HesitatedRight3, t1.SearchedRight1, t1.SearchedRight2, t1.SearchedRight3, t1.FingerTipLeft1, t1.FingerTipRight1, t1.FingerTipLeft2, t1.FingerTipRight2, t1.FingerTipLeft3, t1.FingerTipRight3, t1.MissedNoseLeft1, t1.MissedNoseRight1, t1.MissedNoseLeft2, t1.MissedNoseRight2, t1.MissedNoseLeft3, t1.MissedNoseRight3, t1.BringDownLeft1, t1.BringDownRight1, t1.BringDownLeft2, t1.BringDownRight2, t1.BringDownLeft3, t1.BringDownRight3, t1.Comments, t2.CaseId as CaseHeaders_CaseId, t2.UniqueId as CaseHeaders_UniqueId, t2.StatusId as CaseHeaders_StatusId, t2.ModelId as CaseHeaders_ModelId, t2.LockedByOfficerId as CaseHeaders_LockedByOfficerId, t2.ApprovedByOfficerId as CaseHeaders_ApprovedByOfficerId, t2.OrganizationId as CaseHeaders_OrganizationId, t2.LocationId as CaseHeaders_LocationId, t2.District as CaseHeaders_District, t2.Grid as CaseHeaders_Grid, t2.Version as CaseHeaders_Version, t2.Active as CaseHeaders_Active, t2.ModeId as CaseHeaders_ModeId, t2.ProbableCause as CaseHeaders_ProbableCause, t2.IsTrainingPurpose as CaseHeaders_IsTrainingPurpose, t2.PaidTxDOT as CaseHeaders_PaidTxDOT, t2.StepGrantTypeId as CaseHeaders_StepGrantTypeId, t2.CaseOwnerAgency as CaseHeaders_CaseOwnerAgency, t2.CaseOwnerBadge as CaseHeaders_CaseOwnerBadge, t2.CaseOwnerDepartmentId as CaseHeaders_CaseOwnerDepartmentId, t2.CaseOwnerId as CaseHeaders_CaseOwnerId, t2.CaseOwnerName as CaseHeaders_CaseOwnerName, t2.CaseOwnerRank as CaseHeaders_CaseOwnerRank, t2.TABC as CaseHeaders_TABC, t2.AdditionalInformation as CaseHeaders_AdditionalInformation, t2.ActivityType as CaseHeaders_ActivityType, t2.OfficerStepShiftId as CaseHeaders_OfficerStepShiftId, t2.StepZoneId as CaseHeaders_StepZoneId, t2.OldCaseID as CaseHeaders_OldCaseID
FROM DUI.FSTFingerToNoseTest t1
LEFT JOIN DUI.CaseHeaders t2 ON t1.CaseId = t2.CaseId
WHERE t1.CaseId IS NOT NULL


-- Simple view for FSTHandCoordination
-- Provides secure access to FSTHandCoordination data excluding sensitive information
CREATE VIEW DUI.v_fsthandcoordination AS
SELECT HandCoordinationId, CaseId, TestGiven, ReasonNotGiven, StoppedTest, StatedHandCoordination, UnableToFollow, UnableToFollowDesc, StartWrongTime, StartWrongTimeDesc, ForwardImproperCount, ForwardImproperCountDesc, ForwardImproperTouch, ForwardImproperTouchDesc, ForwardNotPerform, ForwardNotPerformDesc, ClappingImproperCount, ClappingImproperCountDesc, ClappingImproperTouch, ClappingImproperTouchDesc, ClappingImproperReturn, ClappingImproperReturnDesc, ClappingNotPerform, ClappingNotPerformDesc, ReturnImproperCount, ReturnImproperCountDesc, ReturnImproperTouch, ReturnImproperTouchDesc, NotReturnToChest, NotReturnToChestDesc, ReturnNotPerform, ReturnNotPerformDesc, ImproperPosition, ImproperPositionDesc, EndPositionNotPerform, EndPositionNotPerformDesc, TotalClues, Comments
FROM DUI.FSTHandCoordination
WHERE HandCoordinationId IS NOT NULL


-- Relationship view: FSTHandCoordination with CaseHeaders
-- Provides FSTHandCoordination data joined with related CaseHeaders information
CREATE VIEW DUI.v_fsthandcoordination_with_caseheaders AS
SELECT t1.HandCoordinationId, t1.CaseId, t1.TestGiven, t1.ReasonNotGiven, t1.StoppedTest, t1.StatedHandCoordination, t1.UnableToFollow, t1.UnableToFollowDesc, t1.StartWrongTime, t1.StartWrongTimeDesc, t1.ForwardImproperCount, t1.ForwardImproperCountDesc, t1.ForwardImproperTouch, t1.ForwardImproperTouchDesc, t1.ForwardNotPerform, t1.ForwardNotPerformDesc, t1.ClappingImproperCount, t1.ClappingImproperCountDesc, t1.ClappingImproperTouch, t1.ClappingImproperTouchDesc, t1.ClappingImproperReturn, t1.ClappingImproperReturnDesc, t1.ClappingNotPerform, t1.ClappingNotPerformDesc, t1.ReturnImproperCount, t1.ReturnImproperCountDesc, t1.ReturnImproperTouch, t1.ReturnImproperTouchDesc, t1.NotReturnToChest, t1.NotReturnToChestDesc, t1.ReturnNotPerform, t1.ReturnNotPerformDesc, t1.ImproperPosition, t1.ImproperPositionDesc, t1.EndPositionNotPerform, t1.EndPositionNotPerformDesc, t1.TotalClues, t1.Comments, t2.CaseId as CaseHeaders_CaseId, t2.UniqueId as CaseHeaders_UniqueId, t2.StatusId as CaseHeaders_StatusId, t2.ModelId as CaseHeaders_ModelId, t2.LockedByOfficerId as CaseHeaders_LockedByOfficerId, t2.ApprovedByOfficerId as CaseHeaders_ApprovedByOfficerId, t2.OrganizationId as CaseHeaders_OrganizationId, t2.LocationId as CaseHeaders_LocationId, t2.District as CaseHeaders_District, t2.Grid as CaseHeaders_Grid, t2.Version as CaseHeaders_Version, t2.Active as CaseHeaders_Active, t2.ModeId as CaseHeaders_ModeId, t2.ProbableCause as CaseHeaders_ProbableCause, t2.IsTrainingPurpose as CaseHeaders_IsTrainingPurpose, t2.PaidTxDOT as CaseHeaders_PaidTxDOT, t2.StepGrantTypeId as CaseHeaders_StepGrantTypeId, t2.CaseOwnerAgency as CaseHeaders_CaseOwnerAgency, t2.CaseOwnerBadge as CaseHeaders_CaseOwnerBadge, t2.CaseOwnerDepartmentId as CaseHeaders_CaseOwnerDepartmentId, t2.CaseOwnerId as CaseHeaders_CaseOwnerId, t2.CaseOwnerName as CaseHeaders_CaseOwnerName, t2.CaseOwnerRank as CaseHeaders_CaseOwnerRank, t2.TABC as CaseHeaders_TABC, t2.AdditionalInformation as CaseHeaders_AdditionalInformation, t2.ActivityType as CaseHeaders_ActivityType, t2.OfficerStepShiftId as CaseHeaders_OfficerStepShiftId, t2.StepZoneId as CaseHeaders_StepZoneId, t2.OldCaseID as CaseHeaders_OldCaseID
FROM DUI.FSTHandCoordination t1
LEFT JOIN DUI.CaseHeaders t2 ON t1.CaseId = t2.CaseId
WHERE t1.CaseId IS NOT NULL


-- Simple view for FSTHgnTest
-- Provides secure access to FSTHgnTest data excluding sensitive information
CREATE VIEW DUI.v_fsthgntest AS
SELECT HGNId, CaseId, HGNGiven, ReasonNotGiven, HeadInjuries, HeadInjuryExplain, WearGlass, WearGlassExplain, EqualPupilSize, EqualPupilSizeExplain, RestingNystagmus, EqualTracking, FollowStimulus, FollowStimulusExplain, StimulusAboveEyeLevel, ForwardEmergencyLightsActive, DefFacingFlashLight, FlashLightExplain, StatedHGN, LackOfPursuit, LackOfPursuitLeft, LackOfPursuitRight, MaximumDeviation, MaxDeviationLeft, MaxDeviationRight, NystagmusPrior, NystagmusPriorLeft, NystagmusPriorRight, AngleOfOnset, AngleOnsetNystagmus, VerticalNystagmus, TotalHGNClues, Comments, VerticalNystagmusLeft, VerticalNystagmusRight, HGNAdminbyReportingAgent, CluesLeft, CluesRight, OtherComment
FROM DUI.FSTHgnTest
WHERE HGNId IS NOT NULL


-- Relationship view: FSTHgnTest with CaseHeaders
-- Provides FSTHgnTest data joined with related CaseHeaders information
CREATE VIEW DUI.v_fsthgntest_with_caseheaders AS
SELECT t1.HGNId, t1.CaseId, t1.HGNGiven, t1.ReasonNotGiven, t1.HeadInjuries, t1.HeadInjuryExplain, t1.WearGlass, t1.WearGlassExplain, t1.EqualPupilSize, t1.EqualPupilSizeExplain, t1.RestingNystagmus, t1.EqualTracking, t1.FollowStimulus, t1.FollowStimulusExplain, t1.StimulusAboveEyeLevel, t1.ForwardEmergencyLightsActive, t1.DefFacingFlashLight, t1.FlashLightExplain, t1.StatedHGN, t1.LackOfPursuit, t1.LackOfPursuitLeft, t1.LackOfPursuitRight, t1.MaximumDeviation, t1.MaxDeviationLeft, t1.MaxDeviationRight, t1.NystagmusPrior, t1.NystagmusPriorLeft, t1.NystagmusPriorRight, t1.AngleOfOnset, t1.AngleOnsetNystagmus, t1.VerticalNystagmus, t1.TotalHGNClues, t1.Comments, t1.VerticalNystagmusLeft, t1.VerticalNystagmusRight, t1.HGNAdminbyReportingAgent, t1.CluesLeft, t1.CluesRight, t1.OtherComment, t2.CaseId as CaseHeaders_CaseId, t2.UniqueId as CaseHeaders_UniqueId, t2.StatusId as CaseHeaders_StatusId, t2.ModelId as CaseHeaders_ModelId, t2.LockedByOfficerId as CaseHeaders_LockedByOfficerId, t2.ApprovedByOfficerId as CaseHeaders_ApprovedByOfficerId, t2.OrganizationId as CaseHeaders_OrganizationId, t2.LocationId as CaseHeaders_LocationId, t2.District as CaseHeaders_District, t2.Grid as CaseHeaders_Grid, t2.Version as CaseHeaders_Version, t2.Active as CaseHeaders_Active, t2.ModeId as CaseHeaders_ModeId, t2.ProbableCause as CaseHeaders_ProbableCause, t2.IsTrainingPurpose as CaseHeaders_IsTrainingPurpose, t2.PaidTxDOT as CaseHeaders_PaidTxDOT, t2.StepGrantTypeId as CaseHeaders_StepGrantTypeId, t2.CaseOwnerAgency as CaseHeaders_CaseOwnerAgency, t2.CaseOwnerBadge as CaseHeaders_CaseOwnerBadge, t2.CaseOwnerDepartmentId as CaseHeaders_CaseOwnerDepartmentId, t2.CaseOwnerId as CaseHeaders_CaseOwnerId, t2.CaseOwnerName as CaseHeaders_CaseOwnerName, t2.CaseOwnerRank as CaseHeaders_CaseOwnerRank, t2.TABC as CaseHeaders_TABC, t2.AdditionalInformation as CaseHeaders_AdditionalInformation, t2.ActivityType as CaseHeaders_ActivityType, t2.OfficerStepShiftId as CaseHeaders_OfficerStepShiftId, t2.StepZoneId as CaseHeaders_StepZoneId, t2.OldCaseID as CaseHeaders_OldCaseID
FROM DUI.FSTHgnTest t1
LEFT JOIN DUI.CaseHeaders t2 ON t1.CaseId = t2.CaseId
WHERE t1.CaseId IS NOT NULL


-- Simple view for FSTOneLegStandTest
-- Provides secure access to FSTOneLegStandTest data excluding sensitive information
CREATE VIEW DUI.v_fstonelegstandtest AS
SELECT OneLegStandId, CaseId, OneLegStandGiven, ReasonNotGiven, TestStopped, StatedOneLegStand, FootStoodOn, FootRaised, FootwearId, NotKeepBalance, KeepBalanceExplain, Sways, SwaysDesc, Hops, HopsDesc, PutsFootDown, PutsFootDownDesc, UseArmsToBalance, ArmsBalanceDesc, OneLegClues, Comments, PhysicalInjuries, DescribeInjuries, DefMoreThan65, AllCluesAssigned, UnderstoodComments, StoodOnComments, ArchiveComments
FROM DUI.FSTOneLegStandTest
WHERE OneLegStandId IS NOT NULL


-- Relationship view: FSTOneLegStandTest with CaseHeaders
-- Provides FSTOneLegStandTest data joined with related CaseHeaders information
CREATE VIEW DUI.v_fstonelegstandtest_with_caseheaders AS
SELECT t1.OneLegStandId, t1.CaseId, t1.OneLegStandGiven, t1.ReasonNotGiven, t1.TestStopped, t1.StatedOneLegStand, t1.FootStoodOn, t1.FootRaised, t1.FootwearId, t1.NotKeepBalance, t1.KeepBalanceExplain, t1.Sways, t1.SwaysDesc, t1.Hops, t1.HopsDesc, t1.PutsFootDown, t1.PutsFootDownDesc, t1.UseArmsToBalance, t1.ArmsBalanceDesc, t1.OneLegClues, t1.Comments, t1.PhysicalInjuries, t1.DescribeInjuries, t1.DefMoreThan65, t1.AllCluesAssigned, t1.UnderstoodComments, t1.StoodOnComments, t1.ArchiveComments, t2.CaseId as CaseHeaders_CaseId, t2.UniqueId as CaseHeaders_UniqueId, t2.StatusId as CaseHeaders_StatusId, t2.ModelId as CaseHeaders_ModelId, t2.LockedByOfficerId as CaseHeaders_LockedByOfficerId, t2.ApprovedByOfficerId as CaseHeaders_ApprovedByOfficerId, t2.OrganizationId as CaseHeaders_OrganizationId, t2.LocationId as CaseHeaders_LocationId, t2.District as CaseHeaders_District, t2.Grid as CaseHeaders_Grid, t2.Version as CaseHeaders_Version, t2.Active as CaseHeaders_Active, t2.ModeId as CaseHeaders_ModeId, t2.ProbableCause as CaseHeaders_ProbableCause, t2.IsTrainingPurpose as CaseHeaders_IsTrainingPurpose, t2.PaidTxDOT as CaseHeaders_PaidTxDOT, t2.StepGrantTypeId as CaseHeaders_StepGrantTypeId, t2.CaseOwnerAgency as CaseHeaders_CaseOwnerAgency, t2.CaseOwnerBadge as CaseHeaders_CaseOwnerBadge, t2.CaseOwnerDepartmentId as CaseHeaders_CaseOwnerDepartmentId, t2.CaseOwnerId as CaseHeaders_CaseOwnerId, t2.CaseOwnerName as CaseHeaders_CaseOwnerName, t2.CaseOwnerRank as CaseHeaders_CaseOwnerRank, t2.TABC as CaseHeaders_TABC, t2.AdditionalInformation as CaseHeaders_AdditionalInformation, t2.ActivityType as CaseHeaders_ActivityType, t2.OfficerStepShiftId as CaseHeaders_OfficerStepShiftId, t2.StepZoneId as CaseHeaders_StepZoneId, t2.OldCaseID as CaseHeaders_OldCaseID
FROM DUI.FSTOneLegStandTest t1
LEFT JOIN DUI.CaseHeaders t2 ON t1.CaseId = t2.CaseId
WHERE t1.CaseId IS NOT NULL


-- Simple view for FSTOtherTest
-- Provides secure access to FSTOtherTest data excluding sensitive information
CREATE VIEW DUI.v_fstothertest AS
SELECT OtherTestId, CaseId, FingerCountGiven, FingerCountDesc, AlphabetTestGiven, AlphabetTestDesc, OtherTestDesc, StatedAlphabetTest, AlphabetTestGivenInstruction, AlphabetTestRefused, AlphabetTestComplete, AlphabetTestCompleteComments, AlphabetTestSang, AlphabetTestSangComments, AlphabetTestLetterRepeated, AlphabetTestLetterRepeatedComments, AlphabetTestHesitation, AlphabetTestHesitationComments, StatedFingerCountInstruction, FcGaveInstruction, FcRefused, FCComplete, FCCompleteDesc, FCMiscounted, FCMiscountedComments, FCSliding, FCSlidingComment, FCNoSpeedUp, FCNoSpeedUpComments, FCImproperTouch, FCImproperTouchComments, FCImproperCount, FCImproperCountComments, FCOtherObservation, FcSafety, ALetterStart, ALetterFinish, ASafety
FROM DUI.FSTOtherTest
WHERE OtherTestId IS NOT NULL


-- Relationship view: FSTOtherTest with CaseHeaders
-- Provides FSTOtherTest data joined with related CaseHeaders information
CREATE VIEW DUI.v_fstothertest_with_caseheaders AS
SELECT t1.OtherTestId, t1.CaseId, t1.FingerCountGiven, t1.FingerCountDesc, t1.AlphabetTestGiven, t1.AlphabetTestDesc, t1.OtherTestDesc, t1.StatedAlphabetTest, t1.AlphabetTestGivenInstruction, t1.AlphabetTestRefused, t1.AlphabetTestComplete, t1.AlphabetTestCompleteComments, t1.AlphabetTestSang, t1.AlphabetTestSangComments, t1.AlphabetTestLetterRepeated, t1.AlphabetTestLetterRepeatedComments, t1.AlphabetTestHesitation, t1.AlphabetTestHesitationComments, t1.StatedFingerCountInstruction, t1.FcGaveInstruction, t1.FcRefused, t1.FCComplete, t1.FCCompleteDesc, t1.FCMiscounted, t1.FCMiscountedComments, t1.FCSliding, t1.FCSlidingComment, t1.FCNoSpeedUp, t1.FCNoSpeedUpComments, t1.FCImproperTouch, t1.FCImproperTouchComments, t1.FCImproperCount, t1.FCImproperCountComments, t1.FCOtherObservation, t1.FcSafety, t1.ALetterStart, t1.ALetterFinish, t1.ASafety, t2.CaseId as CaseHeaders_CaseId, t2.UniqueId as CaseHeaders_UniqueId, t2.StatusId as CaseHeaders_StatusId, t2.ModelId as CaseHeaders_ModelId, t2.LockedByOfficerId as CaseHeaders_LockedByOfficerId, t2.ApprovedByOfficerId as CaseHeaders_ApprovedByOfficerId, t2.OrganizationId as CaseHeaders_OrganizationId, t2.LocationId as CaseHeaders_LocationId, t2.District as CaseHeaders_District, t2.Grid as CaseHeaders_Grid, t2.Version as CaseHeaders_Version, t2.Active as CaseHeaders_Active, t2.ModeId as CaseHeaders_ModeId, t2.ProbableCause as CaseHeaders_ProbableCause, t2.IsTrainingPurpose as CaseHeaders_IsTrainingPurpose, t2.PaidTxDOT as CaseHeaders_PaidTxDOT, t2.StepGrantTypeId as CaseHeaders_StepGrantTypeId, t2.CaseOwnerAgency as CaseHeaders_CaseOwnerAgency, t2.CaseOwnerBadge as CaseHeaders_CaseOwnerBadge, t2.CaseOwnerDepartmentId as CaseHeaders_CaseOwnerDepartmentId, t2.CaseOwnerId as CaseHeaders_CaseOwnerId, t2.CaseOwnerName as CaseHeaders_CaseOwnerName, t2.CaseOwnerRank as CaseHeaders_CaseOwnerRank, t2.TABC as CaseHeaders_TABC, t2.AdditionalInformation as CaseHeaders_AdditionalInformation, t2.ActivityType as CaseHeaders_ActivityType, t2.OfficerStepShiftId as CaseHeaders_OfficerStepShiftId, t2.StepZoneId as CaseHeaders_StepZoneId, t2.OldCaseID as CaseHeaders_OldCaseID
FROM DUI.FSTOtherTest t1
LEFT JOIN DUI.CaseHeaders t2 ON t1.CaseId = t2.CaseId
WHERE t1.CaseId IS NOT NULL


-- Simple view for FSTPalmPatTest
-- Provides secure access to FSTPalmPatTest data excluding sensitive information
CREATE VIEW DUI.v_fstpalmpattest AS
SELECT PalmPatTestId, CaseId, TestGiven, ReasonNotGiven, StoppedTest, StatedPalmPat, UnableToFollow, UnableToFollowDesc, StartWrongTime, StartWrongTimeDesc, NotCounted, NotCountedDesc, RolledHands, RolledHandDesc, DoublePat, DoublePatDesc, ChoppedPat, ChoppedPatDesc, OtherImproperPat, OtherImproperPatDesc, NotIncreaseSpeed, NotIncreaseSpeedDesc, RotatedHands, RotatedHandsDesc, StoppedBeforeTold, StoppedBeforeToldDesc, TotalPalmPatClues, Comments, PalmPatCompleted, PalmPatCompletedComments, PalmPatSliding, PalmPatSlidingComments, PalmPatHesitation, PalmPatHesitationComments, GivenPalmPatInstruction, PalmPat, PpUnderstoodInstr, ArchivePpRefused, PpNoSpeedup, PpNoSpeedupCom, PpUnable, PpUnableCom, PpImproper, PpImproperCom, PpOtherOb, PpSafety
FROM DUI.FSTPalmPatTest
WHERE PalmPatTestId IS NOT NULL


-- Relationship view: FSTPalmPatTest with CaseHeaders
-- Provides FSTPalmPatTest data joined with related CaseHeaders information
CREATE VIEW DUI.v_fstpalmpattest_with_caseheaders AS
SELECT t1.PalmPatTestId, t1.CaseId, t1.TestGiven, t1.ReasonNotGiven, t1.StoppedTest, t1.StatedPalmPat, t1.UnableToFollow, t1.UnableToFollowDesc, t1.StartWrongTime, t1.StartWrongTimeDesc, t1.NotCounted, t1.NotCountedDesc, t1.RolledHands, t1.RolledHandDesc, t1.DoublePat, t1.DoublePatDesc, t1.ChoppedPat, t1.ChoppedPatDesc, t1.OtherImproperPat, t1.OtherImproperPatDesc, t1.NotIncreaseSpeed, t1.NotIncreaseSpeedDesc, t1.RotatedHands, t1.RotatedHandsDesc, t1.StoppedBeforeTold, t1.StoppedBeforeToldDesc, t1.TotalPalmPatClues, t1.Comments, t1.PalmPatCompleted, t1.PalmPatCompletedComments, t1.PalmPatSliding, t1.PalmPatSlidingComments, t1.PalmPatHesitation, t1.PalmPatHesitationComments, t1.GivenPalmPatInstruction, t1.PalmPat, t1.PpUnderstoodInstr, t1.ArchivePpRefused, t1.PpNoSpeedup, t1.PpNoSpeedupCom, t1.PpUnable, t1.PpUnableCom, t1.PpImproper, t1.PpImproperCom, t1.PpOtherOb, t1.PpSafety, t2.CaseId as CaseHeaders_CaseId, t2.UniqueId as CaseHeaders_UniqueId, t2.StatusId as CaseHeaders_StatusId, t2.ModelId as CaseHeaders_ModelId, t2.LockedByOfficerId as CaseHeaders_LockedByOfficerId, t2.ApprovedByOfficerId as CaseHeaders_ApprovedByOfficerId, t2.OrganizationId as CaseHeaders_OrganizationId, t2.LocationId as CaseHeaders_LocationId, t2.District as CaseHeaders_District, t2.Grid as CaseHeaders_Grid, t2.Version as CaseHeaders_Version, t2.Active as CaseHeaders_Active, t2.ModeId as CaseHeaders_ModeId, t2.ProbableCause as CaseHeaders_ProbableCause, t2.IsTrainingPurpose as CaseHeaders_IsTrainingPurpose, t2.PaidTxDOT as CaseHeaders_PaidTxDOT, t2.StepGrantTypeId as CaseHeaders_StepGrantTypeId, t2.CaseOwnerAgency as CaseHeaders_CaseOwnerAgency, t2.CaseOwnerBadge as CaseHeaders_CaseOwnerBadge, t2.CaseOwnerDepartmentId as CaseHeaders_CaseOwnerDepartmentId, t2.CaseOwnerId as CaseHeaders_CaseOwnerId, t2.CaseOwnerName as CaseHeaders_CaseOwnerName, t2.CaseOwnerRank as CaseHeaders_CaseOwnerRank, t2.TABC as CaseHeaders_TABC, t2.AdditionalInformation as CaseHeaders_AdditionalInformation, t2.ActivityType as CaseHeaders_ActivityType, t2.OfficerStepShiftId as CaseHeaders_OfficerStepShiftId, t2.StepZoneId as CaseHeaders_StepZoneId, t2.OldCaseID as CaseHeaders_OldCaseID
FROM DUI.FSTPalmPatTest t1
LEFT JOIN DUI.CaseHeaders t2 ON t1.CaseId = t2.CaseId
WHERE t1.CaseId IS NOT NULL


-- Simple view for FSTSupplementFingerToNoseTest
-- Provides secure access to FSTSupplementFingerToNoseTest data excluding sensitive information
CREATE VIEW DUI.v_fstsupplementfingertonosetest AS
SELECT FingerToNoseId, SupplementId, TestGiven, ReasonNotGiven, StoppedTest, StatedFingerToNose, UnableToFollow, UnableToFollowDesc, StartWrongTime, StartWrongTimeDesc, NotCloseEyes, NotCloseEyesDesc, NotTiltHead, NotTiltHeadDesc, OpenEyes, OpenEyesDesc, MovedHead, MovedHeadDesc, WrongHandRight1, WrongHandRight2, WrongHandRight3, WrongFingerLeft1, WrongFingerRight1, WrongFingerLeft2, WrongFingerRight2, WrongFingerLeft3, WrongFingerRight3, HesitatedRight1, HesitatedRight2, HesitatedRight3, SearchedRight1, SearchedRight2, SearchedRight3, FingerTipLeft1, FingerTipRight1, FingerTipLeft2, FingerTipRight2, FingerTipLeft3, FingerTipRight3, MissedNoseLeft1, MissedNoseRight1, MissedNoseLeft2, MissedNoseRight2, MissedNoseLeft3, MissedNoseRight3, BringDownLeft1, BringDownRight1, BringDownLeft2, BringDownRight2, BringDownLeft3, BringDownRight3, Comments, OldFingerToNoseId
FROM DUI.FSTSupplementFingerToNoseTest
WHERE FingerToNoseId IS NOT NULL


-- Simple view for FSTSupplementHGNTest
-- Provides secure access to FSTSupplementHGNTest data excluding sensitive information
CREATE VIEW DUI.v_fstsupplementhgntest AS
SELECT HGNId, SupplementId, HGNGiven, ReasonNotGiven, HeadInjuries, HeadInjuryExplain, WearGlass, WearGlassExplain, EqualPupilSize, EqualPupilSizeExplain, RestingNystagmus, EqualTracking, FollowStimulus, FollowStimulusExplain, StimulusAboveEyeLevel, ForwardEmergencyLightsActive, DefFacingFlashLight, FlashLightExplain, StatedHGN, LackOfPursuit, LackOfPursuitLeft, LackOfPursuitRight, MaximumDeviation, MaxDeviationLeft, MaxDeviationRight, NystagmusPrior, NystagmusPriorLeft, NystagmusPriorRight, AngleOfOnset, AngleOnsetNystagmus, VerticalNystagmus, TotalHGNClues, Comments, OldHGNId, VerticalNystagmusLeft, VerticalNystagmusRight, HGNAdminbyReportingAgent, CluesLeft, CluesRight
FROM DUI.FSTSupplementHGNTest
WHERE HGNId IS NOT NULL


-- Simple view for FSTSupplementHandCoordination
-- Provides secure access to FSTSupplementHandCoordination data excluding sensitive information
CREATE VIEW DUI.v_fstsupplementhandcoordination AS
SELECT SupplementHandCoordinationId, SupplementId, TestGiven, ReasonNotGiven, StoppedTest, StatedHandCoordination, UnableToFollow, UnableToFollowDesc, StartWrongTime, StartWrongTimeDesc, ForwardImproperCount, ForwardImproperCountDesc, ForwardImproperTouch, ForwardImproperTouchDesc, ForwardNotPerform, ForwardNotPerformDesc, ClappingImproperCount, ClappingImproperCountDesc, ClappingImproperTouch, ClappingImproperTouchDesc, ClappingImproperReturn, ClappingImproperReturnDesc, ClappingNotPerform, ClappingNotPerformDesc, ReturnImproperCount, ReturnImproperCountDesc, ReturnImproperTouch, ReturnImproperTouchDesc, NotReturnToChest, NotReturnToChestDesc, ReturnNotPerform, ReturnNotPerformDesc, ImproperPosition, ImproperPositionDesc, EndPositionNotPerform, EndPositionNotPerformDesc, TotalClues, Comments, OldHandCoordinationId
FROM DUI.FSTSupplementHandCoordination
WHERE SupplementHandCoordinationId IS NOT NULL


-- Simple view for FSTSupplementOneLegStandTest
-- Provides secure access to FSTSupplementOneLegStandTest data excluding sensitive information
CREATE VIEW DUI.v_fstsupplementonelegstandtest AS
SELECT OneLegStandId, SupplementId, OneLegStandGiven, ReasonNotGiven, TestStopped, StatedOneLegStand, FootStoodOn, FootRaised, FootWearId, NotKeepBalance, KeepBalanceExplain, Sways, SwaysDesc, Hops, HopsDesc, PutsFootDown, PutsFootDownDesc, UseArmsToBalance, ArmsBalanceDesc, OneLegClues, Comments, OldOneLegStandId, UnderstoodComments, StoodOnComments, PhysicalInjuries, DescribeInjuries, DefMoreThan65
FROM DUI.FSTSupplementOneLegStandTest
WHERE OneLegStandId IS NOT NULL


-- Simple view for FSTSupplementOtherTest
-- Provides secure access to FSTSupplementOtherTest data excluding sensitive information
CREATE VIEW DUI.v_fstsupplementothertest AS
SELECT OtherTestId, SupplementId, FingerCountGiven, FingerCountDesc, AlphabetTestGiven, AlphabetTestDesc, OtherTestDesc, FcSafety, ALetterStart, ALetterFinish, ASafety, StatedFingerCountInstruction, FCGaveInstruction, FCRefused, FCComplete, FCCompleteDesc, FCMiscounted, FCMiscountedComments, FCSliding, FCSlidingComment, FCNoSpeedUp, FCNoSpeedUpComments, FCImproperTouch, FCImproperTouchComments, FCImproperCount, FCImproperCountComments, StatedAlphabetTest, AlphabetTestGivenInstruction, AlphabetTestRefused, AlphabetTestComplete, AlphabetTestCompleteComments, AlphabetTestSang, AlphabetTestSangComments, AlphabetTestLetterRepeated, AlphabetTestLetterRepeatedComments, AlphabetTestHesitation, AlphabetTestHesitationComments
FROM DUI.FSTSupplementOtherTest
WHERE OtherTestId IS NOT NULL


-- Simple view for FSTSupplementPalmPatTest
-- Provides secure access to FSTSupplementPalmPatTest data excluding sensitive information
CREATE VIEW DUI.v_fstsupplementpalmpattest AS
SELECT PalmPatTestId, SupplementId, TestGiven, ReasonNotGiven, StoppedTest, StatedPalmPat, UnableToFollow, UnableToFollowDesc, StartWrongTime, StartWrongTimeDesc, NotCounted, NotCountedDesc, RolledHands, RolledHandDesc, DoublePat, DoublePatDesc, ChoppedPat, ChoppedPatDesc, OtherImproperPat, OtherImproperPatDesc, NotIncreaseSpeed, NotIncreaseSpeedDesc, RotatedHands, RotatedHandsDesc, StoppedBeforeTold, StoppedBeforeToldDesc, TotalPalmPatClues, Comments, PalmPat, PpUnderstoodInstr, ArchivePpRefused, PpNoSpeedup, PpNoSpeedupCom, PpUnable, PpUnableCom, PpImproper, PpImproperCom, PpOtherOb, PpSafety, OldPalmPatTestId, GivenPalmPatInstruction, PalmPatCompleted, PalmPatCompletedComments, PalmPatSliding, PalmPatSlidingComments, PalmPatHesitation, PalmPatHesitationComments
FROM DUI.FSTSupplementPalmPatTest
WHERE PalmPatTestId IS NOT NULL


-- Simple view for FSTSupplementWalkAndTurnTest
-- Provides secure access to FSTSupplementWalkAndTurnTest data excluding sensitive information
CREATE VIEW DUI.v_fstsupplementwalkandturntest AS
SELECT WalkAndTurnId, SupplementId, WalkTurnGiven, ReasonNotGiven, TestStopped, StatedWalkTurn, NotKeepBalance, KeepBalanceExplain, StartTooSoon, StartSoonDesc, StopWhileWalk, StopWalkDesc, MissHeelToe, MissHeelToeDesc, StepOffLine, StepsOffLineDesc, UseArmsToBalance, ArmsBalanceDesc, TurnImproperly, TurnImproperlyDesc, WrongSteps, WrongStepsDesc, WalkAndTurnClues, Comments, ArchiveUnderstoodComments, ArchiveComments, PhysicalInjuries, DescribeInjuries, Over65, OldWalkAndTurnId, OtherIndicators
FROM DUI.FSTSupplementWalkAndTurnTest
WHERE WalkAndTurnId IS NOT NULL


-- Simple view for FSTWalkAndTurnTest
-- Provides secure access to FSTWalkAndTurnTest data excluding sensitive information
CREATE VIEW DUI.v_fstwalkandturntest AS
SELECT WalkAndTurnId, CaseId, WalkTurnGiven, ReasonNotGiven, TestStopped, StatedWalkTurn, NotKeepBalance, KeepBalanceExplain, StartTooSoon, StartSoonDesc, StopWhileWalk, StopWalkDesc, MissHeelToe, MissHeelToeDesc, StepOffLine, StepsOffLineDesc, UseArmsToBalance, ArmsBalanceDesc, TurnImproperly, TurnImproperlyDesc, WrongSteps, WrongStepsDesc, WalkAndTurnClues, Comments, OtherIndicators, ArchiveUnderstoodComments, ArchiveComments, PhysicalInjuries, DescribeInjuries, Over65
FROM DUI.FSTWalkAndTurnTest
WHERE WalkAndTurnId IS NOT NULL


-- Relationship view: FSTWalkAndTurnTest with CaseHeaders
-- Provides FSTWalkAndTurnTest data joined with related CaseHeaders information
CREATE VIEW DUI.v_fstwalkandturntest_with_caseheaders AS
SELECT t1.WalkAndTurnId, t1.CaseId, t1.WalkTurnGiven, t1.ReasonNotGiven, t1.TestStopped, t1.StatedWalkTurn, t1.NotKeepBalance, t1.KeepBalanceExplain, t1.StartTooSoon, t1.StartSoonDesc, t1.StopWhileWalk, t1.StopWalkDesc, t1.MissHeelToe, t1.MissHeelToeDesc, t1.StepOffLine, t1.StepsOffLineDesc, t1.UseArmsToBalance, t1.ArmsBalanceDesc, t1.TurnImproperly, t1.TurnImproperlyDesc, t1.WrongSteps, t1.WrongStepsDesc, t1.WalkAndTurnClues, t1.Comments, t1.OtherIndicators, t1.ArchiveUnderstoodComments, t1.ArchiveComments, t1.PhysicalInjuries, t1.DescribeInjuries, t1.Over65, t2.CaseId as CaseHeaders_CaseId, t2.UniqueId as CaseHeaders_UniqueId, t2.StatusId as CaseHeaders_StatusId, t2.ModelId as CaseHeaders_ModelId, t2.LockedByOfficerId as CaseHeaders_LockedByOfficerId, t2.ApprovedByOfficerId as CaseHeaders_ApprovedByOfficerId, t2.OrganizationId as CaseHeaders_OrganizationId, t2.LocationId as CaseHeaders_LocationId, t2.District as CaseHeaders_District, t2.Grid as CaseHeaders_Grid, t2.Version as CaseHeaders_Version, t2.Active as CaseHeaders_Active, t2.ModeId as CaseHeaders_ModeId, t2.ProbableCause as CaseHeaders_ProbableCause, t2.IsTrainingPurpose as CaseHeaders_IsTrainingPurpose, t2.PaidTxDOT as CaseHeaders_PaidTxDOT, t2.StepGrantTypeId as CaseHeaders_StepGrantTypeId, t2.CaseOwnerAgency as CaseHeaders_CaseOwnerAgency, t2.CaseOwnerBadge as CaseHeaders_CaseOwnerBadge, t2.CaseOwnerDepartmentId as CaseHeaders_CaseOwnerDepartmentId, t2.CaseOwnerId as CaseHeaders_CaseOwnerId, t2.CaseOwnerName as CaseHeaders_CaseOwnerName, t2.CaseOwnerRank as CaseHeaders_CaseOwnerRank, t2.TABC as CaseHeaders_TABC, t2.AdditionalInformation as CaseHeaders_AdditionalInformation, t2.ActivityType as CaseHeaders_ActivityType, t2.OfficerStepShiftId as CaseHeaders_OfficerStepShiftId, t2.StepZoneId as CaseHeaders_StepZoneId, t2.OldCaseID as CaseHeaders_OldCaseID
FROM DUI.FSTWalkAndTurnTest t1
LEFT JOIN DUI.CaseHeaders t2 ON t1.CaseId = t2.CaseId
WHERE t1.CaseId IS NOT NULL


-- Simple view for FieldSobrietyTests
-- Provides secure access to FieldSobrietyTests data excluding sensitive information
CREATE VIEW DUI.v_fieldsobrietytests AS
SELECT FieldSobrietyTestId, CaseId, FSTGiven, WhyNotGivenFST, DefendantRefused, PhysicalInjuries, DefMoreThan65, TimeAshore, OnWater, SeatedFST, AttachNote, TimeStartedFST, WaterTestGiven, WhyNotWaterTest, PhysicalProblem, PhysicalProblemDesc, OldCaseId
FROM DUI.FieldSobrietyTests
WHERE FieldSobrietyTestId IS NOT NULL


-- Relationship view: FieldSobrietyTests with CaseHeaders
-- Provides FieldSobrietyTests data joined with related CaseHeaders information
CREATE VIEW DUI.v_fieldsobrietytests_with_caseheaders AS
SELECT t1.FieldSobrietyTestId, t1.CaseId, t1.FSTGiven, t1.WhyNotGivenFST, t1.DefendantRefused, t1.PhysicalInjuries, t1.DefMoreThan65, t1.TimeAshore, t1.OnWater, t1.SeatedFST, t1.AttachNote, t1.TimeStartedFST, t1.WaterTestGiven, t1.WhyNotWaterTest, t1.PhysicalProblem, t1.PhysicalProblemDesc, t1.OldCaseId, t2.CaseId as CaseHeaders_CaseId, t2.UniqueId as CaseHeaders_UniqueId, t2.StatusId as CaseHeaders_StatusId, t2.ModelId as CaseHeaders_ModelId, t2.LockedByOfficerId as CaseHeaders_LockedByOfficerId, t2.ApprovedByOfficerId as CaseHeaders_ApprovedByOfficerId, t2.OrganizationId as CaseHeaders_OrganizationId, t2.LocationId as CaseHeaders_LocationId, t2.District as CaseHeaders_District, t2.Grid as CaseHeaders_Grid, t2.Version as CaseHeaders_Version, t2.Active as CaseHeaders_Active, t2.ModeId as CaseHeaders_ModeId, t2.ProbableCause as CaseHeaders_ProbableCause, t2.IsTrainingPurpose as CaseHeaders_IsTrainingPurpose, t2.PaidTxDOT as CaseHeaders_PaidTxDOT, t2.StepGrantTypeId as CaseHeaders_StepGrantTypeId, t2.CaseOwnerAgency as CaseHeaders_CaseOwnerAgency, t2.CaseOwnerBadge as CaseHeaders_CaseOwnerBadge, t2.CaseOwnerDepartmentId as CaseHeaders_CaseOwnerDepartmentId, t2.CaseOwnerId as CaseHeaders_CaseOwnerId, t2.CaseOwnerName as CaseHeaders_CaseOwnerName, t2.CaseOwnerRank as CaseHeaders_CaseOwnerRank, t2.TABC as CaseHeaders_TABC, t2.AdditionalInformation as CaseHeaders_AdditionalInformation, t2.ActivityType as CaseHeaders_ActivityType, t2.OfficerStepShiftId as CaseHeaders_OfficerStepShiftId, t2.StepZoneId as CaseHeaders_StepZoneId, t2.OldCaseID as CaseHeaders_OldCaseID
FROM DUI.FieldSobrietyTests t1
LEFT JOIN DUI.CaseHeaders t2 ON t1.CaseId = t2.CaseId
WHERE t1.CaseId IS NOT NULL


-- Simple view for NarrativeAILogs
-- Provides secure access to NarrativeAILogs data excluding sensitive information
CREATE VIEW DUI.v_narrativeailogs AS
SELECT Id, CaseId, UserId, GptVersion, Response1, Response2, Response3
FROM DUI.NarrativeAILogs
WHERE Id IS NOT NULL


-- Simple view for OfficerStepShifts
-- Provides secure access to OfficerStepShifts data excluding sensitive information
CREATE VIEW DUI.v_officerstepshifts AS
SELECT StepOfficerShiftId, OfficerId, DepartmentId, ShiftStart, ShiftEnd, TotalHRSWorked, MileageStart, MileageEnd, MileageTotal, Comments, StepShiftId, StepGrantTypeId, Submitted, Approved, ApprovedBy, Rejected, RejectedBy, CreatedBy, Report, OldOfficerStepShiftId
FROM DUI.OfficerStepShifts
WHERE StepOfficerShiftId IS NOT NULL


-- Relationship view: OfficerStepShifts with StepShifts
-- Provides OfficerStepShifts data joined with related StepShifts information
CREATE VIEW DUI.v_officerstepshifts_with_stepshifts AS
SELECT t1.StepOfficerShiftId, t1.OfficerId, t1.DepartmentId, t1.ShiftStart, t1.ShiftEnd, t1.TotalHRSWorked, t1.MileageStart, t1.MileageEnd, t1.MileageTotal, t1.Comments, t1.StepShiftId, t1.StepGrantTypeId, t1.Submitted, t1.Approved, t1.ApprovedBy, t1.Rejected, t1.RejectedBy, t1.CreatedBy, t1.Report, t1.OldOfficerStepShiftId, t2.StepShiftId as StepShifts_StepShiftId, t2.DepartmentId as StepShifts_DepartmentId, t2.LocationId as StepShifts_LocationId, t2.StepGrantTypeId as StepShifts_StepGrantTypeId, t2.ShiftStart as StepShifts_ShiftStart, t2.ShiftEnd as StepShifts_ShiftEnd, t2.CreatedBy as StepShifts_CreatedBy, t2.OldStepShiftId as StepShifts_OldStepShiftId
FROM DUI.OfficerStepShifts t1
LEFT JOIN DUI.StepShifts t2 ON t1.StepShiftId = t2.StepShiftId
WHERE t1.StepShiftId IS NOT NULL


-- Simple view for OtherOfficers
-- Provides secure access to OtherOfficers data excluding sensitive information
CREATE VIEW DUI.v_otherofficers AS
SELECT OtherOfficerId, CaseId, OfficerName, Department, OtherOfficerParticipation, Supplement
FROM DUI.OtherOfficers
WHERE OtherOfficerId IS NOT NULL


-- Relationship view: OtherOfficers with CaseHeaders
-- Provides OtherOfficers data joined with related CaseHeaders information
CREATE VIEW DUI.v_otherofficers_with_caseheaders AS
SELECT t1.OtherOfficerId, t1.CaseId, t1.OfficerName, t1.Department, t1.OtherOfficerParticipation, t1.Supplement, t2.CaseId as CaseHeaders_CaseId, t2.UniqueId as CaseHeaders_UniqueId, t2.StatusId as CaseHeaders_StatusId, t2.ModelId as CaseHeaders_ModelId, t2.LockedByOfficerId as CaseHeaders_LockedByOfficerId, t2.ApprovedByOfficerId as CaseHeaders_ApprovedByOfficerId, t2.OrganizationId as CaseHeaders_OrganizationId, t2.LocationId as CaseHeaders_LocationId, t2.District as CaseHeaders_District, t2.Grid as CaseHeaders_Grid, t2.Version as CaseHeaders_Version, t2.Active as CaseHeaders_Active, t2.ModeId as CaseHeaders_ModeId, t2.ProbableCause as CaseHeaders_ProbableCause, t2.IsTrainingPurpose as CaseHeaders_IsTrainingPurpose, t2.PaidTxDOT as CaseHeaders_PaidTxDOT, t2.StepGrantTypeId as CaseHeaders_StepGrantTypeId, t2.CaseOwnerAgency as CaseHeaders_CaseOwnerAgency, t2.CaseOwnerBadge as CaseHeaders_CaseOwnerBadge, t2.CaseOwnerDepartmentId as CaseHeaders_CaseOwnerDepartmentId, t2.CaseOwnerId as CaseHeaders_CaseOwnerId, t2.CaseOwnerName as CaseHeaders_CaseOwnerName, t2.CaseOwnerRank as CaseHeaders_CaseOwnerRank, t2.TABC as CaseHeaders_TABC, t2.AdditionalInformation as CaseHeaders_AdditionalInformation, t2.ActivityType as CaseHeaders_ActivityType, t2.OfficerStepShiftId as CaseHeaders_OfficerStepShiftId, t2.StepZoneId as CaseHeaders_StepZoneId, t2.OldCaseID as CaseHeaders_OldCaseID
FROM DUI.OtherOfficers t1
LEFT JOIN DUI.CaseHeaders t2 ON t1.CaseId = t2.CaseId
WHERE t1.CaseId IS NOT NULL


-- Simple view for PhysicalEvidence
-- Provides secure access to PhysicalEvidence data excluding sensitive information
CREATE VIEW DUI.v_physicalevidence AS
SELECT PhysicalEvidenceId, CaseId, DispatchRecordingInclude, ExplainDispatchRecording, OtherPhysicalEvidence, HasVideoTape, NoTapeExplain, EvEvidenceDisposition, Ev911TapeDisposition, OldCaseID
FROM DUI.PhysicalEvidence
WHERE PhysicalEvidenceId IS NOT NULL


-- Relationship view: PhysicalEvidence with CaseHeaders
-- Provides PhysicalEvidence data joined with related CaseHeaders information
CREATE VIEW DUI.v_physicalevidence_with_caseheaders AS
SELECT t1.PhysicalEvidenceId, t1.CaseId, t1.DispatchRecordingInclude, t1.ExplainDispatchRecording, t1.OtherPhysicalEvidence, t1.HasVideoTape, t1.NoTapeExplain, t1.EvEvidenceDisposition, t1.Ev911TapeDisposition, t1.OldCaseID, t2.CaseId as CaseHeaders_CaseId, t2.UniqueId as CaseHeaders_UniqueId, t2.StatusId as CaseHeaders_StatusId, t2.ModelId as CaseHeaders_ModelId, t2.LockedByOfficerId as CaseHeaders_LockedByOfficerId, t2.ApprovedByOfficerId as CaseHeaders_ApprovedByOfficerId, t2.OrganizationId as CaseHeaders_OrganizationId, t2.LocationId as CaseHeaders_LocationId, t2.District as CaseHeaders_District, t2.Grid as CaseHeaders_Grid, t2.Version as CaseHeaders_Version, t2.Active as CaseHeaders_Active, t2.ModeId as CaseHeaders_ModeId, t2.ProbableCause as CaseHeaders_ProbableCause, t2.IsTrainingPurpose as CaseHeaders_IsTrainingPurpose, t2.PaidTxDOT as CaseHeaders_PaidTxDOT, t2.StepGrantTypeId as CaseHeaders_StepGrantTypeId, t2.CaseOwnerAgency as CaseHeaders_CaseOwnerAgency, t2.CaseOwnerBadge as CaseHeaders_CaseOwnerBadge, t2.CaseOwnerDepartmentId as CaseHeaders_CaseOwnerDepartmentId, t2.CaseOwnerId as CaseHeaders_CaseOwnerId, t2.CaseOwnerName as CaseHeaders_CaseOwnerName, t2.CaseOwnerRank as CaseHeaders_CaseOwnerRank, t2.TABC as CaseHeaders_TABC, t2.AdditionalInformation as CaseHeaders_AdditionalInformation, t2.ActivityType as CaseHeaders_ActivityType, t2.OfficerStepShiftId as CaseHeaders_OfficerStepShiftId, t2.StepZoneId as CaseHeaders_StepZoneId, t2.OldCaseID as CaseHeaders_OldCaseID
FROM DUI.PhysicalEvidence t1
LEFT JOIN DUI.CaseHeaders t2 ON t1.CaseId = t2.CaseId
WHERE t1.CaseId IS NOT NULL


-- Simple view for QuestionForAI
-- Provides secure access to QuestionForAI data excluding sensitive information
CREATE VIEW DUI.v_questionforai AS
SELECT Id, Section, TableName, ColumnName, ColumnType, ReqGen, ReqCheck, LookUpTable, LookUpColumn, LookUpRelationColumn, Status, Question
FROM DUI.QuestionForAI
WHERE Id IS NOT NULL


-- Simple view for SpecimenBloodTest
-- Provides secure access to SpecimenBloodTest data excluding sensitive information
CREATE VIEW DUI.v_specimenbloodtest AS
SELECT SpecimenBloodTestId, SpecimenReportId, BloodVials, MoreLessIntoxId, PersonName, EmployerName, EmployedId, Location, BWI_Preservative, BWI_NoAlcohol, BWI_Rotated, LabName, BwiStateBwd
FROM DUI.SpecimenBloodTest
WHERE SpecimenBloodTestId IS NOT NULL


-- Relationship view: SpecimenBloodTest with SpecimenReport
-- Provides SpecimenBloodTest data joined with related SpecimenReport information
CREATE VIEW DUI.v_specimenbloodtest_with_specimenreport AS
SELECT t1.SpecimenBloodTestId, t1.SpecimenReportId, t1.BloodVials, t1.MoreLessIntoxId, t1.PersonName, t1.EmployerName, t1.EmployedId, t1.Location, t1.BWI_Preservative, t1.BWI_NoAlcohol, t1.BWI_Rotated, t1.LabName, t1.BwiStateBwd, t2.SpecimenReportId as SpecimenReport_SpecimenReportId, t2.CaseId as SpecimenReport_CaseId, t2.Dic24ReadBy as SpecimenReport_Dic24ReadBy, t2.Dic24Time as SpecimenReport_Dic24Time, t2.Dic24ReadEnglish as SpecimenReport_Dic24ReadEnglish, t2.Dic24ReadSpanish as SpecimenReport_Dic24ReadSpanish, t2.Dic24RecordingUsed as SpecimenReport_Dic24RecordingUsed, t2.Breath as SpecimenReport_Breath, t2.BreathProvided as SpecimenReport_BreathProvided, t2.BreathRefused as SpecimenReport_BreathRefused, t2.Blood as SpecimenReport_Blood, t2.BloodProvided as SpecimenReport_BloodProvided, t2.BloodRefused as SpecimenReport_BloodRefused, t2.BloodSpecimenTaken as SpecimenReport_BloodSpecimenTaken, t2.Urine as SpecimenReport_Urine, t2.UrineProvided as SpecimenReport_UrineProvided, t2.UrineRefused as SpecimenReport_UrineRefused, t2.ProvidedNone as SpecimenReport_ProvidedNone, t2.LabBACResult as SpecimenReport_LabBACResult, t2.AlcoholDetected as SpecimenReport_AlcoholDetected, t2.SearchWarrantSought as SpecimenReport_SearchWarrantSought, t2.TimePresentedToMagistrate as SpecimenReport_TimePresentedToMagistrate, t2.SearchWarrantMagistrateName as SpecimenReport_SearchWarrantMagistrateName, t2.SearchWarrantCourt as SpecimenReport_SearchWarrantCourt, t2.WarrantIssuedByMagistrate as SpecimenReport_WarrantIssuedByMagistrate, t2.MagistrateWarrantTime as SpecimenReport_MagistrateWarrantTime, t2.HandedDic25 as SpecimenReport_HandedDic25, t2.SubjectUnderstood as SpecimenReport_SubjectUnderstood, t2.ProvidedOther as SpecimenReport_ProvidedOther, t2.Refused as SpecimenReport_Refused, t2.SpecimenStorageOther as SpecimenReport_SpecimenStorageOther, t2.SpecimenStorageId as SpecimenReport_SpecimenStorageId, t2.SpecimenSubmittedMethodId as SpecimenReport_SpecimenSubmittedMethodId, t2.OldCaseId as SpecimenReport_OldCaseId, t2.ArchiveProvidedNone as SpecimenReport_ArchiveProvidedNone, t2.PBTUsed as SpecimenReport_PBTUsed
FROM DUI.SpecimenBloodTest t1
LEFT JOIN DUI.SpecimenReport t2 ON t1.SpecimenReportId = t2.SpecimenReportId
WHERE t1.SpecimenReportId IS NOT NULL


-- Simple view for SpecimenBreathTest
-- Provides secure access to SpecimenBreathTest data excluding sensitive information
CREATE VIEW DUI.v_specimenbreathtest AS
SELECT SpecimenBreathTestId, SpecimenReportId, WaitingPeriodTime, VerifyTempId, SubjectComments, BreathIntoxOperator, OperatorName, OperatorAgency, Result1Time, Result2Time, MoreLessIntoxId, ArchiveResult1, ArchiveResult2, ArchiveOperatorOccupationId, ArchiveMoreLessIntoxId, ArchiveDic24OnVideo
FROM DUI.SpecimenBreathTest
WHERE SpecimenBreathTestId IS NOT NULL


-- Relationship view: SpecimenBreathTest with SpecimenReport
-- Provides SpecimenBreathTest data joined with related SpecimenReport information
CREATE VIEW DUI.v_specimenbreathtest_with_specimenreport AS
SELECT t1.SpecimenBreathTestId, t1.SpecimenReportId, t1.WaitingPeriodTime, t1.VerifyTempId, t1.SubjectComments, t1.BreathIntoxOperator, t1.OperatorName, t1.OperatorAgency, t1.Result1Time, t1.Result2Time, t1.MoreLessIntoxId, t1.ArchiveResult1, t1.ArchiveResult2, t1.ArchiveOperatorOccupationId, t1.ArchiveMoreLessIntoxId, t1.ArchiveDic24OnVideo, t2.SpecimenReportId as SpecimenReport_SpecimenReportId, t2.CaseId as SpecimenReport_CaseId, t2.Dic24ReadBy as SpecimenReport_Dic24ReadBy, t2.Dic24Time as SpecimenReport_Dic24Time, t2.Dic24ReadEnglish as SpecimenReport_Dic24ReadEnglish, t2.Dic24ReadSpanish as SpecimenReport_Dic24ReadSpanish, t2.Dic24RecordingUsed as SpecimenReport_Dic24RecordingUsed, t2.Breath as SpecimenReport_Breath, t2.BreathProvided as SpecimenReport_BreathProvided, t2.BreathRefused as SpecimenReport_BreathRefused, t2.Blood as SpecimenReport_Blood, t2.BloodProvided as SpecimenReport_BloodProvided, t2.BloodRefused as SpecimenReport_BloodRefused, t2.BloodSpecimenTaken as SpecimenReport_BloodSpecimenTaken, t2.Urine as SpecimenReport_Urine, t2.UrineProvided as SpecimenReport_UrineProvided, t2.UrineRefused as SpecimenReport_UrineRefused, t2.ProvidedNone as SpecimenReport_ProvidedNone, t2.LabBACResult as SpecimenReport_LabBACResult, t2.AlcoholDetected as SpecimenReport_AlcoholDetected, t2.SearchWarrantSought as SpecimenReport_SearchWarrantSought, t2.TimePresentedToMagistrate as SpecimenReport_TimePresentedToMagistrate, t2.SearchWarrantMagistrateName as SpecimenReport_SearchWarrantMagistrateName, t2.SearchWarrantCourt as SpecimenReport_SearchWarrantCourt, t2.WarrantIssuedByMagistrate as SpecimenReport_WarrantIssuedByMagistrate, t2.MagistrateWarrantTime as SpecimenReport_MagistrateWarrantTime, t2.HandedDic25 as SpecimenReport_HandedDic25, t2.SubjectUnderstood as SpecimenReport_SubjectUnderstood, t2.ProvidedOther as SpecimenReport_ProvidedOther, t2.Refused as SpecimenReport_Refused, t2.SpecimenStorageOther as SpecimenReport_SpecimenStorageOther, t2.SpecimenStorageId as SpecimenReport_SpecimenStorageId, t2.SpecimenSubmittedMethodId as SpecimenReport_SpecimenSubmittedMethodId, t2.OldCaseId as SpecimenReport_OldCaseId, t2.ArchiveProvidedNone as SpecimenReport_ArchiveProvidedNone, t2.PBTUsed as SpecimenReport_PBTUsed
FROM DUI.SpecimenBreathTest t1
LEFT JOIN DUI.SpecimenReport t2 ON t1.SpecimenReportId = t2.SpecimenReportId
WHERE t1.SpecimenReportId IS NOT NULL


-- Simple view for SpecimenReport
-- Provides secure access to SpecimenReport data excluding sensitive information
CREATE VIEW DUI.v_specimenreport AS
SELECT SpecimenReportId, CaseId, Dic24ReadBy, Dic24Time, Dic24ReadEnglish, Dic24ReadSpanish, Dic24RecordingUsed, Breath, BreathProvided, BreathRefused, Blood, BloodProvided, BloodRefused, BloodSpecimenTaken, Urine, UrineProvided, UrineRefused, ProvidedNone, LabBACResult, AlcoholDetected, SearchWarrantSought, TimePresentedToMagistrate, SearchWarrantMagistrateName, SearchWarrantCourt, WarrantIssuedByMagistrate, MagistrateWarrantTime, HandedDic25, SubjectUnderstood, ProvidedOther, Refused, SpecimenStorageOther, SpecimenStorageId, SpecimenSubmittedMethodId, OldCaseId, ArchiveProvidedNone, PBTUsed
FROM DUI.SpecimenReport
WHERE SpecimenReportId IS NOT NULL


-- Relationship view: SpecimenReport with CaseHeaders
-- Provides SpecimenReport data joined with related CaseHeaders information
CREATE VIEW DUI.v_specimenreport_with_caseheaders AS
SELECT t1.SpecimenReportId, t1.CaseId, t1.Dic24ReadBy, t1.Dic24Time, t1.Dic24ReadEnglish, t1.Dic24ReadSpanish, t1.Dic24RecordingUsed, t1.Breath, t1.BreathProvided, t1.BreathRefused, t1.Blood, t1.BloodProvided, t1.BloodRefused, t1.BloodSpecimenTaken, t1.Urine, t1.UrineProvided, t1.UrineRefused, t1.ProvidedNone, t1.LabBACResult, t1.AlcoholDetected, t1.SearchWarrantSought, t1.TimePresentedToMagistrate, t1.SearchWarrantMagistrateName, t1.SearchWarrantCourt, t1.WarrantIssuedByMagistrate, t1.MagistrateWarrantTime, t1.HandedDic25, t1.SubjectUnderstood, t1.ProvidedOther, t1.Refused, t1.SpecimenStorageOther, t1.SpecimenStorageId, t1.SpecimenSubmittedMethodId, t1.OldCaseId, t1.ArchiveProvidedNone, t1.PBTUsed, t2.CaseId as CaseHeaders_CaseId, t2.UniqueId as CaseHeaders_UniqueId, t2.StatusId as CaseHeaders_StatusId, t2.ModelId as CaseHeaders_ModelId, t2.LockedByOfficerId as CaseHeaders_LockedByOfficerId, t2.ApprovedByOfficerId as CaseHeaders_ApprovedByOfficerId, t2.OrganizationId as CaseHeaders_OrganizationId, t2.LocationId as CaseHeaders_LocationId, t2.District as CaseHeaders_District, t2.Grid as CaseHeaders_Grid, t2.Version as CaseHeaders_Version, t2.Active as CaseHeaders_Active, t2.ModeId as CaseHeaders_ModeId, t2.ProbableCause as CaseHeaders_ProbableCause, t2.IsTrainingPurpose as CaseHeaders_IsTrainingPurpose, t2.PaidTxDOT as CaseHeaders_PaidTxDOT, t2.StepGrantTypeId as CaseHeaders_StepGrantTypeId, t2.CaseOwnerAgency as CaseHeaders_CaseOwnerAgency, t2.CaseOwnerBadge as CaseHeaders_CaseOwnerBadge, t2.CaseOwnerDepartmentId as CaseHeaders_CaseOwnerDepartmentId, t2.CaseOwnerId as CaseHeaders_CaseOwnerId, t2.CaseOwnerName as CaseHeaders_CaseOwnerName, t2.CaseOwnerRank as CaseHeaders_CaseOwnerRank, t2.TABC as CaseHeaders_TABC, t2.AdditionalInformation as CaseHeaders_AdditionalInformation, t2.ActivityType as CaseHeaders_ActivityType, t2.OfficerStepShiftId as CaseHeaders_OfficerStepShiftId, t2.StepZoneId as CaseHeaders_StepZoneId, t2.OldCaseID as CaseHeaders_OldCaseID
FROM DUI.SpecimenReport t1
LEFT JOIN DUI.CaseHeaders t2 ON t1.CaseId = t2.CaseId
WHERE t1.CaseId IS NOT NULL


-- Simple view for SpecimenUrineTest
-- Provides secure access to SpecimenUrineTest data excluding sensitive information
CREATE VIEW DUI.v_specimenurinetest AS
SELECT SpecimenUrineTestId, SpecimenReportId, UrineCollectedTime, WitnessedBy, Results, LabName, MoreLessIntoxId, ArchiveUrineBacL5
FROM DUI.SpecimenUrineTest
WHERE SpecimenUrineTestId IS NOT NULL


-- Relationship view: SpecimenUrineTest with SpecimenReport
-- Provides SpecimenUrineTest data joined with related SpecimenReport information
CREATE VIEW DUI.v_specimenurinetest_with_specimenreport AS
SELECT t1.SpecimenUrineTestId, t1.SpecimenReportId, t1.UrineCollectedTime, t1.WitnessedBy, t1.Results, t1.LabName, t1.MoreLessIntoxId, t1.ArchiveUrineBacL5, t2.SpecimenReportId as SpecimenReport_SpecimenReportId, t2.CaseId as SpecimenReport_CaseId, t2.Dic24ReadBy as SpecimenReport_Dic24ReadBy, t2.Dic24Time as SpecimenReport_Dic24Time, t2.Dic24ReadEnglish as SpecimenReport_Dic24ReadEnglish, t2.Dic24ReadSpanish as SpecimenReport_Dic24ReadSpanish, t2.Dic24RecordingUsed as SpecimenReport_Dic24RecordingUsed, t2.Breath as SpecimenReport_Breath, t2.BreathProvided as SpecimenReport_BreathProvided, t2.BreathRefused as SpecimenReport_BreathRefused, t2.Blood as SpecimenReport_Blood, t2.BloodProvided as SpecimenReport_BloodProvided, t2.BloodRefused as SpecimenReport_BloodRefused, t2.BloodSpecimenTaken as SpecimenReport_BloodSpecimenTaken, t2.Urine as SpecimenReport_Urine, t2.UrineProvided as SpecimenReport_UrineProvided, t2.UrineRefused as SpecimenReport_UrineRefused, t2.ProvidedNone as SpecimenReport_ProvidedNone, t2.LabBACResult as SpecimenReport_LabBACResult, t2.AlcoholDetected as SpecimenReport_AlcoholDetected, t2.SearchWarrantSought as SpecimenReport_SearchWarrantSought, t2.TimePresentedToMagistrate as SpecimenReport_TimePresentedToMagistrate, t2.SearchWarrantMagistrateName as SpecimenReport_SearchWarrantMagistrateName, t2.SearchWarrantCourt as SpecimenReport_SearchWarrantCourt, t2.WarrantIssuedByMagistrate as SpecimenReport_WarrantIssuedByMagistrate, t2.MagistrateWarrantTime as SpecimenReport_MagistrateWarrantTime, t2.HandedDic25 as SpecimenReport_HandedDic25, t2.SubjectUnderstood as SpecimenReport_SubjectUnderstood, t2.ProvidedOther as SpecimenReport_ProvidedOther, t2.Refused as SpecimenReport_Refused, t2.SpecimenStorageOther as SpecimenReport_SpecimenStorageOther, t2.SpecimenStorageId as SpecimenReport_SpecimenStorageId, t2.SpecimenSubmittedMethodId as SpecimenReport_SpecimenSubmittedMethodId, t2.OldCaseId as SpecimenReport_OldCaseId, t2.ArchiveProvidedNone as SpecimenReport_ArchiveProvidedNone, t2.PBTUsed as SpecimenReport_PBTUsed
FROM DUI.SpecimenUrineTest t1
LEFT JOIN DUI.SpecimenReport t2 ON t1.SpecimenReportId = t2.SpecimenReportId
WHERE t1.SpecimenReportId IS NOT NULL


-- Simple view for StepOfficerShiftCases
-- Provides secure access to StepOfficerShiftCases data excluding sensitive information
CREATE VIEW DUI.v_stepofficershiftcases AS
SELECT StepOfficerShiftCaseId, StepOfficerShiftId, CaseId, IsInsideZone
FROM DUI.StepOfficerShiftCases
WHERE StepOfficerShiftCaseId IS NOT NULL


-- Relationship view: StepOfficerShiftCases with CaseHeaders
-- Provides StepOfficerShiftCases data joined with related CaseHeaders information
CREATE VIEW DUI.v_stepofficershiftcases_with_caseheaders AS
SELECT t1.StepOfficerShiftCaseId, t1.StepOfficerShiftId, t1.CaseId, t1.IsInsideZone, t2.CaseId as CaseHeaders_CaseId, t2.UniqueId as CaseHeaders_UniqueId, t2.StatusId as CaseHeaders_StatusId, t2.ModelId as CaseHeaders_ModelId, t2.LockedByOfficerId as CaseHeaders_LockedByOfficerId, t2.ApprovedByOfficerId as CaseHeaders_ApprovedByOfficerId, t2.OrganizationId as CaseHeaders_OrganizationId, t2.LocationId as CaseHeaders_LocationId, t2.District as CaseHeaders_District, t2.Grid as CaseHeaders_Grid, t2.Version as CaseHeaders_Version, t2.Active as CaseHeaders_Active, t2.ModeId as CaseHeaders_ModeId, t2.ProbableCause as CaseHeaders_ProbableCause, t2.IsTrainingPurpose as CaseHeaders_IsTrainingPurpose, t2.PaidTxDOT as CaseHeaders_PaidTxDOT, t2.StepGrantTypeId as CaseHeaders_StepGrantTypeId, t2.CaseOwnerAgency as CaseHeaders_CaseOwnerAgency, t2.CaseOwnerBadge as CaseHeaders_CaseOwnerBadge, t2.CaseOwnerDepartmentId as CaseHeaders_CaseOwnerDepartmentId, t2.CaseOwnerId as CaseHeaders_CaseOwnerId, t2.CaseOwnerName as CaseHeaders_CaseOwnerName, t2.CaseOwnerRank as CaseHeaders_CaseOwnerRank, t2.TABC as CaseHeaders_TABC, t2.AdditionalInformation as CaseHeaders_AdditionalInformation, t2.ActivityType as CaseHeaders_ActivityType, t2.OfficerStepShiftId as CaseHeaders_OfficerStepShiftId, t2.StepZoneId as CaseHeaders_StepZoneId, t2.OldCaseID as CaseHeaders_OldCaseID
FROM DUI.StepOfficerShiftCases t1
LEFT JOIN DUI.CaseHeaders t2 ON t1.CaseId = t2.CaseId
WHERE t1.CaseId IS NOT NULL


-- Simple view for StepOfficerShiftZones
-- Provides secure access to StepOfficerShiftZones data excluding sensitive information
CREATE VIEW DUI.v_stepofficershiftzones AS
SELECT StepOfficerShiftZoneId, OfficerStepShiftId, StepZoneId
FROM DUI.StepOfficerShiftZones
WHERE StepOfficerShiftZoneId IS NOT NULL


-- Relationship view: StepOfficerShiftZones with OfficerStepShifts
-- Provides StepOfficerShiftZones data joined with related OfficerStepShifts information
CREATE VIEW DUI.v_stepofficershiftzones_with_officerstepshifts AS
SELECT t1.StepOfficerShiftZoneId, t1.OfficerStepShiftId, t1.StepZoneId, t2.StepOfficerShiftId as OfficerStepShifts_StepOfficerShiftId, t2.OfficerId as OfficerStepShifts_OfficerId, t2.DepartmentId as OfficerStepShifts_DepartmentId, t2.ShiftStart as OfficerStepShifts_ShiftStart, t2.ShiftEnd as OfficerStepShifts_ShiftEnd, t2.TotalHRSWorked as OfficerStepShifts_TotalHRSWorked, t2.MileageStart as OfficerStepShifts_MileageStart, t2.MileageEnd as OfficerStepShifts_MileageEnd, t2.MileageTotal as OfficerStepShifts_MileageTotal, t2.Comments as OfficerStepShifts_Comments, t2.StepShiftId as OfficerStepShifts_StepShiftId, t2.StepGrantTypeId as OfficerStepShifts_StepGrantTypeId, t2.Submitted as OfficerStepShifts_Submitted, t2.Approved as OfficerStepShifts_Approved, t2.ApprovedBy as OfficerStepShifts_ApprovedBy, t2.Rejected as OfficerStepShifts_Rejected, t2.RejectedBy as OfficerStepShifts_RejectedBy, t2.CreatedBy as OfficerStepShifts_CreatedBy, t2.Report as OfficerStepShifts_Report, t2.OldOfficerStepShiftId as OfficerStepShifts_OldOfficerStepShiftId
FROM DUI.StepOfficerShiftZones t1
LEFT JOIN DUI.OfficerStepShifts t2 ON t1.OfficerStepShiftId = t2.StepOfficerShiftId
WHERE t1.OfficerStepShiftId IS NOT NULL


-- Simple view for StepShifts
-- Provides secure access to StepShifts data excluding sensitive information
CREATE VIEW DUI.v_stepshifts AS
SELECT StepShiftId, DepartmentId, LocationId, StepGrantTypeId, ShiftStart, ShiftEnd, CreatedBy, OldStepShiftId
FROM DUI.StepShifts
WHERE StepShiftId IS NOT NULL


-- Relationship view: StepShifts with TBL_OPT_Step_Grant_Type
-- Provides StepShifts data joined with related TBL_OPT_Step_Grant_Type information
CREATE VIEW DUI.v_stepshifts_with_tbl_opt_step_grant_type AS
SELECT t1.StepShiftId, t1.DepartmentId, t1.LocationId, t1.StepGrantTypeId, t1.ShiftStart, t1.ShiftEnd, t1.CreatedBy, t1.OldStepShiftId, t2.StepGrantTypeId as TBL_OPT_Step_Grant_Type_StepGrantTypeId, t2.StepGrantTypeDesc as TBL_OPT_Step_Grant_Type_StepGrantTypeDesc, t2.Active as TBL_OPT_Step_Grant_Type_Active
FROM DUI.StepShifts t1
LEFT JOIN DUI.TBL_OPT_Step_Grant_Type t2 ON t1.StepGrantTypeId = t2.StepGrantTypeId
WHERE t1.StepGrantTypeId IS NOT NULL


-- Simple view for StepZones
-- Provides secure access to StepZones data excluding sensitive information
CREATE VIEW DUI.v_stepzones AS
SELECT StepZoneId, DepartmentId, LocationId, ZoneDesc, StepGrantTypeId, OldStepZoneId, CreatedBy
FROM DUI.StepZones
WHERE StepZoneId IS NOT NULL


-- Relationship view: StepZones with TBL_OPT_Step_Grant_Type
-- Provides StepZones data joined with related TBL_OPT_Step_Grant_Type information
CREATE VIEW DUI.v_stepzones_with_tbl_opt_step_grant_type AS
SELECT t1.StepZoneId, t1.DepartmentId, t1.LocationId, t1.ZoneDesc, t1.StepGrantTypeId, t1.OldStepZoneId, t1.CreatedBy, t2.StepGrantTypeId as TBL_OPT_Step_Grant_Type_StepGrantTypeId, t2.StepGrantTypeDesc as TBL_OPT_Step_Grant_Type_StepGrantTypeDesc, t2.Active as TBL_OPT_Step_Grant_Type_Active
FROM DUI.StepZones t1
LEFT JOIN DUI.TBL_OPT_Step_Grant_Type t2 ON t1.StepGrantTypeId = t2.StepGrantTypeId
WHERE t1.StepGrantTypeId IS NOT NULL


-- Simple view for Supplement
-- Provides secure access to Supplement data excluding sensitive information
CREATE VIEW DUI.v_supplement AS
SELECT SupplementID, CaseID, OfficerID, DeptID, IncludeFst, IncludeIntox, IncludeWitness, IncludeAttach, Supplement, IsTrainingPurpose, DtCreated, Submitted, CreatedBy, OldOfficerSupplementId, ArchiveAddendumId, ArchiveDefendantId_FK, ArchiveIntoxReportId, ArchiveOnWaterId, Active
FROM DUI.Supplement
WHERE SupplementID IS NOT NULL


-- Simple view for SupplementDocuments
-- Provides secure access to SupplementDocuments data excluding sensitive information
CREATE VIEW DUI.v_supplementdocuments AS
SELECT SupplementDocumentsId, SupplementID, DocumentId, UploadedBy, Uploaded, DocumentTypeId
FROM DUI.SupplementDocuments
WHERE SupplementDocumentsId IS NOT NULL


-- Relationship view: SupplementDocuments with Documents
-- Provides SupplementDocuments data joined with related Documents information
CREATE VIEW DUI.v_supplementdocuments_with_documents AS
SELECT t1.SupplementDocumentsId, t1.SupplementID, t1.DocumentId, t1.UploadedBy, t1.Uploaded, t1.DocumentTypeId, t2.DocumentId as Documents_DocumentId, t2.DocumentTypeId as Documents_DocumentTypeId, t2.FileTypeId as Documents_FileTypeId, t2.DocumentName as Documents_DocumentName, t2.OriginalFileName as Documents_OriginalFileName, t2.PhysicalFileName as Documents_PhysicalFileName, t2.Active as Documents_Active, t2.Created as Documents_Created, t2.CreatedBy as Documents_CreatedBy, t2.ObjectId as Documents_ObjectId, t2.ObjectTypeId as Documents_ObjectTypeId, t2.OldDocumentId as Documents_OldDocumentId
FROM DUI.SupplementDocuments t1
LEFT JOIN DUI.Documents t2 ON t1.DocumentId = t2.DocumentId
WHERE t1.DocumentId IS NOT NULL


-- Simple view for SupplementFieldSobrietyTests
-- Provides secure access to SupplementFieldSobrietyTests data excluding sensitive information
CREATE VIEW DUI.v_supplementfieldsobrietytests AS
SELECT FieldSobrietyTestId, SupplementId, FSTGiven, WhyNotGivenFST, DefendantRefused, PhysicalInjuries, DefMoreThan65, TimeAshore, OnWater, SeatedFST, AttachNote, TimeStartedFST, WaterTestGiven, WhyNotWaterTest, PhysicalProblem, PhysicalProblemDesc
FROM DUI.SupplementFieldSobrietyTests
WHERE FieldSobrietyTestId IS NOT NULL


-- Simple view for SupplementIntoxilyzerReport
-- Provides secure access to SupplementIntoxilyzerReport data excluding sensitive information
CREATE VIEW DUI.v_supplementintoxilyzerreport AS
SELECT IntoxReportId, SupplementId, Result1Num, LabToxicologyResults, IsAttachment
FROM DUI.SupplementIntoxilyzerReport
WHERE IntoxReportId IS NOT NULL


-- Simple view for SupplementWitnesses
-- Provides secure access to SupplementWitnesses data excluding sensitive information
CREATE VIEW DUI.v_supplementwitnesses AS
SELECT SupplementWitnessId, SupplementId, LastName, FirstName, RaceId, GenderId, IsVictim, WhatWitnessObserved, StateId, CountyId, Lat, Lng, ArchiveOfficer, ArchiveState
FROM DUI.SupplementWitnesses
WHERE SupplementWitnessId IS NOT NULL


-- Simple view for SystemModeControls
-- Provides secure access to SystemModeControls data excluding sensitive information
CREATE VIEW DUI.v_systemmodecontrols AS
SELECT SystemModeControlId, ModeId, PageId, ControlName, Label, Visible, Required, Enabled, Active, Created, OldSystemModeControlId
FROM DUI.SystemModeControls
WHERE SystemModeControlId IS NOT NULL


-- Relationship view: SystemModeControls with SystemPages
-- Provides SystemModeControls data joined with related SystemPages information
CREATE VIEW DUI.v_systemmodecontrols_with_systempages AS
SELECT t1.SystemModeControlId, t1.ModeId, t1.PageId, t1.ControlName, t1.Label, t1.Visible, t1.Required, t1.Enabled, t1.Active, t1.Created, t1.OldSystemModeControlId, t2.SystemPageId as SystemPages_SystemPageId, t2.Title as SystemPages_Title, t2.PageName as SystemPages_PageName, t2.Active as SystemPages_Active, t2.Created as SystemPages_Created, t2.OldSystemPageId as SystemPages_OldSystemPageId
FROM DUI.SystemModeControls t1
LEFT JOIN DUI.SystemPages t2 ON t1.PageId = t2.SystemPageId
WHERE t1.PageId IS NOT NULL


-- Simple view for SystemPages
-- Provides secure access to SystemPages data excluding sensitive information
CREATE VIEW DUI.v_systempages AS
SELECT SystemPageId, Title, PageName, Active, Created, OldSystemPageId
FROM DUI.SystemPages
WHERE SystemPageId IS NOT NULL


-- Simple view for TABCNotificationLog
-- Provides secure access to TABCNotificationLog data excluding sensitive information
CREATE VIEW DUI.v_tabcnotificationlog AS
SELECT TABCNotificationLogId, CaseId, BodyContents, SendSuccess, MarkedAsSent, Test
FROM DUI.TABCNotificationLog
WHERE TABCNotificationLogId IS NOT NULL


-- Simple view for TBL_OPTIONS_Master
-- Provides secure access to TBL_OPTIONS_Master data excluding sensitive information
CREATE VIEW DUI.v_tbl_options_master AS
SELECT Id, ModelName, TableName, TableLabel, IdFiled, Filed1Name, Field1Label, Field2Name, Field2Label, Field3Name, Field3Label, Field4Name, Field4Label, Field5Name, Field5Label, OrderField, ActiveField, Active
FROM DUI.TBL_OPTIONS_Master
WHERE Id IS NOT NULL


-- Simple view for TBL_OPT_Accidents
-- Provides secure access to TBL_OPT_Accidents data excluding sensitive information
CREATE VIEW DUI.v_tbl_opt_accidents AS
SELECT AccidentId, Active
FROM DUI.TBL_OPT_Accidents
WHERE AccidentId IS NOT NULL


-- Simple view for TBL_OPT_ActivityTypes
-- Provides secure access to TBL_OPT_ActivityTypes data excluding sensitive information
CREATE VIEW DUI.v_tbl_opt_activitytypes AS
SELECT ActivityTypeId, ActivityTypeDesc, FullCase, Active
FROM DUI.TBL_OPT_ActivityTypes
WHERE ActivityTypeId IS NOT NULL


-- Simple view for TBL_OPT_AddressGroup
-- Provides secure access to TBL_OPT_AddressGroup data excluding sensitive information
CREATE VIEW DUI.v_tbl_opt_addressgroup AS
SELECT Icon, Active
FROM DUI.TBL_OPT_AddressGroup
WHERE AddressGroupId IS NOT NULL


-- Simple view for TBL_OPT_AlcoholTypes
-- Provides secure access to TBL_OPT_AlcoholTypes data excluding sensitive information
CREATE VIEW DUI.v_tbl_opt_alcoholtypes AS
SELECT AlcoholTypeId, Alcohol, Active
FROM DUI.TBL_OPT_AlcoholTypes
WHERE AlcoholTypeId IS NOT NULL


-- Simple view for TBL_OPT_BWI_Motors
-- Provides secure access to TBL_OPT_BWI_Motors data excluding sensitive information
CREATE VIEW DUI.v_tbl_opt_bwi_motors AS
SELECT BwiMotorId, BwiMotorDesc, Active
FROM DUI.TBL_OPT_BWI_Motors
WHERE BwiMotorId IS NOT NULL


-- Simple view for TBL_OPT_BWI_Vessels
-- Provides secure access to TBL_OPT_BWI_Vessels data excluding sensitive information
CREATE VIEW DUI.v_tbl_opt_bwi_vessels AS
SELECT BwiVesselId, BwiVesselDesc, Active
FROM DUI.TBL_OPT_BWI_Vessels
WHERE BwiVesselId IS NOT NULL


-- Simple view for TBL_OPT_BodyWaters
-- Provides secure access to TBL_OPT_BodyWaters data excluding sensitive information
CREATE VIEW DUI.v_tbl_opt_bodywaters AS
SELECT BodyOfWaterId, Code, BodyOfWaterDesc, Active
FROM DUI.TBL_OPT_BodyWaters
WHERE BodyOfWaterId IS NOT NULL


-- Simple view for TBL_OPT_Case_Outcome_Dismissals
-- Provides secure access to TBL_OPT_Case_Outcome_Dismissals data excluding sensitive information
CREATE VIEW DUI.v_tbl_opt_case_outcome_dismissals AS
SELECT CaseOutcomeDismissalId, DismissalText, Active
FROM DUI.TBL_OPT_Case_Outcome_Dismissals
WHERE CaseOutcomeDismissalId IS NOT NULL


-- Simple view for TBL_OPT_Case_Outcome_Pleas
-- Provides secure access to TBL_OPT_Case_Outcome_Pleas data excluding sensitive information
CREATE VIEW DUI.v_tbl_opt_case_outcome_pleas AS
SELECT CaseOutcomePleaId, PleaText, Active
FROM DUI.TBL_OPT_Case_Outcome_Pleas
WHERE CaseOutcomePleaId IS NOT NULL


-- Simple view for TBL_OPT_Case_Outcome_Trials
-- Provides secure access to TBL_OPT_Case_Outcome_Trials data excluding sensitive information
CREATE VIEW DUI.v_tbl_opt_case_outcome_trials AS
SELECT CaseOutcomeTrialId, TrialText, Active
FROM DUI.TBL_OPT_Case_Outcome_Trials
WHERE CaseOutcomeTrialId IS NOT NULL


-- Simple view for TBL_OPT_Counties
-- Provides secure access to TBL_OPT_Counties data excluding sensitive information
CREATE VIEW DUI.v_tbl_opt_counties AS
SELECT CountyId, CountyName, Active
FROM DUI.TBL_OPT_Counties
WHERE CountyId IS NOT NULL


-- Simple view for TBL_OPT_DPS_Drugs
-- Provides secure access to TBL_OPT_DPS_Drugs data excluding sensitive information
CREATE VIEW DUI.v_tbl_opt_dps_drugs AS
SELECT DpsDrugListId, DpsDrug, DpsDrugCategory, Active
FROM DUI.TBL_OPT_DPS_Drugs
WHERE DpsDrugListId IS NOT NULL


-- Simple view for TBL_OPT_Dismissals
-- Provides secure access to TBL_OPT_Dismissals data excluding sensitive information
CREATE VIEW DUI.v_tbl_opt_dismissals AS
SELECT DismissalId, Active
FROM DUI.TBL_OPT_Dismissals
WHERE DismissalId IS NOT NULL


-- Simple view for TBL_OPT_DocumentFileTypes
-- Provides secure access to TBL_OPT_DocumentFileTypes data excluding sensitive information
CREATE VIEW DUI.v_tbl_opt_documentfiletypes AS
SELECT FileTypeId, FileName, Extension, Icon, Image, MimeType, Active, Created
FROM DUI.TBL_OPT_DocumentFileTypes
WHERE FileTypeId IS NOT NULL


-- Simple view for TBL_OPT_DocumentTypes
-- Provides secure access to TBL_OPT_DocumentTypes data excluding sensitive information
CREATE VIEW DUI.v_tbl_opt_documenttypes AS
SELECT DocumentTypeId, DocumentTypeName, Active, Created
FROM DUI.TBL_OPT_DocumentTypes
WHERE DocumentTypeId IS NOT NULL


-- Simple view for TBL_OPT_Educations
-- Provides secure access to TBL_OPT_Educations data excluding sensitive information
CREATE VIEW DUI.v_tbl_opt_educations AS
SELECT EducationId, Active
FROM DUI.TBL_OPT_Educations
WHERE EducationId IS NOT NULL


-- Simple view for TBL_OPT_Employed_PWD
-- Provides secure access to TBL_OPT_Employed_PWD data excluding sensitive information
CREATE VIEW DUI.v_tbl_opt_employed_pwd AS
SELECT EmployedId, Employed, Active
FROM DUI.TBL_OPT_Employed_PWD
WHERE EmployedId IS NOT NULL


-- Simple view for TBL_OPT_Ethnicity
-- Provides secure access to TBL_OPT_Ethnicity data excluding sensitive information
CREATE VIEW DUI.v_tbl_opt_ethnicity AS
SELECT Active
FROM DUI.TBL_OPT_Ethnicity
WHERE EthnicityId IS NOT NULL


-- Simple view for TBL_OPT_Eye_Colors
-- Provides secure access to TBL_OPT_Eye_Colors data excluding sensitive information
CREATE VIEW DUI.v_tbl_opt_eye_colors AS
SELECT EyeColorId, EyeColorDesc, NcicCode, Active
FROM DUI.TBL_OPT_Eye_Colors
WHERE EyeColorId IS NOT NULL


-- Simple view for TBL_OPT_Foot_Wear_Types
-- Provides secure access to TBL_OPT_Foot_Wear_Types data excluding sensitive information
CREATE VIEW DUI.v_tbl_opt_foot_wear_types AS
SELECT FootwearTypeId, Active
FROM DUI.TBL_OPT_Foot_Wear_Types
WHERE FootwearTypeId IS NOT NULL


-- Simple view for TBL_OPT_Genders
-- Provides secure access to TBL_OPT_Genders data excluding sensitive information
CREATE VIEW DUI.v_tbl_opt_genders AS
SELECT GenderId, GenderAbbreviation, NcicCode, Active
FROM DUI.TBL_OPT_Genders
WHERE GenderId IS NOT NULL


-- Simple view for TBL_OPT_HGN_Estimated_Angle
-- Provides secure access to TBL_OPT_HGN_Estimated_Angle data excluding sensitive information
CREATE VIEW DUI.v_tbl_opt_hgn_estimated_angle AS
SELECT HgnEstimatedAngleId, EstimatedAngleDesc, Active, DisplayOrder, ShortName
FROM DUI.TBL_OPT_HGN_Estimated_Angle
WHERE HgnEstimatedAngleId IS NOT NULL


-- Simple view for TBL_OPT_Hair_Colors
-- Provides secure access to TBL_OPT_Hair_Colors data excluding sensitive information
CREATE VIEW DUI.v_tbl_opt_hair_colors AS
SELECT HairColorId, HairColorDesc, NcicCode, Active
FROM DUI.TBL_OPT_Hair_Colors
WHERE HairColorId IS NOT NULL


-- Simple view for TBL_OPT_INTOX_VerifyTemp
-- Provides secure access to TBL_OPT_INTOX_VerifyTemp data excluding sensitive information
CREATE VIEW DUI.v_tbl_opt_intox_verifytemp AS
SELECT IntoxVerifytempId, Verifytemp, Active
FROM DUI.TBL_OPT_INTOX_VerifyTemp
WHERE IntoxVerifytempId IS NOT NULL


-- Simple view for TBL_OPT_Injury
-- Provides secure access to TBL_OPT_Injury data excluding sensitive information
CREATE VIEW DUI.v_tbl_opt_injury AS
SELECT InjuryId, Active
FROM DUI.TBL_OPT_Injury
WHERE InjuryId IS NOT NULL


-- Simple view for TBL_OPT_Integration_Vendors
-- Provides secure access to TBL_OPT_Integration_Vendors data excluding sensitive information
CREATE VIEW DUI.v_tbl_opt_integration_vendors AS
SELECT VendorId, VendorName, VendorSystemName, Active, VendorGraphicUrl, VendorXmlVerbiage, VendorPdfVerbiage, VendorXmlButtonText, VendorPdfButtonText
FROM DUI.TBL_OPT_Integration_Vendors
WHERE VendorId IS NOT NULL


-- Simple view for TBL_OPT_Interview_Questions
-- Provides secure access to TBL_OPT_Interview_Questions data excluding sensitive information
CREATE VIEW DUI.v_tbl_opt_interview_questions AS
SELECT QuestionId, Question, QuestionOrder, Active
FROM DUI.TBL_OPT_Interview_Questions
WHERE QuestionId IS NOT NULL


-- Simple view for TBL_OPT_Light_Conditions
-- Provides secure access to TBL_OPT_Light_Conditions data excluding sensitive information
CREATE VIEW DUI.v_tbl_opt_light_conditions AS
SELECT LightConditionId, Active
FROM DUI.TBL_OPT_Light_Conditions
WHERE LightConditionId IS NOT NULL


-- Simple view for TBL_OPT_Mark43_Lookup
-- Provides secure access to TBL_OPT_Mark43_Lookup data excluding sensitive information
CREATE VIEW DUI.v_tbl_opt_mark43_lookup AS
SELECT Mark43LookupId, Mark43AttributeType, Mark43Code, Mark43Desc, LeadrsId, [In], [Out], OrganizationId
FROM DUI.TBL_OPT_Mark43_Lookup
WHERE Mark43LookupId IS NOT NULL


-- Simple view for TBL_OPT_More_Less_Intoxicated
-- Provides secure access to TBL_OPT_More_Less_Intoxicated data excluding sensitive information
CREATE VIEW DUI.v_tbl_opt_more_less_intoxicated AS
SELECT MoreLessIntoxId, Active
FROM DUI.TBL_OPT_More_Less_Intoxicated
WHERE MoreLessIntoxId IS NOT NULL


-- Simple view for TBL_OPT_NCIC_Colors
-- Provides secure access to TBL_OPT_NCIC_Colors data excluding sensitive information
CREATE VIEW DUI.v_tbl_opt_ncic_colors AS
SELECT NcicColorId, NcicCode, Active
FROM DUI.TBL_OPT_NCIC_Colors
WHERE NcicColorId IS NOT NULL


-- Simple view for TBL_OPT_NCIC_Instructions
-- Provides secure access to TBL_OPT_NCIC_Instructions data excluding sensitive information
CREATE VIEW DUI.v_tbl_opt_ncic_instructions AS
SELECT NcicInstructionId, TransportModeId, Instruction, Active
FROM DUI.TBL_OPT_NCIC_Instructions
WHERE NcicInstructionId IS NOT NULL


-- Simple view for TBL_OPT_NCIC_Labels
-- Provides secure access to TBL_OPT_NCIC_Labels data excluding sensitive information
CREATE VIEW DUI.v_tbl_opt_ncic_labels AS
SELECT NcicLabelId, TransportModeId, TableName, NcicCode, Active
FROM DUI.TBL_OPT_NCIC_Labels
WHERE NcicLabelId IS NOT NULL


-- Simple view for TBL_OPT_NCIC_Transport_Make
-- Provides secure access to TBL_OPT_NCIC_Transport_Make data excluding sensitive information
CREATE VIEW DUI.v_tbl_opt_ncic_transport_make AS
SELECT NcicTransportMakeId, TransportTypeId, NcicCode, Comments, Active, ModeId
FROM DUI.TBL_OPT_NCIC_Transport_Make
WHERE NcicTransportMakeId IS NOT NULL


-- Simple view for TBL_OPT_NCIC_Transport_Mode
-- Provides secure access to TBL_OPT_NCIC_Transport_Mode data excluding sensitive information
CREATE VIEW DUI.v_tbl_opt_ncic_transport_mode AS
SELECT NcicTransportModeId, Comments, Active, ModeId
FROM DUI.TBL_OPT_NCIC_Transport_Mode
WHERE NcicTransportModeId IS NOT NULL


-- Simple view for TBL_OPT_NCIC_Transport_Type
-- Provides secure access to TBL_OPT_NCIC_Transport_Type data excluding sensitive information
CREATE VIEW DUI.v_tbl_opt_ncic_transport_type AS
SELECT NcicTransportTypeId, TransportModeId, Active
FROM DUI.TBL_OPT_NCIC_Transport_Type
WHERE NcicTransportTypeId IS NOT NULL


-- Simple view for TBL_OPT_NCIC_Vehcile_Style_Types
-- Provides secure access to TBL_OPT_NCIC_Vehcile_Style_Types data excluding sensitive information
CREATE VIEW DUI.v_tbl_opt_ncic_vehcile_style_types AS
SELECT VehicleStyleId, TransportTypeId, NcicCode, Comments, Active
FROM DUI.TBL_OPT_NCIC_Vehcile_Style_Types
WHERE VehicleStyleId IS NOT NULL


-- Simple view for TBL_OPT_NCIC_Vehicle_Body_Style
-- Provides secure access to TBL_OPT_NCIC_Vehicle_Body_Style data excluding sensitive information
CREATE VIEW DUI.v_tbl_opt_ncic_vehicle_body_style AS
SELECT BodyStyleId, TransportTypeId, NcicCode, Active
FROM DUI.TBL_OPT_NCIC_Vehicle_Body_Style
WHERE BodyStyleId IS NOT NULL


-- Simple view for TBL_OPT_NCIC_Vehicle_Model
-- Provides secure access to TBL_OPT_NCIC_Vehicle_Model data excluding sensitive information
CREATE VIEW DUI.v_tbl_opt_ncic_vehicle_model AS
SELECT NcicVehicleModelId, MakeId, NcicCode, Active
FROM DUI.TBL_OPT_NCIC_Vehicle_Model
WHERE NcicVehicleModelId IS NOT NULL


-- Simple view for TBL_OPT_Offense
-- Provides secure access to TBL_OPT_Offense data excluding sensitive information
CREATE VIEW DUI.v_tbl_opt_offense AS
SELECT OffenseId, OffenseCitation, OffenseClassification, OffenseCode, OffenseComplaintId, OffenseType, OffenseFelony, OffenseIntoxilizer, OffenseOpenContainer, OffensePriors, OffenseMinors, OffenseMinor, OffenseAssault, OffenseManslaughter, OffenseTitle, OffenseSubtitle, OffenseOrder, OffenseBwi, Mark43OffDesc, Active
FROM DUI.TBL_OPT_Offense
WHERE OffenseId IS NOT NULL


-- Simple view for TBL_OPT_Offense_Types
-- Provides secure access to TBL_OPT_Offense_Types data excluding sensitive information
CREATE VIEW DUI.v_tbl_opt_offense_types AS
SELECT OffenseTypeId, OffenseTypeDesc, Active
FROM DUI.TBL_OPT_Offense_Types
WHERE OffenseTypeId IS NOT NULL


-- Simple view for TBL_OPT_Operation_Occupation
-- Provides secure access to TBL_OPT_Operation_Occupation data excluding sensitive information
CREATE VIEW DUI.v_tbl_opt_operation_occupation AS
SELECT OperatorOccupationId, Occupation, Active
FROM DUI.TBL_OPT_Operation_Occupation
WHERE OperatorOccupationId IS NOT NULL


-- Simple view for TBL_OPT_Outcomes
-- Provides secure access to TBL_OPT_Outcomes data excluding sensitive information
CREATE VIEW DUI.v_tbl_opt_outcomes AS
SELECT OutcomeId, Active
FROM DUI.TBL_OPT_Outcomes
WHERE OutcomeId IS NOT NULL


-- Simple view for TBL_OPT_Plea
-- Provides secure access to TBL_OPT_Plea data excluding sensitive information
CREATE VIEW DUI.v_tbl_opt_plea AS
SELECT PleaId, Active
FROM DUI.TBL_OPT_Plea
WHERE PleaId IS NOT NULL


-- Simple view for TBL_OPT_Races
-- Provides secure access to TBL_OPT_Races data excluding sensitive information
CREATE VIEW DUI.v_tbl_opt_races AS
SELECT RaceId, NcicCode, Active
FROM DUI.TBL_OPT_Races
WHERE RaceId IS NOT NULL


-- Simple view for TBL_OPT_Radar_Types
-- Provides secure access to TBL_OPT_Radar_Types data excluding sensitive information
CREATE VIEW DUI.v_tbl_opt_radar_types AS
SELECT RadarTypeId, Active, RadarInfoShown
FROM DUI.TBL_OPT_Radar_Types
WHERE RadarTypeId IS NOT NULL


-- Simple view for TBL_OPT_Reason_For_Stop
-- Provides secure access to TBL_OPT_Reason_For_Stop data excluding sensitive information
CREATE VIEW DUI.v_tbl_opt_reason_for_stop AS
SELECT ReasonForStopId, ReasonForStopTxt, Active, AssocControl, IsCrash, Dwi, Bwi
FROM DUI.TBL_OPT_Reason_For_Stop
WHERE ReasonForStopId IS NOT NULL


-- Simple view for TBL_OPT_Road_Conditions
-- Provides secure access to TBL_OPT_Road_Conditions data excluding sensitive information
CREATE VIEW DUI.v_tbl_opt_road_conditions AS
SELECT RoadConditionId, Active
FROM DUI.TBL_OPT_Road_Conditions
WHERE RoadConditionId IS NOT NULL


-- Simple view for TBL_OPT_Road_Surface
-- Provides secure access to TBL_OPT_Road_Surface data excluding sensitive information
CREATE VIEW DUI.v_tbl_opt_road_surface AS
SELECT RoadSurfaceId, Active
FROM DUI.TBL_OPT_Road_Surface
WHERE RoadSurfaceId IS NOT NULL


-- Simple view for TBL_OPT_Skin_Complexion
-- Provides secure access to TBL_OPT_Skin_Complexion data excluding sensitive information
CREATE VIEW DUI.v_tbl_opt_skin_complexion AS
SELECT SkinId, Abbreviation, NcicCode, Active
FROM DUI.TBL_OPT_Skin_Complexion
WHERE SkinId IS NOT NULL


-- Simple view for TBL_OPT_SpecimenSubmittedMethod
-- Provides secure access to TBL_OPT_SpecimenSubmittedMethod data excluding sensitive information
CREATE VIEW DUI.v_tbl_opt_specimensubmittedmethod AS
SELECT SpecimenSubmittedMethodId, Method, Active
FROM DUI.TBL_OPT_SpecimenSubmittedMethod
WHERE SpecimenSubmittedMethodId IS NOT NULL


-- Simple view for TBL_OPT_Specimen_Storage
-- Provides secure access to TBL_OPT_Specimen_Storage data excluding sensitive information
CREATE VIEW DUI.v_tbl_opt_specimen_storage AS
SELECT SpecimenStorageId, Storage, Active
FROM DUI.TBL_OPT_Specimen_Storage
WHERE SpecimenStorageId IS NOT NULL


-- Simple view for TBL_OPT_States
-- Provides secure access to TBL_OPT_States data excluding sensitive information
CREATE VIEW DUI.v_tbl_opt_states AS
SELECT StateId, StateName, Abbreviation, Active
FROM DUI.TBL_OPT_States
WHERE StateId IS NOT NULL


-- Simple view for TBL_OPT_Status
-- Provides secure access to TBL_OPT_Status data excluding sensitive information
CREATE VIEW DUI.v_tbl_opt_status AS
SELECT StatusId, Active
FROM DUI.TBL_OPT_Status
WHERE StatusId IS NOT NULL


-- Simple view for TBL_OPT_Step_Dar_Event_Types
-- Provides secure access to TBL_OPT_Step_Dar_Event_Types data excluding sensitive information
CREATE VIEW DUI.v_tbl_opt_step_dar_event_types AS
SELECT StepDarEventTypeId, StepDarEventTypeDesc, Active
FROM DUI.TBL_OPT_Step_Dar_Event_Types
WHERE StepDarEventTypeId IS NOT NULL


-- Simple view for TBL_OPT_Step_Grant_Type
-- Provides secure access to TBL_OPT_Step_Grant_Type data excluding sensitive information
CREATE VIEW DUI.v_tbl_opt_step_grant_type AS
SELECT StepGrantTypeId, StepGrantTypeDesc, Active
FROM DUI.TBL_OPT_Step_Grant_Type
WHERE StepGrantTypeId IS NOT NULL


-- Simple view for TBL_OPT_Surfaces
-- Provides secure access to TBL_OPT_Surfaces data excluding sensitive information
CREATE VIEW DUI.v_tbl_opt_surfaces AS
SELECT SurfaceId, Active
FROM DUI.TBL_OPT_Surfaces
WHERE SurfaceId IS NOT NULL


-- Simple view for TBL_OPT_System_Mode
-- Provides secure access to TBL_OPT_System_Mode data excluding sensitive information
CREATE VIEW DUI.v_tbl_opt_system_mode AS
SELECT ModeId, ModeName, ModeOrder, OffenseTypeId, Active, NcicTransportModeId
FROM DUI.TBL_OPT_System_Mode
WHERE ModeId IS NOT NULL


-- Relationship view: TBL_OPT_System_Mode with TBL_OPT_NCIC_Transport_Mode
-- Provides TBL_OPT_System_Mode data joined with related TBL_OPT_NCIC_Transport_Mode information
CREATE VIEW DUI.v_tbl_opt_system_mode_with_tbl_opt_ncic_transport_mode AS
SELECT t1.ModeId, t1.ModeName, t1.ModeOrder, t1.OffenseTypeId, t1.Active, t1.NcicTransportModeId, t2.NcicTransportModeId as TBL_OPT_NCIC_Transport_Mode_NcicTransportModeId, t2.Comments as TBL_OPT_NCIC_Transport_Mode_Comments, t2.Active as TBL_OPT_NCIC_Transport_Mode_Active, t2.ModeId as TBL_OPT_NCIC_Transport_Mode_ModeId
FROM DUI.TBL_OPT_System_Mode t1
LEFT JOIN DUI.TBL_OPT_NCIC_Transport_Mode t2 ON t1.NcicTransportModeId = t2.NcicTransportModeId
WHERE t1.NcicTransportModeId IS NOT NULL


-- Simple view for TBL_OPT_Tox_Spec_Types
-- Provides secure access to TBL_OPT_Tox_Spec_Types data excluding sensitive information
CREATE VIEW DUI.v_tbl_opt_tox_spec_types AS
SELECT ToxSpecTypeId, ToxSpecTypeDesc, Active
FROM DUI.TBL_OPT_Tox_Spec_Types
WHERE ToxSpecTypeId IS NOT NULL


-- Simple view for TBL_OPT_Tox_screen_Result
-- Provides secure access to TBL_OPT_Tox_screen_Result data excluding sensitive information
CREATE VIEW DUI.v_tbl_opt_tox_screen_result AS
SELECT ToxScreenResultId, Result, DisplayTextbox, Active
FROM DUI.TBL_OPT_Tox_screen_Result
WHERE ToxScreenResultId IS NOT NULL


-- Simple view for TBL_OPT_Violation
-- Provides secure access to TBL_OPT_Violation data excluding sensitive information
CREATE VIEW DUI.v_tbl_opt_violation AS
SELECT ViolationId, ViolationDeswc, Active, SortOrder, IsArrest, IsOther, IsCitation, IsWarning
FROM DUI.TBL_OPT_Violation
WHERE ViolationId IS NOT NULL


-- Simple view for TBL_OPT_Water_Surfaces
-- Provides secure access to TBL_OPT_Water_Surfaces data excluding sensitive information
CREATE VIEW DUI.v_tbl_opt_water_surfaces AS
SELECT WaterSurfaceId, WaterSurfaceDesc, Active
FROM DUI.TBL_OPT_Water_Surfaces
WHERE WaterSurfaceId IS NOT NULL


-- Simple view for TBL_OPT_Wave_Height
-- Provides secure access to TBL_OPT_Wave_Height data excluding sensitive information
CREATE VIEW DUI.v_tbl_opt_wave_height AS
SELECT WaveHeightId, WaveHeightDesc, Active, SortOrder
FROM DUI.TBL_OPT_Wave_Height
WHERE WaveHeightId IS NOT NULL


-- Simple view for TBL_OPT_Wave_Types
-- Provides secure access to TBL_OPT_Wave_Types data excluding sensitive information
CREATE VIEW DUI.v_tbl_opt_wave_types AS
SELECT WaveTypeId, WaveTypeDesc, Active
FROM DUI.TBL_OPT_Wave_Types
WHERE WaveTypeId IS NOT NULL


-- Simple view for TBL_OPT_Weather
-- Provides secure access to TBL_OPT_Weather data excluding sensitive information
CREATE VIEW DUI.v_tbl_opt_weather AS
SELECT WeatherId, Active
FROM DUI.TBL_OPT_Weather
WHERE WeatherId IS NOT NULL


-- Simple view for TBL_OPT_Wind_Speed
-- Provides secure access to TBL_OPT_Wind_Speed data excluding sensitive information
CREATE VIEW DUI.v_tbl_opt_wind_speed AS
SELECT WindSpeedId, WindSpeedDesc, Active
FROM DUI.TBL_OPT_Wind_Speed
WHERE WindSpeedId IS NOT NULL


-- Simple view for TBL_OPT_Zones
-- Provides secure access to TBL_OPT_Zones data excluding sensitive information
CREATE VIEW DUI.v_tbl_opt_zones AS
SELECT ZoneId, ZoneDesc, Active
FROM DUI.TBL_OPT_Zones
WHERE ZoneId IS NOT NULL


-- Simple view for Vehicle_Watercraft
-- Provides secure access to Vehicle_Watercraft data excluding sensitive information
CREATE VIEW DUI.v_vehicle_watercraft AS
SELECT VehicleWatercraftId, HIN, MotorId, VesselId, VesselComments, BoatCondition, Less50HP, VehicleId
FROM DUI.Vehicle_Watercraft
WHERE VehicleWatercraftId IS NOT NULL


-- Relationship view: Vehicle_Watercraft with CaseVehicles
-- Provides Vehicle_Watercraft data joined with related CaseVehicles information
CREATE VIEW DUI.v_vehicle_watercraft_with_casevehicles AS
SELECT t1.VehicleWatercraftId, t1.HIN, t1.MotorId, t1.VesselId, t1.VesselComments, t1.BoatCondition, t1.Less50HP, t1.VehicleId, t2.CaseVehicleId as CaseVehicles_CaseVehicleId, t2.CaseId as CaseVehicles_CaseId, t2.VehicleTypeId as CaseVehicles_VehicleTypeId, t2.VehicleMakeId as CaseVehicles_VehicleMakeId, t2.VehicleModelId as CaseVehicles_VehicleModelId, t2.VehicleStyleId as CaseVehicles_VehicleStyleId, t2.VehicleColorId as CaseVehicles_VehicleColorId, t2.Year as CaseVehicles_Year, t2.StateId as CaseVehicles_StateId, t2.VIN as CaseVehicles_VIN, t2.Impounded as CaseVehicles_Impounded, t2.ImpoundedBy as CaseVehicles_ImpoundedBy, t2.StoredAt as CaseVehicles_StoredAt, t2.VehiclePlacedOnHold as CaseVehicles_VehiclePlacedOnHold, t2.HoldReason as CaseVehicles_HoldReason, t2.VehicleWatercraftId as CaseVehicles_VehicleWatercraftId, t2.VehicleWatercraftOwnerId as CaseVehicles_VehicleWatercraftOwnerId, t2.VehicleCommercial as CaseVehicles_VehicleCommercial, t2.VehicleHazMat as CaseVehicles_VehicleHazMat, t2.VehicleCondition as CaseVehicles_VehicleCondition, t2.BoatHullShapeId as CaseVehicles_BoatHullShapeId, t2.VehicleBwiMotorYear as CaseVehicles_VehicleBwiMotorYear, t2.VehicleBwiMotorHorsepower as CaseVehicles_VehicleBwiMotorHorsepower, t2.VehicleBwiMotorManufacturer as CaseVehicles_VehicleBwiMotorManufacturer, t2.VehicleBwiMotorSerial as CaseVehicles_VehicleBwiMotorSerial, t2.VehicleBwiTrailerManufacturer as CaseVehicles_VehicleBwiTrailerManufacturer, t2.VehicleBwiTrailerRegistraitonNum as CaseVehicles_VehicleBwiTrailerRegistraitonNum, t2.VehicleModeId as CaseVehicles_VehicleModeId, t2.OldCaseId as CaseVehicles_OldCaseId
FROM DUI.Vehicle_Watercraft t1
LEFT JOIN DUI.CaseVehicles t2 ON t1.VehicleId = t2.CaseVehicleId
WHERE t1.VehicleId IS NOT NULL


-- Simple view for Vehicle_Watercraft_Owner
-- Provides secure access to Vehicle_Watercraft_Owner data excluding sensitive information
CREATE VIEW DUI.v_vehicle_watercraft_owner AS
SELECT VehicleWatercraftOwnerId, Name, VehicleId, StateId, CountyId, Lat, Lng
FROM DUI.Vehicle_Watercraft_Owner
WHERE VehicleWatercraftOwnerId IS NOT NULL


-- Relationship view: Vehicle_Watercraft_Owner with CaseVehicles
-- Provides Vehicle_Watercraft_Owner data joined with related CaseVehicles information
CREATE VIEW DUI.v_vehicle_watercraft_owner_with_casevehicles AS
SELECT t1.VehicleWatercraftOwnerId, t1.Name, t1.VehicleId, t1.StateId, t1.CountyId, t1.Lat, t1.Lng, t2.CaseVehicleId as CaseVehicles_CaseVehicleId, t2.CaseId as CaseVehicles_CaseId, t2.VehicleTypeId as CaseVehicles_VehicleTypeId, t2.VehicleMakeId as CaseVehicles_VehicleMakeId, t2.VehicleModelId as CaseVehicles_VehicleModelId, t2.VehicleStyleId as CaseVehicles_VehicleStyleId, t2.VehicleColorId as CaseVehicles_VehicleColorId, t2.Year as CaseVehicles_Year, t2.StateId as CaseVehicles_StateId, t2.VIN as CaseVehicles_VIN, t2.Impounded as CaseVehicles_Impounded, t2.ImpoundedBy as CaseVehicles_ImpoundedBy, t2.StoredAt as CaseVehicles_StoredAt, t2.VehiclePlacedOnHold as CaseVehicles_VehiclePlacedOnHold, t2.HoldReason as CaseVehicles_HoldReason, t2.VehicleWatercraftId as CaseVehicles_VehicleWatercraftId, t2.VehicleWatercraftOwnerId as CaseVehicles_VehicleWatercraftOwnerId, t2.VehicleCommercial as CaseVehicles_VehicleCommercial, t2.VehicleHazMat as CaseVehicles_VehicleHazMat, t2.VehicleCondition as CaseVehicles_VehicleCondition, t2.BoatHullShapeId as CaseVehicles_BoatHullShapeId, t2.VehicleBwiMotorYear as CaseVehicles_VehicleBwiMotorYear, t2.VehicleBwiMotorHorsepower as CaseVehicles_VehicleBwiMotorHorsepower, t2.VehicleBwiMotorManufacturer as CaseVehicles_VehicleBwiMotorManufacturer, t2.VehicleBwiMotorSerial as CaseVehicles_VehicleBwiMotorSerial, t2.VehicleBwiTrailerManufacturer as CaseVehicles_VehicleBwiTrailerManufacturer, t2.VehicleBwiTrailerRegistraitonNum as CaseVehicles_VehicleBwiTrailerRegistraitonNum, t2.VehicleModeId as CaseVehicles_VehicleModeId, t2.OldCaseId as CaseVehicles_OldCaseId
FROM DUI.Vehicle_Watercraft_Owner t1
LEFT JOIN DUI.CaseVehicles t2 ON t1.VehicleId = t2.CaseVehicleId
WHERE t1.VehicleId IS NOT NULL


-- Simple view for Witnesses
-- Provides secure access to Witnesses data excluding sensitive information
CREATE VIEW DUI.v_witnesses AS
SELECT WitnessId, CaseId, LastName, FirstName, RaceId, GenderId, IsVictim, WhatWitnessObserved, StateId, CountyId, Lat, Lng, ArchiveOfficer, ArchiveState
FROM DUI.Witnesses
WHERE WitnessId IS NOT NULL


-- Relationship view: Witnesses with CaseHeaders
-- Provides Witnesses data joined with related CaseHeaders information
CREATE VIEW DUI.v_witnesses_with_caseheaders AS
SELECT t1.WitnessId, t1.CaseId, t1.LastName, t1.FirstName, t1.RaceId, t1.GenderId, t1.IsVictim, t1.WhatWitnessObserved, t1.StateId, t1.CountyId, t1.Lat, t1.Lng, t1.ArchiveOfficer, t1.ArchiveState, t2.CaseId as CaseHeaders_CaseId, t2.UniqueId as CaseHeaders_UniqueId, t2.StatusId as CaseHeaders_StatusId, t2.ModelId as CaseHeaders_ModelId, t2.LockedByOfficerId as CaseHeaders_LockedByOfficerId, t2.ApprovedByOfficerId as CaseHeaders_ApprovedByOfficerId, t2.OrganizationId as CaseHeaders_OrganizationId, t2.LocationId as CaseHeaders_LocationId, t2.District as CaseHeaders_District, t2.Grid as CaseHeaders_Grid, t2.Version as CaseHeaders_Version, t2.Active as CaseHeaders_Active, t2.ModeId as CaseHeaders_ModeId, t2.ProbableCause as CaseHeaders_ProbableCause, t2.IsTrainingPurpose as CaseHeaders_IsTrainingPurpose, t2.PaidTxDOT as CaseHeaders_PaidTxDOT, t2.StepGrantTypeId as CaseHeaders_StepGrantTypeId, t2.CaseOwnerAgency as CaseHeaders_CaseOwnerAgency, t2.CaseOwnerBadge as CaseHeaders_CaseOwnerBadge, t2.CaseOwnerDepartmentId as CaseHeaders_CaseOwnerDepartmentId, t2.CaseOwnerId as CaseHeaders_CaseOwnerId, t2.CaseOwnerName as CaseHeaders_CaseOwnerName, t2.CaseOwnerRank as CaseHeaders_CaseOwnerRank, t2.TABC as CaseHeaders_TABC, t2.AdditionalInformation as CaseHeaders_AdditionalInformation, t2.ActivityType as CaseHeaders_ActivityType, t2.OfficerStepShiftId as CaseHeaders_OfficerStepShiftId, t2.StepZoneId as CaseHeaders_StepZoneId, t2.OldCaseID as CaseHeaders_OldCaseID
FROM DUI.Witnesses t1
LEFT JOIN DUI.CaseHeaders t2 ON t1.CaseId = t2.CaseId
WHERE t1.CaseId IS NOT NULL


-- Simple view for __EFMigrationsHistory
-- Provides secure access to __EFMigrationsHistory data excluding sensitive information
CREATE VIEW DUI.v___efmigrationshistory AS
SELECT MigrationId, ProductVersion
FROM DUI.__EFMigrationsHistory
WHERE MigrationId IS NOT NULL


-- Comprehensive Case Summary View
-- Provides a complete overview of DUI cases with related information
CREATE VIEW DUI.v_case_summary AS
SELECT 
    ch.CaseId,
    ch.UniqueId,
    ch.StatusId,
    ch.ModelId,
    ch.DateEntered,
    ch.AgencyCaseNumber,
    ch.ServiceNumber,
    ch.District,
    ch.Grid,
    ch.Version,
    ch.ArrestNumber,
    ch.OfficerId,
    
    -- Defendant Information
    d.DefendantId,
    d.LastName,
    d.MiddleName,
    d.FirstName,
    d.RaceId,
    d.GenderId,
    d.HeightIn,
    d.HeightFt,
    d.EthnicityId,
    
    -- Case Offense Information
    co.CaseOffenseId,
    co.OffenseId,
    co.ArrestDate,
    co.ArrestTime,
    co.ArrestCountyId,
    co.ArrestStateId,
    
    -- Vehicle Information
    cv.CaseVehicleId,
    cv.VehicleId,
    cv.VehicleYear,
    cv.VehicleMake,
    cv.VehicleModel,
    cv.VehicleColor,
    cv.LicensePlate,
    cv.LicenseState,
    
    -- Status Information
    s.StatusName
    
FROM DUI.CaseHeaders ch
LEFT JOIN DUI.Defendants d ON ch.CaseId = d.CaseId
LEFT JOIN DUI.CaseOffenses co ON ch.CaseId = co.CaseId
LEFT JOIN DUI.CaseVehicles cv ON ch.CaseId = cv.CaseId
LEFT JOIN DUI.TBL_OPT_Status s ON ch.StatusId = s.StatusId
WHERE ch.CaseId IS NOT NULL


-- Evidence Summary View
-- Provides comprehensive evidence information for DUI cases
CREATE VIEW DUI.v_evidence_summary AS
SELECT 
    ch.CaseId,
    ch.UniqueId,
    ch.AgencyCaseNumber,
    ch.ServiceNumber,
    ch.DateEntered,
    
    -- Physical Evidence
    pe.PhysicalEvidenceId,
    pe.EvidenceDescription,
    pe.EvidenceType,
    pe.CollectedDate,
    
    -- Evidence Documents
    ed.EvidenceDocumentId,
    ed.DocumentId,
    d.DocumentName,
    d.DocumentTypeId,
    dt.DocumentTypeName,
    d.FileTypeId,
    dft.FileName as FileTypeName,
    
    -- Evidence Recordings
    er.EvidenceRecordingId,
    er.EvidenceNumber as RecordingDescription,
    er.TimeBegan as RecordingDate,
    
    -- Specimen Reports
    sr.SpecimenReportId,
    sr.ReportDate,
    sr.ReportType
    
FROM DUI.CaseHeaders ch
LEFT JOIN DUI.PhysicalEvidence pe ON ch.CaseId = pe.CaseId
LEFT JOIN DUI.EvidenceDocuments ed ON ch.CaseId = ed.CaseId
LEFT JOIN DUI.Documents d ON ed.DocumentId = d.DocumentId
LEFT JOIN DUI.TBL_OPT_DocumentTypes dt ON d.DocumentTypeId = dt.DocumentTypeId
LEFT JOIN DUI.TBL_OPT_DocumentFileTypes dft ON d.FileTypeId = dft.DocumentFileTypeId
LEFT JOIN DUI.EvidenceRecordings er ON ch.CaseId = er.CaseId
LEFT JOIN DUI.SpecimenReport sr ON ch.CaseId = sr.CaseId
WHERE ch.CaseId IS NOT NULL


-- Officer Performance View
-- Provides officer performance metrics and case statistics
CREATE VIEW DUI.v_officer_performance AS
SELECT 
    oo.OtherOfficerId as OfficerId,
    oo.OfficerName,
    oo.BadgeNumber,
    oo.Department,
    oo.OtherOfficerParticipation,
    oo.Supplement,
    
    -- Case Statistics
    COUNT(DISTINCT ch.CaseId) as TotalCases,
    COUNT(DISTINCT CASE WHEN ch.StatusId = 1 THEN ch.CaseId END) as ActiveCases,
    COUNT(DISTINCT CASE WHEN ch.StatusId = 2 THEN ch.CaseId END) as ClosedCases,
    
    -- Arrest Statistics
    COUNT(DISTINCT co.CaseOffenseId) as TotalArrests,
    COUNT(DISTINCT CASE WHEN co.OffenseId = 1 THEN co.CaseOffenseId END) as DUIArrests,
    
    -- Evidence Collection
    COUNT(DISTINCT pe.PhysicalEvidenceId) as EvidenceCollected,
    COUNT(DISTINCT sr.SpecimenReportId) as SpecimenReports,
    
    -- Time Period Analysis
    MIN(ch.DateEntered) as FirstCaseDate,
    MAX(ch.DateEntered) as LastCaseDate,
    
    -- Created/Modified Info
    oo.CaseId
    
FROM DUI.OtherOfficers oo
LEFT JOIN DUI.CaseHeaders ch ON oo.CaseId = ch.CaseId
LEFT JOIN DUI.CaseOffenses co ON ch.CaseId = co.CaseId
LEFT JOIN DUI.PhysicalEvidence pe ON ch.CaseId = pe.CaseId
LEFT JOIN DUI.SpecimenReport sr ON ch.CaseId = sr.CaseId
WHERE oo.OtherOfficerId IS NOT NULL
GROUP BY oo.OtherOfficerId, oo.OfficerName, oo.BadgeNumber, oo.Department, 
         oo.OtherOfficerParticipation, oo.Supplement, oo.CaseId


-- Defendant Summary View
-- Provides comprehensive defendant information for DUI cases
CREATE VIEW DUI.v_defendant_summary AS
SELECT 
    d.DefendantId,
    d.CaseId,
    d.DateEntered,
    d.LastName,
    d.MiddleName,
    d.FirstName,
    d.RaceId,
    d.GenderId,
    d.HeightIn,
    d.HeightFt,
    d.EthnicityId,
    
    -- Demographics
    g.GenderDescription as GenderName,
    r.RaceDescription as RaceName,
    e.EthnicityDescription as EthnicityName,
    
    -- Case Information
    ch.UniqueId,
    ch.AgencyCaseNumber,
    ch.ServiceNumber,
    ch.StatusId,
    s.StatusName,
    
    -- Offense Information
    co.CaseOffenseId,
    co.OffenseId,
    o.OffenseDescription as OffenseName,
    co.ArrestDate,
    co.ArrestTime,
    
    -- Interview Information
    di.DefendantInterviewId,
    di.DateOfInterview as InterviewDate,
    di.TimeOfInterview as InterviewTime,
    
    -- Observations
    do.DefendantObservationId,
    do.OtherObservationsComments as ObservationDescription,
    
    -- Field Sobriety Tests
    fst.FieldSobrietyTestId,
    fst.TestDate,
    fst.TestType
    
FROM DUI.Defendants d
LEFT JOIN DUI.TBL_OPT_Genders g ON d.GenderId = g.GenderId
LEFT JOIN DUI.TBL_OPT_Races r ON d.RaceId = r.RaceId
LEFT JOIN DUI.TBL_OPT_Ethnicity e ON d.EthnicityId = e.EthnicityId
LEFT JOIN DUI.CaseHeaders ch ON d.CaseId = ch.CaseId
LEFT JOIN DUI.TBL_OPT_Status s ON ch.StatusId = s.StatusId
LEFT JOIN DUI.CaseOffenses co ON d.CaseId = co.CaseId
LEFT JOIN DUI.TBL_OPT_Offense o ON co.OffenseId = o.OffenseId
LEFT JOIN DUI.DefendantInterview di ON d.DefendantId = di.DefendantId
LEFT JOIN DUI.DefendantObservations do ON d.DefendantId = do.DefendantId
LEFT JOIN DUI.FieldSobrietyTests fst ON d.CaseId = fst.CaseId
WHERE d.DefendantId IS NOT NULL


-- =====================================================
-- Script completed
-- =====================================================
PRINT 'All DUI views created successfully!'
PRINT 'Run: SELECT COUNT(*) FROM INFORMATION_SCHEMA.VIEWS WHERE TABLE_SCHEMA = ''DUI'' to verify count'
