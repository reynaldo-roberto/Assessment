CREATE table CLEAN_BOM AS

SELECT * FROM BOM WHERE 
`PV Plant_R` LIKE "% " or `PV Plant_R` LIKE " %" or 
`PV Material Plant View_R` LIKE "% " or `PV Material Plant View_R` LIKE " %" or 
`Material type` LIKE "% " or `Material type` LIKE " %" or 
`BI Component_R` LIKE "% " or `BI Component_R` LIKE " %" or 
`Material type1` LIKE "% " or `Material type1` LIKE " %";
