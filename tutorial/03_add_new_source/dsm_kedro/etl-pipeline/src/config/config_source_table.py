#### Template ####
# source_table = {
#     <Database id1>: ["<your table 1>", "<your table 2>"],
#     <Database id2>: ["<your table 3>", "<your table 4>"]
# }

source_table = {
    22: ['DimForecastCountry','DimForecastProducts','DimMenuComMaping','DimMenuComMapingLevel','DimTime','DimType','Dim_Zone',
        'Unit','DimFacTable','DataHSCode','DimExporterAndImport','DimFacTableCountries','Dim_Countrys'],
    23: ['DataExportActivityHistory','DataExportHistory','DimActivities','DimActivityCorporate','DimActivityPerson',
        'DimActivityCountries','DimActivityFactable','DimActivityGroup','DimActivityGroupProductCategory','DimActivityProgress',
        'DimActivityProvince','DimActivityRegion','DimActivityTime','DimActivityType','DimBusinessType','DimComCode','DimCompanies',
        'DimCountrys','DimExportActivityFactable','DimHSCode','DimProductcategories','DimProperties','DimUnderCorporate','DimZone',
        'DBD_JuristicResponse','DITP_Survey_TradeFair_Product','t_DITP_User_Award_API', 'DITP_Survey_Seminar_Answer', 'DITP_Survey_TradeFair_Product_Other', 'DITP_Survey_TradeFair_Answer'],
    24: ['t_view_tb_member','t_member_type1','t_member_type2','t_member_type3','t_member_type4','t_member_type6'],
    25: ['Case_Priority','Product_Type','Country','Currency','Complaint_Type_Sub2','Complaint_Type_Sub1','Complaint_Type','Case_Channel',
        'Case_Close','Case'],
    26: ['t_view_registration','t_view_tm_exhibitor','t_view_tm_user','t_view_tm_user_local','t_view_tm_user_oversea','t_view_tm_usergroup'],  # add from sqlalchemy import MetaData to Schema
    # 27: ['DimActivityPerson','DimPerson','DimMemberType'],
    27: ['DimActivityPerson','DimMemberType'],
    28: ['t_ReportFormApprove_BuyValue','t_ReportFormApproveActivityJoinProduct','t_ReportFormApprove_BIEng'],
    29: ['api_activitymappingditpproduct', 'api_linkallcode'],
    30: ['km'],
}