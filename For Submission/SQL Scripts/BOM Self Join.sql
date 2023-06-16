
USE ASSESSMENT;

SELECT 
	fg.`PV Material Plant View_R`,
    fg.`BI Component_R`as Component,
    b.`PV Plant_R`,
    b.`Material type`
FROM BOM fg
JOIN BOM b
	ON fg.`PV Material Plant View_R` = b.`BI Component_R`
    